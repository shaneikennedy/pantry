from django.db import migrations
import pathlib


def backfill_ingredients(apps, schema_editor):

    Ingredient = apps.get_model('core', 'Ingredient')

    path = pathlib.Path(__file__).parent.absolute()
    with open(f'{path}/ingredients.txt') as f:
        data = f.readlines()

    for line in data:
        i = Ingredient(name=line.strip().lower())
        try:
            i.save()
            print(f'Saving {i.name}')
        except Exception:
            print(f'Could not save duplicate {i.name}')


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('core', '0001_auto_20200513_1952'),
    ]

    operations = [
        migrations.RunPython(backfill_ingredients),
    ]
