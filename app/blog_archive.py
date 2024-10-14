from flask import Blueprint, render_template
from .db import get_db_connection

blog_archive_routes = Blueprint("blog_archive", __name__)

@blog_archive_routes.route('/blog-archive')
def blog_archive():
    try:
        connection = get_db_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM blog")
        blogs = cur.fetchall()
        cur.close()
        connection.close()
        return render_template("blog-archive.html", blogs=blogs)
    except:
        return render_template("blog-archive.html")