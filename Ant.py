#Class ants
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time
import math
import sys
sys.path.append("/Users/lisiyu/Desktop/Network Generation/SingleOD")
from walkerrandom import Walkerrandom
import random

class Ant:
	origin=()
	destination=[]
	richness=[]
	current_location=()
	walk_history=[]        #record the history of walking from origin to destination
	previous_visit=()      #record the point previously visited since the current location
	density=0              #control the density of homocide when returning to home
	reached=0              # 0 if the ant is still in search for destination, 
                           # 1 if the ant has reached destination,proceed to update homocide
	final_stop=()
	
	def __init__(self,origin,destination,richness):   # init an ant
		self.origin=origin
		self.destination=destination                  # this record all the possible destination
		self.final_stop=random.choice(destination)    # this record the destination the ant head to!
		self.richness=richness
		self.current_location=origin
		self.walk_history.append(origin)
	
	def get_origin(self):					# used to return origin
		return self.origin
	
	def get_destination(self):             # used to retrun destination
		return self.destination
	
	def get_richness(self):
		d={i:self.richness[self.destination.index(i)] for i in self.destination}
		return 
    
	def get_current_location(self):        # used to return current location
		return self.current_location
	
	def set_current_location(self,point):	# update current location
		self.current_location=point
		
	def get_previous_visit(self):          # used to return previous visited point
		return self.previous_visit
		
	def set_previous_visit(self,point):	#update previously visited point
		self.previous_visit=point
	
	def get_reached(self):
		return self.reached
	
	def set_reached(self,value):
		self.reached=value
		
	def get_walk_history(self):				# used to get the walking history of this ant (allow revisit)
		return self.walk_history
	
	def update_walk_history(self,point):   # update history path: add a new point 
		self.walk_history.append(point)
	
	def get_walk_history_no_loop(self):        # return the walking history without loop
		history=self.get_walk_history()
		length=len(history)
		history_no_loop=[]
		i=0
		while (i<length):
			for j in range(length-1,i,-1):
				if (history[i]==history[j]):   # check for the largest possible loop
					i=j                          # if detected, remove all nodes from i 
					break
			
			history_no_loop.append(history[i])	
			i=i+1	
		return history_no_loop
	
	def update_location(self,G):
		if self.get_reached()!=1:
			#search for the next posible point
			current=self.get_current_location()
			d=self.final_stop
			neighbors=G.neighbors(current)
			#exclude the previous visited point
			previous=self.get_previous_visit()
			if previous in neighbors:
				neighbors.remove(previous)
			#calculate the probability of choosing each point
			#weight=density/(distance to destination+0.1)
			prob={}
			for point in neighbors:
				#calculate angle theta_to_destination
				CN=(point[0]-current[0],point[1]-current[1])
				CD=(d[0]-current[0],d[1]-current[1])
				cos=float(CN[0]*CD[0]+CN[1]*CD[1])/(pow(CN[0]*CN[0]+CN[1]*CN[1],0.5)*pow(CD[0]*CD[0]+CD[1]*CD[1],0.5))
				theta= math.acos(cos)
				if (theta-math.pi==0):
					w=0
				else:
					w= math.exp(theta/math.pi/(theta-math.pi))
				#calculate angle theta_from_last
				
				#calcuate weight for candidates of next position
				prob[point]=pow(G[current][point]['weight'],2)/\
				float(pow(pow((d[0]-point[0]),2)+pow((d[1]-point[1]),2),2)+0.1)*w
				#prob[point]=pow(G[current][point]['weight'],2)
				
				
			#make choice
			#print prob
			r=Walkerrandom(prob.values(),prob.keys())
			choice=r.random()
			#print choice
			#update ant status variable
			if choice==self.final_stop:
				#self.final_stop=choice
				self.set_reached(1)
			self.set_previous_visit(current)
			self.update_walk_history(choice)
			self.set_current_location(choice)
	
	def update_density(self,G,rate):
		if self.get_reached()==1:
			origin=self.get_origin()
			destination=self.final_stop
			trail=self.get_walk_history_no_loop()
			shortest_distance=math.sqrt(pow((origin[0]-destination[0]),2)+pow((origin[1]-destination[1]),2))
			trail_distance=0
			for i in range(0,len(trail)-1):
				trail_distance=trail_distance+\
				math.sqrt(pow((trail[i][0]-trail[i+1][0]),2)+pow((trail[i][1]-trail[i+1][1]),2))
			
			r=float(self.richness[self.destination.index(destination)])/sum(self.richness)
			self.density=pow(float(shortest_distance)/trail_distance,2)*r*len(self.richness)
			
			for edge in G.edges():
				G[edge[0]][edge[1]]['weight']=rate*G[edge[0]][edge[1]]['weight']
			for i in range(0,len(trail)-1):
				G[trail[i]][trail[i+1]]['weight']=G[trail[i]][trail[i+1]]['weight']+self.density
	
	