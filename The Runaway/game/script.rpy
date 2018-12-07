# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Antony",color="#5942f4",kind=nvl)
define c = Character("[name]",color="#1b4ea0",kind=nvl)

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

    play music "mus/Tention.ogg"

    "Hello."

    a "."

    a "."

    a "So...What is your name?"

    python:
        name = renpy.input("So...What is your name?")

    c "My name is [c]."

    a "Hello,[name]!"

    c "so...WHO THE HELL ARE YOU???"

    a "."

    a "{color=#ff0000}heh.{/color}"

    "hi."

    a "."

    a "."

    a "."

    # This ends the game.
    
    return
