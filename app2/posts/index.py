from flask import Blueprint, render_template, redirect, request, url_for
from models.Post import Post
from config import db

posts = Blueprint('posts', __name__)

@posts.route('/new', methods=['GET'])
def new():
	return render_template('posts/new.html')

@posts.route('/', methods=['GET'])
def index():
	posts = Post.query.order_by(Post.title)
	
	return render_template('posts/index.html', posts = posts)

@posts.route('/', methods=['POST'])
def create():
	post = Post(request.form['title'], request.form['body'])

	db.session.add(post)
	db.session.commit()

	return redirect(url_for('posts.index'))

@posts.route('/<int:id>', methods=['DELETE'])
def remove(id):
	post = Post.query.get(id)

	db.session.delete(post)
	db.session.commit()

	return redirect(url_for('posts.index'))
