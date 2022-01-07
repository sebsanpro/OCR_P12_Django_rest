# Projet 12 : Développez une architecture back-end sécurisée en utilisant Django ORM

Cette application fonctionne grâce à Django Rest, elle simule l'utilisation par la société Epic Event d'un CRM regroupant
les utilisateurs de la société, les clients acquis ou potentiel, les contrats et les évenements qui en découlent.

## Pour commencer

Télécharger le fichier zip contenant le code ou effectuer un ``git clone``

La base de donnée doit être PostgreSQL et un fichier .env dois etre créé à la racine du projet

### Fichier .env

Le fichier dois contenir obligatoirement les informations suivantes pour fonctionner

- SECRET_KEY  -> Secret key de Django
- DB_USER   -> Utilisateur Postgres
- DB_PASSWORD   -> mdp Postgres
- DB_NAME   -> Nom de la BDD

### Pré-requis

Pour commencer, vous devez posséder les logiciel suivant

- Python 3.8 ou ultérieur 
- PyPI
- venv  ``pip install venv``

### Installation

Les étapes d'installation avec Venv....

Pour Windows :
   dans l'invite de commande : ``python -m venv env``  ``env/Scripts/activate``  ``pip install -r requirements.txt``   

Pour linux :
   dans le terminal : ``sudo py3 -m venv env``  ``source env/bin/activate``  ``pip3 install -r requirements.txt``


## Démarrage du server de test Django

Effectuer la migration vers Postgres
``python manage.py migrate``

Restauration des données avec les permissions
``python manage.py loaddata data.json``

Démarrage du server Django
``python manage.py runserver``

## Fabriqué avec

Python 3.9
	
## Auteurs

Sebastien SANNAC, Projet organisé par OpenClassrooms sur le parcourt diplomant Python
