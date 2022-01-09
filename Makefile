.PHONY: build
build:
	docker-compose build

.PHONY: run
run:
	docker-compose up

.PHONY: install-pi
install-pi:
	cd scripts && bash install_raspberry_pi.sh

.PHONY: run-worker
run-worker:
	docker-compose up -d worker

.PHONY: run-server
run-server:
	docker-compose up -d server
