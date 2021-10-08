# InternetSpeed
Project created to monitor the internet speed and automatically generate reports and send them by email to the owner.

Every 15 minutes a function will run that will test your 
internet speed, both download and upload. This data will
be saved in a database. Once per week, mondays at 8am,
a simple report will be generated, stating your average
speed and ping. A graph of the speed over the past week
will also be generated. All this information will be 
sent to your email. 

## Requirements
- Docker
- Docker-compose

## Initial setup
After setting up docker in your computer, create a .env file with
the same data as .env.template, but substitute your email
and password at the respective location - gmail is the default,
if you want another, some settings will have to be changed. Do not worry,
your data will remain there and only will be used to authenticate
your email. 

After that, just type 
```shell
docker-compose build
```
and
```shell
docker-compose up
```
