# SIR Model Simulation

This Python code creates a graph of a given number of nodes and edges, takes in a number of nodes to start infected, and runs a randomized simulation of that network under the SIR infection model.

In SIR, there are three states of nodes,

`Susceptible` - Uninfected, but may become infected

`Infected` - Infected and Contagious

`Recovered` - Recovered and no longer contagious

In this specific model there is also a Death state, where a node is no longer infetious and does not recover.  

During a given time step there is:

  - The chance an `S` node connected to an `I` node becomes infected (`B`)
  - The chance an `I` node recovers (`Y`)
  - The chance an `I` node dies (`D`)

This model can be adapted to account for re-infecting by adding a time dependent probability that an R node reverts to an S node, but that is not implemented here.

The program takes a good while to run depending on the size of the connectivity network, but produces an animated GIF of the course of infection in said network.

Color Map for GIF:

`Susceptible`: <span style="color:blue">Blue</span>

`Infected`: Yellow/Orange

`Recovered`: Green

`Dead`: Red
