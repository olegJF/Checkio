# -*- coding: utf-8 -*-

class Building(object):
    def __init__(self,south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height
        self.north = self.south+self.width_NS
        self.east = self.west+self.width_WE

    def corners(self):
        self.corn = {'south-west':[self.south, self.west],'south-east':[self.south, self.east],'north-east':[self.north,self.east],'north-west':[self.north,self.west]}
        return self.corn
    
    def area(self):
        return self.width_WE*self.width_NS

    def volume(self):
        return self.width_WE*self.width_NS*self.height

    def __repr__(self):
        return 'Building(%r, %r, %r, %r, %r)' %(self.south, self.west, self.width_WE, self.width_NS, self.height) 

   
     
    
a = Building(1, 2, 2, 2, 67)
print(a)
print(a.area())
print(a.volume())
print(a.corners())
