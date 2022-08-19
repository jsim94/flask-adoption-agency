from flask import Flask, render_template, redirect, flash
from sqlalchemy import desc
from models import db, connect_db, Pet
from forms import AddPet, EditPet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ahdlkhawkedhwa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

GLOBAL_SPECIES = ['Cat', 'Dog', 'Porcupine']
GLOBAL_SPECIES_LIST = [(s, s) for s in GLOBAL_SPECIES]


@app.route('/')
def home_route():
    pets = Pet.query.order_by(desc('available')).all()
    return render_template("home.html", pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def show_pet_form():
    form = AddPet()
    form.species.choices = GLOBAL_SPECIES_LIST
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url,
                      age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()

        flash(f'{new_pet.name} added!')
        return redirect(f'/{new_pet.id}')
    else:
        return render_template('pet-form.html', form=form)


@app.route('/<pet_id>', methods=['GET', 'POST'])
def show_pet(pet_id):
    pet = Pet.query.get(pet_id)
    form = EditPet(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()
        flash(f'{pet.name} updated!')
        return redirect(f'/{pet.id}')

    else:
        return render_template('pet.html', form=form, pet=pet)
