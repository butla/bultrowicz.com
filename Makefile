keep_building:
	fd .rst | entr -c ablog build

run:
	ablog serve
