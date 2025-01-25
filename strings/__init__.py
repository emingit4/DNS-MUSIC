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

# Türkçəni əvvəlcə yükləyirik
for filename in os.listdir(r"./strings/langs/"):
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "tr":  # Türkçəni yükləyirik
            languages["tr"] = yaml.safe_load(
                open(r"./strings/langs/tr.yml", encoding="utf8")
            )
            languages_present["tr"] = languages["tr"]["name"]
        else:
            # Digər dilləri yükləyirik, amma Türkçəni əsas olaraq saxlayırıq
            languages[language_name] = yaml.safe_load(
                open(r"./strings/langs/" + filename, encoding="utf8")
            )
            # Türkçədən məlumatı əlavə edirik
            for item in languages["tr"]:
                if item not in languages[language_name]:
                    languages[language_name][item] = languages["tr"][item]
        try:
            languages_present[language_name] = languages[language_name]["name"]
        except:
            print("Dil faylında problem var. Zəhmət olmasa, problemi @TheTeamvk-ya bildirin.")
            sys.exit()

# Başlanğıcda Türkçə dilini seçirik
default_language = "tr"
print(f"Bot başladı, dil: {languages_present.get(default_language)}")
