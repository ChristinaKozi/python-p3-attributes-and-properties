#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    def __init__(self, name='Bruce', breed='Beagle'):
        if type(name) == str and 1 <= len(name) <= 25:
            self.name = name
            if type(breed) == str and breed in APPROVED_BREEDS:
                self.breed = breed
            else:
                print('Breed must be in list of approved breeds.')
        else: 
            print('Name must be string between 1 and 25 characters.')
