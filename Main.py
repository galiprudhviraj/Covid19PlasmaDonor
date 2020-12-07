from flask import Flask, render_template, request, redirect, url_for, session
import boto3
import re
from email.message import EmailMessage
import smtplib


app = Flask(__name__)

app.secret_key = 'welcome'

dynamodb = boto3.resource('dynamodb',  endpoint_url = "http://dynamodb.us-east-2.amazonaws.com", region_name='us-east-2')

@app.route('/plasma/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', msg='')

@app.route('/Login/', methods=['GET', 'POST'])
def Login():
   return render_template('Login.html', msg='')

@app.route('/Signup/', methods=['GET', 'POST'])
def Signup():
    return render_template('Signup.html', msg='')

@app.route('/LoginAction/', methods=['GET', 'POST'])
def LoginAction():
    status = 'none'
    if request.method == 'POST' and 't1' in request.form and 't2' in request.form:
        uname = request.form['t1']
        password = request.form['t2']
        table = dynamodb.Table('Users')
        table_response = table.scan()
        data = table_response['Items']
        for i in range(len(data)):
            un = ''
            pa = ''
            for k,v in data[i].items():
                if k == 'username':
                    un = v
