# Узнать версию питона:
python3 --version

# Создать окружение venv_av:
python3 -m venv venv_av 

# Активировать окружение venv_av:
source venv_av/bin/activate 

# Показать все библиотеки в окружении venv_av:
pip list

# Инициалиазция poetry в проекте (в папке)
poetry init


poetry add fastapi
poetry add alembic
poetry run alembic init migrations
poetry add ruff
poetry add mypy
poetry add dynaconf


git init                # инициализация репозитория
git remote add origin [url]  # добавление удаленного репозитория


git push -u origin main
git push
git push origin +master

git remote -v # просмотр удаленных репозиториев

git branch -m новое_имя_ветки # переименование ветки


