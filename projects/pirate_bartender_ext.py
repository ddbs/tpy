#!/usr/bin/env python3

import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def ask_drink():
    """ask each of the questions in the questions dictionary, and gather the
    responses in a new dictionary."""
    answers = {}
    for k, v in questions.items():
        # ask for input based on questions dict
        a = input(v + " (y/n) ")
        # update answers in new dict with boolean
        if a == "y" or a == "Y":
            answers[k] = True
        else:
            # do nothing because boolean is not iterable
            continue
    return answers


def construct_drink(answers):
    drink = []
    for k, v in answers.items():
        ingredient = k
        for k, v in ingredients.items():
            if k == ingredient:
                random_ingredient = random.choice(v)
                drink.append(random_ingredient)
    return drink

def main_drink():
    """create drink, print name and composition"""
    answers = ask_drink()
    drink = construct_drink(answers)

    # set the drink name
    tastes = list(answers) # convert dict keys to list
    names = ['Chihuahua', 'Rotweiller', 'Labrador', 'Bulldog', 'Waterdog']
    random_taste = random.sample(tastes, 1)
    random_name = random.sample(names, 1)
    drink_name = random_taste[0].title() + " " + random_name[0].title()

    # print the drink details
    print("The contents of the " + drink_name + " are: " )
    for i in drink:
        print(i)

def main_loop():
    serving = True
    while serving:
        a = input("Do you want another drink?")
        if a == "y":
            main_drink()
        else:
            serving = False

if __name__ == "__main__":
    main_drink()
    main_loop()
