Election Scraper - Volební výsledky z volby.cz

Tento program slouží k automatickému stažení a uložení volebních výsledků z webových stránek volby.cz do souboru ve formátu CSV.

Požadavky:

Vytvořte si virtuální prostředí. To vytvoříte v terminálu tímto příkazem:

python -m venv venv

source venv/bin/activate (tímto příkazem aktivujete virtuální prostředí)

Že máte virtuální prostředí aktivní poznáte tak že se vám v terminalu zobrazí toto:

(venv) vase@jmeno: 

Ted už máte virtuální prostředí aktivní a můžete jít na další krok.

Před spuštěním programu se ujistěte, že máte nainstalované následující knihovny:

requests - Pro stahování dat z webu.

beautifulsoup4 - Pro parsování HTML obsahu.

Tuto Knihovnu nemusíš instalovat je součástí pythonu stačí si jí naimportovat příkazem:

import csv - Pro zápis dat do CSV souboru.

Pokud je nemáte nainstalované, spusťte tento příkaz:

pip install -r requirements.txt

Pokud jste na Linuxu zkuste tento příkaz:

pip3 install -r requirements.txt

Spuštění programu

Stáhněte nebo zkopírujte soubor main.py do svého počítače.

Otevřete terminál (příkazový řádek) ve složce, kde je uložen soubor.

Spusťte program pomocí následujícího příkazu:

python main.py "<URL_ADRESA>" "<NAZEV_SOUBORU.csv>"

Důležité: Program vyžaduje dva argumenty, které musí být v uvozovkách aby se program spustil.

První argument – URL adresa stránky na webu volby.cz

Druhý argument – Název souboru, kam se uloží výsledky (musí mít příponu .csv)

Příklad použití:

python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106" "vysledky_ostrava.csv"

Tento příkaz stáhne data z webu volby.cz a uloží je do souboru vysledky_ostrava.csv

Struktura CSV souboru

Výsledný CSV soubor bude obsahovat následující sloupce:

Kód | Město | Registrovaní | Obálky | Hlasy | Strana 1 | Strana 2 | ...

Kód – Kód města/obce
Město – Název města nebo obce
Registrovaní – Počet registrovaných voličů
Obálky – Počet vydaných obálek
Hlasy – Počet platných hlasů
Strana 1, Strana 2, ... – Počet hlasů pro jednotlivé strany

Po spuštění se vám v terminálu zobrazí průběh stahování :

STAHUJI DATA Z VYBRANEHO URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106

UKLADAM DO SOUBORU: vysledky_ostrava.csv

PROGRAM UKONČEN


