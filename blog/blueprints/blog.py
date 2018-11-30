from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint, abort, make_response
from flask_login import current_user

from blog.extensions import db
from blog.forms import CommentForm, AdminCommentForm
from blog.models import Post, Category, Comment
from blog.utils import redirect_back

blog_bp = Blueprint('blog', __name__)

# Fill your code here