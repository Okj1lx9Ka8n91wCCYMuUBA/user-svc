re:
	docker compose down --remove-orphans && docker compose up -d

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

build:
	docker compose build

stop:
	docker compose stop

start:
	docker compose start

restart:
	docker compose restart


migrate:
	docker compose exec web alembic upgrade head

makemigrations:
	docker compose exec -it web alembic revision --autogenerate -m "message"

downgrade:
	docker compose exec -it web alembic downgrade $(revision)
