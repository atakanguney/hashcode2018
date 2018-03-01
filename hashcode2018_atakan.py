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
    
    def __str__(self):
        return [self.row, self.col].__str__()
        

class Ride:
    
    def __init__(self, conf, r_id):
        self.r_id = r_id
        self.start = Intersection(conf[0], conf[1])
        self.end = Intersection(conf[2], conf[3])
        self.early = conf[4]
        self.latest = conf[5]
        self.distance = self.start.distance(self.end)
        
    def findCar(self, vehicles):
        print('[DEBUG] findCar method')
        for i in vehicles:
            vehicles[i].addToAvailable(self)
        
class Vehicle:
    
    def __init__(self, row, col):
        self.location = Intersection(row, col)
        self.available = [(0,0,Ride([0,0,0,0,-1,-1],-1)),(float('inf'),float('inf'),Ride([0,0,0,0,float('inf'),float('inf')],-2))]
        
    def __str__(self):
        ret_str = ''
        for ride in self.available:
            ret_str = ret_str + str(ride[2]) + ' '        
        return ret_str
 
    def addToAvailable(self, newRide):
        print('[DEBUG] addToAvailable method')
        for i in range(len(self.available)-1):
            available, eps_new, epf_new = self.put_between(self.available[i], self.available[i+1], newRide)
            if(available):
                self.available.insert((eps_new, epf_new,newRide),i)
                break
            
    def put_between(self, tuple1, tuple2, newRide):
        print('[DEBUG] put between')
        is_poss, _ , _ , _ = self.reachOnTime(tuple1[2].end, newRide, tuple1[1])
        print(is_poss)
        
        
    def reachOnTime(self, loc, ride, now_time):
        print('[DEBUG] reach on time')
        car_to_start_dist = loc.distance(ride.start)
        start_to_dest_dist = ride.distance
        total_distance = car_to_start_dist + start_to_dest_dist
        total_time = ride.latest - now_time
    
        if now_time>ride.latest:
            print('ERROR Latest finish is already past.')
            return False,-1,False,-1
        
        total_waiting_time = total_time - total_distance
        is_it_possible_ride = total_waiting_time >= 0
        
        precise_waiting_time = (ride.early - now_time) - car_to_start_dist
        is_it_possible_precise_start = precise_waiting_time >= 0
        
        return is_it_possible_ride, total_waiting_time, is_it_possible_precise_start, precise_waiting_time
    
         
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
    begin_ride = Ride([0,0,0,0,-1,-1],-1)
    end_ride = Ride([0,0,0,0,float('inf'),float('inf')],-2)
    rides = {}
    rides[-1] = begin_ride
    rides[-2] = end_ride
    id = 0
    for ride in lines[1:]:
        temp = ride.split()
        rides[id] = Ride([int(t) for t in temp], id)
        id = id + 1
        
    #rides = np.array(rides)
    for i in rides:
        print(rides[i].distance)
        
    vehicles = {}

    for id in range(F):
        vehicles[id] = Vehicle(0, 0)
        

        
    
    myList = []
    for i in rides:
        rides[i].findCar(vehicles)
        myList.append((i, rides[i].distance))
        
    myList.sort(key=lambda tup: tup[1])
    
    for i in vehicles:
        print(vehicles[i].available)

        
    
    
    