from flask import Blueprint, render_template, request, redirect
from ..extensions import db
from ..models.post import Post

post = Blueprint('post', __name__)

@post.route('/', methods=['POST', 'GET'])
def all():
    posts = Post.query.all()
    return render_template('post/all.html', posts=posts)


@post.route('/post/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        teacher = request.form.get('teacher')
        subject = request.form.get('subject')
        student = request.form.get('student')
        print(teacher)
        print(subject)
        print(student)

        post = Post(teacher=teacher, subject=subject, student=student)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(e)
    else:
        return render_template('post/create.html')


@post.route('/post/<int:id>/update', methods=['POST', 'GET'])
def update(id):
    if request.method == 'POST':
        teacher = request.form.get('teacher')
        subject = request.form.get('subject')
        student = request.form.get('student')
        print(teacher)
        print(subject)
        print(student)

        post = Post(teacher=teacher, subject=subject, student=student)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(e)
    else:
        return render_template('post/update.html')
