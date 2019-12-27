#Problem Statement:- House Huntng

        #Write a program to calculate how many months it will take you to save up enough money for a down payment. 
#You will want your main variables to be floats, so you should cast user inputs to floats.

#program should ask the user to enter the following variables: 
        #1.The starting annual salary (annual_salary) 
        #2.The portion of salary to be saved (portion_saved) 
        #3.The cost of your dream home (total_cost)

annual_salary = float(input("Enter your annual salary"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal"))
total_cost = float(input("Enter the cost of your dream home"))


portion_down_payment = total_cost * 0.25
current_savings = 0
rate = 0.04
months = 0

while current_savings < portion_down_payment:
    current_savings += (annual_salary/12) * portion_saved + current_savings * (rate/12)
    months += 1


print("Number of months: ", months)

#Test Case:-
        #Test Case 1 >>> 
                    #Enter your annual salary: 120000 
                    #Enter the percent of your salary to save, as a decimal: . 10 
                    #Enter the cost of your dream home: 1000000 
                    #Number of months: 183 
                    #>>>
                    
        #Test Case 2 >>> 
                    #Enter your annual salary: 80000 
                    #Enter the percent of your salary to save, as a decimal: . 15 
                    #Enter the cost of your dream home: 500000 Number of months: 105 
                    #>>>