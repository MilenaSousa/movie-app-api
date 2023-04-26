from flask import Flask, jsonify
import json

app = Flask(__name__)

with open("movies.json") as dados:
    movies = json.load(dados)


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

if __name__=="__main__":
    app.run(host='127.0.0.9',port=4455) 
