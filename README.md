# README

This README would normally document whatever steps are necessary to get your application up and running.

## What is this repository for?

- Quick summary
- Version
- [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

## Prepare Development Environment

- Configuration

  Create a python virtualenv and activate it:
  ```
  python3 -m venv venv
  . venv/bin/activate
  ```

  Install python dependencies:

  ```
  pip install -v -r requirements.txt 
  ```
  Run using python
  ```
  python application.py
  ```

  Running using docker:

  ```
  docker build -t c1-solution-image .
  docker run -p 80:80 c1-solution-image
  ```

