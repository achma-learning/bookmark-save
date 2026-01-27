from flask import Flask, render_template
import json
import os

app = Flask(__name__)

BOOKMARK_FOLDER = os.path.join(os.getcwd(), 'commit-export+')

# Recursive function to parse bookmarks and preserve folders
def parse_bookmarks(bookmark_node):
    result = []
    if bookmark_node.get('type') == 'folder':
        folder = {
            'name': bookmark_node.get('name', 'Folder'),
            'children': [parse_bookmarks(child) for child in bookmark_node.get('children', [])]
        }
        result.append(folder)
    elif bookmark_node.get('type') == 'url':
        result.append({
            'name': bookmark_node.get('name', 'Unnamed'),
            'url': bookmark_node.get('url')
        })
    return result if len(result) > 1 else result[0]  # flatten single-element folders

def load_bookmarks(filename):
    path = os.path.join(BOOKMARK_FOLDER, filename)
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    children = data.get('roots', {}).get('bookmark_bar', {}).get('children', [])
    bookmarks = []
    for child in children:
        bookmarks.append(parse_bookmarks(child))
    return bookmarks

@app.route('/')
def index():
    # Automatically load all JSON files in commit-export+
    bookmark_files = [f for f in os.listdir(BOOKMARK_FOLDER) if f.endswith('.json')]
    all_bookmarks = {}
    for file in bookmark_files:
        profile_name = file.replace('.json', '')
        all_bookmarks[profile_name] = load_bookmarks(file)
    return render_template('index.html', all_bookmarks=all_bookmarks)

if __name__ == '__main__':
    app.run(debug=True)
