# Basic_Django_Token_Authentication_Repo

### 1. Clone the repo

```bash
git clone https://github.com/kaustubh1971/Basic_Django_Token_Authentication_Repo.git
```

### 2. Considering you have installed python 3, create virtual env and install packages from requirements.txt

- ```bash
  cd Basic_Django_Token_Authentication_Repo
  ```
- Create Virtual environment
    - ```bash
      python3 -m venv my_env
      ``````
- Activate virtual env and inistall packages from requirements.txt
    - ```
      source my_env/bin/activate
      pip install -r requirements.txt
      ```

### 3. Configure and install postgres and create user and database

- Install Postgresql
    - ```bash
      sudo apt update
      sudo apt install postgresql postgresql-contrib
      sudo systemctl start postgresql.service
      ```

- Steps to connect db locally ?
    - ```bash
      sudo -i -u postgres
      psql
      ```

- Create User and password
    - ```postgres
      Create user test_user with password '123456';
      ```

- How to make user a Superuser ?
    - ```postgres
      \du
      ALTER USER test_user SUPERUSER;
      ```

- How to create a database and change owner of it ?
    - ```postgres
      create database test_db;
      ```

- How to check database owner and update database owner ?
    - ```postgres
      \l
      ALTER DATABASE test_db OWNER TO test_user;
      ```

- How to grant all the access to
    - ```postgres
      grant all privileges on database test_db to test_user;
      ```

- Exit this postgres terminal
    - ```postgres
      \q
      exit
      ```

### 4. Migrate the database

- ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- Create Superuser
    - ```bash
      python manage.py createsuperuser
      ```
- Now you can run server and visit admin by "http://127.0.0.1:8000/admin/" this URL and enter the email and password which you have provided while creating superuser.
    - ```bash
      python manage.py runserver
      ```

### 5. Postman documentation
- Use Register API, after that login from Login API mentioned in the postman documentation below. Use the token generated at login API for the further use in Header for Authorization with value token "token_value"
- https://documenter.getpostman.com/view/16504541/2s9YRGxpL3