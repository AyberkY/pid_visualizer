# My senior year math project.

This is a part of my high school senior math project. This code is meant to connect to a balancing robot I built
through a hc-06 arduino bluetooth module, and visualize the robot's PID controller's P, I, and D term outputs.
However, the code only receives the robot's current angle, and integrates and differentiates it to display the 
I and D terms respectively, rather than actually sending the I and D term outputs through bluetooth.

Very clunky at the moment (low fps) because the matplotlib.animate() function deletes everything on the graph and re-plots from scratch.

