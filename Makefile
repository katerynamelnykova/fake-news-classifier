help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


install: ## Install required Python dependencies
	pip3 install -r requirements.txt


run: ## Run the app
	echo "running the app"
	uvicorn webapp.main:app --host 0.0.0.0 --reload --port 8000


install_and_run: install run ## Install dependencies and run the app


docker_build:	## Build the Docker image
	docker build -t fake-news-app .


docker_run:	## Run the Docker container
	docker run -it --rm -p 8000:8000 fake-news-app


docker_all: docker_build docker_run ## Build and run the Docker container

