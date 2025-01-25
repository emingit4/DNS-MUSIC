import os
import sys
from typing import List
import yaml

languages = {}
commands = {}
languages_present = {}

def get_command(value: str) -> List:
    return commands["command"][value]

def get_string(lang: str):
    return languages[lang]

# Türkçe dilini yükləyirik (hər dəfə bot başladıqda)
def load_turkish_language():
    try:
        with open(r"./strings/langs/tuk.yml", encoding="utf8") as file:
            languages["tuk"] = yaml.safe_load(file)
        languages_present["tuk"] = languages["tuk"]["name"]
        print(f"Türkçe dil faylı uğurla yükləndi: {languages['tuk'].get('name', 'Ad tapılmadı')}")
    except Exception as e:
        print(f"Türkçe dil faylı yüklənərkən xəta baş verdi: {str(e)}")
        sys.exit()

# Türkçe dilini yükləyirik
load_turkish_language()

# Bot başladıqda dilin doğru yükləndiyini yoxlayırıq
