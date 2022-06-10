## Run simulation
##
## Usage:
## 		make <target> [<arg>=<value> ...]
##
## Targets:
## 		help:		Show this help message.
ENV?=pv-evaluation

DATA_RAW_S3_URL=https://s3.amazonaws.com/data.patentsview.org/PatentsView-Evaluation/data-raw.zip

.PHONY: help env black data clean

help: makefile
	@sed -n "s/^##//p" $<

.PHONY: all get_disambiguation predicted_clusters sim_records_precision sim_precision_figure sim_records_recall
all: get_disambiguation predicted_clusters sim_records_precision sim_precision_figure sim_records_recall

get_disambiguation: src/1-get-disambiguation.py
	conda run -n $(ENV) $<

predicted_clusters: src/2-make-predicted-clusters.py
	conda run -n $(ENV) $<

sim_records_precision: src/3-make-sim-records-precision.py
	conda run -n $(ENV) $<

sim_precision_figure: src/4-make-sim-precision-figure.ipynb
	conda run -n $(ENV) jupyter run $< 

sim_records_recall: src/5-make-sim-records-recall.py
	conda run -n $(ENV) $<
