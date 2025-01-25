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
                languages["tr"] = yaml.safe_load(open(r"./strings/langs/tr.yml", encoding="utf8"))
                languages_present["tr"] = languages["tr"]["name"]
                print("Türkçe dil faylı uğurla yükləndi.")  # Debug mesajı
            except Exception as e:
                print(f"Türkçe dil faylı yüklənərkən xəta baş verdi: {e}")
                sys.exit()
        else:
            languages[language_name] = yaml.safe_load(open(r"./strings/langs/" + filename, encoding="utf8"))
            for item in languages["tr"]:
                if item not in languages[language_name]:
                    languages[language_name][item] = languages["tr"][item]
        
        try:
            languages_present[language_name] = languages[language_name]["name"]
        except KeyError:
            print(f"Error loading language file: {language_name}. Please check the language file format.")
            sys.exit()

# languages sözlüyünü çap edirik
print("Languages:", languages)

# Başlanğıcda Türkçe dilini seçirik
default_language = "tr"
if default_language in languages:
    print(f"Bot başladı, dil: {languages_present.get(default_language)}")
else:
    print("Türkçe dili tapılmadı. Dil faylını yoxlayın.")
