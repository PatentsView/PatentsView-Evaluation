[![Python package](https://github.com/PatentsView/PatentsView-Evaluation/actions/workflows/python-package.yml/badge.svg)](https://github.com/PatentsView/PatentsView-Evaluation/actions/workflows/python-package.yml)

# PatentsView-Evaluation

**pv_evaluation** is a Python package for the evaluation and benchmarking of PatentsView disambiguation algorithms.

Currently, **pv_evaluation** has the following two submodules:
- **summary**: provides disambiguation summary statistics.
- **metrics**: provides implementations of performance metrics (pairwise metrics and cluster metrics).

The following submodules are planned:
- **data**: access to benchmark and evaluation datasets.
- **benchmarks**: standardized comparison benchmarks.
- **estimators**: performance metric *estimators* to estimate full-data performance from biased samples.
- **tests**: unit testing with pytest.

The `examples` folder provides real-world examples of the use of **pv_evaluation** submodules.


## References

- Ferreira, A. A., Gonçalves, M. A., & Laender, A. H. (2012). A brief survey of automatic methods for author name disambiguation. Acm Sigmod Record, 41(2), 15-26. [[link]](https://s3.amazonaws.com/data.patentsview.org/USPTO_Entity_Resolution_Symposium/Ferreira+et+al_2012_A+Brief+Survey+of+Automatic+Methods+for+Author+Name+Disambiguation.pdf)
- Pfitzner, D., Leibbrandt, R., & Powers, D. (2009). Characterization and evaluation of similarity measures for pairs of clusterings. Knowledge and Information Systems, 19(3), 361-394. [[link]](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.214.7233&rep=rep1&type=pdf)
