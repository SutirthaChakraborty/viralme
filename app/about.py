from flask import Blueprint, render_template
from .db import get_db_connection

about_routes = Blueprint("about", __name__)


@about_routes.route('/about')
def about():
    try:
        connection = get_db_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM about")
        about = cur.fetchall()
        cur.close()
        connection.close()
        return render_template('about.html', about=about)
    except:
        return render_template('about.html')
