from mongoengine import *


class Missions(Document):
    mission_name = StringField()
    description = StringField()

class User(Document):
    username = StringField(unique=True)
    email = StringField(unique= True)
    password = StringField()

# document
class UserMission(Document):
    user =  ReferenceField(User)
    mission = ReferenceField(Missions)
    completed = BooleanField(default = False)
    image = StringField()
    caption = StringField()
    saved = BooleanField(default = False)
    not_save = BooleanField()


class Library(Document):
    user = ReferenceField(User)
    user_missions = ListField(ReferenceField(UserMission))
