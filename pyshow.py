import sys
import pygame
import math

class pyshow:
	window=0
	size=0
	color=0
	origin=0
	destination=0
	richness=0
	def __init__(self,size,title,color,G,origin,destination,richness):
		
		#1.initialize window
		pygame.init()
		pygame.display.init()
		self.window=pygame.display.set_mode(size)
		self.size=size
		pygame.display.set_caption(title)
		self.color=color
		self.origin=origin
		self.destination=destination
		self.richness=richness
		self.window.fill(color)
		#2.  draw the network G as background
		#2.1 determine scale parameter
		x=max([node[0] for node in G.nodes()])+1
		y=max([node[1] for node in G.nodes()])+1
		scale=min(size[0]/x,size[1]/y)
		offsetX=(size[0]-x*scale)/2
		offsetY=(size[1]-y*scale)/2
		#2.2 draw edges
		count=0
		edge_group=int(G.number_of_edges()*0.02)
		for edge in G.edges():
			weight=G[edge[0]][edge[1]]['weight']
			edge_color=(0,0,128)
			start_pos=(edge[0][0]*scale+offsetX,edge[0][1]*scale+offsetY)
			end_pos=(edge[1][0]*scale+offsetX,edge[1][1]*scale+offsetY)
			pygame.draw.line(self.window,edge_color,start_pos,end_pos,weight)
			count=count+1
			if count%edge_group==0:
				pygame.display.update()
		pygame.display.update()
		
		#print origin and destination
		pygame.draw.circle(self.window, (255,0,0), (origin[0]*scale+offsetX,origin[1]*scale+offsetY), 5, 0)
		for d in destination:
			#r=int(8*float(richness[destination.index(d)])/sum(richness))
			pygame.draw.circle(self.window, (255,0,0), (d[0]*scale+offsetX,d[1]*scale+offsetY), 8, 2)
		
		for edge in G.edges():
			weight=G[edge[0]][edge[1]]['weight']
			start_pos=(edge[0][0]*scale+offsetX,edge[0][1]*scale+offsetY)
			end_pos=(edge[1][0]*scale+offsetX,edge[1][1]*scale+offsetY)
			pygame.draw.line(self.window,self.color,start_pos,end_pos,weight)
		pygame.display.update()
		#print pygame.font.get_default_font()
	def update(self,G,ite):
		#font=pygame.font.SysFont(40)
		text="Ant Viz: Iteration #"+str(ite)
		x=max([node[0] for node in G.nodes()])+1
		y=max([node[1] for node in G.nodes()])+1
		scale=min(self.size[0]/x,self.size[1]/y)
		offsetX=(self.size[0]-x*scale)/2
		offsetY=(self.size[1]-y*scale)/2
		self.window.fill(self.color)
		pygame.display.set_caption(text)
		
		pygame.draw.circle(self.window, (255,0,0), (self.origin[0]*scale+offsetX,self.origin[1]*scale+offsetY), 5, 0)
		for d in self.destination:
			#r=int(8*float(self.richness[self.destination.index(d)])/sum(self.richness))
			pygame.draw.circle(self.window, (255,0,0), (d[0]*scale+offsetX,d[1]*scale+offsetY), 8, 2)
			
		#self.window.blit(text,(self.size[0]-50,50))
		for edge in G.edges():
			weight=G[edge[0]][edge[1]]['weight']
			edge_color=(0,0,128)
			start_pos=(edge[0][0]*scale+offsetX,edge[0][1]*scale+offsetY)
			end_pos=(edge[1][0]*scale+offsetX,edge[1][1]*scale+offsetY)
			if weight>=1:
				pygame.draw.line(self.window,edge_color,start_pos,end_pos,int(math.floor(weight)))
			else:
				pygame.draw.line(self.window,self.color,start_pos,end_pos,1)
		pygame.display.update()
		
#pygame.draw.line(window,(255,255,255),(0,0),(30,50))
#pygame.display.update()

