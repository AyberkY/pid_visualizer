"""
This is a part of my high school senior math project. This code is meant to connect to a balancing robot I built
through a hc-06 arduino bluetooth module, and visualize the robot's PID controller's P, I, and D term outputs.
However, the code only receives the robot's current angle, and integrates and differentiates it to display the 
I and D terms respectively, rather than actually sending the I and D term outputs through bluetooth.

Very clunky at the moment (low fps) because the matplotlib.animate() function deletes everything on the graph and re-plots from scratch.

author: Ayberk Yaraneri
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import serial

ser = serial.Serial('COM7', 9600, timeout = 1)		#Change comport accordingly to wherever the bluetooth module connected.

fig = plt.figure(figsize = (16, 6))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)
fig.subplots_adjust(left = 0.05, bottom = 0.05, right = 0.97, top = 0.97, hspace = 0.15)

integral = 0
lastTheta = 0
integrals = [0] * 500
derivatives = [0] * 500
proportionals = [0] * 500

Xs = []
for i in range(500):
	Xs.append(i)

def animate(i):

	global proportionals
	global Xs
	global integral
	global integrals
	global lastTheta
	global derivatives

	ser.write(chr(32))
	theta = float(ser.readline()[:5])

	proportionals = proportionals[1:] + [theta]

	integral += theta * 0.1
	integrals = integrals[1:] + [integral]

	derivative = theta - lastTheta
	derivatives = derivatives[1:] + [derivative]
	lastTheta = theta

	ax1.clear()
	ax2.clear()
	ax3.clear()

	ax1.set_ylim(-90, 90)
	ax1.plot(Xs, proportionals, linewidth = 0.6, color =  'blue')

	ax2.plot(Xs, integrals, linewidth = 0.6, color = 'green')

	ax3.plot(Xs, derivatives, linewidth = 0.6, color = 'red')


calibrated = False

while not calibrated:
	if ser.readline() == '1':		#The robot sends a '1' over bluetooth once it's done calibrating its gyro.
		calibrated = True

ani = animation.FuncAnimation(fig, animate, interval = 20)
plt.show()
