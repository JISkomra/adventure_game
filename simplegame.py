import time
import random


monsters = ("Dragon", "Meeanie-Man", "Tinkie Winkie")


evil_monster = random.choice(monsters)


def print_sleep(message):
    print(message)
    time.sleep(2)


def ending():
    print_sleep("Thanks for playing!")


def play_again():
    while True:
        pa = input("Would you like to play again? (y/n)\n")
        if pa == "y":
            print_sleep("Excellent! Restarting the game ...")
            adventure_game()
            break
        elif pa == "n":
            ending()
            break
        else:
            print_sleep("Sorry, I don't understand.")
            play_again()


def intro(items, evil_monster):
    print_sleep("You find yourself standing in an open field, filled with " +
                "grass and yellow wildflowers. Rumor has it that a % s is " +
                "somewhere around here, and has been terrifying the nearby" +
                " village. In front of you is a house. To your right is a" +
                " dark cave. In your hand you hold your trusty" +
                " (but not very effective) dagger." % evil_monster)


def options(items, evil_monster):
    choice = input(
        "Enter 1 to knock on the door of the house. Enter 2 to peer into the" +
        " cave. What would you like to do? (Please enter 1 or 2.)\n")
    if choice == "1":
        house(items, evil_monster)
    elif choice == "2":
        cave(items, evil_monster)
    else:
        print_sleep("Sorry, I don't understand.")
        options(items, evil_monster)


def house(items, evil_monster):
    print_sleep("You approach the door of the house. You are about to knock" +
                " when the door opens and out steps a %s. " +
                "Eep! This is the %s's house!" % (
                    evil_monster, evil_monster))
    choice = input(
        "The %s attacks you! Would you like to (1) fight or (2)" +
        " run away?\n" % evil_monster)
    if choice == "1":
        if "Sword of Ogoroth" in items:
            print_sleep("As the %s moves to attack, you unsheath " +
                        " your new sword. The Sword of Ogoroth" +
                        " shines brightly in " +
                        " your hand as you brace yourself for" +
                        " the attack. But " +
                        " the %s takes one look at your shiny new" +
                        " toy and runs " +
                        " away! You have rid the town of the %s." +
                        " You are victorious!" % (
                            evil_monster, evil_monster, evil_monster))
            play_again()
        elif "Sword of Ogoroth" not in items:
            fight_house(items, evil_monster)
    elif choice == "2":
        print_sleep(
            "You run back into the field. Luckily, you don't seem " +
            " to have been followed.")
        options(items, evil_monster)
    else:
        print_sleep("Sorry, I don't understand.")
        house(items, evil_monster)


def fight_house(items, evil_monster):
    print_sleep("You feel a bit under-prepared for this, what with only " +
                "having a tiny dagger.")
    fight_or_flight = input("Would you like to (1) fight or (2) run away?\n")
    if fight_or_flight == "1":
        print_sleep(
            "You do your best... but your dagger is no match for the %s. You" +
            " have been defeated!" % evil_monster)
        play_again()
    elif fight_or_flight == "2":
        print_sleep(
            "You run back into the field. Luckily, you don't" +
            " seem to have been followed.")
        options(items, evil_monster)
    else:
        print_sleep("Sorry, I don't understand.")
        fight_house(items, evil_monster)


def cave(items, evil_monster):
    if "Sword of Ogoroth" in items:
        print_sleep("You peer cautiously into the cave. You've" +
                    " been here before, and gotten all the good stuff. It's" +
                    " just an empty cave now. You walk back out to the field.")
        options(items, evil_monster)
    else:
        print_sleep("You peer cautiously into the cave. It turns" +
                    " out to be only a very small cave. Your eye catches a" +
                    " glint of metal behind a rock. You have" +
                    " found the magical" +
                    " Sword of Ogoroth! You discard your silly old " +
                    "dagger and take the sword with you.")
        items.append("Sword of Ogoroth")
        print_sleep("You walk back out to the field.")
        options(items, evil_monster)


def adventure_game():
    items = []
    intro(items, evil_monster)
    options(items, evil_monster)


adventure_game()
