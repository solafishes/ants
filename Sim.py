#The function run the simulation for a given iteration time
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pygame
import time
import math
import sys
sys.path.append("/Users/lisiyu/Desktop/Network Generation/SingleOD")
from Ant import Ant
from pyshow import pyshow

def Sim(Iteration,origin,destination,richness,G,X,rate):
	currentIteration=1
	while currentIteration<= Iteration:
		print "Iteration "+str(currentIteration)+" is running"
		
		a=Ant(origin,destination,richness)
		
		while (a.get_reached()!=1):
			a.update_location(G)
			#if a.get_current_location()==destination:
			#	print 1
		
		print 'Iteration '+str(currentIteration)+": Destination reached!"
		a.update_density(G,rate)
		#print 'In iteration' +str(currentIteration)+", ant takes: " + a.
		X.update(G,currentIteration)
		currentIteration=currentIteration+1
	while True: 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				sys.exit(0)
	return G
			
			
	

	