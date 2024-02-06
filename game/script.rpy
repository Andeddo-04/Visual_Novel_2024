# ---------------------------------------------------
# --- ASSOCIATION DES IMAGES AVEC LES PERSONNAGES ---
# ---------------------------------------------------
image q:
    ""

image c:
    ""

# ----------------------------------------------
# --- ASSOCIATION DES IMAGES AVEC LES SCENES ---
# ----------------------------------------------
image f:
    ""

image g:
    ""

# --------------------------------
# --- CREATION DES PERSONNAGES ---
# --------------------------------
define e = Character('', color="#c8ffc8")

# ------------------------------
# --- INITIALISATIN DU TIMER ---
# ------------------------------
init:
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0


# Le jeu commence ici
label start:

    e "Vous venez de créer un nouveau jeu Ren'Py."

    e "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"
    
    jump questionTime1


    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0



    screen countdown:
        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
            ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

        bar value time range timer_range xalign 0.5 yalign 0.5 xmaximum 500 at alpha_dissolve 
            # ^This is the timer bar.
            
    label questionTime1:
        
        label menu1:
            $ time = 5                                     ### Durée globale du timer
            $ timer_range = 5.1                              ### nombre de tick a laquelle le timer s'écoule
            $ timer_jump = 'menu1_slow'                    ### revoi a un x label a la fin du timer
            show screen countdown                          ### call and start the timer

            menu:
                "Test du timer":
                    #play sound click
                    hide screen countdown                  ### stop the timer
                    jump suite

        label menu1_slow:
            e "defeat"
            jump suite

    
    label suite:

        e "victory"
    
    
    return



"""
# Main code
label start:

    scene Athena:
        xalign 0.5
        yalign 0.5

    athena "Bonjour. Je suis Athéna."
    athena "Je vous accompagnerai durant ce voyage."

    menu:

        athena "Êtes-vous prêt ?"

        "Oui.":
            jump depart

        "Non.":
            jump attente

    label depart:

        $ menu_flag = True

        athena "Bien. C'est parti !"

        jump suite

    label attente:

        $ menu_flag = False

        athena "Très bien, faite moi signe quand vous serez prêt."

        menu:

            "Je suis prêt.":

                jump depart

            "Je doit encore me preparer.":

                jump attente

    label suite:

        # ... the game continues here.

    
return
"""