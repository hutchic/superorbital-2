# Variables
DOCKER_IMAGE_NAME=drone-cli
DOCKER_CONTAINER_NAME=drone-cli

.PHONY: all clean build run dev

# Build Docker image
build:
	@echo "Building the Docker image"
	docker build -t $(DOCKER_IMAGE_NAME) .

# Run Docker container
run: build
	@echo "Running the Drone CLI"
	docker run -d -p 8000:8000 --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME)

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
