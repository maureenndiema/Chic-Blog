from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError, HiddenField
from wtforms.validators import Required, Email
from ..models import Subscriber



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators=[Required()])
    submit = SubmitField('Save')


class BlogForm(FlaskForm):
    title = StringField('Title :', validators=[Required()])
    blog = TextAreaField('Your Blog :', validators=[Required()])
    submit = SubmitField('Blog')


class CommentForm(FlaskForm):
    comment_by = StringField("Enter a nickname", validators=[Required()])
    comment = TextAreaField('Enter Comment : ', validators=[Required()])
    submit = SubmitField("Comment")


class UpdateBlogForm(FlaskForm):
    title = StringField("Blog title :", validators=[Required()])
    blog = TextAreaField("Blog :", validators=[Required()])
    submit = SubmitField("Update")


class SubscriberForm(FlaskForm):
    email = StringField(validators=[Required(), Email()],render_kw={"placeholder": "Enter Email"})
    submit = SubmitField('Subscribe')

    def validate_email(self, data_field):
        if Subscriber.query.filter_by(email=data_field.data).first():
            raise ValidationError('This email is already subscribed!')