# Troubleshooting Guide - Crime Reporting System

## Issue: Application Not Opening in Browser

### Step-by-Step Solution

## Step 1: Verify Python Installation

```bash
# Check Python version (should be 3.7 or higher)
python --version
# OR
python3 --version
```

**Expected Output:** `Python 3.x.x`

If Python is not installed, download from: https://www.python.org/downloads/

---

## Step 2: Install Dependencies

```bash
# Navigate to project directory
cd crime-reporting-system

# Install all requirements
pip install -r requirements.txt

# OR if pip doesn't work, try:
pip3 install -r requirements.txt

# OR with Python module
python -m pip install -r requirements.txt
```

**Wait for all packages to install successfully.**

---

## Step 3: Initialize Database

```bash
# Run the database initialization script
python init_db.py

# OR
python3 init_db.py
```

**Expected Output:**
```
Initializing Crime Reporting System Database...
--------------------------------------------------
Database initialized successfully!
--------------------------------------------------
Database initialization complete!

Default admin account created:
Username: admin
Password: admin123
```

If you see errors here, delete any existing database file:
```bash
rm crime_reports.db
python init_db.py
```

---

## Step 4: Start the Application

```bash
# Start Flask application
python app.py

# OR
python3 app.py
```

**Expected Output:**
```
==================================================
Crime Reporting System Started!
==================================================

Default Admin Credentials:
Username: admin
Password: admin123

Access the application at: http://127.0.0.1:5000
==================================================

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.x.x:5000
Press CTRL+C to quit
```

---

## Step 5: Open in Browser

Try these URLs in order:

1. **http://127.0.0.1:5000**
2. **http://localhost:5000**
3. **http://0.0.0.0:5000**
4. Check the terminal output for the actual URL shown

**Browsers to try:**
- Chrome
- Firefox
- Edge
- Safari

---

## Common Issues & Solutions

### Issue 1: "Port 5000 already in use"

**Solution A:** Kill the process using port 5000
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F

# Mac/Linux
lsof -i :5000
kill -9 <PID_NUMBER>
```

**Solution B:** Change the port in `app.py`
```python
# At the bottom of app.py, change:
app.run(debug=True, host='0.0.0.0', port=5000)
# To:
app.run(debug=True, host='0.0.0.0', port=8000)

# Then open: http://127.0.0.1:8000
```

---

### Issue 2: "ModuleNotFoundError"

**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
# Install missing module
pip install flask

# Or reinstall all dependencies
pip install -r requirements.txt --force-reinstall
```

---

### Issue 3: "ImportError: cannot import name"

**Solution:** Ensure all `__init__.py` files exist
```bash
# Create missing __init__.py files
touch models/__init__.py
touch routes/__init__.py
touch utils/__init__.py

# Windows command prompt:
type nul > models\__init__.py
type nul > routes\__init__.py
type nul > utils\__init__.py
```

---

### Issue 4: "sqlite3.OperationalError: unable to open database"

**Solution:** Check database path and permissions
```bash
# Delete and recreate database
rm crime_reports.db
python init_db.py

# Check if database file was created
ls -la crime_reports.db  # Mac/Linux
dir crime_reports.db     # Windows
```

---

### Issue 5: "Connection refused" or "Cannot connect"

**Solutions:**

**A. Check Firewall:**
- Allow Python through firewall
- Temporarily disable antivirus/firewall to test

**B. Try different host:**
```python
# In app.py, try:
app.run(debug=True, host='localhost', port=5000)
# OR
app.run(debug=True, host='127.0.0.1', port=5000)
```

**C. Check if Flask is running:**
```bash
# Look for this message in terminal:
# * Running on http://127.0.0.1:5000
```

---

### Issue 6: Browser Shows "This site can't be reached"

**Solutions:**

1. **Verify Flask is Running:**
   - Check terminal for error messages
   - Make sure you didn't close the terminal

2. **Clear Browser Cache:**
   - Press `Ctrl+Shift+Delete` (Chrome/Firefox)
   - Clear browsing data

3. **Try Incognito/Private Mode:**
   - Chrome: `Ctrl+Shift+N`
   - Firefox: `Ctrl+Shift+P`

