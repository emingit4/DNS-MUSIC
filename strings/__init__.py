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

# Dil fayllarını yükləmək
for filename in os.listdir(r"./strings/langs/"):
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        
        # Türkçəni ilk olaraq yükləyirik
        if language_name == "tr":  
            try:
                # Türkçə faylını yükləməyə çalışırıq
                languages["tr"] = yaml.safe_load(open(r"./strings/langs/tr.yml", encoding="utf8"))
                languages_present["tr"] = languages["tr"]["name"]
                print("Türkçe dil faylı uğurla yükləndi.")  # Debug mesajı
            except Exception as e:
                print(f"Türkçe dil faylı yüklənərkən xəta baş verdi: {e}")
                sys.exit()
        else:
            # Digər dilləri yükləyirik
            languages[language_name] = yaml.safe_load(open(r"./strings/langs/" + filename, encoding="utf8"))
            # Türkçədən məlumatları əlavə edirik
            for item in languages["tr"]:
                if item not in languages[language_name]:
                    languages[language_name][item] = languages["tr"][item]

        try:
            languages_present[language_name] = languages[language_name]["name"]
        except KeyError:
            print(f"Error loading language file: {language_name}. Please check the language file format.")
            sys.exit()

# Yüklənmiş dilləri yoxlayaq
print("Languages loaded:", languages)

# Əgər Türkçe yüklənməyibsə, Xəta mesajı verək
if "tr" not in languages:
    print("Türkçe dili tapılmadı. Dil faylının doğru yükləndiyini yoxlayın!")
    sys.exit()
