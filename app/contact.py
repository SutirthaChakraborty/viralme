from flask import Blueprint, render_template

contact_routes = Blueprint("contact", __name__)

@contact_routes.route('/contact')
def contact():
    return render_template('contact.html')