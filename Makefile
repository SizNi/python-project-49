install: # install poetry
	poetry install

brain-games: # start brain-games
	poetry run brain-games

brain-even: # start brain-even
	poetry run brain-even

build: # сборка программы, запускать после внесения изменений и перед запуском самой программы
	poetry build

publish: # непонятно что это (посмотреть)
	poetry publish --dry-run

package-install: # установка пакета *.whl (тоже надо запускать после build)
	python3 -m pip install --user dist/*.whl

lint: # запуск flake8 на проект brain_games
	poetry run flake8 brain_games