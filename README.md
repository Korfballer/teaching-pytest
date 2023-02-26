# Teaching PyTest

This repository creates an example python package called `superhelpful` and demonstrates how to write basic tests for it.

This repository has been built on the Windows Operating System and has not been tested on a Linux.

## 1. Setup

### 1.1 Virtual Environment

#### 1.1.1 Create Virtual Environment

When you first use the repository, create the virtual environment.
```
python -m venv ./venv
```

#### 1.1.2 Activate Virtual Environment

Activate the python environment
```shell
# Windows
./venv/Scripts/activate
```

```bash
# Linux
source ./venv/bin/activate
```

Install the package (`superhelpful`) in "dev" mode.
```
# Install package
pip install .[dev]
```

#### 1.1.3 Generate requirement files

As per: https://stackoverflow.com/questions/62885911/pip-freeze-creates-some-weird-path-instead-of-the-package-version
i.e. we don't want personal filepaths for the locally built package `superhelpful`
therefore we **do not** use `pip freeze > requirements-dev.txt`

To generate the requirements-dev.txt, from the dev install:
```
pip list --local --format=freeze > requirements-dev.txt
```

### 1.2 Pre-commit

Ensure pre-commit is installed
```
pre-commit install
```

## 2 Teardown

### 2.1 Virtual Environment

#### 2.1.1 Deactivate Virtual Environment

Deactivate the python environment
```
deactivate
```

#### 2.1.2 Delete Virtual Environment

Delete the python environment
```shell
# Windows
rm venv
```

```bash
# Linux
rm -rf venv
```
