from flask import Flask, render_template, redirect, url_for
import subprocess
import os
import sys

if sys.platform == 'win32':
    subprocess.CREATE_NEW_CONSOLE = 0x00000010

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/canvas')
def canvas():
    return render_template('canvas.html')

@app.route('/launch-canvas', methods=['POST'])
def launch_canvas():
    script_path = os.path.join(os.getcwd(), 'canvas_app.py')
    subprocess.Popen(['start', 'cmd', '/k', f'python "{script_path}"'], shell=True)
    return redirect(url_for('canvas'))

if __name__ == '__main__':
    app.run(debug=True)
