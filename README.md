# ⚓ Projet Bataille Navale

Ce dépôt contient l'implémentation console du jeu classique de la Bataille Navale (Battleship) en Python. Le jeu oppose un joueur humain à une grille de 8x10 sur laquelle 4 bateaux sont placés aléatoirement sans chevauchement.

## 🎯 Fonctionnalités du Jeu

* **Grille de Jeu :** 8 lignes et 10 colonnes.
* **Bateaux :** Un porte-avion, un croiseur, un torpilleur et un sous-marin sont placés aléatoirement au début de chaque partie.
* **Logique de Tir :** Le joueur entre les coordonnées de tir (`LIGNE,COLONNE`).
* **Condition de Victoire :** La partie se termine lorsque tous les bateaux sont coulés.

## ⚙️ Installation et Exécution

Suivez les étapes ci-dessous pour installer et lancer le jeu.

### Prérequis

Assurez-vous d'avoir Python 3 installé sur votre système.

### 1. Cloner le Dépôt

Ouvrez votre terminal et clonez ce dépôt :

```bash
git clone https://github.com/solal-x/bataille_navale
cd bataille_navale

# Créer l'environnement virtuel (le nom 'venv' est le plus courant)
python -m venv venv
# Si cela ne mache pas, essayer
python3 -m venv venv
# Ou
py -m venv venv

# pour la suite, remplacer "python" par python3 ou py selon lequel vous a permis de créer le venv

# Activer l'environnement virtuel
# Sur Windows (Command Prompt) :
# venv\Scripts\activate
# Sur Linux/macOS ou Windows (Git Bash/PowerShell) :
. venv/bin/activate

pip install -r requirement.txt

# le main sans interface travaillée
python main.py

# le main avec une interface un peu plus jolie, faite avec l'aide d'une ia pour les couleurs et l'actualisation
python main_interface.py

pytest
