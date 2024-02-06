# Images de personnage
image ...:
    ""

image ...:
    ""

# Imagesde scène
image ...:
    ""

image ...:
    ""

# Déclarez les personnages utilisés dans le jeu.
define ... = Character('', color="#c8ffc8")


# Le jeu commence ici
label start:

    e "Vous venez de créer un nouveau jeu Ren'Py."

    e "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"

    
    
    
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