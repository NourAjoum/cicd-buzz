import os
from flask import Flask

# Initialiseer de Flask-applicatie
app = Flask(__name__)

# Standaard route
@app.route('/')
def home():
    return "Hello from Render! Your Flask app is running successfully."

# Zorg ervoor dat de applicatie luistert op de juiste poort
if __name__ == "__main__":
    # Render gebruikt de omgevingsvariabele 'PORT', standaard naar 5000
    port = int(os.environ.get('PORT', 5000))
    # De host is ingesteld op '0.0.0.0' zodat het extern toegankelijk is
    app.run(host='0.0.0.0', port=port)
