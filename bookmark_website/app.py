from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Path to commit-ready exported bookmarks
BOOKMARK_FOLDER = os.path.join(os.getcwd(), 'commit-export+')

# Function to read bookmarks from a JSON file
def load_bookmarks(filename):
    path = os.path.join(BOOKMARK_FOLDER, filename)
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Chrome bookmarks are nested; we need "roots" -> "bookmark_bar" -> "children"
    try:
        children = data['roots']['bookmark_bar']['children']
    except KeyError:
        children = []
    bookmarks = []
    for item in children:
        if item.get('type') == 'url':
            bookmarks.append({
                'name': item['name'],
                'url': item['url']
            })
    return bookmarks

@app.route('/')
def index():
    # Load all bookmark profiles
    chrome = load_bookmarks('chrome.json')
    chrome_canary = load_bookmarks('chrome_canary.json')
    profile_chrome = load_bookmarks('profile-chrome.json')
    profile_canary = load_bookmarks('profile-canary.json')
    return render_template('index.html', 
                           bookmarks_rows=[chrome, chrome_canary, profile_chrome, profile_canary])

if __name__ == '__main__':
    app.run(debug=True)
