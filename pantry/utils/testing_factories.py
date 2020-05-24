import factory.fuzzy
from pantry.core.models import Recipe, RecipeIngredient, Ingredient


class IngredientFactory(factory.DjangoModelFactory):
    name = factory.Faker(
        'sentence',
        ext_word_list=None,
    )

    class Meta:
        model = Ingredient


class RecipeIngredientFactory(factory.DjangoModelFactory):
    class Meta:
        model = RecipeIngredient


class RecipeFactory(factory.DjangoModelFactory):
    name = factory.Faker(
        'sentence',
        ext_word_list=None,
    )
    instructions = factory.Faker(
        'paragraph',
        nb_sentences=1,
        variable_nb_sentences=True,
        ext_word_list=None,
    )

    class Meta:
        model = Recipe
