# Day 3: True/False and if-else
# (Practice plans and prices only.)
#
# Practice plans:
#   Starter:  up to 5 users,  10 dollars per user per month
#   Team:     6 to 20 users,  18 dollars per user per month
#   Business: 21+ users,      25 dollars per user per month
#
# Write a program that:
#   1. asks for the number of users and a monthly budget (both whole numbers)
#   2. uses if / elif / else to pick the plan and its price
#   3. works out the monthly cost
#   4. prints the plan and cost, then either "Within budget" or
#      "Over budget by $X" (X = cost - budget)
#   5. extra: if users is 0 or less, print "Users must be at least 1" instead of a plan
#      (hint: put this check first)
#
# Expected output for 8 users, budget 120:
# Users? 8
# Monthly budget? 120
# Plan: Team at $18/user
# Monthly cost: $144
# Over budget by $24
#
# Expected output for 3 users, budget 50:
# Plan: Starter at $10/user
# Monthly cost: $30
# Within budget

# Your code below this line
starter_plan = 10
team_plan = 18
business_plan = 25

number_users = int(input("Provide the number of users: "))
monthly_budget = int(input("How much is the monthly budget: "))

if number_users < 1:
    print("Users must be at least 1")

elif number_users >= 1 and number_users <= 5:
    starter_monthly_cost = number_users * starter_plan
    if starter_monthly_cost <= monthly_budget:              
        print(f"Plan: Starter at ${starter_plan}/user \nMonthly cost: ${starter_monthly_cost} \nYou are within budget for the starter plan")
    else:
        starter_x = starter_monthly_cost - monthly_budget 
        print(f"Plan: Starter at ${starter_plan}/user \nMonthly cost: ${starter_monthly_cost} \nYou are over budget by ${starter_x}")
elif number_users > 5 and number_users <= 20:
    team_monthly_cost = number_users * team_plan
    if team_monthly_cost <= monthly_budget:
        print(f"Team plan at ${team_plan}/user \nMonthly cost: ${team_monthly_cost} \nYou are within budget for the team plan")
    else:
        team_x = team_monthly_cost - monthly_budget 
        print(f"Team plan at ${team_plan}/user \nMonthly cost: ${team_monthly_cost} \nYou are over budget by ${team_x}")
elif number_users > 20:
    business_monthly_cost = number_users * business_plan
    if business_monthly_cost <= monthly_budget:
        print(f"Business plan at ${business_plan}/user \nMonthly cost: ${business_monthly_cost} \nYou are within budget for the business plan")
    else:
        business_x = business_monthly_cost - monthly_budget 
        print(f"Business plan at ${business_plan}/user \nMonthly cost: ${business_monthly_cost} \nYou are over budget by ${business_x}")

