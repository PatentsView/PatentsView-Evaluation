# Changelog

## 2.0.3 (January 11, 2023)

- FIX: Unavailable function in __all__.

## 2.0.2 (December 12, 2022)

- Add inventor_summary_trend_plot() and inventor_estimates_trend_plot() functions.

## 2.0.1 (December 5, 2022)

- Update setup.py with find_packages()


## 2.0.0 (December 2, 2022)

- BREAKING: Major refactoring of the package. Core evaluation functionality has been moved to the er-evaluation package.

## 1.0.1 (November 14, 2022)

- FIX: Replace sklearn dependency with scikit-learn. Add scipy dependency.

## 1.0.0 (November 4, 2022)

- Added assignee benchmark datasets
- Added patents links and preview tooltips to automated reports.
- Added estimates table and plots.
- FIX: Install from Github now includes necessary csv files.
- Added script for processing hand-disambiguated inventor benchmark.
- Removed Harvard inventors benchmark (low data quality).
- BREAKING: change "mention-id" to "mention_id" and "unique-id" to "unique_id" in datasets.
- Added inventor names to raw csv benchmarkd datasets (useful for validation and debugging).
- Added cluster precision and cluster recall estimators (for cluster block sampling).
- Added additional inventor benchmark datasets.
- Added license file (GPL3)

## 0.0.1 (June 27, 2022)

- Initial release