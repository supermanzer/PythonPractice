import datetime as dt


name = input('Enter your name: ')
age = input('Enter your age: ')
repeat = input('Enter an integer between 1 and 100: ')


year_100 = (100 - int(age)) + dt.date.today().year

message = f'Hi {name}!  It looks like you will turn 100 in {year_100}\n'
print(message*int(repeat))
