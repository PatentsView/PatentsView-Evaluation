## Process inventors hand-disambiguation data
##
## Usage:
## 		make <target>
##
## Targets:
## 		help:		Show this help message.
##		debug:		Create debugging spreadsheet for inventors hand-disambiguation
##		all:		Create benchmark csv files for inventors hand-disambiguation
RAWINVENTOR_S3_URL=https://s3.amazonaws.com/data.patentsview.org/download/rawinventor.tsv.zip
INPUT = $(wildcard input/*.xlsx)

.PHONY: help env all debug

debug: $(patsubst input/%.xlsx,output/%-true-clusters.csv.debug.xlsx,$(INPUT))
	echo

all: $(patsubst input/%.xlsx,output/%-true-clusters.csv,$(INPUT))

help: makefile
	@sed -n "s/^##//p" $<

rawinventor.tsv.zip:
	wget -nc ${RAWINVENTOR_S3_URL}

rawinventor.tsv: rawinventor.tsv.zip
	unzip -o rawinventor.tsv.zip

output/%-true-clusters.csv.debug.xlsx: input/%.xlsx rawinventor.tsv
	mkdir -p $(@D)
	process-inventors-hand-disambiguation.py --debug $< rawinventor.tsv -o $@

output/%-true-clusters.csv: input/%.xlsx rawinventor.tsv
	mkdir -p $(@D)
	process-inventors-hand-disambiguation.py $< rawinventor.tsv -o $@
