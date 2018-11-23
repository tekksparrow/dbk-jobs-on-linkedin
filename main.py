from flask import Flask, request, render_template, session
from time  import sleep
from uuid import uuid4

# import requests.auth

import os
import sys
import glob
import webbrowser
import random

from config import *
from lib import tksp_posts, tksp_oauth

app = Flask(__name__)
app.secret_key = SESSION_KEY

payload_raw       = []
payload_posts     = []

@app.route('/')
def hello_world():
	
	imgs_fn = []
	imgs_fn.append("2n9vjp")
	imgs_fn.append("2n9w1c")
	imgs_fn.append("2na0y8")

	rand_img = random.sample(imgs_fn, 1)

	img = "./static/imgs/{}.jpg".format(rand_img[0])

	return render_template('hello_world.html', hello_world=img)

@app.route('/call')
def dollar_bank_call():
	auth_callback_url = ""

	payload_raw       = tksp_posts.get_data(SRC_DATA_URL)
	print ("get data return len # = {}".format(len(payload_raw)))
	

	payload_posts     = tksp_posts.build_posts(payload_raw)
	session['payload'] = payload_posts

	#auth_callback_url = tksp_oauth.seek_permission("linkedin", CLIENT_ID)	
	if not auth_callback_url:
		auth_callback_url = "Development MODE"

	#webbrowser.open(auth_callback_url)

	return render_template('call.html', counter=len(payload_posts), auth_callback_url=auth_callback_url)

@app.route('/call_review')
def dollar_bank_callback_test():
	greeting = "Review Dashboard"
	# print all the posts
	if len(session['payload']) == 0:
		greeting = greeting + "\n\nNo IT posts found on this run."
	else:
		post_bank = session['payload']

	print("the payload\n{}".format(post_bank[0]))


	# add a button to post or reject

	return render_template('review.html', post_bank=post_bank, greeting=greeting)


































@app.route('/dbk-callback')
def dollar_bank_test():

	print("******************dollar bank call-back!!*****************")
	error = request.args.get('error', '')
	if error:
		return "Error: " + error

	print(request.args.get("code"))	

	token = get_linkedin_token(request.args.get("code"))

	# lets finally make a post
	title="This is a test!"

	post = '{"comment": "Check out developer.linkedin.com!","visibility": {"code": "anyone"} }'

	# url = "https://api.linkedin.com/v2/shares"
	# print(post['owner'])
	# url = "https://api.linkedin.com/v2/me"
	# url = "https://api.linkedin.com/v1/people/~"
	url = "https://api.linkedin.com/v1/people/~/shares?format=json"

	# response = requests.post("https://api.linkedin.com/v2/shares",data=post_data)
	headers = {'x-li-format': 'json', 'Content-Type': 'application/json'}
	params = {'oauth2_access_token': token}
	# response = requests.request("POST", url, data=None, params=params, headers=headers, timeout=60)

	print(link_state)
	# response = requests.request("POST", url, data=post, params=params, headers=headers, timeout=60)
	
	return response.text

def get_linkedin_token(code):

	print("CI AND CS -------------------------------- {}{}".format(CLIENT_ID, CLIENT_SECRET))

	client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

	post_data = {"grant_type": "authorization_code",
				 "code": code,
				 "redirect_uri": REDIRECT_URI,
				 "client_id": CLIENT_ID,
				 "client_secret": CLIENT_SECRET}

	response = requests.post("https://www.linkedin.com/oauth/v2/accessToken",
							 data=post_data,
							 headers={"Content-Type": "application/x-www-form-urlencoded"})

	print(response.text)
	return response.json()["access_token"]