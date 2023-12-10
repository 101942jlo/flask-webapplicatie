from flask import Flask, render_template, request, redirect, url_for
from data import users
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', gebruikers = users, title = 'Home')

@app.route('/about')
def about():
    return render_template('about.html', title ='Over ons')

@app.route('/detail/<int:id>')
def detail(id):
    for gebruiker in users:
        if gebruiker['id'] == id:
            return render_template('detail.html', user=gebruiker, title='Details')
        
@app.route('/add')
def add():
    return render_template('add.html', title='Toevoegen')


@app.route('/add_user', methods=['POST'])
def add_user():
    nieuwe_gebruiker = {
        'id': len(users)+1,
        'naam': request.form['name'],
        'leeftijd': request.form['age'],
        'foto': f'https://randomuser.me/api/portraits/{request.form["gender"]}/{random.randint(1, 99)}.jpg'
    }
    users.append(nieuwe_gebruiker)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_user(id):
    indexlist = [n for n, user in enumerate(users) if user['id']==id]
    print(indexlist)
    del users[indexlist[0]]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)