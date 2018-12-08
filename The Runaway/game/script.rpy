# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Antony",color="#5942f4",kind=nvl)
define c = Character("[name]",color="#1b4ea0",kind=nvl)
define t = Character(None,kind=nvl)
define name = "Player"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene circuit

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    "-YEAR 201X-"

    "On year 2025."

    "A major zombie apocalypse have occured."

    "Fortunately,someone from the future..."

    "Have time travelled."

    "To came to give this an end."

    "He had fought his way up to the lab containing the virus."

    "He had faced and fought many problems and zombies. "

    "And now..."

    "In order to stop..."

    "This insanity."

    "This zombie apocalypse"

    "He needs your help."

    "He needs you..."

    "So,will you help him?"

    menu:

        "Yes, I will.":
            jump choice1_yes

        "No, I won't.":
            jump choice1_no

    label choice1_yes:

        $ menu_flag = True

        "Very well..."

        jump choice1_done

    label choice1_no:

        $ menu_flag = False

        "Well..."

        "Too bad."

        "You have no choice,it's your fate!"

        jump choice1_done

    label choice1_done:

    "Now,the future is in your hands."

    "Your choices matter..."

    "Good luck!"
 

    play music "mus/Tention.ogg"

    t "{color=#ff0000}--STATIC--{/color}"

    t "{color=#93abff}--INCOMING TRANSMISSION--{/color}"

    a "H-hello?"

    a "Anyone??"

    c "H-hi??"

    a "Oh what a relieve!"

    a "I was so scared that no one will recieve my signal."

    a "So...What is your name?"

    python:
        name = renpy.input("What is your name?")

    c "My name is [c]."

    a "Hello,[name]!"

    c "so...WHO THE HELL ARE YOU???"

    a "Ah apologize,I havn't introduced myself yet..."

    a "I am [a]."

    c "So where are you? "

    a "I'm outside of a building."

    a "The lab is in it."

    a "Ah,found the entrence!"

    a "And...It's lock."

    c "Predictable..."

    a "I guess lets hack our way in."

    # This ends the game.
    
    return
