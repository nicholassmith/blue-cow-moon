build: ## Build the container
	docker build -t blue-cow-moon-py .

run: build
	docker run -d -p 5000:5000 --name bcmp blue-cow-moon-py:latest

stop: 
	docker stop bcmp && docker rm bcmp