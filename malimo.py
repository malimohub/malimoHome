import os 
from flask import Flask, render_template
import json 
import requests 

app = Flask(__name__)

@app.route('/')
def get_malimo_home():

	workFilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/media/work_experience.json') 
	with open(workFilePath, 'r') as work_file:
		content = work_file.read()
		workData = json.loads(content)
		work_file.close()

	return render_template('home.html', work_data=workData) 

if __name__ == '__main__':
    app.run(debug=True)

