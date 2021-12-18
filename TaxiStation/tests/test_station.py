from TaxiStation.station import CarFleet
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
