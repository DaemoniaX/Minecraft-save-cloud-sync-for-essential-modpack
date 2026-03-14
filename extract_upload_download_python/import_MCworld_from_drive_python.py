import os
import shutil
import json
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
 
# CR2026 @DaemoniaX https://github.com/DaemoniaX

print("\n Starting import...")

config_file = "config.json"

default_config = {
    "save_name": "replace here the Save_Name",
    "modpack_name": "replace here the Modpack_Name, and below this line, let the path empty if it is in the default folder, else replace it",
    "custom_path": "",
    "folder_id": "replace here the google drive code (you should check the doc on github) 1ercgZE57G7-DsdSYSeyurj57hhijl"
}

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

# change name, path, and folder id if needed
user_profile = os.path.expanduser("~")
temp_dir = os.path.join(user_profile, "Desktop", "Temp_MC_Restore")
temp_zip_path = os.path.join(temp_dir, "latest_backup.zip")

if custom_path == "":
    base_instances_dir = os.path.join(user_profile, "curseforge", "minecraft", "Instances")
else:
    base_instances_dir = custom_path

target_dir = os.path.join(base_instances_dir, modpack_name, "saves", save_name)

print("\n Attempting connection...")

gauth = GoogleAuth()
gauth.LoadCredentialsFile("saved_login.txt")

if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("saved_login.txt")
drive = GoogleDrive(gauth)

print("Connected.")

file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

if not file_list:
    print("\n ERROR : No file in the Google Drive !")
    input("Press enter to quit...")
    exit()

file_list.sort(key=lambda x: x['createdDate'], reverse=True)
latest_file = file_list[0]

print(f"File found : {latest_file['title']}")


os.makedirs(temp_dir, exist_ok=True)
print("\n Downloading file...")
latest_file.GetContentFile(temp_zip_path)


print("\n Clearing current save...")
if os.path.exists(target_dir):
    shutil.rmtree(target_dir)
os.makedirs(target_dir, exist_ok=True)

print("Extracting...")
shutil.unpack_archive(temp_zip_path, target_dir, 'zip')
shutil.rmtree(temp_dir)

print("\n Import ended.")
input("Press enter to quit...")