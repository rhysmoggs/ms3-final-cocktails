

technologies used:

- python
- JS
- CSS3
- HTML5

- PostgreSQL - 
- MongoDB - 
- PsycoPG2 - database adapter. library for connecting Python to PostgreSQL.
- SQLAlchemy - ORM lirbary
- PyMongo - 
- Flask - 
- Flash - 
- dnspython - 
- Jinja2? - template
- jquery
- materialize(sp?) - 
- fontawesome - icons
- google fonts
- heroku - 
- git, gitpod, github

- image editing websites/software here
- balsamiq
- era database/ design




Data Schema:

link both together through...


- Relational Database:


    PostgreSQL - open-source, Object-Relational Databse Management System (ORDBMS). fre use, licencing? good for future projects or launching this one if needs be.

    primary key - A unique ID that identifies individual records regardless of any changes that occur



- Non-Relational Database:
    mongoDB - 






------



deployment of website:

1. If you wish to - use Code Institute's template from here:  / copy this projects link/url?
2. install two python packages. Flask and SQLAlchemy to work with Postgres databases. psycopg2 is necessary to work with Postgres database. In command line type: `pip3 install Flask-SQLAlchemy psycopg2`
3. create "env.py" file
4. Create a ".gitignore" file if you choose not to use Code Institute's template. Add `env.py` and the soon to be generated `__pyache__/` to it. All hidden and sensitive files/folders to be added here.
5. in "env.py", type following:
    ```
    import os

    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", "any_secret_key")
    os.environ.setdefault("DEBUG", "True")
    os.environ.setdefault("DEVELOPMENT", "True")
    os.environ.setdefault("DB_URL", "postgresql:///<DATABASE>")
    ```

    The `any_secret_key` can be called whatever you wish: `os.environ.setdefault("SECRET_KEY", "any_secret_key")`or generate a random and secure password here: https://randomkeygen.com/

    make sure to change `os.environ.setdefault("DEBUG", "True")` to "False" before deploying/launching project.

    `<DATABASE>` points to the databse to be created, in this case "my_cocktails".
6. create a folder (in this case, folder is named "cocktails") in the root of your project.
7. within that newly created folder, create a file called `__init__.py`
8. write the following in the new file:
    ```
    import os
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    if os.path.exists("env.py"):
        import env  # noqa


    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

    db = SQLAlchemy(app)

    from cocktails import routes  # noqa
    ```
9. create a "routes.py" file within the "cocktails" folder
10. within that "routes.py" file, write the following:
    ```
    from flask import render_template
    from cocktails import app, db


    @app.route("/")
    def home():
        return render_template("base.html")
    ```
11. in root of project, create "run.py" file
12. within "run.py", write the following:
    ```
    import os
    from cocktails import app


    if __name__ == "__main__":
        app.run(
            host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG")
        )
    ```
13. within "cocktails" folder, create a new "templates" folder. This is where Flask will search for any html templates to be rendered.
14. create a new file "base.html" within the "templates" folder.
15. within the "base.html" file, write whatever you wish to be presented on your website.
16. in the terminal, write `python3 run.py` to launch the project.
17. add, commit and push.


Setting up Databse - postgreSQL database:

make sure you have postgreSQL installed locally if you are not using CI's template?
set up the databse schema as follows:
1. define our models by creating a "models.py" file within the "cocktails" folders
2. write the following in the "models.py" file and create the tables:
    ```
    from cocktails import db


    class Category(db.Model):
        # schema for the Category model
        id = db.Column(db.Integer, primary_key=True)
        category_name = db.Column(db.String(25), unique=True, nullable=False)

        def __repr__(self):
            # __repr__ to represent itself in the form of a string
            return self.category_name


    class Users(db.Model):
        # schema for the Users model
        id = db.Column(db.Integer, primary_key=True)
        user_name = db.Column(db.String(20), unique=True, nullable=False)
        password = db.Column(db.String(260), nullable=False)

        def __repr__(self):
            # __repr__ to represent itself in the form of a string
            return self.user_name
    ```
3. in "routes.py", import these newly created models:
    ```
    from cocktails.models import Category, Users
    ```
4. log in to postgreSQL terminal by typing psql in terminal.
5. type `CREATE DATABASE cocktails;`
6. then `\c cocktails;` to connect to the newly created database.
7. finally `\q` to exit.
8. use python to generate and migrate the models into the database. if any changes are made to this database, you must repeat the same steps to refresh and update your database. in the terminal, type `python3`.
9. type `from cocktails import db`
10. type `db.create_all()`
11. if you wish to check that the tables exist, type `psql -d cocktails` followed by `\dt` then `\q` to quit, otherwise just exit via `exit()`.
12. commit then push


Setting up Database - MongoDB database:

Make sure to that you have a MongoDB account.

