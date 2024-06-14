from setuptools import setup, find_packages

setup(
    name='Deeva',
    version='0.1.0',
    description='Contextual correction of Incorrect words using Distilber-base Backbone',
    author='tvmsandy',
    author_email='tvmsandy33@gmail.com',
    url='https://github.com/tvmsandy33/Deeva',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'datasets',
        'torch',
        'transformers',
        'spacy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
