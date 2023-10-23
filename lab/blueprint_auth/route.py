from flask import Blueprint, render_template, session

# blueprint_auth = Blueprint('bp_auth', __name__, template_folder='templates')
#
#
# @blueprint_auth('/')
# def auth_index():
#     user_id = 1
#     user_group = 'admin'
#     session['user_id'] = user_id
#     session['user_group'] = user_group
#     return True