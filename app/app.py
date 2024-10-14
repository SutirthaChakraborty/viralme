from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from .home import home_routes
from .about import about_routes
from .portfolio import portfolio_routes
from .blog_archive import blog_archive_routes
from .blog_single import blog_single_routes
from .contact import contact_routes

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smpt.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'email'
app.config['MAIL_PASSWORD'] = 'password'

mail = Mail(app)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        email = request.form['email']
        msg = Message('Welcome to our newsletter!', sender='email', recipients=[email])
        msg.body = 'Thank you for subscribing to our newsletter!'
        mail.send(msg)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


app.register_blueprint(home_routes)
app.register_blueprint(about_routes)
app.register_blueprint(portfolio_routes)
app.register_blueprint(blog_archive_routes)
app.register_blueprint(blog_single_routes)
app.register_blueprint(contact_routes)
