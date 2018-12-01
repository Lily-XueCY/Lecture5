import random

from faker import Faker
from sqlalchemy.exc import IntegrityError

from blog.models import Admin, Category, Post, Comment
from blog.extensions import db

fake = Faker()

def fake_admin():
    # Fill your code here
    pass

def fake_categories(count=10):
    # Fill your code here
    pass

def fake_posts(count=50):
    # Fill your code here
    pass

def fake_comments(count=500):
    # Fill your code here
    pass