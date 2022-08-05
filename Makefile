#!make

MANAGE = python
MIGRATE = aerich


# ##########################################################################
# common commands

run:
	$(MANAGE) main.py

# ##########################################################################
# management

init_migrate:
	$(MIGRATE) init -t main.TORTOISE_ORM

create_db:
	$(MIGRATE) init-db

migrations:
	$(MIGRATE) migrate

migrate:
	$(MIGRATE) upgrade




