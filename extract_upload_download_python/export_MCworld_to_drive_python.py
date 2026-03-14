import os
import shutil
import json
from datetime import datetime
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
# CR2026 @DaemoniaX https://github.com/DaemoniaX

print("\n Hi, the export will soon begin, have you configured the variables inside of the config file? such as name and path of the modpack folder?")

config_file = "config.json"

default_config = {
    "save_name": "replace here the Save_Name",
    "modpack_name": "replace here the Modpack_Name, and below this line, let the path empty if it is in the default folder, else replace it",
    "custom_path": "",
    "folder_id": "replace here the google drive code (you should check the doc on github) 1ercgZE57G7-DsdSYSeyurj57hhijl"
}

# check if someone forgot to install the json file aswell
if not os.path.exists(config_file):
    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(default_config, f, indent=4)
    print(f"\n Please fill the '{config_file}' with the right values like in the github documentation.")
    print("\n https://github.com/DaemoniaX/Minecraft-save-cloud-sync-for-essential-modpack")
    input("\n Press enter to quit...")
    exit()

with open(config_file, "r", encoding="utf-8") as f:
    config = json.load(f)

save_name = config["save_name"]
modpack_name = config["modpack_name"]
custom_path = config.get("custom_path", "")
folder_id = config["folder_id"]



user_profile = os.path.expanduser("~")

if custom_path == "":
    base_instances_dir = os.path.join(user_profile, "curseforge", "minecraft", "Instances")
else:
    base_instances_dir = custom_path

source_dir = os.path.join(base_instances_dir, modpack_name, "saves", save_name)
backup_dir = os.path.join(user_profile, "Desktop", "Backup_Minecraft")

#what is a folder id? on google drive, go inside the folder you want your save to be into, and copy only the end of the link
#https://drive.google.com/drive/u/3/folders/1ercgZE57G7-DsdSYSeyurj57hhijl <= only the end part
# folder_id = '1ercgZE57G7-DsdSYSeyurj57hhijl'

day_date = datetime.now().strftime("%d-%m-%Y")
zip_filename = f"{save_name}_{day_date}"
zip_filepath = os.path.join(backup_dir, zip_filename)


if not os.path.exists(source_dir):
    print(f"\n ERROR : Folder not found -> {source_dir}")
    input("\n Press Enter to quit...")
    exit()

os.makedirs(backup_dir, exist_ok=True)

print(f"\n Compressing...")
shutil.make_archive(zip_filepath, 'zip', source_dir)

print(f"\n Success: {zip_filename}.zip is now in the folder backup_minecraft.")

print("\n Initializing export...")

gauth = GoogleAuth()
gauth.LoadCredentialsFile("saved_login.txt")

if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("saved_login.txt")

print("\n Connecting...")
drive = GoogleDrive(gauth)
print("\n Connected. Exportig...")


path_zip = f"{zip_filepath}.zip"

fichier_drive = drive.CreateFile({
    'title': f"{zip_filename}.zip",
    'parents': [{'id': folder_id}]
})


fichier_drive.SetContentFile(path_zip)
fichier_drive.Upload()

print("Done.")
input("Press enter to quit...")