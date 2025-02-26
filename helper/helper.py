from datetime import datetime
import os
from flask import session
import json

def isImage(file):
    filename = file.filename
    separatedFilename = filename.split(".")
    extension = separatedFilename[len(separatedFilename) - 1]
    return extension == "png" or extension == "jpg" or extension == "jpeg"

def deleteFile(filename):
    dir = os.path.abspath("./public/images")
    path = os.path.join(dir,filename)
    if os.path.exists(path):
        os.remove(path)
    return not os.path.exists(path)

def saveFile(file):
    filename = f"image-{str(datetime.now().timestamp())}-{file.filename}"
    dir = os.path.abspath("./public/images")
    path = os.path.join(dir,filename)
    file.save(path)
    return filename

def getUser():
        if not session.get("user"):
            return None
        user = json.loads(session.get("user"))
        return user