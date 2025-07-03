from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    df = pd.read_excel('books.xlsx')
    results = df.to_dict(orient='records')
    
    query = request.form.get('query')
    if query:
        results = [book for book in results if query.lower() in book['Title'].lower()]
    
    return render_template('index.html', books=results)

if __name__ == '__main__':
    app.run(debug=True)
