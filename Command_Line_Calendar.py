from time import sleep, strftime

user_name = "Roma"

calendar = {}

def welcome():
	print("Hello " + user_name.title())
	print("Calendar is opening...")
	sleep(1)
	print("The current date: " + strftime("%A-%d %B-%Y"))
	print("The current time: " + strftime("%H:%M:%S"))
	sleep(1)
	print("What would you like to do ?")
	
def start_calendar():
	welcome()
	start = True
	while start:
		user_choice = input("Enter 'A' for 'Add' / 'U' to 'Update' / 'V' to View / 'D' to 'Delete' / 'X' to 'Exit': ")
		user_choice = user_choice.upper()
		if user_choice == 'V':
			if len(calendar.keys()) < 1:
				print("Calendar is empty!")
			else:
				print(calendar)		
		elif user_choice == 'U':
			if len(calendar.keys()) < 1:
				print("Calendar is empty!")
			else:
				date = input("What date do you want to update(DD/MM/YYYY) ? ")
				update = input("Enter the update: ")
				for d in calendar.keys():
					if date == d:
						calendar[date] = update
						print("Date is successfully updated!")
						print(calendar)
					else:
						print("Entered invalid date!")	
		elif user_choice == 'A':
			date = input("Enter date(DD/MM/YYYY): ")
			event = input("Enter event: ")
			if len(date) != 10 or int(date[6:]) < int(strftime("%Y")):
				print("Entered invalid date!")
				try_again = input(("Try again ? (Enter 'Y' or 'N') "))
				try_again = try_again.upper()
				if try_again == 'Y':
					continue
				else:
					start = False
			else:
				calendar[date] = event
				print("Date and event is succesfull added!")
				print(calendar)	
		elif user_choice == 'D':
			if len(calendar.keys()) < 1:
				print("Calendar is empty!")
			else:
				date = input("Enter date: ")
				for d in calendar.keys():
					if date == d:
						del calendar[d]
						print("Date was successfully deleted!")
						print(calendar)
					else:
						print("Entered invalid event!")		
		elif user_choice == 'X':
			start = False
		else:
			print("Entered invalid command!")
			start = False
			
start_calendar()
				
				
			
			
			


