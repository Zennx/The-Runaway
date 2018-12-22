# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Antony",color="#5942f4",kind=nvl)         #purple
define c = Character("[name]",color="#1b4ea0",kind=nvl)         #blue
define p = Character("Prof.Coloader",color="#ff0000",kind=nvl)  #red
define f = Character("Feleria",color="#bc7aff",kind=nvl)        #violet
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

    play sound "mus/alert1.ogg"
    t "{color=#ff0000}--STATIC--{/color}"

    play sound "mus/alert1.ogg"
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

            jump gameover

        label choice3_done:

        "Hello hacker lol"

        jump choice2_done

    label choice2_done:

    "Why are you here,hacker?"

    python:
        renpy.quit()

label hackin: #Hack in choice.

    a "Just need a little more time..."
    
    a "And...Done!"

    c "Great!"

    a "Now let's go in."

    a "What a scarry corridor..."

    a "So dark..."

    a "So moist..."

    a "Gross..."

    a "I'm feeling dizzy..."

    a "Oh no..."

    a "AHHHHHHHHHHHHHHH"

    c "[a] what happened?"

    a "I fell..."

    c "Are you alright?"

    a "Yeah...I guess."

    a "It hurts a little."

    a "Aww my head..."

    play sound "mus/alert1.ogg"
    t "{color=#ffe900}[a] fainted.{/color}"

    c "[a]?"

    a "Uhh...Where am I?"

    c "You fainted,[a].Are you alright?"

    a "I-I'm alright now,thanks..."

    a "B-but where am I???"

    a "This place...it's so strange..."

    a "It's so dim..."

    a "Why am I imprisoned in..."

    a "Something like a glass tube???"

    a "What is going on..."

    p "Greetings..."
    
    a "Wh-who are you???"

    p "Fear not,my friend..."

    p "I am [p]."

    p "Now you will be my experiment material."

    p "HAHAHAHAHAHAHAHAHA"

    a "No...nononono."

    p "I can't wait MUAHAHAHA..."

    a "..."

    a "So what are you going to do to me?"

    p "Why?Interested?"

    a "..."

    p "Haha...you will know soon,very soon my friend..."

    p "I should go and prepare..."

    p "I'll be back."

    p "HAHAHAHAHAHA"

    a "That guy is crazy!"

    a "Uhhh what should I do..."

    a "What should I do???"

    menu:

        "Escape.":
            jump choice4_yes

        "No idea.":
            jump choice4_no

    label choice4_yes:

        c "Try to escape,fast!"

        jump escapecell

    label choice4_no:

        $ menu_flag = False

        c "I...have no idea."

        jump noidea

    "Hii hacker ahahaha,feelin lost yet?"

    return

label escapecell:

    a "There's no way I can break out..."

    c "There must be something..."

    a "Hmm let me think..."

    c "What do you have on you?"

    a "Hmm...Let me see."

    a "Cutter and screwdrivers seems useful."

    a "Sure it does,now let's see what I can do..."

    a "Yahhhh!"

    a "Whoo im out!"

    c "Now run!"

    a "I am!"

    a "Hmm?"

    a "Is that?"

    a "My friend???"

    a "I have to save her!"

    menu:

        "Save her.":
            jump choice5_yes

        "Don't save her.":
            jump choice5_no

    label choice5_yes:

        c "Yeah we should!"

        jump save

    label choice5_no:

        $ menu_flag = False

        c "No we should'nt."

        jump dontsave

    "Hii hacker ahahaha,feelin lost yet?"

    return

label noidea:

    a "Now what???"

    a "..."

    p "I am back..."

    p "So,are you ready for an experiment?"

    a "N-no..."

    p "Aww too bad."

    p "We will start now."

    a "NOOOO"

    a "AHHHHHHHHHHHHHHHHH"

    jump gameover

label save:

    a "Yeah."

    a "She's my friend."

    a "We have to."

    c "Right."

    a "Hang tight I'm saving you,[f]!"

    f "[a]!"

    a "Yahhhhh!"

    t "Glass shattering is heard."

    a "You're saved!"

    f "T-thanks,[a]."

    f "How do you know I'm here and why are you here?"

    a "No time to explain..."

    a "We need to destroy this lab."

    f "I can help."

    a "Great!I appreciate that,[f]."

    f "Hey it's no-"

    a "We should get going."

    f "Right."

    f "The lab should be-"

    f "*gasp* Oh no..."

    p "Greetings..."

    p "You guys were good at running away huh."

label dontsave:

    a "W-what?Why not?"
    
    a "She's my friend..."

    c "I don't trust if she is still herself..."

    a "No."

    c "[a]."

    a "..."

    a "Right..."

    a "You got a good point."

    a "Let's move on."

    a "No..."

    a "The corridor is blocked."

    c "Find other routes then."

    t "When [a] turned around."

    t "[p] is behind him."

    t "There is no escape."

    p "There is no running now."

    p "Now..."
    
    p "{color=#ff0000}I SHALL PROCEED ON MY EXPERIMENT ON YOU!{/color}"

    p "{color=#ff0000}MUAHAHAHAHAHAHAHA{/color}"

    a "NOOOOOOOOOOOOO"

    a "You...you MONSTER!"

    p "So what?"

    a "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH--"

    jump gameover

    return

label gameover: #Gameover texts
    
    play music "mus/silence.ogg"

    play sound "mus/alert1.ogg"
    t "{color=#ffe900}--RECONNECTING--{/color}"

    play sound "mus/alert2.ogg"
    t "{color=#ff0000}--ERROR-DISCONNECTED--{/color}"

    python:
        renpy.music.play("mus/gameover.ogg",loop=None)

    "Seems that..."

    "[a] have died..."

    "You have failed your mission,[c]."

    "But don't give up just yet!"

    "You can do this."

    "Believe in yourself,[c]!"

    "Stay determined..."

    stop music fadeout 0.3

    # This ends the game.
    
    return
