import bot_movement as bm
from ultrasonic import ultra

def check():
	if ultra() <= 20:
		return False
	else:
		return True