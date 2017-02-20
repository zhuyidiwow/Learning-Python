'''
5.2 
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown.
'''

largest_number_so_far = None;
smallest_number_so_far = None;

while True:
	inp = raw_input("Enter an integer: ")

	if inp == "done":
		break

	try:
		number = int(inp)
	except:
		print "Please enter an integer or 'done'"
		continue

	if largest_number_so_far is None:
		largest_number_so_far = number
	elif number > largest_number_so_far:
		largest_number_so_far = number

	if smallest_number_so_far is None:
		smallest_number_so_far = number
	elif number < smallest_number_so_far:
		smallest_number_so_far = number

print "Largest number:", largest_number_so_far
print "Smallest number:", smallest_number_so_far



