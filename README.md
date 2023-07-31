# DockerDemo

A PoC project created for education reasons

**pythonServer** contains a flask server that only has one endpoint 
```
GET:
localhost:5001/products
```

**vueFrontEnd** is a vueJS app that only sends a GET request to the above endpoint and displays the response

docker-compose.yml file starts 3 services
- pythonServer
- vue_frontend
- postgres (just for shows, no connection is made from backend to db)

In order to run follow the next steps:
- ```cd pythonServer```
- ```docker build -t demo_python_server .```  # create the backend docker image
- ```cd ../vueFrontEnd```
- ```docker build -t demo_vue_frontend .```  # create the backend docker image
- ```cd ..```
- ```docker compose up```

This should start up all containers from the created images and you can have access to them from the outside 
