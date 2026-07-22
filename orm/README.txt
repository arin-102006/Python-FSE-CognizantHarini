Hands-On 7

Commands used:

alembic init migrations
alembic revision --autogenerate -m "initial schema"
alembic upgrade head
alembic current
alembic history --verbose
alembic downgrade -1
alembic downgrade base
alembic upgrade head