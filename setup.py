#!/usr/bin/env python3
from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

if __name__ == "__main__":
    setup(
        name="pv_evaluation",
        version="2.0.0",
        license_files=("LICENSE.txt",),
        author="Olivier Binette, Sarvo Madhavan",
        author_email="olivier.binette@gmail.com",
        description="Tools to evaluate PatentsView's disambiguation algorithms",
        long_description=long_description,
        long_description_content_type='text/markdown',
        url="https://github.com/OlivierBinette/PatentsView-Evaluation",
        include_package_data=True,
        packages=["pv_evaluation"],
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
            "er-evaluation",
        ],
        scripts=["scripts/hand-disambiguation/process-inventors-hand-disambiguation.py"],
    )
