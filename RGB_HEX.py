def rgb_hex():
	invalid_msg = "ERROR! Invalid data was entered!"
	red = int(input("Enter a RED value: "))
	if red < 0 or red > 255:
		print(invalid_msg)
	green = int(input("Enter a GREEN value: "))
	if green < 0 or green > 255:
		print(invalid_msg)
	blue = int(input("Enter a BLUE value: "))
	if blue < 0 or blue > 255:
		print(invalid_msg)
	val = (red << 16) + (green << 8) + blue
	hex_method = hex(val)
	hex_method = str(hex_method)
	print(hex_method[2:].upper())

def hex_rgb():
	hex_val = input("Enter a haxademical value: ")
	if len(hex_val) != 6:
		print("ERROR! Invalid data was entered!")
		return
	else:
		hex_val  = int(hex_val, 16)
	two_hex_digits = 2 ** 8
	
	blue = hex_val % two_hex_digits
	hex_val = hex_val >> 8
	
	green = hex_val % two_hex_digits
	hex_val = hex_val >> 8
	
	red = hex_val % two_hex_digits
	
	print(str(blue + green + red))

def convert():
	while True:
		option = input("Enter '1' to 'convert RGB to HEX'/enter '2' to 'conver HEX to RGB'/enter '0' for 'exit': ")
		if option == '1':
			rgb_hex()
		elif option == '2':
			hex_rgb()
		elif option == 'x':
			break
		else:
			print("ERROR! You must enter '1' or '2' or '0'!")
			continue
convert()
	
