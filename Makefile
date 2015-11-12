runserver:
	../venv/bin/python manage.py runserver 0.0.0.0:8050

pep8:
	../venv/bin/pep8 --exclude=*migrations*,*settings_local.py* --max-line-length=119 --show-source  helena/

pyflakes:
	../venv/bin/pylama --skip=*migrations* -l pyflakes helena/

lint:
	make pep8
	make pyflakes

test:
	../venv/bin/python manage.py test helena -v 2

recompress:
	../venv/bin/python manage.py collectstatic --noinput
	../venv/bin/python manage.py compress --force

ci_test:
	python manage.py test helena -v 2
	pep8 --exclude=*migrations*,*settings_local.py* --max-line-length=119 --show-source  helena/
	pylama --skip=*migrations* -l pyflakes helena/
