# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 00:16:02 2020

@author: Jijngda_yang
"""

import matplotlib.pyplot as plt
from Object.Object import Object
import numpy as np

class World():
    
    def __init__(self, time=10, FPS=60,size=(10,10),gravity=np.array([0,-10])):
        self.__time = time
        self.__FPS = FPS
        self.__size=size 
        self.__objects=[]
        self.__gravity=gravity
        
    def show(self):
        plt.ion()
        frame=0
        while frame < self.__time*self.__FPS:
            plt.clf()
            for obj in self.__objects:
                obj.gravity(self.__gravity/self.__FPS)
                obj.refresh()
                position=obj.position
                plt.scatter(position[0],position[1])
            plt.axis([-self.__size[0],self.__size[0],-self.__size[1],self.__size[1]])
            plt.pause(1/self.__FPS)
            frame+=1
        plt.ioff()       # 关闭画图的窗口，即关闭交互模式
        plt.show()
    
    
    def add_object(self,obj:Object):
        self.__objects.append(obj)
        