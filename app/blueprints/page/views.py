from flask import Blueprint, render_template

from .contexts import PageHomeContext


page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    context = PageHomeContext()
    return render_template('page/home.jinja2', ctx=context)
