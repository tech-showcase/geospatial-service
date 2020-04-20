## GEO SPATIAL SERVICE

### Description
This repo contains project that handle geospatial-related services. 
This service is part of a big system. 
The whole system will be used to present technology show case.

### Features
- Serve weather data

This service serve feature that is mentioned above through HTTP.

### How to run
#### Docker
- Install docker
- Build and run docker image as below
```shell script
$ docker build -t geospatial-service .
$ docker run -p 8081:8081 geospatial-service
```
