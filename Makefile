start-server:
	PYTHONPATH=. flask --app ./server/rules run

requirements:
	pip install -r requirements.txt