1. Create a cluster (https://www.mongodb.com/basics/clusters/mongodb-cluster-setup). This project uses a shared cluster. Choose the closest region to you which is free to use. Free cluster tier and then name your `<CLUSTER>` ("myFirstCluster", in this project).
2. In Database Access, add a new database user (https://www.mongodb.com/docs/atlas/security-add-mongodb-users/#add-database-users).
3. In Network Access, click add IP address and choose 'Allow Access From Anywhere'. Input the IP of your hosts here to add further security.
4. In the newly created `<CLUSTER>`, click on Create a Database and under Database Name, enter a `<DATABASE>` name, ("my_cocktails", in this project)
5. Under collection name, enter `<COLLECTION>` ("cocktails", in this project).
6. Within the `<DATABASE>` ("my_cocktails"), click on Create Collection button and enter any other collections you wish to store.
7. Within each collection, click on Insert Document, and enter the key-value pairs you wish to store in your document. For this project, the following key names and value data types were stored:
    ```
    _id: <ObjectId>
    cocktail_name: <string>
    category_name: <string>
    cocktail_img: <string>
    cocktail_description: <string>
    created_by: <string>
    main_ingredient: <string>
    method: <string>
    other_ingredients: <array>
    prep_time: <Int32> with a default value of "0"
    servings: <Int32> with a default value of "0"
    ```
8. In the terminal, install dnspython `pip3 install dnspython`
9. Install pymongo too `pip3 install flask-pymongo`
10. on the mongo website, in your collection, connect your cluster. Choose 'Connect your application' and choose Python and your version (3.6 or later, in this project).
11. Copy the connection string.
12. In the "env.py" file, add the following environment variables to the already present ones:
    ```
    os.environ.setdefault("MONGO_URI", "mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER>.1megs.mongodb.net/<DATABASE>?retryWrites=true&w=majority")
    os.environ.setdefault("MONGO_DBNAME", "<DATABASE>")
    ```
    Make sure to insert your own information for `<USERNAME>`, `<PASSWORD>`, `<CLUSTER>` and `<DATABASE>`.
13. In "__init__.py" add  `from flask_pymongo import PyMongo`.
14. Add and update:
    ```
    app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

    mongo = PyMongo(app)
    ```
15. In "routes.py", update entire file to be:
    ```
    from flask import (
        flash, render_template,
        request, redirect, session, url_for)
    from bson.objectid import ObjectId
    from cocktails import app, db, mongo
    from cocktails.models import Category, Users


    @app.route("/")
    def home():
        return render_template("cocktails.html")
    ```
16. In terminal, write `touch cocktails/templates/cocktails.html`
17. In "cocktails.html" add your website content here (use templates and link "base.html" to all other pages etc)
18. In terminal, "python3 run.py" to view your work.
19. add, commit, push.


Linking the databases:

1. Using category_id
2. 


Deploy the application to Heroku:

1. Create a "requirements.txt" by typing `pip3 freeze --local > requirements.txt` in the terminal. This lists what is necessary to run the project.
2. Create a Procfile by typing `echo web: python run.py > Procfile` in the terminal. In the newly created "Procfile", check to see if a blank line appears under the written code. If there is, delete and save that change. It can cause issues with Heroku.
3. Commit and push.
4. On the Heroku website. Create a new app and name it. Choose the regeion closest to you.
5. Create a new database on Heroku. Resources > Add-ons, search for heroku postgres and choose the 'Hobby Dev - Free' option, or whichever suits your needs.
6. Once confirmed, go to Settings > Config Vars > Reveal Config Vars, and input the following:
    ```
    IP = 0.0.0.0
    PORT = 5000
    SECRET_KEY = your_secret_key_here
    MONGO_URI = mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER>.1megs.mongodb.net/<DATABASE>?retryWrites=true&w=majority
    MONGO_DBNAME = your_database_name_here
    ```
    You can add:
    ```
    DEBUG = True
    ```
    temporarily but make sure to change to `False` when finalizing the app. Keep to `True` for error fixing during development.
7. In your Config Vars in Heroku, if DATABASE_URL starts with `postgres` instead of `postgresql`, update your `__init__.py` file to:
```
import os
import re
from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

uri = os.environ.get("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku

db = SQLAlchemy(app)
mongo = PyMongo(app)

from cocktails import routes  # noqa
```
This wil ensure that the database is correctly linked.
8. In github, make sure you've added, commited and pushed your latest work.
9. The following point is an extract taken from Code Institute:

    ```Automated Deployments from GitHub disabled by Heroku
    Due to a security issue, Heroku has disabled automated deployments from GitHub. Unfortunately, we have no indication if or when they will reactivate this. In order for you to deploy while this situation persists, please follow the steps below to deploy from your Gitpod workspace:

    - Open the terminal.
    - For those of you who are using MFA/2FA: please scroll down to see the additional steps required.
    For those of you not using MFA/2FA: Log in to Heroku and enter your details.
    command: heroku login -i
    - Get your app name from heroku.
    command: heroku apps
    - Set the heroku remote. (Replace <app_name> with your actual app name and remove the <> characters)
    command: heroku git:remote -a <app_name>
    - Add and commit any changes to your code if applicable
    command: git add . && git commit -m "Deploy to Heroku via CLI"
    - Push to both GitHub and Heroku
    command: git push origin main
    command: git push heroku main

    MFA/2FA enabled?
    - Click on Account Settings (under the avatar menu) on the Heroku Dashboard.
    - Scroll down to the API Key section and click Reveal. Copy the key.
    - Back in your Gitpod workspace, enter the command: heroku_config , and enter your API key you copied when prompted.
    - Continue from step 3 above. If you get prompted to log in at any point:
      - Enter your Heroku username.
      - Enter the API key you just copied.
    
    Need to deploy again?
    You should just be able to add, commit and push, and if prompted enter your username and API key again.

10. Click 'Open App' in heroku, and your project will be displayed here.
11. Due to the automatic deployment issues on heroku's part, any changes to your app will need to manually be updated by following step 8. again.
12. We need to create our tables on the Heroku database. In Heroku, on the top-right, clcik More > Run Console.
13. Type `python3`
14. Type `from cocktails import db` then `db.create_all()` then `exit()`
15. In GitHub, change your `env.py` to reflet the newly created database by deleting `os.environ.setdefault("DB_URL", "postgresql:///cocktails")` and inserting `os.environ.setdefault("DATABASE_URL", "<heroku string>")` from Heroku's config vars.