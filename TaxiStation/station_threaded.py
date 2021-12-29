from sys import stdout
from TaxiStation.cars import Car, Taxi, Lemo, Van, Minibus
import threading
from time import sleep
from copy import deepcopy
from queue import Queue

import logging
from TaxiStation.customer import Customer, CustomerType
from TaxiStation.recipts import Transcation, write_recipt

from TaxiStation.utils import get_type_name

logging.basicConfig(filename='taxi_station.log',
                    encoding='utf-8', level=logging.DEBUG)
info = logging.info

logging.getLogger().addHandler(logging.StreamHandler())


car_types_by_name = {
    car_type.__name__: car_type for car_type in (Taxi, Lemo, Van, Minibus)
}


class CarFleet:
    def __init__(self, cars: list = None) -> None:
        self._data = {}
        if cars:
            self._load_from_list(self._data, cars)

    def __setitem__(self, key, value) -> None:
        if not isinstance(value, Car):
            self._load_from_list(self._data, value)
        else:
            type_name = get_type_name(value)
            if type_name != key or key not in car_types_by_name.keys():
                raise TypeError(
                    f"{CarFleet.__name__} accepts only supported keys and values. got '{key}:{type_name}'"
                )
            else:
                self._data[type_name] = self._data.get(type_name, []) + [value]

    def __getitem__(self, key):
        for car in self._data.get(key, []):
            if car.available and self._data.get(key):
                return car

    @staticmethod
    def _load_from_list(data, cars):
        for car in cars:
            type_name = get_type_name(car)
            if type_name not in car_types_by_name.keys():
                raise TypeError(
                    f"{CarFleet.__name__} accepts only supported cars: {tuple(car_types_by_name.keys())}. but got '{type_name}'"
                )
            data[type_name] = data.get(type_name, []) + [car]

    def to_dict(self):
        return deepcopy(self._data)

    def car_types(self):
        return tuple(self._data.keys())

    def from_dict(self, cars_dict):
        for lst in cars_dict:
            self[""] = lst

    def __repr__(self) -> str:

        return (
            "CarFleet:\n"
            + ", ".join(
                (f"total {kind}: {len(lst)}" for kind,
                 lst in self._data.items())
            )
            + "\n"
            + ", ".join(
                (
                    f"available {kind}: {len([car for car in self._data[kind] if car.available])}"
                    for kind in self._data
                )
            )
        )


MAX_CUST = 100
driver_lock = threading.Lock()
clrek_lock = threading.Lock()

# queue for all trips (clerk will put here,  driver will get from here)
trip_queue = Queue(MAX_CUST)

# queue for classified customers, clerk will get here, driver and main will put
cust_queue = Queue(MAX_CUST)

# queue for finished. drive will put, accountent will get
finished_custs = Queue(MAX_CUST)


class TaxiStation:
    HELP_WAITING = True
    THRAD_NUMBER = 3

    def __init__(self, cars: CarFleet) -> None:
        self.cars = cars
        self.money = 0
        self.owed_money = 0
        self.transcations = {}

    def work(self, clients: list[Customer], trip_number=0):
        self.disappointed = []
        self.trip_number = trip_number
        customers = clients.copy()
      # send drivers to work
        drivers = []
        for i in range(1, self.THRAD_NUMBER+1):

            driver = Driver(
                f'driver-{i}', self.transcations)
            drivers.append(driver)
            driver.start()

        clerk = Clerk(self.cars, self.disappointed)
        clerk.start()

        accountent = Accountent(self.money, self.transcations)
        accountent.start()

        while customers:
            # get first
            self.trip_number += 1
            cust = None
            waiting_cust = None
            if customers:
                cust = customers.pop(0)
                self.transcations[self.trip_number] = []

                # initail help vars
                cust.trip_number = self.trip_number
                cust.bill = 0

                info(
                    f"new customer {cust.trip_number}, type:{cust.type} quantity:{cust.num_of_passengers}")
                self._classifiy(cust)

                if not cust.wanted_type:
                    continue

            driver_lock.acquire()
            cust_queue.put(cust)
            driver_lock.release()

            # driver can go homer after finished
        for driver in drivers:
            driver.stop()
            sleep(0.1)  # give some time for the clerk to put more trips
            # note: to really make sure no race condition, check both trip_queue and cust_queue before stopping
        for driver in drivers:
            driver.join()
        clerk.stop()
        accountent.stop()
        self.money = accountent.money
        print("thats it")

    def _classifiy(self, cust: Customer) -> str | None:
        """determine what car is good for this customer"""

        # decide what is the right type
        if cust.type == CustomerType.buisness:
            if cust.num_of_passengers > 100:
                self.disappointed.append(cust)
                info(f"customer {cust.trip_number} added to disappointed")
            else:
                cust.wanted_type = Lemo.__name__
        else:
            if cust.num_of_passengers <= Taxi.SEATS:
                cust.wanted_type = Taxi.__name__
            elif cust.num_of_passengers <= Van.SEATS:
                cust.wanted_type = Van.__name__
            elif cust.num_of_passengers <= Minibus.SEATS:
                cust.wanted_type = Minibus.__name__
            else:
                self.disappointed.append(cust)
                cust.wanted_type = None
                info(f"customer {cust.trip_number} added to disappointed")


