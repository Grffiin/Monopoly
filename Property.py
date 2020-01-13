# TODO: Separate (child) class for utils / RR's (who calculate stuff different)
from abc import ABC, abstractmethod


class AbsProp(ABC):
    """Class for ownable properties"""

    # initializer for importing from CSV
    def __init__(self, name, price, mortgage, propset):
        self.name = name
        self.price = price
        self.mortgage = mortgage
        self.propset = propset


class RailroadProperty(AbsProp):
    def __init__(self, name, price, rent1, rent2, rent3, rent4, mortgage, propset):
        super().__init__(name, price, mortgage, propset)
        self.rent1 = rent1
        self.rent2 = rent2
        self.rent3 = rent3
        self.rent4 = rent4


class UtilityProperty(AbsProp):
    def __init__(self, name, price, rent1, rent2, mortgage, propset):
        super().__init__(name, price, mortgage, propset)
        self.rent1 = rent1
        self.rent2 = rent2

class Property(AbsProp):
    def __init__(self, name, price, rent, housecost, hotelcost, rent1, rent2, rent3, rent4, renth, mortgage, propset):
        super().__init__(name, price, mortgage, propset)
        self.rent1 = rent1
        self.rent2 = rent2
        self.rent3 = rent3
        self.rent4 = rent4
        self.rent = rent
        self.housecost = housecost
        self.hotelcost = hotelcost
        self.renth = renth
