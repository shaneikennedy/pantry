frontend:
		cd ui && npm run serve

run-backend:
		python manage.py runserver

test:
		python manage.py test

lint:
		scripts/linting.sh

install:
		python -m pip install -r requirements.txt

install-fe:
		cd ui && npm i && cd ..

bootstrap:
		python manage.py bootstrap
