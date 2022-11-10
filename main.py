from flask import Flask, jsonify, request;
import csv;
from demographic_filtering import output;
from content_filtering import get_recommendations, similarity;

all_articles = []

with open('articles.csv') as f:
    data = csv.reader(f)
    all_data = data.to_list()
    all_articles = all_data[1:]

liked_articles = []
not_liked_aricles = []

app = Flask(__name__)

@app.route('/get_article')

def get_article() :
    return jsonify({
        'data' : all_articles[0],
        'status' : 'success'
    })

@app.route('/liked_article', methods = ['POST'])

def liked_article() :
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        'status' : 'success'
    }), 201

@app.route('/not_liked_article', methods = ['POST'])

def not_liked_article() :
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_aricles.append(article)
    return jsonify({
        'status' : 'success'
    }), 201

@app.route('/get_output')

def get_output() :
    return jsonify({
        'data' : output,
        'status' : 'success'
    })

@app.route('/get_recommendation')

def get_recommendation() :
    return jsonify({
        'data' : get_recommendations('Bitcoin Future: When GBPcoin of Branson Wins Over USDcoin of Trump', similarity),
        'status' : 'success'
    })
