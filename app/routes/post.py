from flask import Blueprint, render_template
from ..extensions import db
from ..models.post import Post

post = Blueprint('post', __name__)

@post.route('/post/create', methods=['POST', 'GET'])
def create():
    return render_template('post/create.html')
