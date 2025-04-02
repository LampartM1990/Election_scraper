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

Stahuji data z vybraneho URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106

Ukladam data do: vysledky_ostrava.csv

Program ukončem

Částečný výstup:

Kod obce,Nazev obce,Voliči,Vydané obalky,Platné hlasy,Občanská demokratická strana,.......
569119,Čavisov,419,318,316,29,0,0,22,0,16,34,4,2,2,0,0,36,0,0,5,103,0,0,27,0,1,2,0,29
506711,Dolní Lhota,1 202,904,899,95,2,0,69,0,31,41,9,3,2,1,1,90,0,0,25,356,0,2,65,0,6,7,0,91
569500,Horní Lhota,691,481,474,49,0,0,39,1,17,52,5,4,1,0,0,38,0,0,8,152,0,0,19,0,2,5,0,82
599549,Klimkovice,3 652,2 453,2 434,230,0,0,166,1,56,200,32,16,34,3,6,292,0,4,97,835,2,0,156,2,22,8,7,256
554049,Olbramice,545,368,356,27,0,0,33,2,13,16,5,4,4,0,0,25,0,0,12,122,0,2,41,0,1,1,1,45
554821,Ostrava,237 254,125 244,124 258,10 288,114,82,10 566,124,3 045,10 640,1 540,804,1 537,141,129,11 446,62,99,3 451,44 268,125,220,5 405,34,1 091,281,318,17 799



