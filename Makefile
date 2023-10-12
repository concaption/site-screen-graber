setup:
	chmod +x ./setup.sh &&\
		./setup.sh

URL ?= "https://www.buildberg.co"

capture:
	python site_screen_graber.py $(URL)
