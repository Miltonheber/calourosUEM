from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/profissoes')
def profissoes():
    return render_template('profissoes.html')

@app.route('/livros')
def livros():
    return render_template('livros.html')

@app.route('/labz')
def labz():
    return render_template('labz.html')




app.run(debug=True)
