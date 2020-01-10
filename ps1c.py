#Problem Statement:- Finding the right amount to save money.

         #write a program to calculate the best savings rate, as a function of your starting salary. 
#You should use bisection search to help you do this efficiently. 
#You should keep track of the number of steps it takes your bisections search to finish.


annual_salary = float(input("Enter the starting salary"))

semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000
steps = 0
current_savings = 0
low = 0
high = 10000
guess_rate = (high + low)//2

while abs(current_savings - total_cost * portion_down_payment) >= 100:
 
    current_savings = 0

    for_annual_salary = annual_salary
    rate = guess_rate/10000
    for month in range(36):

        if month % 6 == 0 and month > 0:
            for_annual_salary += for_annual_salary * semi_annual_raise
        
        monthly_salary = for_annual_salary/12
        
        current_savings += monthly_salary * rate + current_savings * r/12
    
    if current_savings < total_cost*portion_down_payment:
        low = guess_rate
        
    else:
        
        high = guess_rate
    guess_rate = (high + low) // 2
    steps += 1

    if steps > 13:
        break

if steps > 13:
    
    print("It is not possible to pay the down payment in three years")
    
else:
    
    print("Best savings rate", rate)
    print("Steps in bisection search", steps)
    
#Test Case:-
    
       #Test Case 1 >>> 
                   #Enter the starting salary: 150000 
                   #Best savings rate: 0.4411 
                   #Steps in bisection search: 12 
                   #>>>
                   
       #Test Case 2 >>> 
                  #Enter the starting salary: 300000 
                  #Best savings rate: 0.2206 
                  #Steps in bisection search: 9 
                  #>>> 
                  
      #Test Case 3 >>> 
                 #Enter the starting salary: 10000 
                 #It is not possible to pay the down payment in three years. 
                 #>>>