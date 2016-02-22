# Resiliency

### How to run with new database configuration:

In the data folder exists psycopg2-2.6.1-cp35-none-win_amd64.whl.  
Run in cmd or terminal:  
```sh
$ pip install psycopg2-2.6.1-cp35-none-win_amd64.whl
```
- Install [PostgreSQL]  
- I also suggest watching [this video] (use port 3304)
- Follow the video and look in the installation folder/bin of PostgreSQL for pgAdmin3 and run it (I suggest creating a shortcut)  
- Create a database called 'rise'

In cmd or terminal in the respository:
```sh
$ python manage.py makemigrations client
$ python manage.py migrate
```

All done! Run with:
```sh
$ python manage.py runserver
```

   [PostgreSQL]: <http://www.postgresql.org/download/>
   [this video]: <https://www.youtube.com/watch?v=-f9lke78g2U>

