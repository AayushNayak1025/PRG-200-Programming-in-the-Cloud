# This program splits a bill among friends and randomly selects a lucky person who pays an extra amount.
import random

random.seed(42)

friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]
total_bill = 3750


def split_bill(friends, total):
    return total / len(friends)


def pick_lucky(friends):
    return random.choice(friends)


def final_summary(friends, total):
    share = split_bill(friends, total)
    lucky_person = pick_lucky(friends)

    print("Bill Summary")
    print("----------------")

    for friend in friends:
        print(friend, "pays NPR", share)

    # Local variable
    lucky_total = share + 50

    print("\nLucky Person:", lucky_person)
    print(lucky_person, "pays extra NPR 50")
    print("Total paid by", lucky_person, "=", lucky_total)


final_summary(friends, total_bill)