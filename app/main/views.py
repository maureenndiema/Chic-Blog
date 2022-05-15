from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_quotes
from ..models import Quote,User,Blog,Upvote,Downvote,Comment,Subscriber
from .forms import UpdateProfile, BlogForm, CommentForm, UpdateBlogForm,SubscriberForm
from .. import db,photos
from flask_login import login_required,current_user
from ..email import mail_message
import markdown2

# Views
@main.route('/',methods=["GET", "POST"])
def index():
    '''
    View root page function that returns the index page and its content
    '''
    name = "Time to get started "
    # context ={
    #     name: name
    # }
    return render_template('index.html', name=name)