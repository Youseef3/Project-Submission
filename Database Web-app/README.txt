How to run our app:
1. The first thing to do is to create a fresh database in PostGreSQL. 
   Also make sure to run "pip install -r requirements.txt" to ensure that the needed modules are downloaded.

2. Second thing is to run the SQL files (CreateCountries.sql and CreateUsers.sql) inside the PSQL tool, 
   which will create the needed tables for our web-app. 
   IMPORTANT: Make sure to FIRST create the table for users (CreateUsers.sql), as the countries table has a reference to users.

3. Next, you go inside the app.py file and change the dbname, username and password. 
   Make sure that the dbname matches your database name that you created in PostGreSQL in step 1.

4. You can now run our web-app by running "python app.py". 

First step is to create an account. After you have created an account, you can log in. 
Here you can add new countries to the list of countries.




Note:
Our idea for this project does not really make any sense (you log into a website to see the population and gdp of every country).
We do however focus on the assignment at hand which is to create a web-app that interacts with a database.



Made by:
Mikail Cifci, psw892
Yahya Hajji, zjt766
Youseef Al-Janabi, bmr535