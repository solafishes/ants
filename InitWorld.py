#The function initialize a directed network for ants.
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def InitWorld(length=10,height=10,scale=1):
	G=nx.DiGraph()
	pos={}
	for x in range(int(length/scale)):
		for y in range(int(height/scale)):
			G.add_node((x,y))
			#G[(x,y)]['pos']=(x,y)
			pos[(x,y)]=(x,y)
	initial_density=1
	for x in range(int(length/scale)):
		for y in range(int(height/scale)):
			if 0<=(x+1)<=int(length/scale-1) and 0<=(y+1)<=int(height/scale-1):
				G.add_edge((x,y),(x+1,y+1),weight=initial_density)
			if 0<=x<=int(length/scale-1) and 0<=(y+1)<=int(height/scale-1):
				G.add_edge((x,y),(x,y+1),weight=initial_density)
			if 0<=(x+1)<=int(length/scale-1) and 0<=y<=int(height/scale-1):
				G.add_edge((x,y),(x+1,y),weight=initial_density)
			if 0<=(x-1)<=int(length/scale-1) and 0<=(y-1)<=int(height/scale-1):
				G.add_edge((x,y),(x-1,y-1),weight=initial_density)
			if 0<=x<=int(length/scale-1) and 0<=(y-1)<=int(height/scale-1):
				G.add_edge((x,y),(x,y-1),weight=initial_density)
			if 0<=(x-1)<=int(length/scale-1) and 0<=y<=int(height/scale-1):
				G.add_edge((x,y),(x-1,y),weight=initial_density)
			if 0<=(x+1)<=int(length/scale-1) and 0<=(y-1)<=int(height/scale-1):
				G.add_edge((x,y),(x+1,y-1),weight=initial_density)
			if 0<=(x-1)<=int(length/scale-1) and 0<=(y+1)<=int(height/scale-1):
				G.add_edge((x,y),(x-1,y+1),weight=initial_density)
	
	return G,pos




	