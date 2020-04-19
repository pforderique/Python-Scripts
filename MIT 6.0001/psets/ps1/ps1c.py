# # #####################
# # ps1c
# # PSET 1C
# # #####################

def bestSavingsRate():
    #knowns
    annual_salary = float(input("Annual salary: "))
    total_cost = 1000000
    portion_down_payment = 0.25
    total_down_payment = portion_down_payment*total_cost
    current_savings = 0
    #bisection search
    possible = True
    epsilon = 100
    low = 0
    high = 10000
    rate = (low+high)//2
    steps = 0
    current_savings = 0
    while abs(current_savings - total_down_payment) >= epsilon:
        current_savings = savingsIn3Years(rate, annual_salary)
        if(current_savings < total_down_payment):
            low = rate
        else:
            high = rate
        rate = (low+high)//2
        steps+=1
        if(rate == 9999 and steps > 1):
            possible = False
            break
    if not possible:
        print("It is not possible to pay the down payment in three years.")
    else:
        print("Best Savings rate:", rate/10000)
        print("Steps in bisection search:", steps)

def savingsIn3Years(savings_rate, annual_salary):
    #knowns
    monthly_salary = annual_salary/12
    semi_annual_raise = 0.07
    r = 0.04
    #calculates savings after 36 months
    portion_saved = savings_rate/10000
    current_savings = 0
    for month in range(1,37):
        current_savings+=(current_savings*r/12)
        current_savings+=portion_saved*monthly_salary
        if month%6 == 0:
            annual_salary+=semi_annual_raise*annual_salary
            monthly_salary = annual_salary/12
    return current_savings

bestSavingsRate()
        