class Driver(threading.Thread):
    """
    drive worker
    """
    _stop_event = False
    _activated = True

    def __init__(self, threadID, trans: dict):
        self.threadID = threadID
        self.lock = driver_lock
        self.transcations = trans
        info(f"worker {threadID} initalized")
        super().__init__()

    def drive_cust(self, cust: Customer, car: Car):
        price, dist_travelled = car.drive(cust.distance)
        trip_completed = True
        if dist_travelled < cust.distance:
            clrek_lock.acquire()
            cust_queue.put(cust)
            clrek_lock.release()
            trip_completed = False
            # discount for partial trip
            price = 0.85 * price
            transaction = Transcation(
                f'{dist_travelled} trip (partial)', price)
        else:
            info(
                f"cust {cust.trip_number} reached destination (after {dist_travelled}).")
            transaction = Transcation(f'{dist_travelled} trip', price)
        cust.bill += price
        info(
            f"cust {cust.trip_number} drove {dist_travelled} out of {cust.distance}. it costs {price} and it's current bill is {cust.bill}")
        cust.distance -= dist_travelled

        self.transcations[cust.trip_number].append(transaction)

        return trip_completed

    def run(self):
        while not self._stop_event:
            cust = car = None
            self.lock.acquire()
            while not trip_queue.empty():
                cust, car = trip_queue.get()
                self.lock.release()
                if car:
                    result = self.drive_cust(cust, car)
                    if result:
                        self.lock.acquire()
                        finished_custs.put(cust)
                        self.lock.release()
                self.lock.acquire()
            # after inner loop
            self.lock.release()

    def stop(self):
        self.lock.acquire()
        self._stop_event = True
        self.lock.release()

    def stopped(self):
        return self._stop_event


class Clerk(threading.Thread):
    """
    car finder worker
    """

    def __init__(self, cars: CarFleet, disappointed: list):
        self.lock = clrek_lock
        self.cars = cars
        self.disappointed = disappointed
        self._stop_event = False
        super().__init__()

    def run(self):
        while not self._stop_event:
            cust = car = None
            self.lock.acquire()
            while not cust_queue.empty():
                cust = cust_queue.get()
                self.lock.release()
                car = self.find_car(cust)
                self.lock.acquire()
                if car:
                    driver_lock.acquire()
                    trip_queue.put((cust, car))
                    driver_lock.release()
            # after inner loop
            self.lock.release()

    def find_car(self, cust):
        avl_car = self.cars[cust.wanted_type]
        if avl_car:
            info(f"found available {cust.wanted_type}")
            return avl_car

        if cust.wanted_type in self.cars.car_types():
            info(
                f"did not find available {cust.wanted_type}. adding to line")
            # he will wait for the right taxi to return
            self.cust_queue.put(cust)
        else:
            self.disappointed.append(cust)
            info(
                f"no {cust.wanted_type} in station, customer added to disappointed")

    def stop(self):
        self.lock.acquire()
        self._stop_event = True
        self.lock.release()

    def stopped(self):
        return self._stop_event


class Accountent(threading.Thread):
    """
    money charge worker
    """

    def __init__(self, money, trans: dict):
        self.money = money
        self.transcations = trans
        self.lock = driver_lock
        self._stop_event = False
        super().__init__()

    def run(self):
        while not self._stop_event:
            self.lock.acquire()
            while not finished_custs.empty():
                cust = finished_custs.get()
                self.lock.release()
                self.charge(cust)
                self.lock.acquire()

            # after inner loop
            self.lock.release()

    def charge(self, cust: Customer):
        self.money += cust.bill
        info(
            f"charged {cust.bill} from {cust.trip_number}. balance: {self.money}")
        cust.bill = 0
        write_recipt(f'cust_{cust.trip_number}',
                     self.transcations[cust.trip_number], cust.recipt_type)

    def stop(self):
        self.lock.acquire()
        self._stop_event = True
        self.lock.release()

    def stopped(self):
        return self._stop_event
