from models.service import Service
import mlab
from faker import Faker
from random import randint,choice
from pymongo import MongoClient




fake = Faker()

mlab.connect()


for i in range(100):
    print('Saving Service', i + 1, '...........')
    gender = randint(0,1)
    name = fake.name_male() if gender==1 else fake.name_female()
    if gender == 0 :
        image = choice(['https://www.pexels.com/photo/portrait-of-a-beautiful-woman-255349/'])
    elif gender == 1:
        image = 'https://thumbs.dreamstime.com/z/fashion-man-beautiful-young-male-handsome-boy-outdoors-park-dressing-white-sweater-gray-trousers-exciting-64958203.jpg'
    new_service = Service(name = name, yob = randint(1995,2000), gender = randint(0,1), height = randint(145,168),
                        phone = fake.phone_number(), address = fake.address(), status = choice([True,False]),description = fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None),
                        measurements = [randint(70, 120), randint(70, 123), randint(70, 120)],image =image)
    new_service.save()
