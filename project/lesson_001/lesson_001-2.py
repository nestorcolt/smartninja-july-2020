# Flow control
##############################################################################################
# if / else
mood = input("How are you felling today? >> ")

"""
if mood == "happy":
    print("It is great to see you happy!")
else:
    print("Cheer up, mate!")
"""

if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "angry":
    print("Don't be mad.")
else:
    print("Cheer up, mate!")
