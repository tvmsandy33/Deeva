from setuptools import setup, find_packages

setup(
    name="your_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "datasets",
        "torch",
        "transformers",
        "spacy"
    ],
    entry_points={
        'console_scripts': [
            'your_package=your_package:main',
        ],
    },
)
