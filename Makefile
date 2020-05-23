ui:
		cd ui && npm run serve

backend:
		python manage.py runserver

test:
		python manage.py test

lint:
		scripts/linting.sh

install:
		python -m pip install -r requirements.txt

install-ui:
		cd ui && npm i
