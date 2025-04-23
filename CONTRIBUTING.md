# Contributing to Kollie
Kollie project embraces the Open Source approach so we welcome your contributions in all shapes and forms! 

Ways in which you can contribute includes:

- Reporting a bug
- Discussing the current state of the code or architecture
- Submitting a fix
- Proposing new features
- Developing new features
- Reviewing PRs

Please read the rest of this document to familiarise yourself with what is expected when you contribute.

## We Develop with Github
We use github to host code, to track issues and feature requests. Code changes are delievered via pull requests.

## We Use [Github Flow](https://docs.github.com/en/get-started/quickstart/github-flow), So All Code Changes Happen Through Pull Requests
Pull requests are the best way to propose changes to the codebase (we use [Github Flow](https://docs.github.com/en/get-started/quickstart/github-flow)). We actively welcome your pull requests:

1. Clone this repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Open a pull request!

## Report bugs using Github's [issues](https://github.com/kollie-org/kollie/issues)
We use GitHub issues to track bugs. Report a bug by [opening a new issue](https://github.com/kollie-org/kollie/issues/new); it's that easy!

## Write bug reports with detail, background, and sample code
Please include as much information as you can when opening an issue so that developers have enough context to investigate and work on it immediately. The more detailed the issue, the higher the chance of it will be picked up!

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can.
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## Coding Style and linting
- We use [Black formatter](https://github.com/psf/black). Please make sure your code is formatted using Black or else the CI steps will fail.
- We check for PEP8 and Pyflakes using [Ruff linter](https://github.com/astral-sh/ruff)

## Setting up local environment

The included docker + docker-compose setup makes it quick and easy to get started with Kollie. Follow the instructions below:

To get started with Kollie, you'll need to set up a local development environment.

### Cloning the project

The first step is to clone the Kollie project from GitHub. You can do this by running the following command:

```
git clone git@github.com:kollie-org/kollie.git
```

### Building the project

Once you have cloned the project, you can build it using the `make build` command. This will build the Docker image for the Kollie application.

If it's your first time building the project, you will need to run `make setup-secrets` before running the application. This attempts to populate a `current_user.env` file for auth purposes when working in your local env. If your local git config uses something other than your email address you will need to correct the value stored against the `X_AUTH_REQUEST_EMAIL` key.

### Running the application

To run the Kollie application, you can use the `make run` command. This will start the Kollie application in a Docker container.

### Testing the application

To test the Kollie application, you can use the `make test` command. This will run the unit tests for the Kollie application.
