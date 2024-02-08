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


define nrt = Character('')
define commissaire_lestrade = Character('Commissaire Lestrade', color="#e2651d")
define inspecteur = Character("Inspecteur [name]",color="#c2073f")
define jean = Character("Jean Levallois",color="#9aa819")
define richard = Character("Richard Levallois",color="#9aa819")
define elisabeth = Character("Elisabeth Levallois",color="#9aa819")
define anne = Character("Anne Levallois",color="#9aa819")

# ------------------------------
# --- INITIALISATIN DU TIMER ---
# ------------------------------
init:
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

# Le jeu commence ici
label start:

    label intro:

        hide ecran_start

        scene black_background

        centered """{color=#ffffff}
                21 décembre 1952_
                \n \n {w}
                "Whitechapel, un quartier rongé par un mal au goût amer de réalité.
                \n {w}
                Entre psychopathes, camés et autres prostituées on dirait
                \n
                que les enfers eux même rejettent leurs pourritures informes
                \n
                jusque dans l'âme des citoyens.
                \n {w}
                Le procureur veut faire un ... exemple ...
                \n
                Une comdamnation à {color=#c40000}mort{color=#ffffff}.
                \n {w}
                Faire comprendre à la raclure comment finissent\n les esprits égarés.
                """

        nvl clear

        centered """{color=#ffffff}
                Comme si depuis son bureau doré, le c*l bien
                \n
                vissé sur son thrône, il s'improvisait Dieu.
                \n {w}
                Comme si son palais, rongé par le sel de son caviar,
                \n
                pouvait distiller la seule vérité qui compte...
                \n \n {w}
                Enfin... peu importe au final. Moi je ne suis qu'un des 
                \n
                chiens de garde de cet enfer aristocratique.
                \n {w}
                Bref celui qui fait le sale boulot.
                \n
                Et de mes choix, dans 4 jours ...
                \n \n {w}
                Un homme {color=#c40000}{b}mourrat{/b}{color=#ffffff}."
                """

        nvl clear

        scene grey_background

        jump Day_zero


    label identite:
        python:
            name = renpy.input("Quel est votre nom ?")
            name = name.strip() or "Smith"
        jump Day_zero_continu


    label Day_zero:

        commissaire_lestrade "Pouvez vous me rapeller votre nom ?"

        jump identite

        label Day_zero_continu:
            pass

        commissaire_lestrade "Très bien [inspecteur].\nComme je vous ai dit le procureur nous pousse au c*l pour qu'on envoie quelqu'un a l'échafaud.\nEt on a notre candidat."
        
        scene transmition_dossier

        nrt "{i}le commissaire vous tends un dossier"

        scene grey_background

        inspecteur "La victime n'a que 7 ans ?!"

        commissaire_lestrade "Le corps a été retrouvé il y 1 semaine, balloté par la tamise. On a réussi a identifié le corps mais tout les supects avait un alibi fiable. Les seuls que nous n'avons pas interrogés sont... Sa famille"

        inspecteur "..."

        commissaire_lestrade "Quoi qu'il arrive je veux que vous retrouviez le s*l*p*rd qui a fait ça avant Noël."

        inspecteur """
                    {color=#707070}{i}"Une executions le jour de Noël ? Jolie cadeau Mr. le procureur."{i}{color=#000000}
                    \n
                    Compris chef.
                    """
    
    ###############################################################
    #########################             #########################
    #########################    JOUR 1   #########################
    #########################             #########################
    ###############################################################
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
                    jump Dialogue_Jean
                
                "Richard":
                    jump Dialogue_Richard
                
                "Elisabeth":
                    jump Dialogue_Elisabeth

                "Anne":
                    jump Dialogue_Anne
    
        #######################################################################################################
        #######################################################################################################
        ##### 
        ##### DIALOGUE JEAN
        ##### 
        ##### =================================================================================================
        label Dialogue_Jean:

            centered """{i}{color=#000000}
                "Jean Levallois... Il semblait calme. Bien trop calme.
                \n {w}
                Son visage, impassible, ne laissait rien entrevoir d'autre 
                \n
                que sa future sénilité et pourtant il reussissait a garder son calme.
                \n \n
                Il etait a l'image d'un prédateur se camouflant parmis
                \n
                nous autre afin qu'on se méfie pas des ses crocs.
                \n
                Mais il était aussi a l'image d'un vieux sage eyant vu les
                \n
                secrets de l'univers.
                \n \n
                Qui était il? Je comptais bien le découvrir..."
                """

            menu:
                
                "Ecouter son Alibi":
                    jump Alibi_Jean

            label Alibi_Jean:

                inspecteur "Mr Levallois que faisiez vou.."

                jean "Mr l'agent ... Croyez vous en Dieu ?"

                menu:
                    "...":
                        pass
                
                jean """
                    Vous savez c'est moi qui m'ocuppe de l'éducation {a=indice_12}RELIGIEUSE{/a}
                    de cette famille... Rose... Quelle tragédie!
                    \n
                    Son âme pouvait être sauvée si nous avions eu plus de temps ...
                    \n
                    Vous voulez savoir ce que je faisait le 13 décembre n'est pas ?
                    """
                
                menu:
                    "...":
                        pass
                
                jean """
                    Je priais... Je priais pour Rose et je lui montrais comment il fallait
                    \n
                    montrer notre amour au Seigneur...
                    """ 

                menu:
                    "Etiez-vous avec elle ?":
                        pass
                
                jean "Lorsque les invité de mon fils sont arrivés au domicile je suis allé faire un tour dans le parc et Rose est partie dormir"
            

                inspecteur """{i}"Passons à quelqu'un d'autre"{i}"""

                menu:
                    "Richard":
                        jump Dialogue_Richard
                    
                    "Elisabeth":
                        jump Dialogue_Elisabeth

                    "Anne":
                        jump Dialogue_Anne
                    
                    "Conclure la journée":
                        jump to_be_continued
            
        #######################################################################################################
        #######################################################################################################
        ##### 
        ##### DIALOGUE RICHARD
        ##### 
        ##### =================================================================================================
        label Dialogue_Richard:

            centered """{i}{color=#000000}
                "Richard Levallois... Un banquier qui aurait assez d'argent pour racheter
                \n
                Buckingham palace s'il n'en dépensait pas la moitié pour alimenter sa future cirrhose
                \n
                (maladie du foie, fréquemment liée à l'excès d'alcool). 
                \n
                Tout chez lui transpire l'alcool. De sa chemise, sur laquelle on peut voir des
                \n
                traces de cognac mal lavées, à son eau de cologne très chère disimulant a peine
                \n
                lordeur de cendres de son cigare en passant par son ame, aussi pourri que son foie.
                \n
                L'argent ne fait pas le bohneur... Il rends l'homme stupides.
                \n
                Richard, quant a lui, était le plus stupides d'entre eux..."
                """

            menu:                
                "Ecouter son Alibi":
                    jump Alibi_Richard

            label Alibi_Richard:

                inspecteur "Bien, vous allez me décrire les evenements de la journée du 13 décembre dernier."

                richard "Je ... heu ... je peux parler à ma femme avant ?"

                inspecteur "Pourquoi? Peur de dire des betises Mr. Levallois?"
                
                richard "... laissez tomber."

                inspecteur "Bien. Vous pouvez commencer."

                richard """
                    ... heu ... du poker je crois ... oui c'est ça! Notre partie de [[POKER|indice n°7]] mensuelle.
                    Suite a cela mon et mon père avons partagé un petit verre de whisky avant que je n'aille me coucher. 
                    \n
                    Le lendemain m'a femme m'a annoncé la terrible nouvelle...
                    """
                
                inspecteur "Et qu'avez vous fait ensuite?"
                
                richard "J'ai voulut prévenir la police mais le corps avait déjà été retrouvé..." 

                inspecteur """{i}"Passons à quelqu'un d'autre"{i}"""

                menu:
                    "Jean":
                        jump Dialogue_Jean
                    
                    "Elisabeth":
                        jump Dialogue_Elisabeth

                    "Anne":
                        jump Dialogue_Anne
                    
                    "Conclure la journée":
                        jump to_be_continued

        #######################################################################################################
        #######################################################################################################
        ##### 
        ##### DIALOGUE ELISABETH
        ##### 
        ##### =================================================================================================
        label Dialogue_Elisabeth:

            centered """{i}{color=#000000}
                Elisabeth Levallois... Son visage ne laissait transparaitre qu'un
                \n
                demon froid et calculateur caché derriere du fond de teint. 
                \n
                Elle avait tout de la femme parfaite, les manières, la beauté, l'intelligence.
                \n \n
                Il aurait été facile de confondre cette succube avec un ange.
                \n
                C'était une sirène. Mais son chant n'atteindrait pas ma volonté.
                \n \n
                Je suis là car je doit decouvrir les sombres secrets qui se cachent derrière cette histoire..."
                """

            menu:
                
                "Ecouter son Alibi":
                    jump Alibi_Elisabeth

            label Alibi_Elisabeth:

                inspecteur "Bon si vous voulez bien on va revenir sur les évenements du 13 décembre."

                elisabeth """
                    {i}soupir{i}
                    \n
                    Combien de temps cela va-t-il encore durer ?
                    \n
                    L'assassin de ma fille cours dans les rues et vous perdez
                    \n
                    votre temps et le miens avec vos questions."""
                
                inspecteur "Mme Levallois, je ne fais que mon devoir. Veuillez passer à votre deposition."

                elisabeth """
                    Ce jour là Richard était au boulot et nous devions recevoir le soir meme,
                    j'ai donc passer ma journée à [[NETOYER|indice n°1]] cette satanée maison.
                    """
                
                elisabeth """
                    Mon mari est rentré du boulot lorsque que j'ai eu finis de préparé le
                    [[REPAS|indice n°2]]. Suite a cela je suis parti lire un [[LIVRE|indice n°3]] 
                    dans ma chambre afin de me détendre et puis je me suis endormie.
                    \n
                    Le lendemain... Rose... {i}sanglote{i} elle avait disparu.
                    """

                inspecteur "Comment vous en etes vous rendu compte ?"

                elisabeth """
                    J'etait la première levée ce jour la et j'ai pris l'habitude de reveiller
                    \n
                    Anne et Rose tot le dimanche afin de leur dispensé des [[LECONS DE PIANO|indice n°4]]
                    avant la messe. Lorsque je suis rentrée dans la chambre de Rose...
                    """
                
                elisabeth """
                    La fenetre etait brisée et la pièce sans dessus dessous.
                    \n
                    Quant a ma fille... introuvable...
                    """

                inspecteur """{i}"Passons à quelqu'un d'autre"{i}"""

                menu:
                    "Jean":
                        jump Dialogue_Jean
                    
                    "Richard":
                        jump Dialogue_Richard

                    "Anne":
                        jump Dialogue_Anne
                    
                    "Conclure la journée":
                        jump to_be_continued

        #######################################################################################################
        #######################################################################################################
        ##### 
        ##### DIALOGUE ANNE
        ##### 
        ##### =================================================================================================
        label Dialogue_Anne:

            centered """{color=#000000}
                Anne Levallois était une jeune fille au bouffi par
                \n
                des souvenirs... douloureux.
                \n
                La jeune fille semblait maurtri par le poids
                \n
                de sombres secrets. Que cachait - elle?
                \n
                Elle donnait l'impression d'etre un gentil petit agneaux au millieu de la meute affamé
                de loup qu'était sa famille.
                \n \n
                Cependant... Les chiens ne font pas des chats et les démons font rarements des anges...
                """

            menu:
                "Ecouter son Alibi":
                    jump Alibi_Anne

            label Alibi_Anne:

                inspecteur "Mlle Anne ? Que faisiez vous le 13 décembre dernier ?"

                anne "..."

                inspecteur "Mlle ?"
                
                anne "..."

                inspecteur "MLLE ANNE !"

                anne """
                    Pardon, Veuillez m'excuser. Ce jour là je répètait mes [[LECONS DE PIANO|indice n°8]]
                    mais j'ai du [[ARRETER|indice n°9]] en debut d'après midi.
                    \n
                    J'ai alors fait un peu de peinture en attendant ma lecons de couture.
                    """

                inspecteur "Est-ce Mme Elisabeth qui vous dispense ces cours ?"

                anne """
                    Oui. Mais je me souviens que j'ai du me débrouiller [[TOUTE SEULE|indice n°10]] ce jours là...
                    \n
                    Le soir j'ai joué du piano devant les [[INVITES|indice n°7]].
                    """

                inspecteur "Et après cela ?"

                anne "Je... Je n'ai pas très bien dormi et je suis allé voir dans la chambre de rose à [[L'AUBE|indice n°11]]."
                
                inspecteur """{i}"Passons à quelqu'un d'autre"{i}"""

                menu:
                    "Jean":
                        jump Dialogue_Jean
                    
                    "Richard":
                        jump Dialogue_Richard
                    
                    "Elisabeth":
                        jump Dialogue_Elisabeth
                    
                    "Conclure la journée":
                        jump to_be_continued




    label to_be_continued:

        scene black_background

        centered """
            {color=#c40000}{i}{b}TO BE CONTINUED_{/b}{/i}{color=#ffffff}
            \n
            \n
            By :\n
                {color=#ff0000}CHANVRIL{color=#ffffff} Liam | {color=#ff0000}CHAPELLIERE{color=#ffffff} Youenn\n
                {color=#ff0000}DA COSTA REIS{color=#ffffff} Mickaël | {color=#ff0000}JOURDAN{color=#ffffff} Gabin\n
                {color=#ff0000}LE ROUX{color=#ffffff} Maxime\n
            """
        
        jump end


