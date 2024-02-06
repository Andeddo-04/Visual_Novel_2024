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
define narrateur_nvl = Character('Major_Bogo', color="#692d0b", kind= nvl)
define narrateur     = Character('Major_Bogo', color="#692d0b")

# ------------------------------
# --- INITIALISATIN DU TIMER ---
# ------------------------------
init:
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0


# Le jeu commence ici
label start:

    narrateur_nvl "Bonjour à vous sergent.{w} Je vous charge de cette affaire, une enfant de 7 ans, morte.{w} Bonne chance à vous."
    
    nvl clear

    jump Day_One

    label Day_One:
        
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

                $ time = 2               ### Durée globale du timer (en secondes)
                $ timer_range = 2.1      ### nombre de tick a laquelle le timer s'écoule

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

    label Day_Two:
    
    label Day_Three:

    label end:
            #isnss






























































    
    return