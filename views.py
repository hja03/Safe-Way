from flask import Blueprint, render_template, redirect, url_for, request, make_response, flash
from database import *

core = Blueprint('core', __name__, template_folder='templates')

@core.route("/")

def index():
    return render_template('index.html')