
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
X    :the sum of all xi (the total minority population)
yi   :the majority population of area i
Y    :the sum of all yi (the total majority population)
ti   :the total population of area i
T    :the sum of all ti (the total population)
pi   :the ratio of xi to ti (proportion of area i’s population 
      that is minority)
P    :the ratio of X to T (proportion of the metropolitan area’s 
      population that is minority)
ai   :the land area of area i
A   :the sum of all ai (the total land area)
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
    '''Centralization is the degree to which a 
    group is spatially located near the center
    of an urban area.
    Definition from:
    http://isites.harvard.edu/fs/docs/icb.topic98848.files/massey.denton.pdf
    '''
    @staticmethod
    def absolute(pair):
        '''
        input: pair: pair = (xi, ai, di)
            xi: minority population in area i 
            ai: the land area of area i 
            di: istance from CBD of area i 
        CDB: Central Business District 
        '''
        #order pair by di
        pair = sorted(pair, key=lambda x: x[2])
        Xi = [pair[0][0]]
        Ai = [pair[0][1]]
        index = 0
        for i in range(1, len(pair)):
            Xi.append(Xi[i-1]+pair[i][0])
            Ai.append(Ai[i-1]+pair[i][1])
            index += Xi[i-1]*Ai[i] - Xi[i]*Ai[-1]
        return index / ( Xi[-1] * Ai[-1] )

    @staticmethod
    def relative():
        '''
        input: pair: pair = (xi, yi, di)
            xi: minority population in area i 
            yi: majority population in area i 
            di: istance from CBD of area i 
        CDB: Central Business District 
        '''
        #order pair by di
        pair = sorted(pair, key=lambda x: x[2])
        Xi = [pair[0][0]]
        Yi = [pair[0][1]]
        index = 0
        for i in range(1, len(pair)):
            Xi.append(Xi[i-1]+pair[i][0])
            Yi.append(Yi[i-1]+pair[i][1])
            index += Xi[i-1]*Yi[i] - Xi[i]*Yi[-1]
        return index / ( Xi[-1] * Yi[-1] )


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




