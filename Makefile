install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=greeting --cov=web tests
	python -m pytest --nbval notebook.ipynb
	python -m pytest -v tests/test_web.py

debug:
	python -m pytest -vv --pdb

format: 
	black *.py

lint:
	pylint --disable=R,C *.py

all: install lint test format

