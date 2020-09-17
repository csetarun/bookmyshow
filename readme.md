# Movie ticketing system using Django Rest Framework
This project is for creating a backend for movie ticketing system similar to bookmyshow

# Installation 
1. Install [Docker](https://docs.docker.com/engine/install/ubuntu/)
2. Then run <code>bash run.sh</code> in terminal

Credentials for Django backend

username : **root**

password : **root**

**List of Theatres and adding new theatre :** http://localhost:8000/theatre/

**All the theatres in a city :** http://localhost:8000/theatre/?city=:city

**List of shows adding new shows :** http://localhost:8000/show/

**All cinemas in whcih a movie is playing :** http://localhost:8000/show/?movie=:movie_name

**List of movies and adding new movies :** http://localhost:8000/movie/

**All the movies playing in a city :** http://localhost:8000/movie/?city=:city

**List of seats and adding seats to shows :** http://localhost:8000/seat/

**Available seats(filter booked seats) for a particular show :** http://localhost:8000/seat/?show=:show_id

**These APIs can be accessed only after sign-in**

**List of bookings and making a new booking :** http://localhost:8000/booking/

**List of booked seats :** http://localhost:8000/booked_seat/


**Request parameters and response format can be found by using the Swagger**

http://localhost:8000/swagger/

**API Documentation can be found here.**

http://localhost:8000/redoc/

**Tests can be ran by running the following commands:**

<code>
cd bms

python manage.py test
</code>
