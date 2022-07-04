from PIL import ImageGrab

def Screenshot():
	try:
		screen = ImageGrab.grab()
		screen.save(r'C:\hesoyam8927163\sreenshot.jpg')
	except Exception as e:
		print(e)