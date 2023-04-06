# guests

guests = ['Bob', 'MArlin', 'Filip', 'George', 'Marly']

for num, guest in enumerate(guests):
    print(f"Hello, {guest}")
    if num == 2:
        print(f"Sorry but {guests[1]} will not be absent on the dinner.")
        guests.pop(1)
        guests.insert(1, 'Terry')


print(f"Sorry but {guests[1]} will not be absent on the dinner.")
print(guests)

