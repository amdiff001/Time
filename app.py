from flask import Flask 
import time

app = Flask(__name__)

@app.route('/')
def index():
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    return f"Поточний час: {curr_time}"
