from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Path ke file CSV
CSV_FILE = 'data/engagement_data.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    likes = int(request.form['likes'])
    comments = int(request.form['comments'])
    shares = int(request.form['shares'])
    followers = int(request.form['followers'])

    # Menghitung engagement rate
    engagement_rate = ((likes + comments + shares) / followers) * 100

    # Menyimpan data ke CSV
    data = {
        'Likes': likes,
        'Comments': comments,
        'Shares': shares,
        'Followers': followers,
        'Engagement Rate': engagement_rate
    }
    df = pd.DataFrame([data])
    
    # Jika file CSV sudah ada, tambahkan data baru
    if os.path.exists(CSV_FILE):
        df.to_csv(CSV_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(CSV_FILE, index=False)

    return render_template('result.html', engagement_rate=engagement_rate)

if __name__ == '__main__':
    app.run(debug=True)