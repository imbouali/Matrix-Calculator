import numpy as np

banner = """
                                                              _..._                       _..._                                  .-'''-.            
                                                           .-'_..._''.         .---.   .-'_..._''.        .---.                 '   _    \          
 __  __   ___                         .--.               .' .'      '.\        |   | .' .'      '.\       |   |               /   /` '.   \         
|  |/  `.'   `.                       |__|              / .'                   |   |/ .'                  |   |              .   |     \  '         
|   .-.  .-.   '            .| .-,.--..--.             . '                     |   . '                    |   |            .||   '      |  .-,.--.  
|  |  |  |  |  |   __     .' |_|  .-. |  |____     ____| |                __   |   | |                    |   |   __     .' |\    \     / /|  .-. | 
|  |  |  |  |  |.:--.'. .'     | |  | |  `.   \  .'    | |             .:--.'. |   | |              _    _|   |.:--.'. .'     `.   ` ..' / | |  | | 
|  |  |  |  |  / |   \ '--.  .-| |  | |  | `.  `'    .'. '            / |   \ ||   . '             | '  / |   / |   \ '--.  .-'  '-...-'`  | |  | | 
|  |  |  |  |  `" __ | |  |  | | |  '-|  |   '.    .'   \ '.          `" __ | ||   |\ '.          .' | .' |   `" __ | |  |  |              | |  '-  
|__|  |__|  |__|.'.''| |  |  | | |    |__|   .'     `.   '. `._____.-'/.'.''| ||   | '. `._____.-'/  | /  |   |.'.''| |  |  |              | |      
               / /   | |_ |  '.| |         .'  .'`.   `.   `-.______ // /   | |'---'   `-.______ |   `'.  '---/ /   | |_ |  '.'            | |      
               \ \._,\ '/ |   /|_|       .'   /    `.   `.          ` \ \._,\ '/                `'   .'|  '/  \ \._,\ '/ |   /             |_|      
                `--'  `"  `'-'          '----'       '----'            `--'  `"                   `-'  `--'    `--'  `"  `'-'                          
by @iambouali  
"""

print(banner)

usage_guide = """
Guide d'utilisation :

1. Entrez le nombre de lignes et de colonnes pour chaque matrice.
2. Pour chaque ligne de chaque matrice, entrez les éléments séparés par un espace.
3. Choisissez l'opération à effectuer : 
   - 's' pour l'addition de matrices
   - 'p' pour le produit de matrices
   - 'i' pour l'inverse d'une matrice
4. Suivez les instructions pour entrer les matrices en conséquence.

Note: Si l'opération est 'i', le programme n'attendra qu'une seule matrice.

"""

print(usage_guide)

def saisir_matrice():
    lignes = int(input("Entrez le nombre de lignes de la matrice : "))
    colonnes = int(input("Entrez le nombre de colonnes de la matrice : "))
    
    matrice = []
    for i in range(lignes):
        ligne_str = input(f"Entrez les éléments de la ligne {i + 1} séparés par un espace : ")
        ligne = [float(element) for element in ligne_str.split()]
        
        if len(ligne) != colonnes:
            raise ValueError("Le nombre d'éléments de la ligne ne correspond pas au nombre de colonnes.")
        
        matrice.append(ligne)
    
    return np.array(matrice)

def somme_matrices(matrices):
    if len(matrices) < 2:
        raise ValueError("Au moins deux matrices sont nécessaires pour l'addition.")
    
    somme = np.zeros_like(matrices[0])
    
    for matrice in matrices:
        if np.shape(matrice) != np.shape(somme):
            raise ValueError("Les dimensions des matrices ne sont pas compatibles pour l'addition.")
        
        somme = np.add(somme, matrice)
    
    return somme

def produit_matrices(matrices):
    if len(matrices) < 2:
        raise ValueError("Au moins deux matrices sont nécessaires pour le produit.")
    
    produit = matrices[0]
    
    for matrice in matrices[1:]:
        if np.shape(produit)[1] != np.shape(matrice)[0]:
            raise ValueError("Les dimensions des matrices ne sont pas compatibles pour le produit.")
        
        produit = np.dot(produit, matrice)
    
    return produit

def inverse_matrice(matrice):
    try:
        inverse = np.linalg.inv(matrice)
        return inverse
    except np.linalg.LinAlgError:
        raise ValueError("La matrice n'est pas inversible.")

operation = input("\nChoisissez l'opération (s, p, or i pour inverse) : ").lower()
n = int(input("Entrez le nombre de matrices : ")) if operation != "i" else 1

matrices = [saisir_matrice() for _ in range(n)]

try:
    if operation == "s":
        resultat = somme_matrices(matrices)
    elif operation == "p":
        resultat = produit_matrices(matrices)
    elif operation == "i":
        resultat = inverse_matrice(matrices[0])
    else:
        raise ValueError("Opération non reconnue.")
    
    print(f"\nRésultat de l'opération {operation} des matrices :\n", resultat)

except ValueError as e:
    print(f"Erreur : {e}")
