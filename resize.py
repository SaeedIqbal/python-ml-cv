#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:53:20 2019

@author: saeed
"""
import os, sys
from PIL import Image
#path = "/home/phd/Desktop/Python/images/BullCart"
path = "/home/phd/Desktop/PhDThesisTemplate/ThesisFigs/images/"
size = 512, 512
resizedFolder = os.path.join(os.path.dirname(path), "resized")
if not os.path.exists(resizedFolder):
    os.makedirs(resizedFolder)
    
for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") :       
        if file.endswith(".jpg"):
            outfile = os.path.splitext(file)[0] + ".jpg"
        if file.endswith(".jpeg"):       
            outfile = os.path.splitext(file)[0] + ".jpeg"
        if file.endswith(".png"):               
            outfile = os.path.splitext(file)[0] + ".png"
        newFolder = os.path.join(resizedFolder, outfile)                    
        try:
            img = Image.open(file)
            img.thumbnail(size)
            img.save(newFolder, "JPEG")
        except IOError as ioe:
            print("cannot resize", file)
            print(str(ioe))
