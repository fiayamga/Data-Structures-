#list of available cars and their prices
#Github link: https://github.com/fiayamga/Data-Strucutures.git
    
cars={
      'Toyota Prius':5000,'Nissan Navara':6000,'Toyota Yaris':4000,
     'Kia Sportage':4000,'Honda Accord':3200,'Hyundai Elantra':5000,
     'Toyota Rav4':3400,'Ford Explorer':7000,'Bugatti Veyron':10000}
#get input for the name of the car
car_name=input('Please enter a car name: ')
#check if car_name is in the list of available cars
if car_name in cars:
    print('Yes')
    #if car name is present get its price
    car_price=cars[car_name]
    print(f'The price of {car_name} is {car_price}.')
else:
    #if car name is not in the available list,inform the user
    print(f'Sorry, {car_name} is not available')