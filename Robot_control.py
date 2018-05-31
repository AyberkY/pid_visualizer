from pynput
import keyboard
import serial

ardu = serial.Serial('com5', 9600, timeout = 1)

print('connected')

pressedKey = 0

def on_press(key):
	global pressedKey

	if key == keyboard.Key.right:
		ardu.write(chr(1))
	elif key == keyboard.Key.left:
		ardu.write(chr(2))
	elif key == keyboard.Key.up:
		ardu.write(chr(4))
	elif key == keyboard.Key.down:
		ardu.write(chr(8))
	elif key == keyboard.Key.esc:
		ardu.write(chr(16))
		ardu.close()
		return False

def on_release(key):
	ardu.write(chr(16))

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
	listener.join()


  