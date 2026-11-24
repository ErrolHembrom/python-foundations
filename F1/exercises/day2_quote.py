# Day 2: print, input and f-strings
# (Practice numbers only.)
#
# Write a "price quote" program that:
#   1. asks: "Your name? "
#   2. asks: "Price per user per month? "  (it can have decimals, e.g. 12.5)
#   3. asks: "Number of users? "            (a whole number)
#   4. works out the monthly and yearly cost
#   5. prints a quote using f-strings, money with 2 decimal places and a thousands comma
#   6. prints how many characters are in the name, using len()
#
# Remember: input() always gives back TEXT. Convert with float() or int() before doing maths.
#
# Expected output when you type Errol, 12.5 and 9:
# Your name? Errol
# Price per user per month? 12.5
# Number of users? 9
# --------------------
# Quote for Errol
# Monthly: $112.50
# Yearly:  $1,350.00
# --------------------
# (Your name has 5 letters.)

# Your code below this line

name = input("What is your name: ")
product_cost = float(input("How much do you pay for the service: "))
users = int(input("Number of active users: "))
monthly_cost = product_cost * users
yearly_cost = monthly_cost * 12
print(f"Hello {name}, the product costs ${product_cost:.2f}. For {users} users, the cost will be ${monthly_cost:,.2f} per month and ${yearly_cost:,.2f} yearly.")
print(f"Your name {name} has {len(name)} characters")
