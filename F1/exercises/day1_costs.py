# Day 1: numbers, text and variables
# (Practice numbers only, not real vendor prices.)
#
# A CRM costs 14 dollars per user per month. A team has 6 users.
#
# Write code that:
#   1. stores the price in a variable called price_per_user
#   2. stores the team size in a variable called users
#   3. works out monthly_cost (price x users) and yearly_cost (monthly x 12)
#   4. a yearly plan gives 2 months free: work out yearly_plan_cost (monthly x 10)
#   5. works out saving (yearly_cost - yearly_plan_cost)
#   6. prints each result on its own line. For now, print the number on its own:
#      print(monthly_cost)
#
# Then answer these in comments at the bottom (try each one in the terminal first):
#   a. What does 17 // 5 give? And 17 % 5? What would you use each for?
#   b. What happens with print("Users: " + users)? Why? How do you fix it?
#   c. What does "-" * 20 print?
#
# Expected output:
# 84
# 1008
# 840
# 168

# Your code below this line

price_per_user = 14
users = 6
monthly_cost = price_per_user * users
yearly_cost = monthly_cost * 12
yearly_plan_cost = monthly_cost * 10
saving = yearly_cost - yearly_plan_cost

print(f"The CRM costs ${price_per_user}")
print(f"The total number of users in a team is {users}")
print(f"The monthly cost for {users} users is {monthly_cost}")
print(f"The yearly cost for {users} users is {yearly_cost}")
print(f"The cost of purchasing a yearly membership is {yearly_plan_cost}")
print(f"The saving from purchasing a yearly membership is {saving}")

# 17 // 5 gives: 3 because the integer division operator rounds down the answer. 17 % 5 gives 2, this is the modulo operator that gives remainder. The interger division can be used when the answer needs to be round down and the modulo operator can be used for confiming odd and even numbers.

# print("Users: " + users) gives a TypeError because Python does not allow concatenation of string with number, this can be fixed by changing the type of the interger 6 to a string using the str function.

# This prints -, 20 times.