# README

This README would normally document whatever steps are necessary to get your application up and running.

## What is this repository for?

- Quick summary
- Version
- [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

## Prepare Development Environment

- Configuration

  Ensure that [AWS CLI](https://aws.amazon.com/cli/) is installed and configured with appropriate AWS credentials with run `aws configure`..

  Create a python virtualenv and activate it:

  ```
  python3 -m venv venv
  . venv/bin/activate
  ```

  Install python dependencies:

  ```
  pip install -v -r requirements.txt 
  ```

  Run the setup file:

  ```
  python setup.py develop
  ```

- VSCode Configuration

  The content of [.vscode/launch.json]() file is:

  ```
  {
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: FastAPI",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": ["app.main:app", "--reload", "--port", "8000"],
      "justMyCode": false,
      "serverReadyAction": {
        "pattern": "http:\\/\\/\\S+:([0-9]+)",
        "uriFormat": "http://localhost:%s/docs",
        "action": "openExternally"
      }
    }
  ]
  }

  ```

- Dependencies
- Database configuration
- How to run tests
- Deployment instructions

## Contribution guidelines

- Writing tests
- Code review
- Other guidelines

## Who do I talk to?

- Repo owner or admin
- Other community or team contact
