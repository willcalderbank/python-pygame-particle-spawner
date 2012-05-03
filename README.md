python-pygame-particle-spawner
==============================

Possibly one of the most pointless pygame programs ever created, written in an a few hours just to see how pygame works. If nothing else it looks pretty.

How it works/structure
======================

X number of points are created each one of these has a "track", these tracks are straight lines orginating from one point radiating randomly outwards, this point is the center point for the spawner. The points also have a ttl/distance to live, randomly assigned to them when created up to a maximum stated number.

For each new clock tick these points are moved alone their track a distance C then redrawen, if they have travelled further than there ttl they are removed and deleted. 

Points are randomly created thoughout the running of the program based on a random number that is generated at each clock tick.

The chance of a point being created is easily changed, along with the colour, size and max ttl.

The center point of the spawner can be moved with a mouse click

(Wow that was a lot of documentation for something so small and probably be forgot about)