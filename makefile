## Development utilities for c-stringcompare
##
## Usage:
## 		make <target> [<arg>=<value> ...]
##
## Targets:
## 		help:		Show this help message.
##		env: 		Create or update conda environment "pv-evaluation"

.PHONY: help env black

help: makefile
	@sed -n "s/^##//p" $<

env: environment.yml
	@(echo "Creating pv-evaluation environment..."; conda env create -f $<) \
	|| (echo "Updating pv-evaluation environment...\n"; conda env update -f $<)

black:
	black . --line-length=127