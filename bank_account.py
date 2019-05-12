class BankAccount():
	balance = 0
	
	def __init__(self, name):
		self.name = name
		
	def __repr__(self):
		return self.name + " : " + str(float(self.balance))
		
	def show_balance(self):
		print(str(float(self.balance)))
		
	def deposit(self, amount):
		if amount < 0 or amount == 0:
			print("Error! You can not to deposit less or 0 amount of cash!")
			return
		else:
			print("You depositing " + str(float(amount)) + " amount of cash on your account.")
			self.balance += amount
			self.show_balance()
			
	def withdraw(self, amount):
		if amount > self.balance:
			print("Error! You can not to withdraw greater than amount on your account!")
			return
		else:
			print("You withdrawing " + str(float(amount)) + " amount from your account.")
			self.balance -= amount
			self.show_balance()
			
bank_account = BankAccount("Mr. Johnson")
print(bank_account)
bank_account.show_balance()
bank_account.deposit(1000)
bank_account.withdraw(505.95)
print(bank_account)

		
