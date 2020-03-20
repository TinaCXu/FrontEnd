import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
#configuring the basic environment for the project

import django
django.setup()

#fake population script
import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker()
#call the function faker, return a instance and give the instance to fakegen
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    #Topic, as a derived class of models.Model, has the objects attribute
    #get_or_create: will return a tuple and we only need the first element of the tuple
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top = add_topic()
        #create the fake data for that entry 
        #fakegen, the instance of Faker, has function url(),call the funcion url() in instance fakegen
        #return the value and give it to fake_url
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        #create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        #create a fake access record for that webpage: watch out the foreign key relationship
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    #__name__ is a special system variable representing the name of the module: __main__  represents it 
    #is the main module, if it is a imported module, then the name should be like 'django','os'
    print('populating')
    populate(20)
    print('populating complete！')
