# README

This README contains the necessary steps to get the application up and running.

## What is this repository for?

- Quick summary

This repo is the solution for the task provided by C1.\
I used fastapi as python framework to do the task.\
Python version to implement the solution is Python 3.7

## Running the application

- Create a python virtualenv and activate it:

  ```
  python3 -m venv venv
  . venv/bin/activate
  ```

- Install python dependencies:

  ```
  pip install -v -r requirements.txt
  ```

- Run using python

  ```
  python application.py
  ```

- Open a browser and do GET request:

  http://localhost:9876/navigator?search_term=arrow

  You can run the code also using docker image

- build the image:

  ```
  docker build -t c1-solution-image .
  ```

- Run the container:

  ```
  docker run -p 9876:9876 c1-solution-image
  ```

- Open a browser and do GET request:

  http://localhost:9876/navigator?search_term=arrow
