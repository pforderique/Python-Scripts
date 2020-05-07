'''
DESCRIPTION:
    Program that organizes my downloads folder
    >>> pdf's into "PDF Files" folder
    >>> text documents in "Text Files" folder
    >>> images (jpg or png) in "Downloaded Images" folder

    @author Piero Orderique
    @date 
'''
import os
import shutil
from time import sleep

DOWNLOADS_PATH = 'C:\\Users\\fabri\\Downloads\\'
DIRECTORIES = {
    '.pdf':'PDF Folder',
    '.png':'Images Folder',
    '.jpg':'Images Folder',
    '.exe':'Installers and Setups',
    '.msi':'Installers and Setups',
    '.docx':'Word Folder',
    'other':'Unidentified'
}

def createDirectories():
    for key in DIRECTORIES:
        dirName = DOWNLOADS_PATH+DIRECTORIES[key]
        if not os.path.exists(dirName):
            os.mkdir(dirName)
            print("Directory" , dirName ,  "Created")
        else:    
            print("Directory" , dirName ,  "already exists")

def listFiles(path=DOWNLOADS_PATH):
    for file in os.listdir(path): 
        if file.endswith('.pdf'):
            # print('PDF File:',file)
            pass
        elif file.endswith('.png') or file.endswith('.jpg'):
            # print('Image File:',file)
            pass
        else:
            print('UNIDENTIFIED:',file)

def organizeDownloads():
    for file in os.listdir(DOWNLOADS_PATH):
        ext = file[file.rfind('.'):]
        try:
            shutil.move(DOWNLOADS_PATH+file,DOWNLOADS_PATH+DIRECTORIES[ext])
            print(DOWNLOADS_PATH+file,'moved to',DOWNLOADS_PATH+DIRECTORIES[ext])
        except:
            if file.find('.') > -1:
                try:
                    shutil.move(DOWNLOADS_PATH+file,DOWNLOADS_PATH+DIRECTORIES['other'])   
                    print(DOWNLOADS_PATH+file,'moved to',DOWNLOADS_PATH+DIRECTORIES['other'])
                except:
                    print('Error Unknown')
            else:
                print('Already a folder:',DOWNLOADS_PATH+file)

if __name__ == "__main__":
    while True:
        try:
            organizeDownloads()
            sleep(10)
        except KeyboardInterrupt:
            print("Downloads Organizer Program Terminated.")
            break