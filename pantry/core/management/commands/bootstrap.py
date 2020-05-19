import pathlib
from pantry.core.models import Ingredient
from django.core.management.base import BaseCommand
from django.db import IntegrityError


def insert_ingredients():

    path = pathlib.Path(__file__).parent.absolute()
    with open(f'{path}/ingredients.txt') as f:
        data = f.readlines()

    for line in data:
        i = Ingredient(name=line.strip().lower())
        try:
            i.save()
            print(f'Saving {i.name}')
        except IntegrityError:
            print(f'Could not save duplicate {i.name}')


class Command(BaseCommand):
    help = 'Inserts ingredients to database'

    def handle(self, *args, **options):
        insert_ingredients()
