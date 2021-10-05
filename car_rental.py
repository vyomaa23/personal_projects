# Car Rental
message = "Hello, nice to meet you."
message += "\nPlease tell us your name: "
name = input(message)
name = name.title()
print(f'\nHello, {name}!')

cars_available = {
                  'A': {'Title': 'Honda', 'rent_day': 50},
                  'B': {'Title': 'Subaru', 'rent_day': 25}, 
                  'C': {'Title': 'Chevy', 'rent_day': 55}, 
                  'D': {'Title': 'Ford', 'rent_day': 15},
                  'E': {'Title': 'Tesla', 'rent_day': 70}
                 }

car_brand = input('Okay, so what brand of car you are looking to rent? ')
car_brand = car_brand.title()

for keys, values in cars_available.items():
    if car_brand == values['Title']:
        tit = values['Title']
        rent = values['rent_day']
        print('Awesome, we have it available in our inventory!')
        days = input(f'\nSo, for how many days you are going to need it: ')
        days = int(days)
        total_rent = days*rent
        print(f'\nSo the total amount you will be required to pay for renting {tit} for {days} days would be: {total_rent} USD') 
        confirm = input("If you wanna go ahead and confim, type 'Yes'. Type 'No' to go back to chose some other car!\n")
        if confirm.title() == 'Yes':
            print('Congrats, you can come and pick it up tomorrow!')
        else:
            print("Please go back and start the process")
        break
    else:
        print("Sorry, the car you are looking for isn't available at the moment")
        break





    






