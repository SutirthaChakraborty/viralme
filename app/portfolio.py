from flask import Blueprint, render_template
from .db import get_db_connection

portfolio_routes = Blueprint("portfolio", __name__)

@portfolio_routes.route("/portfolio")  # pylint: disable=too-many-return-statements
def portfolio():
    try:
        connection = get_db_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM portfolio INNER JOIN portfolio_category ON portfolio.id = portfolio_category.portfolio_id")
        portfolio = cur.fetchall()
        cur.close()
        connection.close()
        return render_template("portfolio.html", portfolio=portfolio)
    except:
        return render_template("portfolio.html")
