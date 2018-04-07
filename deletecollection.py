from models.service import Service
from mongoengine import *
import mlab

mlab.connect()

Service.objects().delete()
