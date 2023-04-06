# rent car

# car = True

# while car:
#     car_name = str(input(f"Please write car name: \nIf you want to exit please write exit"))
#
#     if car_name == 'exit':
#         car = False
#     else:
#         print(f"Let me see if I can find you {car_name}")


# restaurant table

# active = True
#
# while active:
#     number_of_guests = int(input('Please write a number: '))
#     if number_of_guests > 8:
#         print(f"Sorry but you order for {number_of_guests} is too large we can accept just 8 person.")
#         active = False
#     else:
#         print(f"Your table for {number_of_guests} is ready!")

# even number

while True:
    number = int(input('Please write number: '))
    if number == 0:
        break
    elif number % 2 == 0:
        print(f"Even number")
    else:
        print(f"Odd")


