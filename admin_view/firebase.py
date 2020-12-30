import pyrebase

from django.conf import settings

firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
storage = firebase.storage()

def upload_to_firebase(img_name,folder_name,path_local):
    path_on_cloud = f'{folder_name}/{img_name}.jpg'
    imgurl = storage.child(path_on_cloud).put(path_local)
    img_url=storage.child(path_on_cloud).get_url(imgurl['downloadTokens'])

    print(img_url)

    return img_url