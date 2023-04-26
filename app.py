from flask import Flask, jsonify
import json

app = Flask(__name__)

with open("movies.json") as dados:
    movies = json.load(dados)

# Add uma um retorno para a raiz
@app.route("/")
def index():
    return "Bem vindo(a) a API Movies!"

# Retorna todos os livros
@app.route('/movies', methods = ['GET'])
def get_movies():
    return movies

# Retorna apenas um livro pelo ID
@app.route('/movies/<int:id>', methods= ['GET'])
def get_movie_by_id(id):
    for movie in movies:
        if movie.get('id') == id:
            return jsonify(movie)

