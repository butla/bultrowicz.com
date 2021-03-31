keep_building:
	fd .rst | entr -c ablog build

run:
	ablog serve

deploy:
	cd deployment; bash deploy.sh

# requirements created with "pip install ablog; pip freeze > requirements.txt"
install_into_venv:
	pip install -r requirements.txt
