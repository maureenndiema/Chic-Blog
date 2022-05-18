## MY CHIC BLOG

## Author
   
   Maureen Ndiema

## Description

   This is  a personal Chic blogging website where you can create and share your opinions and other users can read and comment on them. 

## Live Link
   
   Git clone https://github.com/maureenndiema/Chic-Blog.git

## User Stories
1. As a user, I would like to view the blog posts on the site
2. As a user, I would like to comment on blog posts
3. As a user, I would like to view the most recent posts
4. As a user, I would like to an email alert when a new post is made by joining a subscription.
5. As a user, I would like to see random quotes on the site
6. As a writer, I would like to sign in to the blog.
7. As a writer, I would also like to create a blog from the application.
8. As a writer, I would like to delete comments that I find insulting or degrading.
9. As a writer, I would like to update or delete blogs I have created.

## Behaviour Driven Development (BDD)
#  Users
   
   Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | *On page load* | Get all posts, Select between signup and login on the right side|
| Select SignUp| *Email,Username,Password* | Redirect to login|
| Select Login | *Username* and *password* | Redirect to page with app Blog-Web based on categories and commenting section|
| Select comment button | *Comment* | Form that you input your comment|
| Click on submit |  | Redirect to all comment

## Set-Up Installations
   
 1. clone repository https://github.com/maureenndiema/Chic-Blog.git
 2. Move to the folder and install requirements cd blogomatic pip     install -r requirements.txt

## Running the Application

1. Run main apllication
   Change in manage.py create_app('development')
   python3.8 manage.py server
2. Run tests
   Change in manage.py create_app('test')
   python3.8 manage.py test

## Technologies Used
   
 1. Python3.8
 2. Flask 1.1.2
 3. Flask-Bootstrap
 4. HTML
 5. CSS

## Contact Information
 For any further inquiries or contributions or comments, reach me at
 (ndiemam@gmail.com)

 ## License
  MIT License 
  Copyright @ 2022 Maureen Ndiema
