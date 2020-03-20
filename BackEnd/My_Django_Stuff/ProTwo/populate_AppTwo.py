import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')
#configuring the basic environment for the project

import django
django.setup()

#fake population script
import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()
#call the function faker, return a instance and give the instance to fakegen

def populate(N=5):
    for _ in range(N):
        #create fake data
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_mail = fakegen.email()
        #create the new user entry
        Users = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,mail=fake_mail)[0]

if __name__ == '__main__':
    print('populating')
    populate(25)
    print('populating complete！')

