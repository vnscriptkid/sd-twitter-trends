up:
	docker compose up -d

down:
	docker compose down --remove-orphans --volumes

psql:
	docker compose exec pg psql -U postgres -d postgres