print('-'*65)
print('Narrative Bot')
print()
name = input('Student Name:')
grade = input('Grade:')
grade = int(grade)
if grade > 65:
	print(name + ', your final grade is ' + str(grade) + '%.' + ' You have passed.')
else: 
	print(name + ', your final grade is ' + str(grade) + '%.' + ' You have failed.')