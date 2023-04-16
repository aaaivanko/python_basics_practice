from random import randint, choice


class Die:

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        return randint(1, self.sides)


new_die = Die()

# lottery_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
# winning_ticket = []
#
# for item in range(4):
#     winning_ticket.append(choice(lottery_list))
#
#
# print(winning_ticket)


def lottery(user_ticket):
    lottery_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
    counter = 0
    active = True

    while active:
        winning_ticket = []
        counter += 1
        for item in range(4):
            winning_ticket.append(choice(lottery_list))
            print(winning_ticket)
        print(winning_ticket)
        if winning_ticket == user_ticket:
            active = False

    return f"The winning ticket has won {user_ticket} with {counter} attempt"


print(lottery([3, 5, 7, 9]))
