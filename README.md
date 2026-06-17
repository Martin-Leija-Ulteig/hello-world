# Hello World

A small Python test project that demonstrates a simple function with an automated test.

## What it does

The project provides a `greet` function in [src/hello.py](src/hello.py) that returns a friendly greeting for a given name. The behavior is verified by tests in [tests/test_hello.py](tests/test_hello.py) using `pytest`.

## Project structure

```
.
├── README.md
├── requirements.txt
├── src/
│   └── hello.py
└── tests/
    └── test_hello.py
```

## Setup

Create a virtual environment and install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Running the script

```powershell
python src/hello.py
```

## Running the tests

```powershell
pytest
```