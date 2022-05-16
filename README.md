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
