"""
Main Flask Application
Crime Reporting System with Prediction
"""
from flask import Flask, render_template, session
from flask_login import LoginManager
import os
from datetime import timedelta

# Import configuration
from config import Config

# Import routes
from routes.auth import auth
from routes.reports import reports
from routes.admin import admin

# Import models
from models.database import Database, User

# Import utilities
from utils.security import SecurityHeaders, generate_csrf_token
from utils.helpers import format_datetime, get_time_ago, get_status_badge_class, get_priority_badge_class

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please login to access this page.'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    """Load user for Flask-Login"""
    return User.get_by_id(int(user_id))

# Register blueprints
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(reports)
app.register_blueprint(admin)

# Context processors for templates
@app.context_processor
def utility_processor():
    """Make utility functions available in templates"""
    return {
        'format_datetime': format_datetime,
        'get_time_ago': get_time_ago,
        'get_status_badge_class': get_status_badge_class,
        'get_priority_badge_class': get_priority_badge_class,
        'csrf_token': generate_csrf_token
    }

# Add security headers to all responses
@app.after_request
def apply_security_headers(response):
    """Apply security headers to all responses"""
    return SecurityHeaders.add_security_headers(response)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('errors/500.html'), 500

@app.errorhandler(403)
def forbidden(error):
    """Handle 403 errors"""
    return render_template('errors/403.html'), 403

# Initialize database on first run
def init_app():
    """Initialize application"""
    db = Database()
    
    # Check if database exists, if not create it
    if not os.path.exists(Config.DATABASE_PATH):
        print("Initializing database...")
        db.init_database()
        print("Database initialized successfully!")
    
    # Create templates/errors directory if it doesn't exist
    errors_dir = os.path.join(app.template_folder, 'errors')
    if not os.path.exists(errors_dir):
        os.makedirs(errors_dir)

if __name__ == '__main__':
    # Initialize app
    init_app()
    
    # Run application
    print("\n" + "="*50)
    print("Crime Reporting System Started!")
    print("="*50)
    print("\nDefault Admin Credentials:")
    print("Username: admin")
    print("Password: admin123")
    print("\nAccess the application at: http://127.0.0.1:5000")
    print("="*50 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)