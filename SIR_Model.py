from PIL import Image
import glob

import random

import matplotlib as mpl

import matplotlib.pyplot as plt

import numpy as np

import networkx as nx

import imageio

import os

status = []  # A list that will correspond one-to-one with the node list, where each node's "status" will be saved as a 0, 1, 2,or 3

nodes = [] # List of each node (saved with numbers as names)

edges = []  # List of edges

networkxedges = [] # List of networkx friendly edges   # ANIMATION STUFF

images = [] # List of graph images #ANIMATION STUFF

Susceptible = 0
Infectious = 1
Recovered = 2
Dead = 3  ##

B = 0.05  # Chance of Infection

Y = 0.04 # Chance of Recovery

# DYING
D = 0.01  # Chance of death ##


### CONNECTIVITY-GRAPH MAKER

numnode = int(input('How many nodes do you want?'))

for h in range(0, numnode):  # Quick for loop that adds the desired number of nodes (with number names) to the node list
    nodes.append(h)

possedges = int(numnode * (numnode - 1) * 0.5) # Math equation to determine the maximum edges for the given nodes (complete graph)

print('The maximum number of edges is', possedges, ".")

numedge = int(input('How many edges?'))

for h in range(len(nodes)):

    row=[]

    for j in range(len(nodes)):

        row.append(0)
    
    edges.append(row)

for k in range(0, numedge):

    check = 0

    while check == 0:
   
        rancolumn=random.randint(0, len(nodes)-1)

        ranrow=random.randint(0, len(nodes)-1)
        
        if edges[ranrow][rancolumn]!=1 and edges[ranrow][rancolumn]!=1 and ranrow!=rancolumn:

                edges[ranrow][rancolumn]=1

                edges[rancolumn][ranrow]=1

                networkxedges.append((rancolumn,ranrow)) # ANIMATION STUFF
            
                check = 1

## Creation of Status List

for j in range(len(nodes)):
    status.append(Susceptible)

starternum = int(input("How many will start sick?"))

for n in range(starternum):

    checker = 0

    while checker == 0:

        starter = random.randint(0, len(nodes) - 1)

        if status[starter]!=Infectious:
    
            status[starter] = Infectious

            checker = 1

time = 0

t = []

z = []

w = []

y = []

e = []  ##

G = nx.Graph() # ANIMATION STUFF

G.add_nodes_from(nodes) # ANIMATION STUFF

G.add_edges_from(networkxedges) # ANIMATION STUFF

pos = nx.spring_layout(G, iterations=200)

statuschanged = []

numPic = 1 #GIF?
filenames = [] #GIF?

while Infectious in status:

    for f in status:

        statuschanged.append(f)

        colormap = [] # map of colors

    for i in range(len(nodes)):

        if status[i] == 0:
            colormap.append('blue')
        if status[i] == 1:
            colormap.append('orange')
        if status[i] == 2:
            colormap.append('green')
        if status[i] == 3:
            colormap.append('red')
    
    S = 0
    I = 0
    R = 0
    E = 0  ##

    infectable = []

    for g in range(len(nodes)):
            
        for u in range(0, g+1):
           
            if edges[g][u]==Infectious:
                if status[g]==Infectious and status[u]==Susceptible:
                    infectable.append(u)
                if status[g]==Susceptible and status[u]==Infectious:
                    infectable.append(g)
    
    # RECOVERING
    for j in range(len(status)):

        if status[j] == Infectious:

            rand = random.random()

            if rand < Y:
                status[j] = Recovered

    # DYING
    if time > 0:  ##

        for g in range(len(status)):  ##

            if status[g] == Infectious:  ##

                rando = random.random()  ##

                if rando < D:  ##

                    status[g] = Dead  ##

    # INFECTING
    for x in range(len(infectable)):

        ran = random.random()

        if ran < B:
            status[infectable[x]] = Infectious

    time = time + 1
    
    for i in range(len(status)):

        if status[i] == Susceptible:
            S = S + 1

    for i in range(len(status)):

        if status[i] == Infectious:
            I = I + 1

    for i in range(len(status)):

        if status[i] == Recovered:
            R = R + 1

    # DYING
    for i in range(len(status)):  ##

        if status[i] == Dead:  ##

            E = E + 1  ##

    t.append(str(time))

    y.append(S)

    z.append(I)

    w.append(R)

    e.append(E) ##

    if statuschanged != status:
        images.append(nx.draw(G, pos, node_color=colormap, with_labels=True))
        if(len(images)>0):
            filename = f'Graph{numPic}.PNG'
            plt.savefig(filename)
            plt.show(block=False)
            numPic+=1
            filenames.append(filename)
    statuschanged = []

colormap = [] # map of colors

for i in range(len(nodes)):

    if status[i] == 0:
        colormap.append('blue')
    if status[i] == 1:
        colormap.append('orange')
    if status[i] == 2:
        colormap.append('green')
    if status[i] == 3:
        colormap.append('red')
    
images.append(nx.draw(G, pos, node_color=colormap, with_labels=True))

filename = f'Graph{numPic}.PNG'
plt.savefig(filename)
plt.show(block=False)
filenames.append(filename)

print('Done in', time, 'steps.')

print('Death Rate is:', E / (len(nodes)-S))  ##

with imageio.get_writer('SIRSpread.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

for filename in set(filenames):
    os.remove(filename)