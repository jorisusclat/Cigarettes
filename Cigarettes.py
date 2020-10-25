#Calculateur des dépenses en cigarettes sur X années.

def cigarettes():
    #Demande des valeurs 
    print("Nous allons calculer les économies que vous aurez pu faire si vous n'aurez jamais commencé à fumer ou si vous êtes en train d'arrêter. Allons-y !")
    print("\n")
    print("Renseignez le prix de votre paquet (€) :")
    prix_paquet = int(input())
    print("\n")
    print("Combien de paquets fumez-vous par semaine ? :")
    prix_semaine = int(input())
    print("\n")
    print("Depuis combien d'années fumez-vous ? :")
    temps_an = int(input())
    print("\n")
    #Calcul du prix total, /an, /semaine, /jour

    total = (prix_paquet*prix_semaine)*(52)*temps_an
    total_an = (prix_paquet*prix_semaine)*52
    total_semaine = prix_paquet*prix_semaine
    total_jour = (prix_paquet*prix_semaine)/7

    #Valeur arrondies
    round_total = round(total)
    round_total_an = round(total_an)
    round_total_semaine = round(total_semaine, 1)
    round_total_jour = round(total_jour, 1)

    #Renvoi des valeurs
    print("Vous avez dépenser au total {}€".format(round_total))
    print("Vous dépensez par an {} €".format(round_total_an))
    print("Vous dépensez par semaine {} €".format(round_total_semaine))
    print("Vous dépensez par jour {} €".format(round_total_jour))
    print("\n")

    #Recommencer
    print("Pour recommencer le calcul appuyer sur \"Entrée\".")
    print("\n")
    input()
    return cigarettes()


print("Bonjour !")
print("\n")
cigarettes()


#Par Joris USCLAT