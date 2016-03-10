# Resiliency

### How to run with new database configuration:

# For Windows:  
In the data folder exists psycopg2-2.6.1-cp35-none-win_amd64.whl.
Then in that directory in cmd:
```sh
$ pip install psycopg2-2.6.1-cp35-none-win_amd64.whl
```
- Install [PostgreSQL]  
- Watch this [video] and use port 3304
- Follow the video and look in the installation folder/bin of PostgreSQL for pgAdmin3 and run it (I suggest creating a shortcut)  
- Use the password 'capstone' since it is the default in settings.py
- Create a database called 'rise'

# For Mac:
install [Postgres.app]
Then in terminal:
```sh
$ touch ~/.bash_profile; open ~/.bash_profile
```
- A file should open
- Copy and paste these lines and save the file:
   ```sh
   PATH="/Applications/Postgres.app/Contents/Versions/9.5/bin:$PATH"
   export DYLD_FALLBACK_LIBRARY_PATH=$HOME/anaconda/lib:$DYLD_FALLBACK_LIBRARY_PATH
   ```
- Run this command in terminal:
```sh
$ pip install psycopg2
```
NOTE: You may need to run this afterwards:
```sh
$ pip install django
```

# After above is complete
In cmd or terminal in the respository directory:
```sh
$ python manage.py makemigrations client
$ python manage.py migrate
```

All done! Run with:
```sh
$ python manage.py runserver
```
   [Postgres.app]: <http://postgresapp.com/>
   [PostgreSQL]: <http://www.postgresql.org/download/>
   [video]: <https://www.youtube.com/watch?v=-f9lke78g2U>
