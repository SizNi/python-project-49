install: # install poetry
	poetry install

brain-games: # start brain-games
	poetry run brain-games

build:
	poetry build

publish: # непонятно что это (посмотреть)
	poetry publish --dry-run

package-install: # установка пакета *.whl
	python3 -m pip install --user dist/*.whl