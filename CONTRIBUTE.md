# Contributing to the project

This project is still under construction. We welcome any contributions. Please **carefully** read the following instructions before contributing.

## Code style

We use `isort` with `black` to enforce a consistent code style.
```shell
pip install isort==5.12.0 black==23.9.0
```

Configs can be found in `pyproject.toml`.

CI also checks code style before pushing to `main` branch. Try to run `isort` and `black` locally before pushing to avoid unnecessary CI failures:
```shell
isort .
black .
```

### Pre-commit hook

To automatically run `isort` and `black` before each commit, install `pre-commit`:
```shell
pip install pre-commit
```

Then run `pre-commit install` to install the hook.

## Commit message

Check out [this article](https://www.conventionalcommits.org/en/v1.0.0/) for a detailed explanation of how to write a good commit message.

Commit messages started with `feat` will trigger a major version bump, `fix` will trigger a minor version bump.

Also check out [semantic-release](https://github.com/semantic-release/semantic-release) for details.

## Test

⚠ Under construction. ⚠
