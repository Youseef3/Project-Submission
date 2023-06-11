from flask import Flask, redirect, session, render_template, url_for, request, flash
import psycopg2
import os

app = Flask(__name__)

# SET YOUR OWN VALUES HERE 
db = "dbname='Countries' user='Youseef' host='localhost' password='Youseef'"
connection = psycopg2.connect(db)
cursor = connection.cursor()

@app.route("/createaccount", methods=['POST', 'GET'])
def createacc():
    cur1 = connection.cursor()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            # Try to insert the new user
            cur1.execute("INSERT INTO users(username, password) VALUES (%s, %s) RETURNING user_id", (username, password))
            connection.commit()
            flash('Account has been successfully created!')
            return redirect(url_for('home'))  # home page
        except psycopg2.IntegrityError:  
            # This exception is raised when there is a unique constraint violation (i.e., duplicate username)
            connection.rollback()
            flash('Username is already in use! Please choose another username!')
    return render_template('createacc.html')


@app.route("/")
def home():
    if session.get('logged') == False:
        return render_template('login.html')
    else:
        return redirect(url_for("countries"))

@app.route("/countries")
def countries():
    if session.get('logged') == False:
        return redirect(url_for("home"))
    else:
        cur = connection.cursor()
        cur.execute("SELECT * FROM countries ORDER BY country")
        rows = cur.fetchall()
        countries_data = [dict(country=row[0], population=row[1], gdp=row[2]) for row in rows]
        return render_template('index.html', countries=countries_data)

@app.route("/login", methods=['POST'])
def login():
    cur = connection.cursor()
    username = request.form['username']
    password = request.form['password']

    cur.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    user = cur.fetchone()

    if user is None:
        flash("Username or password is incorrect!")
    else:
        flash("You have successfully logged in!")
        session['logged'] = True
        session['username'] = username
        session['user_id'] = user[0]
    
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session['logged'] = False
    return redirect(url_for("home"))

@app.before_request
def before_request():
    if 'logged' not in session:
        session['logged'] = False

@app.route("/addcountry", methods=['GET', 'POST'])
def addcountry():
    if request.method == 'POST':
        country = request.form['country']
        population = request.form['population']
        gdp = request.form['gdp']
        user_id = session.get('user_id')

        cur = connection.cursor()
        cur.execute("INSERT INTO countries(country, population, gdp, user_id) VALUES (%s, %s, %s, %s)", (country, population, gdp, user_id))
        connection.commit()

        flash("Country has been successfully added!")
        return redirect(url_for('countries'))
    else:
        return render_template('add_country.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(32)
    app.run(debug=True)
