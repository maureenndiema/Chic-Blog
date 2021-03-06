from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quote:
    
    def __init__(self,author,quote):
        self.author=author
        self.quote=quote

class User (UserMixin, db.Model):
    __tablename__ ='users'
    id= db.Column(db.Integer,primary_key =True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blogs = db.relationship('Blog', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)
    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    blog = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    upvote = db.relationship('Upvote', backref='blog', lazy='dynamic')
    downvote = db.relationship('Downvote', backref='blog', lazy='dynamic')
    comment = db.relationship('Comment', backref='blog', lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def get_all_blogs(cls):
        return Blog.query.order_by(Blog.time.desc()).all()
    
    def __repr__(self):
        return f'Blog {self.blog}'

class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer, default=1)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id', ondelete='SET NULL'), nullable=True)

    def save_upvote(self):
        db.session.add(self)
        db.session.commit()

    def upvote(cls, id):
        upvote_post = Upvote(user=current_user, pitch_id=id)
        upvote_post.save_upvote()

    @classmethod
    def query_upvotes(cls, id):
        upvote = Upvote.query.filter_by(pitch_id=id).all()
        return upvote

    def __repr__(self):
        return f'{self.blog_id}'

class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer, primary_key=True)
    downvote = db.Column(db.Integer, default=1)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id', ondelete='SET NULL'), nullable=True)


    def save_downvote(self):
        db.session.add(self)
        db.session.commit()

    def downvote(cls, id):
        downvote_post = Downvote(user=current_user, pitch_id=id)
        downvote_post.save_downvote()

    @classmethod
    def query_downvotes(cls, id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
        return downvote

    def __repr__(self):
        return f'{self.blog_id}'

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    comment_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    comment_by = db.Column(db.String)
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id",ondelete='SET NULL'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id",ondelete='SET NULL'), nullable=True)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_comment(cls, id):
        gone = Comment.query.filter_by(id=id).first()
        db.session.delete(gone)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(blog_id=id).all()
        return comments

    def __repr__(self):
        return f'{self.blog_id}'

class Subscriber(db.Model):
    __tablename__ = "subscribers"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True)


