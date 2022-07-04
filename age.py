driving = input('Have you ever driven a car? ')
if driving != 'Yes' and driving != 'No':
	print('Please key in "Yes" or "No"')
	raise SystemExit

age = input('How old are you? ')
age = int(age)
if driving == 'Yes':
	if age >= 18:
		print('You passed the test! ')
	else:
		print('It is strange that you have driven a car.. ')
elif driving == 'No':
	if age >= 18:
		print('You can try to have a license!')
	else:
		print('Then, wait a few years first...')

