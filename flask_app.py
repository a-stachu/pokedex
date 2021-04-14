import sqlite3

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def homepage():
    return redirect(url_for('get_pokemon'))

@app.route('/pokedex/')
def get_pokemon():
    conn = sqlite3.connect('pokemon.db')
    cursor = conn.cursor()
    query = "SELECT * FROM pokemon"
    cursor.execute(query)
    data = cursor.fetchall()

    conn.commit()
    conn.close()
    return render_template('pokemon.html', data=data)

@app.route('/update-pokemon/<int:id>', methods=["GET"])
def update_pokemon_form(id):
    try:
        conn = sqlite3.connect('pokemon.db')
        cursor = conn.cursor()
        query = "SELECT * FROM pokemon WHERE pokemon_id=?"
        cursor.execute(query, (id, ))
        data = cursor.fetchall()

        conn.commit()
        conn.close()
        return render_template('update-pokemon.html', data=data[0])

    except Exception as err:
        return "Error!" + str(err), 500

@app.route('/update-pokemon', methods=["POST"])
def update_pokemon_db():
    try:
        Name = request.form['Name']
        Type1 = request.form['Type1']
        Type2 = request.form['Type2']
        HP = int(request.form['HP'])
        Attack = float(request.form['Attack'])
        pokemon_id = int(request.form['pokemon_id'])

        conn = sqlite3.connect('pokemon.db')
        cursor = conn.cursor()

        query = "UPDATE pokemon SET Name=?,Type1=?,Type2=?,HP=?, Attack=? WHERE pokemon_id=?"
        cursor.execute(query, (Name, Type1, Type2, HP, Attack, pokemon_id))
        conn.commit()
        conn.close()

        return redirect(url_for('get_pokemon'))
    except Exception as err:
        return "Error" + str(err), 500

@app.route('/add-pokemon-1')
def add_pokemon_1():
    try:
        conn = sqlite3.connect('pokemon.db')
        cursor = conn.cursor()
        query = "SELECT * FROM pokemon"
        cursor.execute(query)
        data = cursor.fetchall()

        conn.commit()
        conn.close()
        return render_template('add-pokemon.html', data=data[1])
    except Exception as err:
        return "Error" + str(err), 500

@app.route('/add-pokemon-2', methods=["POST"])
def add_pokemon_2():
    try:
        Name = request.form['Name']
        Type1 = request.form['Type1']
        Type2 = request.form['Type2']
        HP = int(request.form['HP'])
        Attack = float(request.form['Attack'])

        conn = sqlite3.connect('pokemon.db')
        cursor = conn.cursor()

        query = "INSERT INTO pokemon(Name, Type1, Type2, HP, Attack) VALUES(?, ?, ?, ?, ?)"
        cursor.execute(query, (Name, Type1, Type2, HP, Attack))
        conn.commit()
        conn.close()

        return redirect(url_for('get_pokemon'))
    except Exception as err:
        return "Error" + str(err), 500


@app.route('/remove-pokemon', methods=["POST"])
def remove_pokemon():
    try:
        pokemon_id = int(request.form['pokemon_id'])

        conn = sqlite3.connect('pokemon.db')
        cursor = conn.cursor()

        query = "DELETE FROM pokemon WHERE pokemon_id=?"
        cursor.execute(query, (pokemon_id, ))
        conn.commit()
        conn.close()

        return redirect(url_for('get_pokemon'))
    except Exception as err:
        return "Error" + str(err), 500



if __name__ == '__main__':
    app.run()
