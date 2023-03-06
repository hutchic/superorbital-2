# RentADrone :tm: :copyright: :unicorn: :moneybag:

## Overview

Welcome To RentADrone! We are very happy to have you here.

Your first task will be to build the initial release of a CLI that can interact with our existing **RentADrone** backend server API. This CLI will help our users rent time on our upcoming drones-as-a-service platform. The backend server is provided to you as an OCI-compliant container image that you'll need to run locally. All of its APIs are documented with [Swagger](https://swagger.io/). Please be aware that the provided server may not be extremely reliable yet, as it is in very heavy development.

You can complete this task in your choice of either `Go` or `Python`.  We've provided a starter template in each language to get you going, but feel free to ignore them and start from scratch if you think that will lead to better results.

We've also provided example request and response payloads for the backend API in the `example-requests` and `example-responses` directories.

## Development Setup

Requirements:

Ability to run and connect to a Linux Container ([Docker](https://docs.docker.com/get-docker/) or [Podman](https://podman.io/getting-started/installation))

Start the Drone API server and copy the static API token as this is required for API calls.

``` console
$ docker run -it --rm -p 8080:8080 superorbital/drone-api
# or
$ podman run -it --rm -p 8080:8080 superorbital/drone-api
```

View the API documentation here: http://localhost:8080/swagger/index.html

Again, example request and response payloads for the API can be found in the `example-requests` and `example-responses` directories.

## Day One Goal

Complete a production-ready CLI that supports creating and listing drones. This will require writing client code to interact with the backend server API. The related user stories for this task are below.

### **Note**

We are actively hiring for the CLI team, so please ensure that your submission is in a state that will make it easy for others to quickly get up to speed and contribute.

We are currently running a closed-beta test and want to ensure that everyone's experience using the software is as smooth as possible. We may go into production any day now, so let's make sure this is ready.

Please try to utilize best-practices for your preferred language and don't forget to include documentation, logs, testing, error handling, and all the typical things that a robust project requires.

### Task: Add Create Drone to CLI

User Story

> **As an** employee of RentADrone
>
> **I want to** add a new drone to our fleet
>
> **so that I can** make sure that it is available for customer's to rent

Acceptance Criteria

> **Given** the user has the CLI installed and configured
>
> **When** the user runs `drone create` and passes in a JSON file
>
> **Then** the CLI should verify that the JSON file is valid
>
> **Given** The JSON file is valid
>
> **When** The CLI submits the JSON file to the backend server successfully
>
> **Then** The user should receive confirmation that the action has completed.

### Task: Add List Drone to CLI

User Story

> **As an** employee of RentADrone
>
> **I want to** list the details about all of the drones that are currently in fleet
>
> **so that I can** easily confirm the existence and current status of any drone

Acceptance Criteria

> **Given** the user has the CLI installed and configured
>
> **When** the user runs `drone list`
>
> **Then** The user should receive a list of details about all the drones currently registered in the system

## Evaluation Criteria

1. Implement working `drone create` and `drone list` commands.
2. Provide unit/integration tests to ensure the correctness of your code.
3. Handle basic error conditions, including retries where appropriate.
4. Follow best practices of the language you choose.
5. Provide documentation and examples of how to run CLI.
6. Provide documentation on how to develop and run tests for CLI.

## Submitting Your Solution

Once you've completed the tasks, please create a tarball containing your complete solution and email it to us. Be sure to include your `.git` directory if you used one.
