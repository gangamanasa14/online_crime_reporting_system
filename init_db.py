"""
Database Initialization Script
Run this script to initialize or reset the database
"""
from models.database import Database

def main():
    """Initialize the database"""
    print("Initializing Crime Reporting System Database...")
    print("-" * 50)
    
    db = Database()
    db.init_database()
    
    print("-" * 50)
    print("Database initialization complete!")
    print("\nDefault admin account created:")
    print("Username: admin")
    print("Password: admin123")
    print("\nPlease change the default password after first login!")

if __name__ == '__main__':
    main()
    