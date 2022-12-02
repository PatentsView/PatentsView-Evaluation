[![Python package](https://github.com/PatentsView/PatentsView-Evaluation/actions/workflows/python-package.yml/badge.svg)](https://github.com/PatentsView/PatentsView-Evaluation/actions/workflows/python-package.yml)
[![pages-build-deployment](https://github.com/PatentsView/PatentsView-Evaluation/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/PatentsView/PatentsView-Evaluation/actions/workflows/pages/pages-build-deployment)

## 📊 PatentsView-Evaluation: Benchmark Disambiguation Algorithms

**pv_evaluation** is a Python package built to help advance research on **author/inventor name disambiguation** systems such as [PatentsView](https://patentsview.org/). It provides:

1. A large set of benchmark datasets for U.S. patents inventor name disambiguation.
2. Disambiguation summary statistics, evaluation methodology, and performance estimators through the [ER-Evaluation Python package](https://github.com/olivierBinette/er-evaluation). 

See the **[project website](https://patentsview.github.io/PatentsView-Evaluation/build/html/index.html)** for full documentation. The [Examples](https://patentsview.github.io/PatentsView-Evaluation/build/html/examples.html) page provides real-world examples of the use of **pv_evaluation** submodules.

### Submodules

**pv_evaluation** has the following submodules:

- [**benchmark.data**](https://patentsview.github.io/PatentsView-Evaluation/build/html/pv_evaluation.benchmark.html): Access to evaluation datasets and standardized comparison benchmarks. The following benchmark datasets are available:
    - Academic Life Sciences (ALS) inventors benchmark.
    - Israeli inventors benchmark.
    - Engineering and Sciences (ENS) inventors benchmark.
    - Lai's 2011 inventors benchmark.
    - PatentsView's 2021 inventors benchmark.
    - Binette et al.'s 2022 inventors benchmark.
- [**benchmark.report**](https://patentsview.github.io/PatentsView-Evaluation/build/html/pv_evaluation.benchmark.html): Visualization of key monitoring and performance metrics.
- [**templates**](https://patentsview.github.io/PatentsView-Evaluation/build/html/pv_evaluation.templates.html): Templated performance summary reports.

## Installation

Install the released version of **pv_evaluation** using
```shell
pip install pv-evaluation
```

Rendering reports requires the installation of quarto from [quarto.org](https://quarto.org/docs/get-started/).

## Examples

Note: Working with the full patent data requires large amounts of memory (we suggest having 64GB RAM available).

See the examples page for complete reproducible examples. The examples below only provide a quick overview of **pv_evaluation**'s functionality.

### Metrics and Summary Statistics

Generate an html report summarizing properties of the current disambiguation algorithm (see [this example](https://patentsview.github.io/PatentsView-Evaluation/build/html/examples/templates/templates.html)):
```python
from pv_evaluation.templates import render_inventor_disambiguation_report

render_inventor_disambiguation_report(
    ".", 
    disambiguation_files=["disambiguation_20211230.tsv", "disambiguation_20220630.tsv"],
    inventor_not_disambiguated_file="g_inventor_not_disambiguated.tsv"
)
```

### Benchmark Datasets

Access PatentsView-Evaluation's large collection of benchmark datasets:
```python
from pv_evaluation.benchmark import *

load_lai_2011_inventors_benchmark()
load_israeli_inventors_benchmark()
load_patentsview_inventors_benchmark()
load_als_inventors_benchmark()
load_ens_inventors_benchmark()
load_binette_2022_inventors_benchmark()
load_air_umass_assignees_benchmark()
load_nber_subset_assignees_benchmark()
```

### Representative Performance Evaluation

See [this example](https://patentsview.github.io/PatentsView-Evaluation/build/html/examples/estimators/binette-2022-benchmark.html) of how representative performance estimates are obtained from Binette's 2022 benchmark dataset.


## Contributing

### Contribute code and documentation

Look through the [GitHub issues](https://github.com/PatentsView/PatentsView-Evaluation/issues) for bugs and feature requests. To contribute to this package:

1. Fork this repository
2. Make your changes and update CHANGELOG.md
3. Submit a pull request
4. For maintainers: if needed, update the "release" branch and create a release.

A conda environment is provided for development convenience. To create or update this environment, make sure you have conda installed and then run `make env`. You can then activate the development environment using `conda activate pv-evaluation`.

The makefile provides other development utilities such as `make black` to format Python files, `make data` to re-generate benchmark datasets from raw data located on AWS S3, and `make docs` to generate the documentation website.

#### Raw data

Raw public data is located on PatentsView's AWS S3 server at [https://s3.amazonaws.com/data.patentsview.org/PatentsView-Evaluation/data-raw.zip](https://s3.amazonaws.com/data.patentsview.org/PatentsView-Evaluation/data-raw.zip). This zip file should be updated as needed to reflect datasets provided by this package and to ensure that original data sources are preserved without modification.

#### Testing

The minimal testing requirement for this package is a check that all code executes without error. We recommend placing execution checks in a runnable notebook and using the [testbook](https://pypi.org/project/testbook/) package for execution within unit tests. User examples should also be provided to exemplify usage on real data.

### Report bugs and submit feedback

Report bugs and submit feedback at https://github.com/PatentsView/PatentsView-Evaluation/issues.

### Contributors

- Olivier Binette (American Institutes for Research, Duke University)
- Sarvo Madhavan (American Institutes for Research)
- Siddharth Engineer (American Institutes for Research)

## References

### Citation

- [Binette, Olivier, Sokhna A York, Emma Hickerson, Youngsoo Baek, Sarvo Madhavan, Christina Jones. (2022). Estimating the Performance of Entity Resolution Algorithms: Lessons Learned Through PatentsView.org. arXiv e-prints: arxiv:2210.01230](https://arxiv.org/abs/2210.01230)

### Datasets

- Trajtenberg, M., & Shiff, G. (2008). Identification and mobility of Israeli patenting inventors. Pinhas Sapir Center for Development. [[link]](https://econ.tau.ac.il/sites/economy.tau.ac.il/files/media_server/Economics/Sapir/papers/%D7%9E%D7%A0%D7%95%D7%90%D7%9C%20%D7%98%D7%A8%D7%9B%D7%98%D7%A0%D7%91%D7%A8%D7%92%205-08%20%D7%9E%D7%A9%D7%95%D7%9C%D7%91.pdf)
- Morrison, G. (2017). Harvard Inventors Benchmark(Version1). figshare. [[link]](https://doi.org/10.6084/m9.figshare.3502754.v1)
- Monath, N., Madhavan, S. & Jones, C. (2021) PatentsView: Disambiguating Inventors, Assignees, and Locations. Technical report. [[link]](https://s3.amazonaws.com/data.patentsview.org/documents/PatentsView_Disambiguation_Methods_Documentation.pdf)