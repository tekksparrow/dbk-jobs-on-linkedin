
from flask import Flask

from flask import request
from time  import sleep
from uuid import uuid4

import requests
import requests.auth
import json
import time
import os
import sys
import webbrowser

from config import *

app = Flask(__name__)
posts = []

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/dbk')
def dollar_bank_call():

	# if token empty do the first part else make some posts

	print("********************dollar bank call********************")

	# get dollar bank job listing json, and extract IT jobs
	# 
	# notes: to ensure the title keys were matching with whole words only
	#        the job["title"] is split on white space and only then is the
	#        "in" operator performed on the list.
	try:
		r = requests.get(url="https://dollarbankcareers.jobs/feed/json")
		extract_job_file = r.json()
		extract_list = []

		for job in extract_job_file:
			for title_key in JOB_TITLE_KEYS:
				split_title = job["title"].upper().split()
				if title_key in split_title:
					extract_list.append(job)

		current_job_file = extract_list
		print(type(extract_list))

	except requests.exceptions.RequestException as e:
		print(e)
		sys.exit(1)

	# build string for current job file name
	localtime = time.localtime(time.time())

	   # this code keeps file names to a fix length convention
	if localtime.tm_mon < 10:
		fn_month = "{}{}".format("0", localtime.tm_mon)
	else:
		fn_month = localtime.tm_mon

	if localtime.tm_mday < 10:
		fn_day = "{}{}".format("0", localtime.tm_mday)
	else:
		fn_day = localtime.tm_mday

	if localtime.tm_sec < 10:
		fn_sec = "{}{}".format("0", localtime.tm_sec)
	else:
		fn_sec = localtime.tm_sec

	incoming_job_file_string = "dbk-jobfile-{}{}{}{}".format(
		fn_month,
		fn_day,
		localtime.tm_year,
		fn_sec)

	# write new (current run) job list (json) to file using file name string
	with open("./previous-job-files/{}.json".format(incoming_job_file_string), "w") as outfile:
		json.dump(current_job_file, outfile, indent=4)

	# build post strings
	counter = 1

	post_string = ""
	for job in current_job_file:
		post_string = POST_TEMPLATE_P_ONE
		post_string = post_string + str(job["title"]) + " " + str(job["location"]) + 
		              "\n" + str(job["url"])
		post_string = post_string + POST_TEMPLATE_P_ONE
		print (str(counter))
		counter += 1
		print (post_string)
		posts.append(post_string)
		post_string = ""

	# authroization
	link_base = "https://www.linkedin.com/oauth/v2/authorization?"
	link_response_code = "response_type=code"
	link_redirect_url = "redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fdbk-callback"

	# 	# create state variable to prevent cross srf attacks
	# state = str(uuid4())
	# save_created_state(state)

	link_state = CSFR_SECRET
	link_scope = "r_fullprofile%20w_share"
	get_auth_url = "{}{}&client_id={}&{}&{}&{}".format(link_base, link_response_code, CLIENT_ID, 
		link_redirect_url, link_state, link_scope)

	webbrowser.open(get_auth_url)
	return "hello_world"

@app.route('/dbk-callback')
def dollar_bank_test():

	print("******************dollar bank call-back!!*****************")
	error = request.args.get('error', '')
	if error:
		return "Error: " + error

	print(request.args.get("code"))

	token = get_linkedin_token(request.args.get("code"))
	# url = "https://api.linkedin.com/v2/shares"
	# print(post['owner'])
	# url = "https://api.linkedin.com/v2/me"
	# url = "https://api.linkedin.com/v1/people/~"
	url = "https://api.linkedin.com/v1/people/~/shares?format=json"

	# lets finally make a post
	for job_post in posts:
		title="DBK JOB POSTING"
		post_json = {"comment": job_post, "visibility": {"code": "anyone"} }
		post_as_string = json.dumps(post_json)
		# post = "{}{}{}".format("'{'comment': '", job_post, "','visibility': {'code': 'anyone'} }")

	# response = requests.post("https://api.linkedin.com/v2/shares",data=post_data)
		headers = {'x-li-format': 'json', 'Content-Type': 'application/json'}
		params = {'oauth2_access_token': token}
		response = requests.request("POST", url, data=post_as_string, params=params, headers=headers, timeout=60)
		
	
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



import requests
r = requests.get(url="https://dollarbankcareers.jobs/feed/json")
extract_job_file = r.json()
extract_list = []

for job in extract_job_file:
	for title_key in JOB_TITLE_KEYS:
		split_title = job["title"].upper().split()
		if title_key in split_title:
			extract_list.append(job)

current_job_file = extract_list
print(type(extract_list))