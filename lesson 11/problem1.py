print('-'*65)
print('Is it Brick Bot:')
print()
temp = input('Temperature in Fahrenheit:')
temp = int(temp)
if temp > 32:
	print('It is not brick.')
else: 
	print('It is brick.')