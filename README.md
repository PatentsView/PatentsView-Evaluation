[![Python package](https://github.com/PatentsView/PatentsView-Evaluation/actions/workflows/python-package.yml/badge.svg)](https://github.com/PatentsView/PatentsView-Evaluation/actions/workflows/python-package.yml)

## PatentsView-Evaluation: Benchmark Disambiguation Algorithms

**pv_evaluation** is a Python package for the evaluation and benchmarking of PatentsView disambiguation algorithms. It has the following submodules:

- **summary**: Disambiguation summary statistics.
- **metrics**: Implementation of performance evaluation metrics such as precision and recall.
- **benchmark**: Access to evaluation datasets and standardized comparison benchmarks. 
- **data**: Processed data used in this package. Use `make data` to re-generate processed data from original datasets.
- **templates**: Quarto report templates.
- **estimators**: performance metric *estimators* to estimate full-data performance from biased samples.

The `examples` page provides real-world examples of the use of **pv_evaluation** submodules.

## Installation

Install **pv_evaluation** in editable mode using
```shell
git clone https://github.com/PatentsView/PatentsView-Evaluation.git
cd PatentsView-Evaluation
pip install -e .
```

Rendering reports requires the installation of quarto from [quarto.org](https://quarto.org/docs/get-started/).

## Examples

Note: Working with the full patent data requires large amounts of memory (we suggest having 64GB RAM available).

See the examples page for complete reproducible examples. The examples below only provide a quick overview of **pv_evaluation**'s functionality.

### Metrics and Summary Statistics

Generate an html report summarizing properties of the current disambiguation algorithm (uses the `rawinventor.tsv` data file from PatentsView's [downloads page](https://patentsview.org/download/data-download-tables)):
```python
from pv_evaluation.templates import render_inventor_disambiguation_report

render_inventor_disambiguation_report(".", summary_table_files=["rawinventor.tsv"])
```

### Estimate Precision and Recall

Estimate precision and recall from clusters sampled with probability proportional to their size:
```python
from pv_evaluation.estimators import pairwise_precision_estimator
from pv_evaluation.benchmark import load_lai_2011_inventors_benchmark

current_disambiguation = # TODO: Make this the current disambiguation membership vector
pairwise_precision_estimator(current_disambiguation, load_lai_2011_inventors_benchmark(), sampling_type="cluster_block", weights="cluster_size")
pairwise_recall_estimator(current_disambiguation, load_lai_2011_inventors_benchmark(), sampling_type="cluster_block", weights="cluster_size")
```

### Access Benchmark Datasets

Access PatentsView-Evaluation's collection of benchmark datasets:
```python
from pv_evaluation.benchmark import load_lai_2011_inventors_benchmark, load_israeli_inventors_benchmark, load_patentsview_inventors_benchmark

load_lai_2011_inventors_benchmark()
load_israeli_inventors_benchmark()
load_patentsview_inventors_benchmark()
```

## Contributing

### Contribute code and documentation

Look through the [GitHub issues](https://github.com/PatentsView/PatentsView-Evaluation/issues) for bugs and feature requests. To contribute to this package:

1. Fork this repository
2. Make your changes and update CHANGELOG.md
3. Submit a pull request

A conda environment is provided for development convenience. To create or update this environment, make sure you have conda installed and then run `make env`. You can then activate the development environment using `conda activate pv-evaluation`.

The makefile provides other development utilities such as `make black` to format Python files and `make data` to re-generate benchmark datasets from raw data located on AWS S3.

### Report bugs and submit feedback

Report bugs and submit feedback at https://github.com/PatentsView/PatentsView-Evaluation/issues.

## References

### Methodology

- Menestrina, D., Whang, S. E., & Garciamolina, H. (2010). Evaluating entity resolution results. Proceedings of the VLDB Endowment, 3(1), 208–219. https://doi.org/10.14778/1920841.1920871
- Michelson, M., & Macskassy, S. A. (2009). Record linkage measures in an entity centric world. Proceedings of the 4th Workshop on Evaluation Methods for Machine Learning.
- Ferreira, A. A., Gonçalves, M. A., & Laender, A. H. (2012). A brief survey of automatic methods for author name disambiguation. Acm Sigmod Record, 41(2), 15-26. [[link]](https://s3.amazonaws.com/data.patentsview.org/USPTO_Entity_Resolution_Symposium/Ferreira+et+al_2012_A+Brief+Survey+of+Automatic+Methods+for+Author+Name+Disambiguation.pdf)
- Pfitzner, D., Leibbrandt, R., & Powers, D. (2009). Characterization and evaluation of similarity measures for pairs of clusterings. Knowledge and Information Systems, 19(3), 361-394. [[link]](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.214.7233&rep=rep1&type=pdf)
- Barnes, M. (2015). A Practioner’s Guide to Evaluating Entity Resolution Results. 1–6. http://arxiv.org/abs/1509.04238
- Marchant, N. G., & Rubinstein, B. I. P. (2017). In search of an entity resolution OASIS: Optimal asymptotic sequential importance sampling. Proceedings of the VLDB Endowment, 10(11), 1322–1333. https://doi.org/10.14778/3137628.3137642

### Datasets

- Trajtenberg, M., Shiff, G., & Melamed, R. (2006). The" names game": Harnessing inventors' patent data for economic research. [link]
- Trajtenberg, M., & Shiff, G. (2008). Identification and mobility of Israeli patenting inventors. Pinhas Sapir Center for Development. [link]
- Morrison, G. (2017). Harvard Inventors Benchmark(Version1). figshare. https://doi.org/10.6084/m9.figshare.3502754.v1 
