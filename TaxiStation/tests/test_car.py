from TaxiStation.cars import Taxi, Lemo, Van, Minibus, Car


class TestBaseCar:
    def test_drive_sanity(self):
        t = Car(10)
        t.drive(20)
        assert t.distance == 20
        assert t.fuel == 9

    def test_partial_drive(self):
        t = Car(1)
        t.drive(21)
        assert t.distance == 20
        assert t.fuel == 0

    def test_refuel(Self):
        t = Car(1)
        assert t.fuel == 1
        t.refuel(1)
        assert t.fuel == 2
        t.drive(20)
        assert t.fuel == 1


class TestTaxi:
    def test_taxi_price(self):
        t = Taxi(fuel=10)
        t.drive(10)
        assert t.money == 10 * t.KM_COST * 0.9

    def test_lemo_price(self):
        l = Lemo(10)
        assert l.KM_COST != Taxi.KM_COST
        print(l.KM_COST)
        l.drive(10)
        assert l.money == 10 * l.KM_COST * 0.9

    def test_van_price(self):
        assert Van.KM_COST == 6

    def test_minibus_price(self):
        assert Minibus.KM_COST == 8
