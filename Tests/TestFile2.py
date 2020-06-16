#exec("TestFile1.py")
#print(X)

#import TestFile1 as TF1 ## this is how you import from separate files make sure to not put '.py'
#print(TF1.Variable1) # also if you use anything from a separate file instead of Variable1 it's called TF1.Variable1
import os
import sys
import pygame
import TestFile1 as TF1
print(TF1.X)
