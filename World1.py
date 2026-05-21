from Stats import stats

#used for development only
print("Your health is", stats["health"])
print("Your water is", stats["water"])
print("Your food is", stats["food"])

print("Would you like to go left or right?")
print("Enter 1 for left 2 for right")
print("Enter 0 to go home - Development Only")
movement = int(input())
if movement == 1:
    print("Debug - left selected")
    exec(open('World2.py').read())
elif movement == 2:
    print("Debug - right selected")
    exec(open('World3.py').read())
elif movement == 0:
    exec(open('MainMenu.py').read())
else:
    print("Enter 1 or 2")