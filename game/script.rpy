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
image ecran_start:
    "start_screen-ui.png"
    zoom 0.3

image grey_background:
    "grey_background.png"
    zoom 10.0

image black_background:
    "black_background.png"
    zoom 1.0

image transmition_dossier:
    "transmition_dossier.png"
    zoom 0.55


# --------------------------------
# --- CREATION DES PERSONNAGES ---
# --------------------------------
python:
    name = renpy.input("Quel est votre nom ?")
 
define nrt_nvl = Character('', color="#692d0b", kind= nvl)
define nrt     = Character('', color="#692d0b")

define commissaire_lestrade_nvl = Character('Commissaire Lestrade', color="#692d0b", kind= nvl)
define commissaire_lestrade     = Character('Commissaire Lestrade', color="#692d0b")

define inspecteur_nvl = Character("Inspecteur [name]", color="#c2073f", kind= nvl)
define inspecteur     = Character("Inspecteur [name]",color="#c2073f")

# ------------------------------
# --- INITIALISATIN DU TIMER ---
# ------------------------------
init:
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0


# Le jeu commence ici
label start:

    scene grey_background

    menu:
        "Lancer Histoire":
            jump intro
        
        "Question jour 1":
            jump Day_One
        
        "Question jour 2":
            jump Day_Two

        "Question jour 3":
            jump Day_Three

    label intro:

        hide ecran_start

        scene black_background

        centered """{color=#ffffff}
                21 décembre 1952_
                \n\n{w}
                "Whitechapel, un quartier rongé par un mal au goût amer de réalité.
                \n
                {w}
                Entre psychopathes, camés et autres prostituées on dirait
                \n
                que les enfers eux même rejettent leurs pourritures informes
                \n
                jusque dans l'âme des citoyens.
                \n
                {w}
                Le procureur veut faire un ... exemple ...
                \n
                Une comdamnation à {color=#c40000}mort{color=#ffffff}.
                \n
                {w}
                Faire comprendre à la raclure comment finissent\n les esprits égarés.
                """

        nvl clear

        centered """{color=#ffffff}
                Comme si depuis son bureau doré, le c*l bien
                \n
                vissé sur son thrône, il s'improvisait Dieu.
                \n
                {w}
                Comme si son palais, rongé par le sel de son caviar,
                \n
                pouvait distiller la seule vérité qui compte...
                \n
                \n
                {w}
                Enfin... peu importe au final. Moi je ne suis qu'un des 
                \n
                chiens de garde de cet enfer aristocratique.
                {w}
                \n
                Bref celui qui fait le sale boulot.
                \n
                Et de mes choix, dans 4 jours ...
                \n
                \n
                {w}
                Un homme {color=#c40000}{b}mourrat{/b}{color=#ffffff}."
                """

        nvl clear

        scene grey_background

        commissaire_lestrade "Pouvez vous me rapeller votre nom ?"

        label identitée:
        python:
            name = renpy.input("Quel est votre nom ?", length=32)
            name = name.strip() or "Smith"

        commissaire_lestrade "Très bien [inspecteur].\nComme je vous ai dit le procureur nous pousse au c*l pour qu'on envoie quelqu'un a l'échafaud.\nEt on a notre candidat."
        
        scene transmition_dossier

        nrt "{i}*vous tends un dossier*"

        scene grey_background

        inspecteur "La victime n'a que 7 ans ?!"

        commissaire_lestrade "Le corps a été retrouvé il y 1 semaine, balloté par la tamise. On a réussi a identifié le corps mais tout les supects avait un alibi fiable. Les seuls que nous n'avons pas interrogés sont... Sa famille"

        inspecteur "..."

        nvl clear

        inspecteur "..."

        commissaire_lestrade "Quoi qu'il arrive je veux que vous retrouviez le s*l*p*rd qui a fait ça avant Noël."

        inspecteur """
                    {color=#707070}{i}"Une executions le jour de Noël ? Jolie cadeau Mr. le procureur."{i}{color=#000000}\nCompris chef.
                    """
    

    # --------------
    # --- Jour 1 ---
    # --------------
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

        nrt "Jour 1_"
        
        label Coffe_time_1:
            
            label menu_day_one:

                # Durée globale du timer (en secondes - 4)
                $ time = 6

                # nombre de tick a laquelle le timer s'écoule
                $ timer_range = 7.0

                # revoi a un x label a la fin du timer
                $ timer_jump = 'menu_day_one_slow'

                # call and start the timer
                show screen countdown

                menu:
                    "It's coffee time !":
                        #play sound click
                        hide screen countdown                  ### stop the timer
                        jump Selection_pour_interrogation_1

            label menu_day_one_slow:
                nrt "defeat"
                jump dev_codes

        label Selection_pour_interrogation_1:

            menu:
                "Jean":
                    jump dev_codes
                
                "Richard":
                    jump dev_codes
                
                "Elisabeth":
                    jump dev_codes

                "Anne":
                    jump dev_codes

    # =================================================================================================

    # jump questionTime2

    # =================================================================================================

    label Day_Two:
        
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
                
        label Coffe_time_2:
            
            label menu_day_two:

                # Durée globale du timer (en secondes - 2)
                $ time = 3

                # nombre de tick a laquelle le timer s'écoule
                $ timer_range = 3.0

                # revoi a un x label a la fin du timer
                $ timer_jump = 'menu_day_two_slow'

                # call and start the timer
                show screen countdown

                menu:
                    "It's coffee time !":
                        #play sound click
                        hide screen countdown # stop the timer
                        jump suite

            label menu_day_two_slow:
                nrt "defeat"
                jump dev_codes

        label Selection_pour_interrogation_2:

            menu:
                "Jean":
                    jump intro
                
                "Richard":
                    jump Day_One
                
                "Elisabeth":
                    jump Day_Two

                "Anne":
                    jump Day_Three



    # =================================================================================================

    # jump questionTime3

    # =================================================================================================
    label Day_Three:

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
                
        label Coffe_time_3:
            
            label menu_day_three:

                # Durée globale du timer (en secondes - 4)
                $ time = 1.5

                # nombre de tick a laquelle le timer s'écoule
                $ timer_range = 1.5

                # revoi a un x label a la fin du timer
                $ timer_jump = 'menu_day_three_slow'

                # call and start the timer
                show screen countdown

                menu:
                    "It's coffee time !":
                        #play sound click
                        hide screen countdown # stop the timer
                        jump suite

            label menu_day_three_slow:
                nrt "defeat"
                jump dev_codes
        
        label Selection_pour_interrogation_3:

            menu:
                "Jean":
                    jump intro
                
                "Richard":
                    jump Day_One
                
                "Elisabeth":
                    jump Day_Two

                "Anne":
                    jump Day_Three



    label suite:

        nrt "Victory"
        
        jump dev_codes

        label dev_codes:          
            
            menu:
                "Question jour 1":
                    jump Selection_pour_interrogation_1
                
                "Question jour 2":
                    jump Selection_pour_interrogation_2

                "Question jour 3":
                    jump Selection_pour_interrogation_3
                
                "Restart":
                    jump intro

    label end:
            #isnss



    return
