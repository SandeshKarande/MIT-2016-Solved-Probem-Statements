#Problem Statement:-Saving with Raise
        
        #Write a program to calculate how many months it will take you save up enough money for a down payment. 
#LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%).

#program should ask the user to enter the following variables:
        #1.The starting annual salary (annual_salary) 2
        #2.The percentage of salary to be saved (portion_saved) 
        #3.The cost of your dream home (total_cost) 
        #4.The semiannual salary raise (semi_annual_raise)
        

annual_salary = float(input("Enter your annual salary"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal"))
total_cost = float(input("Enter the cost of your dream home"))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal"))

portion_down_payment = total_cost * 0.25
current_savings = 0
rate = 0.04
months = 0

while current_savings < portion_down_payment:
    current_savings += (annual_salary/12) * portion_saved + current_savings * (rate/12)
    months += 1
    
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

print("Number of months: ", months)

#Test Case:-

        #Test Case 1 >>> 
                    #Enter your starting annual salary: 120000 
                    #Enter the percent of your salary to save, as a decimal: . 05 
                    #Enter the cost of your dream home: 500000 
                    #Enter the semiannual raise, as a decimal: .03 
                    #Number of months: 142
                    #>>>
        
        #Test Case 2 >>> 
                    #Enter your starting annual salary: 80000 
                    #Enter the percent of your salary to save, as a decimal: . 1 
                    #Enter the cost of your dream home: 800000 
                    #Enter the semiannual raise, as a decimal: .03 
                    #Number of months: 159 
                    #>>> 
        
        #Test Case 3 >>> 
                    #Enter your starting annual salary: 75000 
                    #Enter the percent of your salary to save, as a decimal: . 05 
                    #Enter the cost of your dream home: 1500000 
                    #Enter the semiannual raise, as a decimal: .05 
                    #Number of months: 261 
                    #>>>