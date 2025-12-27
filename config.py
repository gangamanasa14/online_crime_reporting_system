"""
Configuration settings for the Crime Reporting System
"""
import os
from datetime import timedelta

class Config:
    """Base configuration class"""
    
    # Secret key for session management (change in production)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database configuration
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'crime_reports.db')
    
    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)
    SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Security settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Pagination
    REPORTS_PER_PAGE = 10
    
    # Crime categories
    CRIME_CATEGORIES = [
        'Theft',
        'Assault',
        'Burglary',
        'Vandalism',
        'Robbery',
        'Fraud',
        'Cybercrime',
        'Drug Offense',
        'Domestic Violence',
        'Vehicle Theft',
        'Other'
    ]
    
    # Priority levels
    PRIORITY_LEVELS = ['Low', 'Medium', 'High', 'Critical']
    
    # Status options
    STATUS_OPTIONS = ['Pending', 'Under Investigation', 'Resolved', 'Closed']