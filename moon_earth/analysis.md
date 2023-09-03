## Analysis

To measure the accuracy and precision of the simulation of the simple moon-earth orbit, we need to
consider all possible facets of the simulation.

0. Is the general data right:

- Is the apogee at 405,000km?
- Is the perigree at 360,000km?
- Is the average 382,500km?

- Investigate the relationship between `dt` and the drift in energy (dE/dt) (Energy should be conserved)
- Explore other methods of differentiation that can allow for a larger `dt` while keeping dE/dt minimal.

1. Absolute distance

- What are the peaks and troughs of the elliptical over one orbit
- Do the peaks and troughs drift over many orbits?

2. Numerical drift

- If we take one point of the orbit, and then add a full period, how far off are we from the first point?
