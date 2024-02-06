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
python:
    name = renpy.input("Quel est votre nom ?")
 
define narrateur_nvl = Character('', color="#692d0b", kind= nvl)
define narrateur     = Character('', color="#692d0b")

define commissaire_lestrade_nvl = Character('Commissaire Lestrade', color="#692d0b", kind= nvl)
define commissaire_lestrade     = Character('Commissaire Lestrade', color="#692d0b")

define inspecteur_nvl = Character("[name]", color="#c2073f", kind= nvl)
define inspecteur     = Character("[name]",color="#c2073f")

# ------------------------------
# --- INITIALISATIN DU TIMER ---
# ------------------------------
init:
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0


# Le jeu commence ici
label start:

    centered """{w}
21 décembre 1952_\n\n{w}
"Whitechapel, un quartier rongé par un mal au gout amer de réalité.\n{w}
Entre psychopathes, camés et autre prostituées on dirait\n que les enfers eux meme rejetent sa pourriture informe\n jusque dans l'ame des citoyens.\n{w}
Le procureur veut faire un ... exemple\n
Une comdamnation a MORT.\n{w}
Faire comprendre a la raclure comment finissent\n les esprits égarés.
...
    """

    nvl clear

    centered """{w}
Comme si depuis son bureau dorée, le cul bien
\n
visser sur son thrones, il s'improvisais Dieu.
\n
{w}
Comme si son palais, rongée par le sel de son caviar,
\n
pouvait distillé la seule vérité qui compte...
\n
\n
{w}
Enfin... peu importe au final. Moi je ne suis que le chien de garde
\n
de cet enfer aristocratique. Ses yeux, ses bras...{w}
\n
Bref celui qui fait le sale boulot. Et de mes choix, dans 4 jours ...
\n
\n
{w}
Un homme mourrat.
"
    """

    nvl clear

    commissaire_lestrade_nvl "Vous pouvez me rapeller votre nom ?"

    python:
        name = renpy.input("Quel est votre nom ?", length=32)
        name = name.strip()

        if not name:
            name = "Smith"

    commissaire_lestrade_nvl "Très bien Inspecteur [name]. Comme je vous ai dit le procureur nous pousse au cul pour qu'on envoie quelqu'un a l'echafaud. Et on a notre candidat."

    narrateur_nvl "*vous tends un dossier*"

    inspecteur_nvl "La victime n'a que 7 ans ?!"

    commissaire_lestrade_nvl "Le corps a été retrouvé il y 1 semaine, balloté par la tamise. On a réussi a identifié le corps mais tout les supects avait un alibi fiable. Les seuls que nous n'avons pas interrogés sont... Sa famille"

    inspecteur_nvl "..."

    commissaire_lestrade_nvl "Quoi qu'il arrive je veux que vous retrouviez le salopard qui a fait ça avant Noël."

    inspecteur_nvl "Une executions le jour de Noël? Jolie cadeau Mr. le procureur. Compris chef."
    

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
            
            label menu_day_one:

                # Durée globale du timer (en secondes)
                $ time = 10

                # nombre de tick a laquelle le timer s'écoule
                $ timer_range = 10.1

                # revoi a un x label a la fin du timer
                $ timer_jump = 'menu_day_one_slow'

                # call and start the timer
                show screen countdown

                menu:
                    "Test du timer":
                        #play sound click
                        hide screen countdown                  ### stop the timer
                        jump questionTime2

            label menu_day_one_slow:
                narration "defeat"
                jump end

    # =================================================================================================

    jump questionTime2

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
                
        label questionTime2:
            
            label menu_day_two:

                # Durée globale du timer (en secondes)
                $ time = 4

                # nombre de tick a laquelle le timer s'écoule
                $ timer_range = 2.1

                # revoi a un x label a la fin du timer
                $ timer_jump = 'menu_day_two_slow'

                # call and start the timer
                show screen countdown

                menu:
                    "Test du timer":
                        #play sound click
                        hide screen countdown # stop the timer
                        jump questionTime3

            label menu_day_two_slow:
                narrateur "defeat"
                jump end

    # =================================================================================================

    jump questionTime3

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
                
        label questionTime3:
            
            label menu_day_three:

                # Durée globale du timer (en secondes)
                $ time = 1

                # nombre de tick a laquelle le timer s'écoule
                $ timer_range = 1.1

                # revoi a un x label a la fin du timer
                $ timer_jump = 'menu_day_three_slow'

                # call and start the timer
                show screen countdown

                menu:
                    "Test du timer":
                        #play sound click
                        hide screen countdown # stop the timer
                        jump suite

            label menu_day_three_slow:
                narrateur "defeat"
                jump end


    label suite:

        nvl hide dissolve
        nvl show dissolve
        narration "victory"

    label end:
            #isnss



    return
