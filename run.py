#The function initialize a directed network for ants.
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.append("/Users/lisiyu/Desktop/Network Generation/SingleOD")
from InitWorld import InitWorld
from Ant import Ant
from Sim import Sim
from pyshow import pyshow
###################Simulation Control Variables#####################
X=80
Y=80

origin=(10,10)
destination=[(70,61),(20,40),(50,20),(30,70)]
richness=[8,2,5,7]

screen_size=(600,600)
title="Ant Viz"
color=(0,250,150)

d_rate=0.95
############################END#####################################
G,pos=InitWorld(length=X,height=Y)
X=pyshow(screen_size,title,color,G,origin,destination,richness)

N=Sim(1500,origin,destination,richness,G,X,d_rate)

#execfile("vidcap.py")
#Sim()


	