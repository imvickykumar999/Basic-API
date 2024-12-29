from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Folder path to list files
FOLDER_PATH = "./"  # Replace with your folder path

@app.route('/')
def list_files():
    try:
        entries = os.listdir(FOLDER_PATH)
        files_and_dirs = []
        for entry in entries:
            entry_path = os.path.join(FOLDER_PATH, entry)
            if os.path.isdir(entry_path):
                files_and_dirs.append(f"{entry}/")
            else:
                files_and_dirs.append(entry)
        return render_template('index.html', files_and_dirs=files_and_dirs, folder_path=FOLDER_PATH)
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
        return render_template('folder_contents.html', files_and_dirs=files_and_dirs, foldername=foldername)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
