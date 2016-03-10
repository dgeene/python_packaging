# Python Packaging. From Init to Deploy
An example of how to apckage some python code.

## Terms
Module - Any python code saved in a file.

(Import) Package - Namespace Directory with an __init__.py.

(Distribution) Package - Shareable/Installable. Source formats and built formats.

### Source Distribution - sdist
Can contain some c extensions.

### Built Distribution - bdist_wheel
Dropped in. Don't build an egg. Build a wheel

## Requirements
Some helpful tools to assist building packages.

Install these pip packages
wheel - (should already be installed) Allows wheel format.

twine - allows upload to PyPI in a secure manner

tox- test runner

## Helpful tools
Cookiecutter - Generates a project structure from a template. Pip install cookicutter


## Creating your package

### Run cookiecutter against a template repo
` $ cookiecutter https://github.com/tylerdave/cookiecutter-python-package.git`

You will be prompted to input information about your project.


## Links
Python Packaging Authority. PyPA!
https://python-packaging-user-guide.readthedocs.org/en/latest/

PyPI - Python Packaging Index
