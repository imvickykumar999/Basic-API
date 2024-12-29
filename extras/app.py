from flask import Flask, render_template_string, request, send_from_directory
import os

app = Flask(__name__)

# Folder path to list files
FOLDER_PATH = "./"  # Replace with your folder path

@app.route('/')
def list_files():
    try:
        # Get the list of files and directories in the folder
        entries = os.listdir(FOLDER_PATH)
        files_and_dirs = []
        for entry in entries:
            entry_path = os.path.join(FOLDER_PATH, entry)
            if os.path.isdir(entry_path):
                # If directory, append the directory name with a slash
                files_and_dirs.append(f"{entry}/")
            else:
                # If file, append the file name
                files_and_dirs.append(entry)
        return render_template_string(
            """<!doctype html>
            <html>
            <head>
                <title>File List</title>
                <style>
                    * {
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                    }

                    body {
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background: #f9f9f9;
                        color: #333;
                        margin: 0;
                        padding: 0;
                    }

                    .container {
                        max-width: 900px;
                        margin: 50px auto;
                        padding: 20px;
                        background: #ffffff;
                        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
                        border-radius: 10px;
                        text-align: left;
                    }

                    h1 {
                        font-size: 1.8rem;
                        margin-bottom: 20px;
                        color: #333;
                        text-align: center;
                    }

                    .file-list {
                        list-style: none;
                        padding: 0;
                    }

                    .file-list li {
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        padding: 10px 15px;
                        border-bottom: 1px solid #ddd;
                    }

                    .file-list li:last-child {
                        border-bottom: none;
                    }

                    .file-name {
                        font-size: 1rem;
                        color: #555;
                    }

                    .view-button {
                        text-decoration: none;
                        padding: 8px 15px;
                        border: 1px solid #007BFF;
                        background-color: #007BFF;
                        color: #ffffff;
                        border-radius: 5px;
                        font-size: 0.9rem;
                        font-weight: bold;
                        transition: all 0.3s ease;
                    }

                    .view-button:hover {
                        background-color: #0056b3;
                        border-color: #0056b3;
                        cursor: pointer;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Files in {{ folder_path }}</h1>
                    <ul class="file-list">
                        {% for entry in files_and_dirs %}
                            <li>
                                <span class="file-name">{{ entry }}</span>
                                {% if entry.endswith('/') %}
                                    <a href="/folder/{{ entry[:-1] }}" class="view-button">View</a>
                                {% else %}
                                    <a href="/file/{{ entry }}" class="view-button">View</a>
                                {% endif %}
                            </li>
                        {% endfor %}
                    </ul>
                </div>
            </body>
            </html>""",
            files_and_dirs=files_and_dirs, folder_path=FOLDER_PATH
        )
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/file/<path:filename>')
def serve_file(filename):
    try:
        return send_from_directory(FOLDER_PATH, filename)
    except Exception as e:
        return f"An error occurred while opening the file: {e}"

@app.route('/folder/<path:foldername>')
def list_folder_contents(foldername):
    try:
        folder_path = os.path.join(FOLDER_PATH, foldername)
        if not os.path.isdir(folder_path):
            return "Folder not found", 404
        entries = os.listdir(folder_path)
        files_and_dirs = []
        for entry in entries:
            entry_path = os.path.join(folder_path, entry)
            if os.path.isdir(entry_path):
                files_and_dirs.append(f"{entry}/")
            else:
                files_and_dirs.append(entry)
        return render_template_string(
            """<!doctype html>
            <html>
            <head>
                <title>Folder Contents</title>
                <style>
                    * {
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                    }

                    body {
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background: #f9f9f9;
                        color: #333;
                        margin: 0;
                        padding: 0;
                    }

                    .container {
                        max-width: 900px;
                        margin: 50px auto;
                        padding: 20px;
                        background: #ffffff;
                        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
                        border-radius: 10px;
                        text-align: left;
                    }

                    h1 {
                        font-size: 1.8rem;
                        margin-bottom: 20px;
                        color: #333;
                        text-align: center;
                    }

                    .file-list {
                        list-style: none;
                        padding: 0;
                    }

                    .file-list li {
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        padding: 10px 15px;
                        border-bottom: 1px solid #ddd;
                    }

                    .file-list li:last-child {
                        border-bottom: none;
                    }

                    .file-name {
                        font-size: 1rem;
                        color: #555;
                    }

                    .view-button {
                        text-decoration: none;
                        padding: 8px 15px;
                        border: 1px solid #007BFF;
                        background-color: #007BFF;
                        color: #ffffff;
                        border-radius: 5px;
                        font-size: 0.9rem;
                        font-weight: bold;
                        transition: all 0.3s ease;
                    }

                    .view-button:hover {
                        background-color: #0056b3;
                        border-color: #0056b3;
                        cursor: pointer;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Files in {{ foldername }}</h1>
                    <ul class="file-list">
                        {% for entry in files_and_dirs %}
                            <li>
                                <span class="file-name">{{ entry }}</span>
                                {% if entry.endswith('/') %}
                                    <a href="/folder/{{ foldername }}/{{ entry[:-1] }}" class="view-button">View</a>
                                {% else %}
                                    <a href="/file/{{ foldername }}/{{ entry }}" class="view-button">View</a>
                                {% endif %}
                            </li>
                        {% endfor %}
                    </ul>
                </div>
            </body>
            </html>""",
            files_and_dirs=files_and_dirs, foldername=foldername
        )
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
