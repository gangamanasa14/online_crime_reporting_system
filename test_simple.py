"""
Simple Flask Test - Use this to verify Flask is working
If this works, then check your main app.py for issues
"""

from flask import Flask, render_template_string

app = Flask(__name__)

# Simple HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Test - Crime Reporting System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: white;
            color: #333;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        h1 { color: #667eea; }
        .success { color: #28a745; font-size: 24px; }
        .info { background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 20px 0; }
        .step { margin: 10px 0; padding: 10px; background: #e9ecef; border-radius: 5px; }
        a { color: #667eea; text-decoration: none; font-weight: bold; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Flask is Working!</h1>
        <p class="success">✓ Your Flask installation is successful</p>
        
        <div class="info">
            <h3>Next Steps:</h3>
            <div class="step">
                <strong>1.</strong> Stop this test server (Press CTRL+C in terminal)
            </div>
            <div class="step">
                <strong>2.</strong> Run the verification script:
                <code>python verify_setup.py</code>
            </div>
            <div class="step">
                <strong>3.</strong> If all checks pass, run the main application:
                <code>python app.py</code>
            </div>
            <div class="step">
                <strong>4.</strong> Open <code>http://127.0.0.1:5000</code> in your browser
            </div>
        </div>
        
        <h3>System Information:</h3>
        <ul>
            <li><strong>Flask Version:</strong> {{ flask_version }}</li>
            <li><strong>Python Version:</strong> {{ python_version }}</li>
            <li><strong>Test URL:</strong> <a href="http://127.0.0.1:5555">http://127.0.0.1:5555</a></li>
        </ul>
        
        <h3>Troubleshooting:</h3>
        <p>If you're having issues with the main app:</p>
        <ul>
            <li>Check that all files exist in correct locations</li>
            <li>Run: <code>pip install -r requirements.txt</code></li>
            <li>Run: <code>python init_db.py</code></li>
            <li>Check <code>TROUBLESHOOTING.md</code> for detailed solutions</li>
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Test route"""
    import flask
    import sys
    
    return render_template_string(
        HTML_TEMPLATE,
        flask_version=flask.__version__,
        python_version=f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    )

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Flask Test Server Starting...")
    print("=" * 60)
    print("\n✓ Flask is installed and working!")
    print("\n📱 Open your browser and go to:")
    print("   http://127.0.0.1:5555")
    print("   or")
    print("   http://localhost:5555")
    print("\n⌨️  Press CTRL+C to stop the server")
    print("\n" + "=" * 60 + "\n")
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5555)
    except OSError as e:
        if "address already in use" in str(e).lower():
            print("\n❌ Port 5555 is already in use!")
            print("Try running: python test_simple.py")
            print("Or change the port number in test_simple.py")
        else:
            print(f"\n❌ Error: {e}")
    except KeyboardInterrupt:
        print("\n\n✓ Server stopped successfully!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")