#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 21:09:28 2018

@author: atakan1
"""

import numpy as np
import pandas as pd


class Intersection:
    
    def __init__(self,row, col):
        self.row = row
        self.col = col
        
    def distance(self, other):
        return abs(self.row-other.row) + abs(self.col-other.col)
        

class Ride:
    
    def __init__(self, conf):
        self.start = Intersection(conf[0], conf[1])
        self.end = Intersection(conf[2], conf[3])
        self.early = conf[4]
        self.latest = conf[5]
        
    
        
if __name__ == '__main__':
    
    file_name = 'a_example.in'
    f = open(file_name)
    lines = f.readlines()
    f.close()
    lines = [line[:-1] for line in lines]
    
    first_line = lines[0].split()
    R = int(first_line[0])
    C = int(first_line[1])
    F = int(first_line[2])
    N = int(first_line[3])
    B = int(first_line[4])
    T = int(first_line[5])
    
    rides = []
    for ride in lines[1:]:
        temp = ride.split()
        rides.append(Ride([int(t) for t in temp]))
        
    #rides = np.array(rides)
    distances = [x.start.distance(x.end) for x in rides]
    
    print(distances)
    
    