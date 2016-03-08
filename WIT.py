from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/whyIT/')
def why_IT():
    return render_template('article.html', title="Why IT?")


@app.route('/events/')
def events():
    return render_template('events.html', title="Events")

@app.route('/exec/')
def current_exec():
    return render_template('404.html')


@app.route('/contact/')
def contact():
    return render_template('404.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
