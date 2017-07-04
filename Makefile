install-dev:
	@pip install -r requirements/development.txt

run:
	@python manage.py runserver

shell:
	@python manage.py shell

deploy-stage:
	@git push stage master
	@heroku run python manage.py migrate --remote stage

deploy-prod:
	@git push prod master
	@heroku run python manage.py migrate --remote prod

deploy-full:
	@git push stage master
	@heroku run python manage.py migrate --remote stage
	@git push prod master
	@heroku run python manage.py migrate --remote prod
	@python manage.py runserver

migrate:
	@python manage.py makemigrations
	@python manage.py migrate

startdev:
	@git remote add stage https://git.heroku.com/jueleo-stage.git
	@git remote add prod https://git.heroku.com/jueleo.git
	@pip install -r requirements/development.txt
	@make migrate