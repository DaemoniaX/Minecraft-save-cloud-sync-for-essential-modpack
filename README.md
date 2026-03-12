# Minecraft-save-cloud-sync-for-essential-modpack
  
Hi, I was playing on a Minecraft horror modpack on Curseforge using Essentials, and I was wondering...how can I share 
my world to my friend so they can play while I can't host. Like a regular server. And automate it.  
  
And so I got this idea : 
- creating a script that automate the process of grabing the save, compress it and drop it on google drive,
- another script grab the save on the google drive and put it in the modpack folder,
- no one have to install any dependencies except the script itself.
  
I thought I could craete an all distrib script in bash....but bash needs some dependencies on windows...  
Powershell would take me too much time to learn, and so I did it in batch....but batch can't work with Google Drive.  
There is right now the 2 python script, but they need you to install Python and it's dependencies, wich is not plug-and-play.
So later this week(probably) or next week I'll drop the Python .exe script that can do this. 
  
## Table of Contents

* [🔧 Installation](#-installation)
* [💡 Usage](#-usage)
* [✨ Features](#-features)
* [🛠️ Tech Stack](#️-tech-stack)
* [🤝 Contributing](#-contributing)
* [✉️ Contact](#️-contact)
* [📄 License](#-license)

---

## 🔧 Installation BATCH, ALWAYS READ THE CONTENT OF A BATCH SCRIP BEFORE USING IT

1. **Download**

   Install the 2 scripts in /minecraft_essential_exctract_batch
     
2. **Edit**

    Change the path and the name of the mods/folder if needed.  
    
3. **Share**
      
   Share the edited script to your friends.  
   
## 🔧 Installation PYTHON

1. **Download**

   Install the 2 scripts '.py' in /extract_upload_download_python
     
2. **Edit**

    Change the path and the name of the mods/folder if needed, and the Google Drive folder ID.
    
3. **Share**
      
   Share the edited script to your friends. 
  
4. **Setup the Google Server access**

   You can follow this tutorial about it : https://www.youtube.com/watch?v=wde6yn9z-vY
  
  
## 💡 Usage

* Batch : Use the script to compress the save, use the other scipt to decompress it.
* Python : Install Python and :
```cmd
python -m venv venv
venv\Scripts\activate
pip install pydrive2 pyinstaller
```


## 🛠️ Tech Stack

* **Language**: batch

---

## 🤝 Contributing

This was made following a batch tutorial, and the official Microsoft Doc.  
This doc about Pydrive2 : https://docs.iterative.ai/PyDrive2/filemanagement/
This doc about gauth : https://docs.iterative.ai/PyDrive2/oauth/

Contributions, issues and feature requests are welcome! Please feel free to:

* Fork the repository

---

## ✉️ Contact

**Name**: Antonin Marolleau  
**School**: ESIEE Paris – Integrated Engineering Program second year  
**Email**: [antonin.marolleau@edu.esiee.fr](mailto:antonin.marolleau@edu.esiee.fr)  
**LinkedIn**: [https://www.linkedin.com/in/antonin-marolleau-7b5497339](https://www.linkedin.com/in/antonin-marolleau-7b5497339)  

---

## 📄 License

This project is licensed under the CC0 License.