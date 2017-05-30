#Simple Python Programs
#https://wiki.python.org/moin/SimplePrograms

#Loop
#List of friends, each within single quotes, list in brackets
#For each value of 'friends', print iteration number and name of friend taken from list.
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print "iteration {iteration} is {name}".format(iteration=i, name=name)
    
#Looping assignment
#This one confuses me a bit.  There is a list of two items, "parents" and "babies"
#Assigned 1 and 1.  When babies are les than 100, you print a line.
#Something in here, however, steps up this number.  I need to think about this.
#Also, {0}
parents, babies = (1, 1)
while babies < 100:
    print 'This generation has {0} babies'.format(babies)
    parents, babies = (babies, parents + babies)
    
#Import
#Import a file.  For each string in the list, check for a match.
#If it matches the insane regular expression, print the number and say it's a valid number. 
#Expression says, it should be 3 numbers, then a dash, then 4 more numbers.
#If it's not, say it's not.
import re
for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print test_string, 'is a valid US local phone number'
    else:
        print test_string, 'rejected'

#Lists with math and adding.
#Starts with lists of products and prices
#Then indicates the combination of those products (what, how many)
#Then it prints the expression with the total amount from an equation.
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print 'I owe the grocer $%.2f' % grocery_bill

#Time printing
#Import a file with local times.
#Indicate the time each activity is taking place.
#Don't understand time_now.tim_hour
#Make a decision and print text based on the combination of those pieces of info (time
#that things happen, what time it is now.

from time import localtime

activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting' }

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
        break
else:
    print 'Unknown, AFK or sleeping!'
    
#This one is classes. I feel like I need this function, but I don't know what it is.
class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0
my_account = BankAccount(15)
my_account.withdraw(5)
print my_account.balance

#


