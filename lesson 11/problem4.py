print('-'*65)
print('Booze Bot:')
age = input('What is your age today?')
age = int(age)
year = 21 - age
if age > 20:
 drink = input('What would you like to order?')
 print('Please pay for ' + drink + '.')
else: 
	print('Come back in ' + str(year) + ' years.')