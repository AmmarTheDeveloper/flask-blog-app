import json
from flask import session
from helper.helper import getUser

def inject():
    return dict(getUser=getUser)