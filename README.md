Projet de Web Scraping - Books to Scrape

Description

Ce projet est un scraper développé en Python qui extrait les données des livres du site Books to Scrape et les enregistre dans une base de données PostgreSQL. Le projet permet de récupérer les livres par catégorie, note, et tranche de prix.

Technologies utilisées

Python 3

Requests - Pour récupérer le contenu HTML

BeautifulSoup4 - Pour parser le HTML

SQLAlchemy - Pour gérer la base de données

PostgreSQL - Base de données pour stocker les livres

Structure du projet

book_scraper/
│── scraper.py          # Code principal du scraper
│── database.py         # Connexion à PostgreSQL
│── models.py           # Définition des tables avec SQLAlchemy
│── create_table.py     # Script pour créer les tables dans PostgreSQL
│── check_db.py         # Script pour vérifier les données en base
│── README.md           # Documentation du projet
│── requirements.txt    # Liste des dépendances

Configurer PostgreSQL

Créer une base de données books_db dans pgAdmin ou avec la commande SQL :

CREATE DATABASE books_db ENCODING 'UTF8';

DATABASE_URL = "postgresql://votre_utilisateur:votre_mot_de_passe@localhost:5432/books_db"

python scraper.py

Vérifier les données en base

Via pgAdmin ou en SQL :

SELECT * FROM books LIMIT 10;

Ou avec Python :
python check_db.py

 Fonctionnalités

- Scrape toutes les catégories de livres
- Enregistre les titres, prix, notes et disponibilités
- Stocke les données proprement dans PostgreSQL
- Filtrage possible par note et prix

Améliorations futures

Ajouter une interface tkinter 

Exporter les données en CSV 

Ajouter plus de filtres

Ajouter un champ de recherche dynamique

