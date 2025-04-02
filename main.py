
import requests
import sys
from bs4 import BeautifulSoup as bs

def get_web(url):
    """Stáhne HTML stránku a převede ji na objekt BeautifulSoup."""
    response = requests.get(url)
    return bs(response.content, "html.parser")

def get_base_url(url):
    """Vrátí základní část URL."""
    parts = url.split("/")
    return "/".join(parts[:-1]) + "/"

def get_locations(soup, base_url):
    """Najde odkazy na jednotlivé obce."""
    links = []
    for link in soup.select(".cislo a"):
        links.append(base_url + link.get("href"))
    return links

def extract_election_data(soup, location, is_foreign):
    """Získá informace o volbách pro jednu obec."""
    data = {}
    if is_foreign:
        loc_code = soup.select_one("#publikace > h3:nth-child(3)").text.split(":")[-1].strip()
        loc_name = soup.select_one("#publikace > h3:nth-child(4)").text.split(":")[-1].strip()
    else:
        loc_code = location.split("obec=")[-1].split("&")[0]
        loc_name = soup.select_one("#publikace > h3:nth-child(4)").text.split(":")[-1].strip()
    
    data["Kod obce"] = loc_code
    data["Nazev obce"] = loc_name
    data["Voliči"] = soup.select_one("td[headers='sa2']").text
    data["Vydané obalky"] = soup.select_one("td[headers='sa3']").text
    data["Platné hlasy"] = soup.select_one("td[headers='sa6']").text
    
    parties = [p.text for p in soup.select(".overflow_name")]
    votes = [v.text for v in soup.select("td[headers*='t1sb3'], td[headers*='t2sb3']")]
    for i in range(len(parties)):
        data[parties[i]] = votes[i]
    
    return data

def get_results(locations, is_foreign):
    """Stáhne a zpracuje volební data pro každou obec."""
    results = []
    for loc in locations:
        soup = get_web(loc)
        results.append(extract_election_data(soup, loc, is_foreign))
    return results

def check_args():
    """Zkontroluje správnost argumentů."""
    if len(sys.argv) != 3:
        print("Špatný počet argumentů!")
        sys.exit()
    if not sys.argv[1].startswith("https://www.volby.cz/pls/ps2017nss/"):
        print("Neplatná URL!")
        sys.exit()
    if not sys.argv[2].endswith(".csv"):
        print("Druhý argument musí být CSV soubor!")
        sys.exit()

def save_data(results, filename):
    """Uloží výsledky do CSV souboru."""
    with open(filename, "w", encoding="utf-8") as file:
        headers = results[0].keys()
        file.write(",".join(headers) + "\n")
        for row in results:
            file.write(",".join(row.values()) + "\n")

def main():
    """Hlavní funkce programu."""
    check_args()
    url = sys.argv[1]
    csv_file = sys.argv[2]
    print(f"Stahuji data z URL: {url}")
    base_url = get_base_url(url)
    soup = get_web(url)
    locations = get_locations(soup, base_url)
    is_foreign = "ps36?" in url
    results = get_results(locations, is_foreign)
    print(f"Ukládám data do: {csv_file}")
    save_data(results, csv_file)
    print("Program ukončen")

if __name__ == "__main__":
    main()
