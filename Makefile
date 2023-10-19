include .env
export

flask-debug:
	source $(CONDAROOT)/bin/activate MLOps-app && flask run
