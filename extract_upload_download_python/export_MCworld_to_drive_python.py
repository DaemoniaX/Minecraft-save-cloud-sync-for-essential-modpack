import os
import shutil
from datetime import datetime
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
# CR2026 @DaemoniaX https://github.com/DaemoniaX

print("\n Hi, the export will soon begin, have you configured the variables inside of the python file? such as name and path of the modpack folder?")

# Change the name, path and folder id
user_profile = os.path.expanduser("~")
save_name = "SAVE_NAME"
source_dir = os.path.join(user_profile, "curseforge", "minecraft", "Instances", "MODPACK_NAME", "saves", "SAVE_NAME")
#source_dir = os.path.join(user_profile, "curseforge", "minecraft", "Instances", "Endless Terrors", "saves", "Survie Horreur")
backup_dir = os.path.join(user_profile, "Desktop", "Backup_Minecraft")

#what is a folder id? on google drive, go inside the folder you want your save to be into, and copy only the end of the link
#https://drive.google.com/drive/u/3/folders/1ercgZE57G7-DsdSYSeyurj57hhijl <= only the end part
folder_id = '1ercgZE57G7-DsdSYSeyurj57hhijl'

date_jour = datetime.now().strftime("%d-%m-%Y")
zip_filename = f"{save_name}_{date_jour}"
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
input("Appuyez sur Entree pour quitter...")