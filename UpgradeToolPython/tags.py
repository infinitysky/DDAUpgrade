import tkinter as tk
import tkinter.font as tkFont
import requests
import os
import urllib.request
import os.path


def createTempFolder():
    directory ="C:\Ziitech"
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print("yes")

def DDAInstallationProcess(FileToInstall):
    print("start")
    runCMD1='cmd /c taskkill /IM "AssistantServer(v1.2.1).exe" /F'
    runCMD2='cmd /c taskkill /IM "ZiiPOSClassicRetail.exe" /F'
    runCMD3="cmd /c" + FileToInstall + " /S"
    os.system(runCMD1)
    os.system(runCMD2)
    os.system(runCMD3)
    exit();


def downloadZiiPOSRetail(dornloadURL,filePath):
    #filePath = path+"\ZiiPOSRetail"+version+".exe"
    urllib.request.urlretrieve(dornloadURL, filePath)
    file_exists = os.path.exists(filePath)
    if (file_exists==True):
        DDAInstallationProcess(filePath)
    else:
        print("Error")


    



def getDDAVersion():
    URL = "https://wombat-api.ziicloud.com/api/vs/client-version/version?clientName=Zii.Retail_Classic&version=1"
    r = requests.get(url = URL)
    data = r.json()
    version = str(data['data']['versionValue'])
    downloadurl=data['data']['upgradeUrl']
    print(downloadurl)
    createTempFolder()
    directory ="C:\Ziitech"
    filePath = "C:\Ziitech\ZiiPOSRetail"+version+".exe"
    downloadZiiPOSRetail(downloadurl,filePath)
    


class App:
    def __init__(self, root):
        #setting title
        root.title("ZiiPOS Retail Upgrade")
        #setting window size
        width=229
        height=146
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_936=tk.Button(root)
        GButton_936["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_936["font"] = ft
        GButton_936["fg"] = "#000000"
        GButton_936["justify"] = "center"
        GButton_936["text"] = "getZiiPOSretailUpgrade"
        GButton_936.place(x=40,y=40,width=153,height=52)
        GButton_936["command"] = self.GButton_936_command

    def GButton_936_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
