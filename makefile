build:
	docker-compose -f local.yml build --no-cache

run:
	docker-compose -f local.yml up

mm:
	docker-compose -f local.yml run web python manage.py makemigrations

m:
	docker-compose -f local.yml run web python manage.py migrate

su:
	docker-compose -f local.yml run web python manage.py createsuperuser

pi:
	docker-compose -f local.yml run web python manage.py populate_inventory

ri:
	docker-compose -f local.yml run web python manage.py reset_inventory

t:
	docker-compose -f local.yml exec web pytest