#######################################################################################################
#######################################################################################################
##### 
##### Indices
##### 
##### =================================================================================================
label indice_1:
    "Elisabeth à passer la journée a nettoyer"

label indice_2:
    "Elisabeth a cuisiné du boeuf"

label indice_3:
    "Elisabeth lisait Mort sur le Nil"

label indice_4:
    "Anne est nulle en piano"

label indice_5:
    "Richard était a la banque toute la journée"

label indice_6:
    "Elisabeth lisait un manifeste"

label indice_7:
    "Les Fox et Mr. Penn étaient present"

label indice_8:
    "Elisabeth frappe les doigts d'Anne"

label indice_9:
    "Jean et Richard se sont disputé"

label indice_10:
    "Elisabeth s'est absentée"

label indice_11:
    "Richard est parti dans la nuit"

label indice_12:
    "La famille Levallois est très religieuse"

label indice_13:
    ""

label indice_14:
    ""

label indice_15:
    ""

label indice_16:
    ""

label indice_17:
    ""

label indice_18:
    ""

label indice_19:
    ""

label indice_20:
    ""

label indice_21:
    ""

label indice_22:
    ""

label indice_23:
    ""

label indice_24:
    ""

label indice_25:
    ""

label indice_26:
    ""

label indice_27:
    ""

label indice_28:
    ""

label indice_29:
    ""

label indice_30:
    ""






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
        pass

return
