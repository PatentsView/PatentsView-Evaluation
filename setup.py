#!/usr/bin/env python3
from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="pv_evaluation",
        version="1.0.1",
        license_files = ('LICENSE.txt',),
        author="Olivier Binette, Sarvo Madhavan",
        author_email="olivier.binette@gmail.com",
        description="Tools to evaluate disambiguation algorithms",
        url="https://github.com/OlivierBinette/PatentsView-Evaluation",
        include_package_data=True,
        packages=find_packages(),
        install_requires=[
            "pandas",
            "dask",
            "matplotlib",
            "pyarrow",
            "python-snappy",
            "numpy",
            "plotly",
            "scikit-learn",
            "scipy",
            "quarto",
            "jinja2",
            "kaleido",
            "openpyxl",
        ],
        scripts=["scripts/hand-disambiguation/process-inventors-hand-disambiguation.py"],
    )
