.PHONY: build
build:
	docker-compose build

.PHONY: run
run:
	docker-compose up

.PHONY: run-worker
run-worker:
	docker-compose up -d worker

.PHONY: run-server
run-server:
	docker-compose up -d server

.PHONY: update-requirements
update-requirements: ## Update all requirements.txt files
	pip-compile --quiet --allow-unsafe --upgrade server/requirements.in
	pip-compile --quiet --allow-unsafe --upgrade worker/requirements.in
	pre-commit run requirements-txt-fixer --all-files --show-diff-on-failure
