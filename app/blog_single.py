from flask import Blueprint, render_template, request
from .db import get_db_connection

blog_single_routes = Blueprint("blog_single", __name__)

@blog_single_routes.route('/blog-single', methods=['GET'])
def blog_single():
    try:
        id = request.args.get('id')
        connection = get_db_connection()
        cur = connection.cursor()
        cur.execute("SELECT * from blog WHERE id = %s", (id,))
        blog = cur.fetchone()
        cur.execute("SELECT * FROM blog_comment WHERE blog_id = %s", (id,))
        comments = cur.fetchall()
        cur.close()
        connection.close()
        return render_template("blog-single.html", blog=blog, comments=comments)
    except:
        return render_template("blog-single.html")