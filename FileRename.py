#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:36:24 2019

@author: saeed
"""

import os 
  
def renamee(): 
    i = 0
    dir = "/home/phd/Downloads/datasets/NumberPlatess/"
    for filename in os.listdir(dir): 
        dst =""+ str(i) + ".jpg"
        src = dir + filename 
        dst = dir + dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
if __name__ == '__main__': 
    # Calling main() function 
    renamee() 
