mad_libs_list_string = """\
    Just waking up in the morning, gotta ___ God
    I don't know but today seems kinda ___
    No barking from the ___, no smog
    And momma ___ a breakfast with no hog (yeah)
    I got my grub on, but didn't ___ out
    Finally got a call from a ___ I want to dig out (wassup?)
    Hooked it up for later as I hit the ___
    Thinking, "Will I ___ another twenty fo'?"
    I gotta go 'cause I got ___ a drop top
    And if I hit the switch, I can make the ___ drop
"""

print("\n\n")

mad_libs_list = mad_libs_list_string.split("\n")

for sentence in mad_libs_list:
    s = sentence.strip()
    print(s)
    word = input("Enter a word to replace the '___' place: ")
    s = s.replace("___", word)

    print(f"The new sentence is '{s}'")
    print("-"*(len(s)+len("The new sentence is ")))
