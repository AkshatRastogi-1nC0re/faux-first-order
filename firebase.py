import pyrebase

config = {
    "apiKey": "AIzaSyAPmnrMVtjPRlhEuo24U-VCxuZyRroH_MQ",
    "authDomain": "hackathon-buhack.firebaseapp.com",
    "projectId": "hackathon-buhack",
    "storageBucket": "hackathon-buhack.appspot.com",
    "messagingSenderId": "8724895688",
    "appId": "1:8724895688:web:c957fbd1cdfecf93f912fd",
    "measurementId": "G-BLR804JCFL",
    "databaseURL": ""
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def getLink():
    mp4name = "results.mp4"
    path_on_cloud="res.mp4"
    storage.child(path_on_cloud).put(mp4name)
    a = storage.child(path_on_cloud).get_url(None)
    return a