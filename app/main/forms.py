from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError, HiddenField
from wtforms.validators import DataRequired, Email
from ..models import Subscriber



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators=[DataRequired()])
    submit = SubmitField('Save')


class BlogForm(FlaskForm):
    title = StringField('Title :', validators=[DataRequired()])
    blog = TextAreaField('Your Blog :', validators=[DataRequired()])
    submit = SubmitField('Blog')


class CommentForm(FlaskForm):
    comment_by = StringField("Enter a nickname", validators=[DataRequired()])
    comment = TextAreaField('Enter Comment : ', validators=[DataRequired()])
    submit = SubmitField("Comment")


class UpdateBlogForm(FlaskForm):
    title = StringField("Blog title :", validators=[DataRequired()])
    blog = TextAreaField("Blog :", validators=[DataRequired()])
    submit = SubmitField("Update")


class SubscriberForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()],render_kw={"placeholder": "Enter Email"})
    submit = SubmitField('Subscribe')

    def validate_email(self, data_field):
        if Subscriber.query.filter_by(email=data_field.data).first():
            raise ValidationError('This email is already subscribed!')