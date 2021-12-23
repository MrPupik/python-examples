import timeit
from os import stat
from TaxiStation.station import CarFleet, TaxiStation
from TaxiStation.customer import Customer, CustomerType
from TaxiStation.cars import *
import pytest


class TestCarFleet:
    def test_single(self):
        c = CarFleet()
        # sanity
        c["Taxi"] = Taxi(10)
        c["Lemo"] = Lemo(10)
        c["Van"] = Van(10)
        c["Minibus"] = Minibus(Minibus)

        # error
        with pytest.raises(TypeError):
            c["Taxi"] = Lemo(10)
        with pytest.raises(TypeError):
            c["Big bus"] = Minibus(10)

        # get
        assert isinstance(c["Taxi"], Taxi)
        assert isinstance(c["Lemo"], Lemo)
        assert isinstance(c["Van"], Van)
        assert isinstance(c["Minibus"], Minibus)

        # get when empty
        c = CarFleet()
        assert c["Minibus"] is None

        # get when non avialble
        van = Van(10)
        van.available = False
        c["Van"] = van
        assert c["Van"] is None

    def test_list(self):

        # sanity init
        c = CarFleet([Taxi(10), Lemo(10), Minibus(10), Van(10)])
        assert isinstance(c["Taxi"], Taxi)
        assert isinstance(c["Lemo"], Lemo)
        assert isinstance(c["Van"], Van)
        assert isinstance(c["Minibus"], Minibus)

        # sanity set item
        c = CarFleet()
        c[""] = [Taxi(10), Lemo(10), Minibus(10), Van(10)]
        assert isinstance(c["Taxi"], Taxi)
        assert isinstance(c["Lemo"], Lemo)
        assert isinstance(c["Van"], Van)
        assert isinstance(c["Minibus"], Minibus)

        # error  set item
        with pytest.raises(TypeError):
            c[""] = [Taxi(10), Car(10), Minibus(10), Van(10)]

        # error init
        with pytest.raises(TypeError):
            CarFleet([Taxi(10), Car(10), Minibus(10), Van(10)])

        def dict_conv(self):
            c = CarFleet([Taxi(10), Van(10)])
            d = c.to_dict()
            d["Taxi"] = []
            assert d["Taxi"]


class TestWork:
    def test_sanity(self):
        cust_list = [
            Customer(CustomerType.private, 2, 60), Customer(
                CustomerType.private, 150, 60),
            Customer(CustomerType.private, 15, 60), Customer(
                CustomerType.buisness, 5, 60)
        ]

        station = TaxiStation(
            CarFleet([Taxi(100), Lemo(100), Minibus(100), Van(100)]))

        station.work(cust_list)

        assert not station.disappointed

    def test_wrong_pass_quantity(self):
        cust_list = [
            Customer(CustomerType.private, 90, 60), Customer(
                CustomerType.buisness, 150, 60),
        ]

        station = TaxiStation(
            CarFleet([Taxi(100), Lemo(100), Minibus(100), Van(100)]))

        station.work(cust_list)
        assert len(station.disappointed) == 2

    def test_missing_car_types(self):
        cust_list = [
            Customer(CustomerType.private, 2, 60), Customer(
                CustomerType.buisness, 10, 60),
        ]
        station = TaxiStation(
            CarFleet([Taxi(10)]))

        station.work(cust_list)
        assert len(station.disappointed) == 1


cust_list = [
    Customer(CustomerType.private, 2, 21), Customer(
        CustomerType.private, 10, 10),
    Customer(CustomerType.private, 15, 10), Customer(
        CustomerType.buisness, 5, 10)
]

station = TaxiStation(
    CarFleet([Taxi(1), Lemo(100), Minibus(100), Van(100), Taxi(1)]))

starttime = timeit.default_timer()

station.work_threaded(cust_list)
print("time :", timeit.default_timer() - starttime)
