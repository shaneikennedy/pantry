# Pantry

## Intro
Hi, Lendo!

This is a project I call pantry. It was something that my sister and I started at the begining of the covid-19 pandemic. My sister is now in her final year of a computer science degree back in Canada and wanted to learn web development on a more long term, and production-ready codebase (aka something more than just a quick assignment).

The idea behind this app is a crowd-sourced Recipe Catalog. Users should be able to create their own recipes, discover others' recipes, and like them to save for later.

## For Lendo
The main branch of this repo has frontend code so that a real user could eventually use it, but for simplicity and the purpose of this role I figured that stripping it down to an API would be best.
The code demo'd here will just be a REST api for checking out the ingredients that are available (as well as adding one's that aren't there), searching existing recipes and creating some of your own.

The list-endpoint are all paginated and support searching. To search, find the "filters" button in the UI. The list-endpoints also support creation (just scroll to the bottom and fill out the form)

The detail endpoints are read-only.

To see the endpoint-patterns you can checkout the files in the project `urls.py`, the ones I'd like to demo for you are in the `core` folder (each endpoint in this folder or django "app" are accessible at /api/rest-of-the-pattern/).

I've pre-filled the database with a bunch of ingredients, a recipe, and a user (so that you can make a recipe for yourself).

#### Caveats
As this was a real project, there is some user/accounts code that made use of JWT in order to be able to talk to a custom frontend app. This functionality doesn't play well with the basic DjangoRestFramework UI so I've stripped the accounts api down a bit in order for the app to still build and test properly (aka don't visit those endpoints).

## Checking it out

``` shell
git clone git@github.com:shaneikennedy/pantry.git && cd pantry && git checkout lendo
```

The only dependencies here are docker, docker-compose and an internet connection

### Running tests
`make test`

### Checking out the API ui
`make see`

### Tearing it all down
`make clean`
