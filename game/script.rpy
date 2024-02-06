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
define narrateur_nvl = Character('Zhongli', color="#692d0b", kind= nvl)
define narrateur = Character('Zhongli', color="#692d0b")

# ------------------------------
# --- INITIALISATIN DU TIMER ---
# ------------------------------
init:
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0


# Le jeu commence ici
label start:

    narrateur_nvl "Vous venez de créer un nouveau jeu Ren'Py.{w} Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"
    
    nvl clear

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
            narrateur "defeat"
            jump end

    
    label suite:

        nvl hide dissolve
        nvl show dissolve
        narrateur "victory"


    label end:
        #isnss
    

































































    
    return