import os
import click

from flask import Flask, render_template

from blog.blueprints.blog import blog_bp
from blog.extensions import bootstrap, db, ckeditor, moment, login_manager
from blog.models import Admin, Post, Category, Comment
from blog.configs import config


def create_app(config_name=None):
    # Fill your code here


def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    moment.init_app(app)


def register_blueprints(app):
    # Fill your code here


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)


def register_template_context(app):
    @app.context_processor
    def make_template_context():
        admin = Admin.query.first()
        categories = Category.query.order_by(Category.name).all()
        return dict(admin=admin, categories=categories)


def register_errors(app):
    # Fill your code here


def register_commands(app):
    # Fill your code here