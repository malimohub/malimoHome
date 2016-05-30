import os 
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message as MailMessage
import json 
import requests 

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def get_malimo_home():

	workFilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/media/work_experience.json') 
	with open(workFilePath, 'r') as work_file:
		content = work_file.read()
		workData = json.loads(content)
		work_file.close()

	return render_template('index.html', work_data=workData) 



@app.route('/sendMessage', methods=['POST']) 
def messenger():
	inquirerName = request.form['name']
	inquirerEmail = request.form['email']
	inquirerMessage = request.form['message']
	msg = MailMessage(inquirerMessage,
              	sender=inquirerEmail,
		recipients=["malcolmian.monroe@gmail.com"])
	mail.send(msg)
	return redirect(url_for('get_malimo_home'))



if __name__ == '__main__':
    app.run(debug=True)

