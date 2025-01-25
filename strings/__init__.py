import os
import sys
import yaml

languages = {}
languages_present = {}

def get_string(lang: str):
    return languages[lang]

try:
    # Türkçe faylını yükləyirik (tuk.yml)
    print("Türkçe dil faylını yükləyirik...")
    with open(r"./strings/langs/tuk.yml", encoding="utf8") as file:
        languages["tuk"] = yaml.safe_load(file)
    
    # Fayl strukturunu yoxlayırıq
    if "name" not in languages["tuk"]:
        print("Türkçe dil faylında 'name' açarı tapılmadı. Fayl düzgün formatda deyil.")
        sys.exit()
    
    languages_present["tuk"] = languages["tuk"]["name"]
    print(f"Türkçe dil faylı uğurla yükləndi: {languages['tuk'].get('name', 'Ad tapılmadı')}")
except Exception as e:
    print(f"Türkçe dil faylı yüklənərkən xəta baş verdi: {str(e)}")
    sys.exit()

# Yüklənmiş dilləri yoxlayaq
print("Languages loaded:", list(languages.keys()))

# Faylın düzgün yüklənib-yüklənmədiyini test edirik
print("Türkçe dil faylı başlığı:", languages["tuk"]["name"])

# DEBUG üçün məlumatları göstərmək
if os.getenv("DEBUG") == "1":
    for item, value in languages["tuk"].items():
        print(f"{item}: {value}")
