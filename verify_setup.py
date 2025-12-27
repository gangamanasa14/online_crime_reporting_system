"""
Setup Verification Script
Run this to verify your Crime Reporting System is properly configured
"""

import sys
import os

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    if version.major >= 3 and version.minor >= 7:
        print("✓ Python version is compatible")
        return True
    else:
        print("✗ Python 3.7+ required")
        return False

def check_dependencies():
    """Check if all required packages are installed"""
    required_packages = [
        'flask',
        'flask_login',
        'werkzeug',
        'sklearn',
        'numpy',
        'pandas',
        'dotenv',
        'email_validator'
    ]
    
    print("\nChecking Dependencies:")
    print("-" * 50)
    
    all_installed = True
    for package in required_packages:
        try:
            if package == 'sklearn':
                __import__('sklearn')
            elif package == 'dotenv':
                __import__('dotenv')
            else:
                __import__(package)
            print(f"✓ {package} installed")
        except ImportError:
            print(f"✗ {package} NOT installed")
            all_installed = False
    
    return all_installed

def check_file_structure():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'config.py',
        'init_db.py',
        'requirements.txt',
        'models/__init__.py',
        'models/database.py',
        'models/predictor.py',
        'routes/__init__.py',
        'routes/auth.py',
        'routes/reports.py',
        'routes/admin.py',
        'utils/__init__.py',
        'utils/validators.py',
        'utils/security.py',
        'utils/helpers.py',
        'templates/base.html',
        'templates/index.html',
        'templates/login.html',
        'static/css/style.css',
        'static/js/main.js'
    ]
    
    print("\nChecking File Structure:")
    print("-" * 50)
    
    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} MISSING")
            all_exist = False
    
    return all_exist

def check_database():
    """Check if database exists"""
    print("\nChecking Database:")
    print("-" * 50)
    
    if os.path.exists('crime_reports.db'):
        print("✓ Database file exists")
        return True
    else:
        print("✗ Database not found - Run: python init_db.py")
        return False

def test_flask_import():
    """Test if Flask can be imported and basic app created"""
    print("\nTesting Flask:")
    print("-" * 50)
    
    try:
        from flask import Flask
        test_app = Flask(__name__)
        
        @test_app.route('/')
        def home():
            return "Test successful!"
        
        print("✓ Flask can be imported")
        print("✓ Test app created successfully")
        return True
    except Exception as e:
        print(f"✗ Flask test failed: {e}")
        return False

def main():
    """Main verification function"""
    print("=" * 50)
    print("Crime Reporting System - Setup Verification")
    print("=" * 50)
    
    results = []
    
    # Run all checks
    results.append(("Python Version", check_python_version()))
    results.append(("Dependencies", check_dependencies()))
    results.append(("File Structure", check_file_structure()))
    results.append(("Database", check_database()))
    results.append(("Flask Import", test_flask_import()))
    
    # Summary
    print("\n" + "=" * 50)
    print("VERIFICATION SUMMARY")
    print("=" * 50)
    
    all_passed = all(result[1] for result in results)
    
    for check_name, passed in results:
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{check_name}: {status}")
    
    print("=" * 50)
    
    if all_passed:
        print("\n🎉 All checks passed! Your system is ready.")
        print("\nTo start the application:")
        print("  python app.py")
        print("\nThen open in browser:")
        print("  http://127.0.0.1:5000")
    else:
        print("\n⚠️  Some checks failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("  1. Install dependencies: pip install -r requirements.txt")
        print("  2. Initialize database: python init_db.py")
        print("  3. Ensure all files are in the correct location")
    
    print("\n")

if __name__ == '__main__':
    main()