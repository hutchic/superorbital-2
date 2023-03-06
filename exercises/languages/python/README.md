# Usage

## Prerequisites

- docker
- access to the drone backend

## Running

```
./drone_cli <arguments>
```

For example

```
./drone_cli list
./drone_cli create /input/valid.json
```

# Development

If you want to make changes to the code, you can use the following commands:

- make dev: This will start a Docker container with the CLI tool and a Bash shell. You can make changes to the code in your local editor and test them out in the container.
- make test: This will run the unit tests for the CLI tool in a Docker container.


# TODO

- Setup CI / CD
- Remove hardcoded url and secrets from drone_cli.py
- Implement integration tests
- Migrate to docker compose
- I've heard good things about python vcr
