export PYTHONUTF8=1

run:
	uv run manage.py runserver

lint:
	uv run pre-commit run --all-files

makemigrations:
	uv run manage.py makemigrations

migrate:
	uv run manage.py migrate

createsuperuser:
	uv run manage.py createsuperuser

deletepost:
	uv run manage.py delete_post

updatepost:
	uv run manage.py update_post

printpublishedposts:
	uv run manage.py print_published_posts

createpost:
	uv run manage.py create_post
