# Variables
DOCKER_IMAGE_NAME=drone-cli
DOCKER_CONTAINER_NAME=drone-cli
PYTEST_COMMAND=pytest

.PHONY: all clean build run dev

# Build Docker image
build:
	@echo "Building the Docker image"
	docker build -t $(DOCKER_IMAGE_NAME) .

# Run Docker container
run:
	@echo "Running the Drone CLI"
	docker run -d -v $(PWD)/input:/input --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME) $(ARGS)

# Stop Docker container
stop:
	docker stop $(DOCKER_CONTAINER_NAME)

# Remove Docker container
rm: stop
	docker rm $(DOCKER_CONTAINER_NAME)

# Clean up Docker image
clean: rm
	docker image rm $(DOCKER_IMAGE_NAME)

dev: build
	@echo "Running the Drone CLI in dev mode"
	docker run --network host --rm -it -v $(PWD):/app --entrypoint /bin/bash $(DOCKER_IMAGE_NAME)

test: build
	@echo "Running the tests"
	docker run --rm -t $(DOCKER_IMAGE_NAME) sh -c "$(PYTEST_COMMAND)"

# Run linters
lint:
	flake8 .

# Remove Python bytecode files and cache directories
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
