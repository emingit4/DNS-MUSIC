import os
import sys
import yaml

languages = {}
languages_present = {}

def get_string(lang: str):
    return languages[lang]

# Dil fayllarını yükləmək
try:
    # Türkçe faylını yükləyirik (tuk.yml)
    print("Türkçe dil faylını yükləyirik...")
    with open(r"./strings/langs/tuk.yml", encoding="utf8") as file:
        languages["tuk"] = yaml.safe_load(file)  # Burada 'tuk' dilini yükləyirik
    languages_present["tuk"] = languages["tuk"]["name"]  # 'tuk' dilini istifadə edirik
    print(f"Türkçe dil faylı uğurla yükləndi: {languages['tuk']}")
except Exception as e:
    print(f"Türkçe dil faylı yüklənərkən xəta baş verdi: {e}")
    sys.exit()

# Yüklənmiş dilləri yoxlayaq
print("Languages loaded:", languages)

# Əgər Türkçe yüklənməyibsə, Xəta mesajı verək
if "tuk" not in languages:
    print("Türkçe dili tapılmadı. Dil faylının doğru yükləndiyini yoxlayın!")
    sys.exit()

# Dil faylının düzgün yüklənib-yüklənmədiyini test edirik
print("Türkçe dil faylı:", languages["tuk"])

# Faylın içindəki bütün dil məlumatlarını ekrana çıxartmaq (Test məqsədli)
for item in languages["tuk"]:
    print(f"{item}: {languages['tuk'][item]}")
