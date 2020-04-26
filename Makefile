keep_building:
	fd .rst | entr -c ablog build

run:
	ablog serve

deploy:
	cd deployment; bash deploy.sh
