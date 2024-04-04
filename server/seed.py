#!/usr/bin/env python3
# server/seed.py

from app import app
from models import db, Pet
from faker import Faker
from random import choice

with app.app_context():
    # Create and initialize a Faker instance
    fake = Faker()

    # Delete all rows in the "pets" table
    Pet.query.delete()

    # Create an empty list
    pets = []

    # Species list
    species = ['Dog', 'Cat', 'Hamster', 'Snake']

    # Add some Pet instances to the list
    for _ in range(3):
        pets.append(Pet(name=fake.first_name(), species=choice(species)))

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()
