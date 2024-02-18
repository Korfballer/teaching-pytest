# Teaching PyTest

This repository creates an example python package called `superhelpful` and demonstrates how to write basic tests for it.

This repository has been built on a Windows Operating System and has not been tested on Linux.

## 1. Content

The content of this repo aims to demonstrate:
* Plain asserts (`assert actual == expected`)
* Third party asserts (`np.testing.assert_allclose`, `pd.testing.assert_frame_equal`)
* Checking for correctly raised errors (`pytest.raises`)
* Structuring tests
* Fixtures (`@pytest.fixture`) and their scope (`@pytest.fixture(scope="session")`)
* Paramaterization (`@pytest.mark.parametrize`)
* Skip logic (`@pytest.skip`, `@pytest.skipif`)
* Configuring tests via the `conftest.py`
* Mocking (`fastapi.testclient.TestClient`)
* Register markers in a `pytest.ini`

## 2. Setup

### 2.1 Virtual Environment

When you first use the repository, create the virtual environment.
```
python -m venv ./venv
```

Activate the python environment
```shell
# Windows
./venv/Scripts/activate
```

```bash
# Linux
source ./venv/bin/activate
```

Install dependencies via the `superhelpful` package in "dev" mode.
```
# Install package
pip install .[dev]
```

### 2.2. Generate requirement files

As per: https://stackoverflow.com/questions/62885911/pip-freeze-creates-some-weird-path-instead-of-the-package-version
i.e. we don't want personal filepaths for the locally built package `superhelpful`
therefore we **do not** use `pip freeze > requirements-dev.txt`

To generate the requirements-dev.txt, from the dev install:
```
pip list --local --format=freeze > requirements-dev.txt
```

### 2.3 Pre-commit

Ensure pre-commit is installed
```
pre-commit install
```

## 3 Teardown

### 3.1 Virtual Environment

Deactivate the python environment
```
deactivate
```

Delete the python environment
```shell
# Windows
rm venv
```

```bash
# Linux
rm -rf venv
```

## 4 FAQ

### 4.1 Configuration

On Windows, how do I fix the following error?
`./venv/Scripts/activate : File .\venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system.`

See corresponding [StackOverflow post](https://stackoverflow.com/questions/56199111/visual-studio-code-cmd-error-cannot-be-loaded-because-running-scripts-is-disabl)

In Visual Studio Code:
* Open the repository as a folder
* Hit F1
* Navigate to: `Preferences: Open User Settings (JSON)`
* Ensure that there are no entries for `terminal.integrated.profiles.windows`: delete any that exist.
* Navigate to: `Preferences: Open Workspace Settings (JSON)`
* Add an arbitrary space and then re-save the file
* Reload Visual Studio Code
* "Kill" the old terminal (the bin icon in the top-right of the terminal panel)
* Start a new terminal (Terminal > New Terminal)
* Test this has worked by activating the virtual environment (see instructions above)

### 4.2 Testing

My Testing panel reads: "Pytest Discovery Error"

This has probably happened because either:
1. You are using the wrong virtual environment. See section on activating the virtual environment.
2. You haven't installed the dependencies by running `pip install .[dev]`. See section on installing dependencies.

### 4.3 Linting

Pre-commit doesn't seem to be checking the code.

This happens when you haven't run `pre-commit install`. See section on pre-commit.
