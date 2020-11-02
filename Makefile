build:
	docker build -t pantry/pantry .

db:
	docker-compose up --remove-orphans -d db

test: build db
	docker-compose run web python manage.py test

lint:
		scripts/linting.sh

clean:
	docker-compose down

bootstrap:
	docker-compose run web python manage.py bootstrap

migrate:
	docker-compose run web python manage.py migrate

see: db build migrate bootstrap
	docker-compose up -d web
	sleep 5
	open http://localhost:8000/api/ingredients
