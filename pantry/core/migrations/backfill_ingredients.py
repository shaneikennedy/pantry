from django.db import migrations
import pathlib


def backfill_ingredients(apps, schema_editor):

    Ingredient = apps.get_model('core', 'Ingredient')

    path = pathlib.Path(__file__).parent.absolute()
    with open(f'{path}/ingredients.txt') as f:
        data = f.readlines()

    ingredients = [
        Ingredient(name=line.strip().lower())
        for line in data
    ]

    Ingredient.objects.bulk_create(ingredients)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(backfill_ingredients),
    ]
