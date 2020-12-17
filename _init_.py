# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 00:17:59 2020

@author: Jijngda_yang
"""

from World.World import World
from Object.RigidBody import RigidBody
import numpy as np

def main():
    world = World(time=5,FPS=60,size=(100,100))
    position=np.array([-100,100])
    qaulity=1
    rigidBody = RigidBody(position,qaulity)
    rigidBody.forced(qaulity*np.square(np.array([10,0]))/2)
    world.add_object(rigidBody)
    world.show()
    
    
if __name__ == "__main__":
    main()