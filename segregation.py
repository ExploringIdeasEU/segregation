
'''
a library to implement the indexes described here: 
    http://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf

homepage: https://github.com/ExploringIdeasEU/segregation
'''




'''
n    :the number of areas (census tracts) in the metropolitan area, 
     ranked smallest to largest by land area

m    :the number of areas (census tracts) in the metropolitan area, 
      ranked by increasing distance from the Central Business 
      District (m = n)
xi   :the minority population of area i
yi   :the majority population of area i
yj   :the majority population of area j
ti   :the total population of area i
tj   :the total population of area j
X    :the sum of all xi (the total minority population)
Y    :the sum of all yi (the total majority population)
T    :the sum of all ti (the total population)
pi   :the ratio of xi to ti (proportion of area i’s population 
      that is minority)
P    :the ratio of X to T (proportion of the metropolitan area’s 
      population that is minority)
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
    '''“Exposure measures the degree of
    potential contact, or possibility of
    interaction, between minority and
    majority group members” (Massey
    and Denton, p. 287).
    '''
    @staticmethod
    def interaction(x,y,t):
        ''' The interaction index measures 
        the exposure of minority group mem-
        bers to members of the majority
        group as the minority-weighted
        average of the majority proportion
        of the population in each areal
        unit.''' 
        X = np.sum(x)
        index = np.dot(x / X, y / t)
        return index

    @staticmethod
    def isolation(x,t):
        '''The isolation index measures
        “the extent to which minority
        members are exposed only to one
        another,” (Massey and Denton, p.
        288) and is computed as the
        minority-weighted average of the
        minority proportion in each area.
        '''
        X = np.sum(x)
        index = np.dot(x / X, x / t)
        return index

    @staticmethod
    def correlation(x,t):
        '''An adjustment of the isolation index
        '''
        T = np.sum(t)
        X = np.sum(x)
        P = X / T
        index = (self.isolation(x, t) - P) / (1 - P)
        return index

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




