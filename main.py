print("welcome to the treasure isalnd")
print("Your mission is to find the treusure.")
choice1=input('You are on a cross road,where do you wna to go ? type "left" or "right"').lower()
if choice1 == "left":
 choice2=input('"Now you ahave come to lake what do you wana to do ? "swim" or "wait" for a boat.').lower()
 if choice2 == "wait":
    choice3=input('"now you are again on a cross road to win chose a door? type color of the door "red" , "blue", "yellow" ,').lower()
    if choice3 == "red":
       print("burned by fire, game over")
    elif choice3 == "blue":
       print("eaten by beasts, game over ")
    elif choice3 == "yellow":
       print("you find the treusre , you win")
    else:
       print("game over")
 elif choice2 == "swim":
    print("you are attacked by a trout, agme over")
 else:
    print("game over ")

else:
    print("game over, you are gone")


