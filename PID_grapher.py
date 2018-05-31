import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import serial

ser = serial.Serial('COM7', 9600, timeout = 1)

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
	if ser.readline() == '1':
		calibrated = True

ani = animation.FuncAnimation(fig, animate, interval = 20)
plt.show()

