#!/usr/bin/env python3
from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="pv_evaluation",
        version="0.0.0",
        author="Olivier Binette",
        author_email="olivier.binette@gmail.com",
        description="Tools to evaluate disambiguation algorithms",
        url="https://github.com/OlivierBinette/PatentsView-Evaluation",
        include_package_data=True,
        packages=find_packages(),
        install_requires=["pandas", "dask", "matplotlib", "fastparquet", "numpy", "plotly"],
        extra_require={"test":["sklearn", "jupyter", "pytest", "testbook", "ipykernel"]}
    )
