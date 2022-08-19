from models import db, Pet
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

pets = [Pet(name='Coco', species='Cat', photo_url='https://upload.wikimedia.org/wikipedia/commons/4/4c/Blackcat-Lilith.jpg',
            age=2, notes='Rambunctious', available=True),
        Pet(name='Snickers', species='Dog', photo_url='https://upload.wikimedia.org/wikipedia/commons/3/34/Labrador_on_Quantock_%282175262184%29.jpg',
            age=8, notes='Diabetic', available=True),
        Pet(name='Peach', species='Cat', photo_url='https://upload.wikimedia.org/wikipedia/en/c/c1/Orange_catpc.jpg',
            age=3, notes='', available=False)]

db.session.add_all(pets)

db.session.commit()
