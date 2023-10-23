import os
from flask import Blueprint, render_template, request, current_app
from lab.work_with_db import select_dict
from lab.sql_provider import SQLProvider
import lab.view_data as view_data

blueprint_query = Blueprint('bp_query', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_query.route('/query_menu', methods=['GET', 'POST'])
def query_menu():
    if request.method == 'GET':
        table_items = view_data.query_menu_table_items
        return render_template('query_menu.html', table_items=table_items)
    else:
        query_name = request.form.get('query_name')
        return handle_query_post_request(query_name)


def handle_query_post_request(query_name: str):
    sql = provider.get(query_name + ".sql")
    answer = select_dict(current_app.config['db_config'], sql)

    return render_template('dynamic.html', table_items=answer, back_site='bp_query.query_menu')


@blueprint_query.route('/cat_price', methods=['GET', 'POST'])
def query_index_cat_price():
    if request.method == 'GET':
        return render_template('input_param_cat_price.html', wrong=False)
    else:
        category = request.form.get('category')
        price = request.form.get('price')

        sql = provider.get('product_1.sql', prod_category=category, prod_price=price)
        products = select_dict(current_app.config['db_config'], sql)

        if products:
            return render_template('dynamic.html', products=products, back_site='bp_query.query_index_cat_price')
        else:
            return render_template('input_param_cat_price.html', wrong=True)


@blueprint_query.route('/name', methods=['GET', 'POST'])
def query_index_name():
    if request.method == 'GET':
        return render_template('input_param_name.html', wrong=False)
    else:
        name = request.form.get('name')
        price = request.form.get('price')

        sql = provider.get('product_2.sql', prod_name=name, prod_price=price)
        products = select_dict(current_app.config['db_config'], sql)
        if products:
            return render_template('dynamic.html', products=products, back_site='bp_query.query_index_name')
        else:
            return render_template('input_param_name.html', wrong=True)
