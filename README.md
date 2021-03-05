# Tournoi de jeu d'échecs
Dans ce projet, un potentiel client souhaite avoir un programme pour pouvoir gérer des tournois de jeu d'échecs hors ligne.
Le logiciel doit pouvoir être lancé depuis la console (termminal).

# Description 
Le défi est de réaliser un programme en python qui peut commencer un tournoi, accepter des entrées de joeurs et sur le tournoi en général, générer des paires, inscrire le score ainsi que de consulter le rapport sur des tournois passées.
Les paires doivent être générées selon le système de [tournoi suisse](https://fr.wikipedia.org/wiki/Syst%C3%A8me_suisse)

## Etapes
1. Créer un nouveau tournoi.
2. Ajouter huit joueurs.
3. L'ordinateur génère des paires de joueurs pour le premier tour.
4. Lorsque le tour est terminé, entrez les résultats.
5. Répétez les étapes 3 et 4 pour les tours suivants jusqu'à ce que tous les tours soient joués, et que le tournoi soit terminé.

# Environnement
* L'installation de [Python 3](https://www.python.org/downloads/) est nécessaire pour la réalisation de ce projet
* Après l'installation de Python3, l'installation de [pip](https://pypi.org/project/pip/) est recommandé
* Après il est nécessaire d'installe [virtualenv](https://pypi.org/project/virtualenv/)
* L'outil de dévelopement utilisé et recommandé: [Visual Studio Code (Vscode)](https://code.visualstudio.com/)
* Le programme peut être executé sur Linux, Mac et Windows
* Base de donnée: [TinyDB](https://tinydb.readthedocs.io/en/latest/)

# Installation
1. Cloner, en premier, le projet sur votre bureau ou environnement local
   - Clicker sur le bouton vert 'Clone' en haut à droite et copier le lien sous HTPPS ou SSH (selon la configuration de votre [git](https://git-scm.com/)
   - Cloner le project dans un dossier que vous aurez créer exclusivement pour ce projet, en entrant la commande dans le terminal:
    ```bash
    git clone [le lien copié]
    ```
    
    ![alt text](https://github.com/davymariko/python_chess/blob/main/donnees/clone.JPG)
    
    Dans notre cas, ça sera:
    ```bash
    git clone git@github.com:davymariko/python_chess.git
    ```
   Entrer dans le dossier généré

2. Installer l'environnement virtuel avec la commande (test_env est un nom au choix):
   ```bash
   virtualenv test_env
   ```
   et l'activer avec la commande:
   ```bash
   source test_env/bin/activate
   ```
   ou pour Windows, avec:
   ```bash
   test_env/Scripts/activate
   ```
   à la fin, pour désactiver l'environnement:
   ```bash
   deactivate
   ```
 
3. Installer les pre-requis pour ce projet en lançant la commande:
```bash
pip install -r requirements.txt
```

# Execution
Pour lancer le programme lancer le fichier 
```bash
python -m chess
```
Vous devrez avoir un menu d'acceuil semblable à celui ci


![alt text](https://github.com/davymariko/python_chess/blob/main/donnees/terminal.JPG)

# Pep8, flake8
Le code respecte les règles du pep8 avec la limite de longueur par ligne à 119.
Un rapport flake 8 est présent dans le dossier [flake8_rapport]() et un autre rapport peut être généré en éxécutant la commande
```bash
flake8 --format=html --htmldir=flake8_rapport
```

Le nom de flake8_rapport peut être changé.
Ce code présente aucune violation aux règles comme celà peut être vu dans la page html générée par la commande

![alt text](https://github.com/davymariko/python_chess/blob/main/donnees/flake8.JPG)


# Auteur
Le programme a été conçu et maintenu par [Davy Nimbona](https://www.linkedin.com/in/davy-nimbona/)
