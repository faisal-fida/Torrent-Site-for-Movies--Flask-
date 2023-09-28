from flask import Flask, render_template, request
import logging

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
   
    logging.info(request.form)

if __name__ == '__main__':
    app.run(debug=True)