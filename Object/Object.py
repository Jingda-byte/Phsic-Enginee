# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 00:16:35 2020

@author: Jijngda_yang
"""
import numpy as np

class Object():
    
    def __init__(self, position,quality):
        self.__position=position
        self.__quality=quality
        self.__acceleration=np.array([0,0])
             
    @property
    def position(self):
       return self.__position
    
    @position.setter
    def position(self,position):
        self.__position=position
    
    
    def forced(self,power:np):
        self.__acceleration=np.add(self.__acceleration,np.sqrt(power*2/self.__quality))
    
    def refresh(self):
        self.__position=np.add(self.__position,self.__acceleration)
        
    def gravity(self,grav):
        self.__acceleration+=grav
    
