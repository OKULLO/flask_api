from app import app

@app.route('/')
def index():
  return 'index page running'

@app.route('/about')
def about():
  return 'about page running'