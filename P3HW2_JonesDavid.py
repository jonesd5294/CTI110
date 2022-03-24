import math
#CTI-110
#P3HW2-Pizza Order
#David Jones
#3-24-2022
#

#Variables
#Get number of students and how many people per pizza
tax_amount = float(.06)
pizza_cost = int(5)
students = int(input('How many students do you want to order pizza for? '))
sharing = float(input('Enter number of people sharing a pizza (1.5, 2 or 3): '))

#If else statements and calculations
if (sharing == 1.5) or (sharing == 2) or (sharing == 3):
    pizzas = students / sharing
    pizzas = math.ceil(pizzas)
    
    sub_total = pizzas * pizza_cost
    tax = sub_total * tax_amount
    price = sub_total * tax
    print('----Pizza Order--------')
    print('Number of Students: ', students)
    print('Pizzas Needed : ', pizzas)
    print(f'Price: ${price:.2f}')
else:
    print('INVALID ENTRY \nShould have entered 1.5, 2 or 3 \n\nRun program again')




    
