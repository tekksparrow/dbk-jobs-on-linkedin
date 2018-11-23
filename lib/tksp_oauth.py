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

import requests

import json
import time

# Function: Used to obtain OAuth2 premission from user.
#
# Args:
# str_host_site: String of the host site, keep all lower case. ex: "linkedin"
# CLIENT_ID    : String of the CLIENT_ID provided by the host site. This is stored in the config file
def seek_permission(str_host_site, CLIENT_ID):

	# Authroization
	#
	# Step 1: Determine which host site the program needs to seek permission
	# Step 2: Else/If statement will build the necessary request link - must be a better way to do this?
	# Step 3: Redirect user with authorization url, which will allow them to grant access to the program.
	link_base = HOST_SITE_AUTH_URL[str_host_site]
	if (str_host_site = "linkedin"):

		link_response_code = "response_type=code"
		link_redirect_url = "redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fcall_review"

		#learn how to incorperate a state variable to prevent cross srf attacks
		#link_state = CSFR_SECRET

		link_scope = "r_fullprofile%20w_share"
		get_auth_url = "{}{}&client_id={}&{}&{}".format(link_base, link_response_code, CLIENT_ID, 
		link_redirect_url, link_scope)


	webbrowser.open(get_auth_url)
	return "You are being redirected to : " + get_auth_url

# @app.route('/dbk-callback')
# def dollar_bank_test():

# 	print("******************dollar bank call-back!!*****************")
# 	error = request.args.get('error', '')
# 	if error:
# 		return "Error: " + error

# 	print(request.args.get("code"))

# 	token = get_linkedin_token(request.args.get("code"))
# 	# url = "https://api.linkedin.com/v2/shares"
# 	# print(post['owner'])
# 	# url = "https://api.linkedin.com/v2/me"
# 	# url = "https://api.linkedin.com/v1/people/~"
# 	url = "https://api.linkedin.com/v1/people/~/shares?format=json"

# 	# lets finally make a post
# 	for job_post in posts:
# 		title="DBK JOB POSTING"
# 		post_json = {"comment": job_post, "visibility": {"code": "anyone"} }
# 		post_as_string = json.dumps(post_json)
# 		# post = "{}{}{}".format("'{'comment': '", job_post, "','visibility': {'code': 'anyone'} }")

# 	# response = requests.post("https://api.linkedin.com/v2/shares",data=post_data)
# 		headers = {'x-li-format': 'json', 'Content-Type': 'application/json'}
# 		params = {'oauth2_access_token': token}
# 		response = requests.request("POST", url, data=post_as_string, params=params, headers=headers, timeout=60)
		
	
# 	return response.text

# def get_linkedin_token(code):

# 	print("CI AND CS -------------------------------- {}{}".format(CLIENT_ID, CLIENT_SECRET))

# 	client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

# 	post_data = {"grant_type": "authorization_code",
# 				 "code": code,
# 				 "redirect_uri": REDIRECT_URI,
# 				 "client_id": CLIENT_ID,
# 				 "client_secret": CLIENT_SECRET}

# 	response = requests.post("https://www.linkedin.com/oauth/v2/accessToken",
# 							 data=post_data,
# 							 headers={"Content-Type": "application/x-www-form-urlencoded"})

# 	print(response.text)
# 	return response.json()["access_token"]
# =======
# 		post_string = ""
# >>>>>>> 93b9b89ab762647361309de61ecc0f84ef4acb00:dbk_tools/dbk_posts.py