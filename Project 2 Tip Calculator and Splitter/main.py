#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to Tip Calculator")
total_bill = float(input("Enter total bill : \n"))
tip = int(input("Enter tip in percentage : \n"))
num_of_persons = int(input("Enetr number of people paying : \n"))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
tip_amount = total_bill * (tip/100)
Total_bill_with_tax = total_bill + tip_amount
each_person_pay = round(Total_bill_with_tax / num_of_persons,2)
print(f"Each Person Pays : {each_person_pay}")
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
