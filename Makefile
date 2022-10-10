install: # install poetry
	poetry install

brain-games: # start brain-games
	poetry run brain-games

build: # сборка программы, запускать после внесения изменений и перед запуском самой программы
	poetry build

publish: # непонятно что это (посмотреть)
	poetry publish --dry-run

package-install: # установка пакета *.whl (тоже надо запускать после build)
	python3 -m pip install --user dist/*.whl