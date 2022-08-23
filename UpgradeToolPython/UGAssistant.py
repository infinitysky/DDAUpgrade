
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
    runCMD3='cmd /c taskkill /IM "PDAServer.exe" /F'
    runCMD4="cmd /c" + FileToInstall + " /S"
    os.system(runCMD1)
    os.system(runCMD2)
    os.system(runCMD3)
    os.system(runCMD4)
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
    


        

if __name__ == "__main__":
    getDDAVersion()
