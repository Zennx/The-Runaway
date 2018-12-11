# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Antony",color="#5942f4",kind=nvl)
define c = Character("[name]",color="#1b4ea0",kind=nvl)
define t = Character(None,kind=nvl)
define name = "Player"

# The game starts here.
init python:
    config.developer="auto"

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

    a "Any idea?"

    menu:

        "Hack in.":
            jump choice2_yes

        "Find another way.":
            jump choice2_no

    label choice2_yes:

        $ menu_flag = True

        c "I think hack it in is a good idea."

        a "Knew you will always support me :)."

        a "Alright,I'll try."

        jump hackin

    label choice2_no:

        $ menu_flag = False

        c "Well..."

        c "I think it is better to find other ways in."

        a "Hmm...yeah."

        a "Let me look around."

        a "Oh no..."

        c "What [a]?"

        a "I..I.."

        a "I was surrounded by zombies..."

        menu:

            "Run.":
                jump choice3_yes

            "Just DIEE.":
                jump choice3_no

        label choice3_yes:

            $ menu_flag = True

            c "RUNNNN,[a]!"

            a "I...I can't..."

            c "Wait...what?Why?"

            a "I have nowhere to run..."

            a "I...I am sorry..."

            a "Goodbye my frien-"

            jump gameover

        label choice3_no:

            $ menu_flag = False

            c "Very good..."

            a "W-what?"

            c "Don't you get it?"

            a "No...It can't be..."

            c "How pathetic..."

            c "Just..."

            c "{color=#ff0000}DIE NOW ALREADY!{/color}"

            a "..."

            a "Alright my friend..."

            a "AHHHHHHHHHHH--"

            "Monster..."

            "Why."

            "Why do you do this..."

            "You murderer..."

            "You don't even try."

            "To save him..."

            return

            jump choice3_done

        label choice3_done:

        "Good"

        jump choice2_done

    label choice2_done:

    "continue hwew"

label hackin: #Hack in choice.

    a "Just need a little more time..."
    
    a "And...Done!"

    c "Great!"

    a "Now let's go in."

    a "What a scarry corridor..."

    a "So dark..."

    return




label gameover: #Gameover texts

    play sound "mus/alert1.ogg"
    t "{color=#ffe900}--RECONNECTING--{/color}"

    play sound "mus/alert2.ogg"
    t "{color=#ff0000}--ERROR-DISCONNECTED--{/color}"

    "Seems that..."

    "[a] have died..."

    "You have failed your mission,[c]."

    "But don't give up just yet!"

    "You can do this."

    "Believe in yourself,[c]!"

    "Stay determined..."

    # This ends the game.
    
    return
