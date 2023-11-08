import uuid
import os
from django.db import models

# Create your models here.
#We will create a specific folder and in that folder we will dump the files useer will upload and then we will zip it and send it.

class Folder(models.Model):#A model for folder
    uid = models.UUIDField(primary_key=True,editable=False ,default=uuid.uuid4)#basically a directory where the files will get uploaded
    created_at= models.DateField(auto_now=True)

def get_upload_path(instance, filename): #creates a random folder based on uid and save files in that folder which will be zipped
    return os.path.join(str(instance.folder.uid),filename)

class Files(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)#we cant write a dyanmic field directly we need a function thqat creates a folder and dumps all the files
    created_at= models.DateField(auto_now=True)
    
  
