from app import app

# routes are defined here

@app.route('/')
def root():
    return "Hello, World!"
