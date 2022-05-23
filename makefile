## Development utilities for pv_evaluation
##
## Usage:
## 		make <target> [<arg>=<value> ...]
##
## Targets:
## 		help:		Show this help message.
##		env: 		Create or update conda environment "pv-evaluation"
## 		black:		Format Python files.
##		data:		Make processed data folder.

DATA_RAW_S3_URL=https://s3.amazonaws.com/data.patentsview.org/PatentsView-Evaluation/data-raw.zip

.PHONY: help env black data clean

help: makefile
	@sed -n "s/^##//p" $<

env: environment.yml
	@(echo "Creating pv-evaluation environment..."; conda env create -f $<) \
	|| (echo "Updating pv-evaluation environment...\n"; conda env update -f $<)

black:
	black . --line-length=127

data: \
	pv_evaluation/data/inventor/israeli-inventors-benchmark.csv\
	pv_evaluation/data/inventor/patentsview-inventors-benchmark.csv

data-raw.zip:
	wget $(DATA_RAW_S3_URL)

data-raw/.tag: data-raw.zip
	unzip data-raw.zip
	touch data-raw/.tag

pv_evaluation/data/inventor/%.csv: scripts/%.py data-raw/.tag
	python3 $<

.PHONY: quarto
quarto:
	conda run -v --live-stream -n pv-evaluation quarto render examples/benchmark/full-report.qmd --to html

.PHONY: test
test:
	conda run -v --live-stream -n pv-evaluation quarto render pv_evaluation/templates/test.qmd --to html


clean:
	rm -r data-raw
	rm data-raw.zip
	rm *.egg-info