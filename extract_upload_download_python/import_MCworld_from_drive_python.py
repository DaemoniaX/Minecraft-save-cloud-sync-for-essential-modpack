import os
import shutil
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
 
# CR2026 @DaemoniaX https://github.com/DaemoniaX

print("\n Starting import...")

# change name, path, and folder id if needed
user_profile = os.path.expanduser("~")
target_dir = os.path.join(user_profile, "curseforge", "minecraft", "Instances", "Endless Terrors", "saves", "Survie Horreur")
temp_dir = os.path.join(user_profile, "Desktop", "Temp_MC_Restore")
temp_zip_path = os.path.join(temp_dir, "latest_backup.zip")
folder_id = '1rcheeZRT-RpBDH74evyEYrkA' #random id

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