dev:
	python manage.py runserver
lint:
	flake8
test:
	python manage.py test

check: test lint