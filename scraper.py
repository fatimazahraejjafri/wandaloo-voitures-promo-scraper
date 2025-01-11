import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de base pour les promotions
BASE_URL = "https://www.wandaloo.com/neuf/promo-voiture-neuve-maroc"

# Fonction pour extraire les liens et noms des véhicules sur une page donnée
def scrape_vehicles_links(page_url):
    response = requests.get(page_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        vehicle_data = []
        
        # Sélectionner les balises <p> avec la classe 'marque-modele'
        for item in soup.find_all('p', class_='marque-modele'):
            a_tag = item.find('a')  # Chercher la balise <a> à l'intérieur de <p>
            if a_tag:
                link = a_tag.get('href')
                
                name = a_tag.text.strip()
                vehicle_data.append({"name": name, "link": link})
        
        return vehicle_data
    else:
        print(f"Erreur lors de la récupération de {page_url} : {response.status_code}")
        return []

# Fonction pour extraire les détails d'un véhicule à partir de son lien
def scrape_vehicle_details(vehicle):
    response = requests.get(vehicle["link"])
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extraire les détails
        model = vehicle["name"]
        finition_elements = soup.find_all('p', class_='finition')

        # Parcourir les élements trouvés
        for element in finition_elements:
            # Trouver la balise <a> à l'interieur de <p>
            a_tag = element.find('a')
            if a_tag:
                version = a_tag.text.strip()  # Recuperer la version
        details = soup.find('ul', class_='detail').text.strip() 
        prices = soup.find('p', class_='prix').text.strip() if soup.find('p', class_='prix') else "N/A"
        
        # Extraire les prix initial et promo
        prices_split = prices.split("-")
        prix_promo = prices_split[0].strip() if len(prices_split) > 0 else "N/A"
        prix_initial = prices_split[1].strip() if len(prices_split) > 1 else "N/A"
        
        return {
            "Modèle": model,
            "Version": version,
            "Détails": details,
            "Prix initial": prix_initial,
            "Prix promo": prix_promo
        }
    else:
        print(f"Erreur lors de la récupération des détails de {vehicle['link']} : {response.status_code}")
        return None

# Fonction pour scraper toutes les pages
# Fonction pour scraper toutes les pages
def scrape_all_pages(start_page, end_page, max_vehicles=3):
    all_vehicles = []
    total_scraped = 0  # Counter for the total number of vehicles scraped
    
    # Scraper la page principale (sans numéro de page)
    print(f"Scraping {BASE_URL}...")
    vehicles = scrape_vehicles_links(BASE_URL)
    all_vehicles.extend(vehicles)
    total_scraped += len(vehicles)
    
    if total_scraped >= max_vehicles:
        return all_vehicles[:max_vehicles]  # Limit to the first 20 cars
    
    # Scraper les pages numérotées
    for page in range(start_page, end_page + 1):
        page_url = f"{BASE_URL}/{page}.html"
        print(f"Scraping {page_url}...")
        vehicles = scrape_vehicles_links(page_url)
        all_vehicles.extend(vehicles)
        total_scraped += len(vehicles)
        
        if total_scraped >= max_vehicles:
            return all_vehicles[:max_vehicles]  # Limit to the first 20 cars
    
    return all_vehicles[:max_vehicles]  # Ensure no more than max_vehicles are returned


# Spécifier les pages à scraper (par exemple, de la page 1 à 6)
start_page = 1
end_page = 6  # Changez cette valeur selon le nombre de pages disponibles

# Scraper toutes les pages et collecter les liens des véhicules
all_vehicles = scrape_all_pages(start_page, end_page)

# Extraire les détails de chaque véhicule
vehicle_details = []
for vehicle in all_vehicles:
    print(f"Scraping details for {vehicle['name']}...")
    details = scrape_vehicle_details(vehicle)
    if details:
        vehicle_details.append(details)

# Convertir les données en DataFrame Pandas
df = pd.DataFrame(vehicle_details)
print(df)
# Enregistrer les données dans un fichier CSV
output_file = "promotions_voitures.csv"
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"Données enregistrées dans {output_file}")
