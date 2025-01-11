# wandaloo-voitures-promo-scraper


**wandaloo-voitures-promo-scraper** est un projet Python qui permet de scraper les promotions de voitures neuves à partir du site marocain [wandaloo.com](https://www.wandaloo.com). Il collecte des informations sur les modèles de voitures, les versions, les détails, et les prix promotionnels, puis sauvegarde les données dans un fichier CSV pour analyse.

## Fonctionnalités

- Scrape les détails des promotions de voitures sur plusieurs pages du site.
- Extrait des données telles que :
  - Nom du modèle
  - Version
  - Spécifications
  - Prix initial
  - Prix promotionnel
- Sauvegarde les données dans un fichier CSV structuré.

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-nom-utilisateur/promo-scraper-voitures.git
   ```
2. Accédez au dossier du projet :
   ```bash
   cd wandaloo-voitures-promo-scraper
   ```
3. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Ouvrez le fichier `scraper.py` et configurez les paramètres suivants :
   - `start_page` : Le numéro de la première page à scraper.
   - `end_page` : Le numéro de la dernière page à scraper.
   - `max_vehicles` : Le nombre maximum de véhicules à scraper.

2. Exécutez le script :
   ```bash
   python scraper.py
   ```

3. Le fichier CSV contenant les données sera généré sous le nom `promotions_voitures.csv` dans le dossier du projet.

## Exemple de sortie

Un fichier CSV généré contient les colonnes suivantes :
- Modèle
- Version
- Détails
- Prix initial
- Prix promo

## Prérequis

- Python 3.7 ou une version ultérieure
- Bibliothèques Python nécessaires :
  - `requests` pour les requêtes HTTP
  - `BeautifulSoup` (de `bs4`) pour le parsing HTML
  - `pandas` pour la manipulation des données

Pour installer les dépendances, exécutez :
```bash
pip install requests beautifulsoup4 pandas
```

## Remarques

- Assurez-vous que la structure du site web n’a pas changé avant d’exécuter le scraper.
- Utilisez le scraper de manière responsable et évitez de surcharger le site cible.

## Structure du projet

```
wandaloo-voitures-promo-scraper/
│
├── scraper.py          # Script principal pour le scraping
├── requirements.txt    # Liste des bibliothèques Python nécessaires
├── promotions_voitures.csv  # Fichier de sortie (généré après l'exécution du script)
└── README.md           # Documentation du projet
```

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.

## Contribution

Toute contribution est la bienvenue ! Vous pouvez soumettre des issues ou des pull requests pour améliorer ce projet.

## Remerciements

- Source des données : [wandaloo.com](https://www.wandaloo.com)
- Développé avec Python 🐍
```

