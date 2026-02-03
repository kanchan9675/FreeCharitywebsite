from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/causes.html')
def causes():
    return render_template('causes.html')

@app.route('/event.html')
def event():
    return render_template('event.html')

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

@app.route('/single.html')
def single():
    return render_template('single.html')

@app.route('/service.html')
def service():
    return render_template('service.html')

@app.route('/team.html')
def team():
    return render_template('team.html')

@app.route('/donate.html')
def donate():
    return render_template('donate.html')

@app.route('/volunteer.html')
def volunteer():
    return render_template('volunteer.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
