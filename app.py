from flask import Flask, request, render_template, redirect, session 
from sqlalchemy import create_engine, text

app = Flask(__name__)
app.secret_key = "something-very-secret"

engine = create_engine(
        "mysql+pymysql://root:tsDnHFAhmftFWhJFZFMeMwDkazULlMTQ@shortline.proxy.rlwy.net:55403/railway?charset=utf8mb4"
    )


@app.route('/', methods=['GET', 'POST'])
def homepage():
        return render_template('home.html')


@app.route('/login/<subject>', methods=['GET', 'POST'])
def login(subject):
            if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']

                with engine.connect() as conn:
                    result = conn.execute(
                        text(f"SELECT * FROM {subject} WHERE us = :u AND ps = :p"),
                        {'u': username, 'p': password}
                    )
                    user = result.fetchone()

                if user:
                    session['username'] = username
                    return render_template(f"{subject}.html")
                else:
                    return 'Invalid login'

            return render_template('login1.html', subject=subject)


@app.route('/eco.html', methods=['GET', 'POST'])
def eco():
        return render_template('eco.html')

@app.route('/bcom.html', methods=['GET', 'POST'])
def bcom():
        return render_template('bcom.html')
@app.route('/phy.html', methods=['GET', 'POST'])
def bba():
        return render_template('phy.html')
@app.route('/pol.html', methods=['GET', 'POST'])
def pol():
        return render_template('pol.html')

@app.route('/mat.html', methods=['GET', 'POST'])
def bms():
        return render_template('mat.html')
@app.route('/timewaste.html', methods=['GET', 'POST'])
def tmw():
        return render_template('timewaste.html')

@app.route('/syllabus.html', methods=['GET', 'POST'])
def syl():
        return render_template('syllabus.html')

@app.route('/soon.html', methods=['GET', 'POST'])
def soon():
        return render_template('soon.html')

if __name__ == "__main__":
        app.run(debug=True, host="0.0.0.0", port=5000)
        # app.run(debug=True)
