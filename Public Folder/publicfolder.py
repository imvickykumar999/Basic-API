from flask import Flask, render_template_string, send_from_directory, url_for
import os

app = Flask(__name__)

# Folder path to list files
FOLDER_PATH = "./Server"  # Replace with your folder path


@app.route('/')
def list_files():
    try:
        # Get the list of files and directories in the folder
        entries = os.listdir(FOLDER_PATH)
        directories = []
        files = []
        for entry in entries:
            entry_path = os.path.join(FOLDER_PATH, entry)
            if os.path.isdir(entry_path):
                directories.append(f"{entry}/")
            else:
                files.append(entry)

        directories.sort(key=lambda x: x.lower())
        files.sort(key=lambda x: x.lower())

        files_and_dirs = directories + files

        return render_template_string(
            """<!doctype html>
            <html>
            <head>
                <title>{{ title }}</title>
                <style>
                    body {
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background: #f9f9f9;
                        color: #333;
                    }

                    .container {
                        max-width: 900px;
                        margin: 50px auto;
                        padding: 20px;
                        background: #ffffff;
                        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
                        border-radius: 10px;
                    }

                    h1 {
                        text-align: center;
                        font-size: 1.8rem;
                    }

                    .breadcrumb {
                        font-size: 0.9rem;
                        margin-bottom: 20px;
                        text-align: center;
                    }

                    .breadcrumb a {
                        color: #007BFF;
                        text-decoration: none;
                    }

                    .breadcrumb a:hover {
                        text-decoration: underline;
                    }

                    .file-list {
                        list-style: none;
                        padding: 0;
                    }

                    .file-list li {
                        display: flex;
                        justify-content: space-between;
                        padding: 10px;
                        border-bottom: 1px solid #ddd;
                    }

                    .file-name {
                        font-size: 1rem;
                    }

                    .folder-name {
                        color: blue;
                        font-weight: bold;
                    }

                    .open-button, .view-button {
                        text-decoration: none;
                        padding: 8px 15px;
                        border-radius: 5px;
                        font-size: 0.9rem;
                        color: white;
                        transition: all 0.3s ease;
                    }

                    .open-button {
                        background-color: #28a745;
                        border: 1px solid #28a745;
                    }

                    .open-button:hover {
                        background-color: #1e7e34;
                    }

                    .view-button {
                        background-color: #007BFF;
                        border: 1px solid #007BFF;
                    }

                    .view-button:hover {
                        background-color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>{{ title }}</h1>
                    <div class="breadcrumb">
                        <a href="{{ url_for('list_files') }}">Home</a>
                    </div>
                    <ul class="file-list">
                        {% for entry in files_and_dirs %}
                            <li>
                                <span class="file-name {% if entry.endswith('/') %}folder-name{% endif %}">{{ entry }}</span>
                                {% if entry.endswith('/') %}
                                    <a href="{{ url_for('list_folder_contents', foldername=entry[:-1]) }}" class="open-button">Open</a>
                                {% else %}
                                    <a href="{{ url_for('serve_file', filename=entry) }}" class="view-button">View</a>
                                {% endif %}
                            </li>
                        {% endfor %}
                    </ul>
                </div>
            </body>
            </html>""",
            title="Home",
            files_and_dirs=files_and_dirs,
        )
    except Exception as e:
        return f"An error occurred: {e}"


@app.route('/file/<path:filename>')
def serve_file(filename):
    try:
        requested_file = os.path.join(FOLDER_PATH, filename)
        if not os.path.isfile(requested_file):
            return "File not found", 404
        return send_from_directory(FOLDER_PATH, filename)
    except Exception as e:
        return f"An error occurred: {e}"


@app.route('/folder/<path:foldername>')
def list_folder_contents(foldername):
    try:
        requested_path = os.path.join(FOLDER_PATH, foldername)
        if not os.path.isdir(requested_path):
            return "Folder not found", 404

        entries = os.listdir(requested_path)
        directories = []
        files = []
        for entry in entries:
            entry_path = os.path.join(requested_path, entry)
            if os.path.isdir(entry_path):
                directories.append(f"{entry}/")
            else:
                files.append(entry)

        directories.sort(key=lambda x: x.lower())
        files.sort(key=lambda x: x.lower())

        files_and_dirs = directories + files

        breadcrumb = [{"name": "Home", "url": url_for('list_files')}]
        path_parts = foldername.split('/')
        for i, part in enumerate(path_parts):
            breadcrumb.append({
                "name": part,
                "url": url_for('list_folder_contents', foldername="/".join(path_parts[:i+1]))
            })

        return render_template_string(
            """<!doctype html>
            <html>
            <head>
                <title>{{ title }}</title>
                <style>
                    body {
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background: #f9f9f9;
                        color: #333;
                    }

                    .container {
                        max-width: 900px;
                        margin: 50px auto;
                        padding: 20px;
                        background: #ffffff;
                        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
                        border-radius: 10px;
                    }

                    h1 {
                        text-align: center;
                        font-size: 1.8rem;
                    }

                    .breadcrumb {
                        font-size: 0.9rem;
                        margin-bottom: 20px;
                        text-align: center;
                    }

                    .breadcrumb a {
                        color: #007BFF;
                        text-decoration: none;
                    }

                    .breadcrumb a:hover {
                        text-decoration: underline;
                    }

                    .file-list {
                        list-style: none;
                        padding: 0;
                    }

                    .file-list li {
                        display: flex;
                        justify-content: space-between;
                        padding: 10px;
                        border-bottom: 1px solid #ddd;
                    }

                    .file-name {
                        font-size: 1rem;
                    }

                    .folder-name {
                        color: blue;
                        font-weight: bold;
                    }

                    .open-button, .view-button {
                        text-decoration: none;
                        padding: 8px 15px;
                        border-radius: 5px;
                        font-size: 0.9rem;
                        color: white;
                        transition: all 0.3s ease;
                    }

                    .open-button {
                        background-color: #28a745;
                        border: 1px solid #28a745;
                    }

                    .open-button:hover {
                        background-color: #1e7e34;
                    }

                    .view-button {
                        background-color: #007BFF;
                        border: 1px solid #007BFF;
                    }

                    .view-button:hover {
                        background-color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>{{ title }}</h1>
                    <div class="breadcrumb">
                        {% for crumb in breadcrumb %}
                            <a href="{{ crumb.url }}">{{ crumb.name }}</a>
                            {% if not loop.last %} &gt; {% endif %}
                        {% endfor %}
                    </div>
                    <ul class="file-list">
                        {% for entry in files_and_dirs %}
                            <li>
                                <span class="file-name {% if entry.endswith('/') %}folder-name{% endif %}">{{ entry }}</span>
                                {% if entry.endswith('/') %}
                                    <a href="{{ url_for('list_folder_contents', foldername=current_path + '/' + entry[:-1]) }}" class="open-button">Open</a>
                                {% else %}
                                    <a href="{{ url_for('serve_file', filename=current_path + '/' + entry) }}" class="view-button">View</a>
                                {% endif %}
                            </li>
                        {% endfor %}
                    </ul>
                </div>
            </body>
            </html>""",
            title=f"Files in {foldername}",
            files_and_dirs=files_and_dirs,
            breadcrumb=breadcrumb,
            current_path=foldername
        )
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

