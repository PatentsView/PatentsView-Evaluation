[![Python package](https://github.com/PatentsView/PatentsView-Evaluation/actions/workflows/python-package.yml/badge.svg)](https://github.com/PatentsView/PatentsView-Evaluation/actions/workflows/python-package.yml)

# PatentsView-Evaluation

**pv_evaluation** is a Python package for the evaluation and benchmarking of PatentsView disambiguation algorithms.

Currently, **pv_evaluation** has the following submodules:
- **summary**: provides disambiguation summary statistics.
- **metrics**: provides implementations of performance metrics (pairwise metrics and cluster metrics).
- **benchmark**: access to benchmark and evaluation datasets and standardized comparison benchmarks. 
- **data**: Processed data used in this package. Use `make data` to re-generate processed data from original datasets.

The following submodules are planned:
- **estimators**: performance metric *estimators* to estimate full-data performance from biased samples.

The `examples` folder provides real-world examples of the use of **pv_evaluation** submodules.


## References

### Methodology

- Ferreira, A. A., Gonçalves, M. A., & Laender, A. H. (2012). A brief survey of automatic methods for author name disambiguation. Acm Sigmod Record, 41(2), 15-26. [[link]](https://s3.amazonaws.com/data.patentsview.org/USPTO_Entity_Resolution_Symposium/Ferreira+et+al_2012_A+Brief+Survey+of+Automatic+Methods+for+Author+Name+Disambiguation.pdf)
- Pfitzner, D., Leibbrandt, R., & Powers, D. (2009). Characterization and evaluation of similarity measures for pairs of clusterings. Knowledge and Information Systems, 19(3), 361-394. [[link]](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.214.7233&rep=rep1&type=pdf)

### Datasets

- Trajtenberg, M., Shiff, G., & Melamed, R. (2006). The" names game": Harnessing inventors' patent data for economic research. [link]
- Trajtenberg, M., & Shiff, G. (2008). Identification and mobility of Israeli patenting inventors. Pinhas Sapir Center for Development. [link]
- Morrison, G. (2017). Harvard Inventors Benchmark(Version1). figshare. https://doi.org/10.6084/m9.figshare.3502754.v1 
