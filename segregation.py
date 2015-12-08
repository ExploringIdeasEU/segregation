
'''
a library to implement the indexes described here: 
    http://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf

homepage: https://github.com/ExploringIdeasEU/segregation
'''


import numpy

class Eveness(object):

    @staticmethod
    def dissimilarity():
        raise NotImplementedError()

    @staticmethod
    def Gini():
        raise NotImplementedError()

    @staticmethod
    def entropy():
        raise NotImplementedError()

    @staticmethod
    def Atkinson():
        raise NotImplementedError()

class Exposure(object):

    @staticmethod
    def interaction():
        raise NotImplementedError()

    @staticmethod
    def isolation():
        raise NotImplementedError()

    @staticmethod
    def correlation():
        raise NotImplementedError()

class Concentration(object):

    @staticmethod
    def delta():
        raise NotImplementedError()

    @staticmethod
    def absolute():
        raise NotImplementedError()

    @staticmethod
    def relative():
        raise NotImplementedError()

class Centralization(object):

    @staticmethod
    def absolute():
        raise NotImplementedError()

    @staticmethod
    def relative():
        raise NotImplementedError()


class Clustering(object):

    @staticmethod
    def absolute():
        raise NotImplementedError()

    @staticmethod
    def relative():
        raise NotImplementedError()

    @staticmethod
    def spatial_proximity():
        raise NotImplementedError()

    @staticmethod
    def distance_decay_interaction():
        raise NotImplementedError()

    @staticmethod
    def distance_decay_isolation():
        raise NotImplementedError()