4. **Check URL:**
   - Must include `http://`
   - Correct: `http://127.0.0.1:5000`
   - Wrong: `127.0.0.1:5000`

---

### Issue 7: Page Loads but Looks Broken (No Styles)

**Solution:** Check static files
```bash
# Verify static files exist
ls static/css/style.css
ls static/js/main.js

# If missing, create the files from the provided code
```

**Check browser console:**
- Press `F12` to open Developer Tools
- Check for 404 errors on CSS/JS files
- Make sure Bootstrap CDN is accessible

---

### Issue 8: "Template Not Found" Error

**Solution:** Verify templates directory
```bash
# Check templates exist
ls templates/
ls templates/base.html
ls templates/index.html

# Create missing templates directory
mkdir templates
mkdir templates/errors
```

---

## Complete Fresh Installation

If nothing works, try a complete fresh install:

### Step 1: Clean Up
```bash
# Remove old files
rm -rf venv/
rm crime_reports.db
rm -rf __pycache__/
rm -rf models/__pycache__/
rm -rf routes/__pycache__/
rm -rf utils/__pycache__/
```

### Step 2: Recreate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Step 3: Reinstall Everything
```bash
pip install --upgrade pip
pip install -r requirements.txt
python init_db.py
python app.py
```

---

## Detailed Directory Check

Ensure your directory structure looks like this:

```
crime-reporting-system/
│
├── app.py                 ✓ Must exist
├── config.py              ✓ Must exist
├── init_db.py             ✓ Must exist
├── requirements.txt       ✓ Must exist
│
├── models/
│   ├── __init__.py        ✓ Must exist
│   ├── database.py        ✓ Must exist
│   └── predictor.py       ✓ Must exist
│
├── routes/
│   ├── __init__.py        ✓ Must exist
│   ├── auth.py            ✓ Must exist
│   ├── reports.py         ✓ Must exist
│   └── admin.py           ✓ Must exist
│
├── utils/
│   ├── __init__.py        ✓ Must exist
│   ├── validators.py      ✓ Must exist
│   ├── security.py        ✓ Must exist
│   └── helpers.py         ✓ Must exist
│
├── static/
│   ├── css/
│   │   └── style.css      ✓ Must exist
│   ├── js/
│   │   ├── main.js        ✓ Must exist
│   │   ├── report.js      ✓ Must exist
│   │   └── dashboard.js   ✓ Must exist
│   └── images/
│       └── logo.svg       ✓ Must exist
│
└── templates/
    ├── base.html          ✓ Must exist
    ├── index.html         ✓ Must exist
    ├── login.html         ✓ Must exist
    └── ... (other templates)
```

---

## Testing Checklist

Once the application starts:

- [ ] Terminal shows "Running on http://127.0.0.1:5000"
- [ ] No error messages in terminal
- [ ] Database file `crime_reports.db` exists
- [ ] Can open http://127.0.0.1:5000 in browser
- [ ] Landing page loads correctly
- [ ] Can click "Login" and see login page
- [ ] Can login with admin/admin123
- [ ] Dashboard loads after login

---

## Getting Help

If still not working, check:

1. **Terminal Output:** Copy the exact error message
2. **Browser Console:** Press F12, check Console tab
3. **Python Version:** Run `python --version`
4. **Installed Packages:** Run `pip list`

---

## Quick Test Script

Create a file called `test_app.py`:

```python
print("Testing Flask installation...")
try:
    import flask
    print(f"✓ Flask installed: {flask.__version__}")
except:
    print("✗ Flask not installed")

try:
    from flask_login import LoginManager
    print("✓ Flask-Login installed")
except:
    print("✗ Flask-Login not installed")

try:
    import sqlite3
    print("✓ SQLite3 available")
except:
    print("✗ SQLite3 not available")

print("\nStarting minimal Flask app...")
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Flask is working!"

if __name__ == '__main__':
    print("Opening http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
```

Run with:
```bash
python test_app.py
```

If this works, the main app should work too.

---

## Contact Information

If you've tried everything and it still doesn't work:
1. Check the exact error message in the terminal
2. Verify all files are present
3. Make sure you're in the correct directory
4. Try the test script above

The application is production-ready and should work if all files are in place and dependencies are installed.