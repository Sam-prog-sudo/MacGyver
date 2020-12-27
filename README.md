# MacGyver

[![image](https://img.shields.io/github/license/Sam-prog-sudo/sam.github.io?style=flat-square)](https://github.com/Sam-prog-sudo/MacGyver/blob/master/LICENSE)
---
## Avant-propos

Aider MacGyver à s'échapper du labyrinth, sans se faire attraper par le garde .

## Table des matières

- [Avant-propos](#avant-propos)  
- [Introduction](#introduction)  
- [Installation](#installation)  
- [Utilisation](#utilisation)  
  - [Console](#console)  
  - [Pygame](#pygame)
- [Améliorations possibles](#améliorations-possibles)
- [License](#license)
---
## Introduction
Pour ce troisième projet de la formation, l'objectif est de créer un jeu en python.  

Plus exactement, un labyrinthe 2D dans lequel MacGyver est enfermé.  
L’unique sortie est surveillée par un garde.  
Une seule échapatoire possible: l'endormir.  

Pour ce faire, il faudra réunir les éléments suivants: une aiguille, un petit tube en plastique et de l'éther.  
Ils permettront à MacGyver d'endormir le garde, pour en sortir.

---
## Installation

* Installer [Python 3.8+](https://www.python.org/downloads/).  

* Télécharger le code source.  
Plusieurs solutions s'offrent à vous:  

  - 👯Cloner ce repo sur votre machine local à l'aide de cette adresse:  
https://github.com/Sam-prog-sudo/MacGyver.git`.  

  - 🍴Forker ce repo.

  - 💾Télécharger le code source à cette adresse:  
https://github.com/Sam-prog-sudo/MacGyver/archive/master.zip

* Activer votre environnement virtuel.

Exemple avec venv:
```shell
python3 -m venv /chemin_vers_env
```
**ou sous windows**  
```shell
py -m venv /chemin_vers_env
```

----
## Utilisation
* Activer l'environement virtuel.  
```shell
source /chemin_vers_env/bin/activate
```
* Installer les [modules requis](https://github.com/Sam-prog-sudo/MacGyver/blob/master/requirements.txt). 
```shell
pip install -r requirements.txt
```
* Lancer \_\_main__.py pour démarer une partie.

### Console
Lors de l'invite de commande entrer ``c``.  
Puis diriger MacGyver à l'aide de l'invite de commande. Commandes correctes:  
`'up', 'down', 'left', 'right'`.

### Pygame

Pour choisir l'interface graphique, entrer ``g``, lors de l'invite de commande.  
Puis diriger MacGyver à l'aide des touches directionnelles du clavier.

## Améliorations possibles
Cette liste est non-exhaustive:   

- Mettre en place des test avec pytest.  
- Générer une documentation avec sphinx.  
- Permettre une saugarde physique de la partie.  


## License
**[MIT license](http://opensource.org/licenses/mit-license.php)**
