# Saturday mini-project: Plan picker
# (Practice plans and prices only.)
#
# Practice plans (per user per month):
#   Free:     up to 2 users,  $0
#   Starter:  up to 5 users,  $10
#   Team:     up to 20 users, $18
#   Business: any size,       $25
#
# The program should:
#   1. ask for the number of users, repeating until it's a whole number of 1 or more
#   2. ask for the monthly budget, repeating until it's a whole number of 0 or more
#   3. pick the cheapest plan that allows that many users (if/elif/else)
#   4. print the plan, the monthly cost and the yearly cost (money to 2 decimal places)
#   5. say whether it fits the budget
#   6. print a small table: the cost of that plan for 1 to 5 more users than now
#      (use a for loop), so the team can see the cost if it grows
#   7. ask "Check another team? (y/n) " and start again on "y"; stop on anything else
#
# Example run:
# Users? 4
# Monthly budget? 30
# Plan: Starter ($10.00/user)
# Monthly: $40.00 | Yearly: $480.00
# Over budget by $10.00
# If you grow:
#   5 users: $50.00/month (Starter)
#   6 users: $108.00/month (Team)
#   7 users: $126.00/month (Team)
#   8 users: $144.00/month (Team)
#   9 users: $162.00/month (Team)
# Check another team? (y/n) n
# Goodbye!
#
# Step 6 is the hardest part: each "grow" line needs its own plan check.
# It's fine to repeat the if/elif block for now. Next week you'll learn functions,
# which remove that repetition.

# Your code below this line

