#The user is prompted to enter values for the five inputs needed for the calculations
miles = input("Enter the daily mileage: ")
cpg = input("Enter the cost per gallon of gasoline: ")
mpg = input("Enter the average number of miles per gallon: ")
parking_fee = input("Enter the daily parking fee: ")
toll_cost = input("Enter the toll cost per day: ")

#The daily number of miles is divided by the number of miles per gallon of gasoline to calculate the number of gallons used daily
#Note: The daily number of miles is multiplied by 1.0 to allow the quotient to be any real number, not just an integer
number_gallons = (miles*1.0) / mpg

#The number of gallons used daily is multiplied by the cost per gallon to calculate the total daily cost of gasoline
total_gas_cost = (number_gallons) * cpg

#The total daily commute cost is calculated by taking the sum of the total gasoline cost, daily parking fee, and toll cost
total_daily_cost = total_gas_cost + parking_fee + toll_cost

#The total daily commute cost is displayed as long as no negative numbers are entered, otherwise an error message is displayed
#Note: The value for miles per gallon must be greater than zero to avoid division by zero
if (miles >= 0 and cpg >= 0 and mpg > 0 and parking_fee >= 0 and toll_cost >= 0):
    print "The total daily commute cost is: $", total_daily_cost

else:
    print "There are one or more invalid inputs. Make sure input values are greater than or equal to zero, and not zero for miles per gallon."
