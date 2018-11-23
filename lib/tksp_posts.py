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

from config import *

import requests

import json
import time

# Function: Used to obtain raw job post data from source url. This version parses .json object into a
#           list of "jobs".
#
#			Step  1: Download .json data file and parse.
#			Step  2: Filter file on job title and append to list.
#
# Args:
# target_url : String of URL location of json data set.
# job_titles : List of Strings representing job titles to filter upon.
def get_data(target_url, job_titles):
	# STEP 1
	try:
		r = requests.get(url=target_url)
		extract_job_file = r.json()
		extract_list = []
	#STEP 2
		for job in extract_job_file:
			for title_key in JOB_TITLE_KEYS:
				split_title = job["title"].upper().split()
				if title_key in split_title:
					extract_list.append(job)

		current_job_file = extract_list

	except requests.exceptions.RequestException as e:
		print(e)
		sys.exit(1)

def build_posts(payload_raw):

	# Build post String
	post_string = ""
	for job in payload_raw:
		post_string = POST_TEMPLATE_P_ONE
		post_string = post_string + str(job["title"]) + " " + str(job["location"]) + 
		              "\n" + str(job["url"])
		post_string = post_string + POST_TEMPLATE_P_ONE
		posts.append(post_string)
		post_string = ""

	# # Format/Build LinkedIn post
	# for job_post in posts:
	# 	title="DBK JOB POSTING"
	# 	post_json = {"comment": job_post, "visibility": {"code": "anyone"} }
	# 	post_as_string = json.dumps(post_json)
	# 	# post = "{}{}{}".format("'{'comment': '", job_post, "','visibility': {'code': 'anyone'} }")

	# # response = requests.post("https://api.linkedin.com/v2/shares",data=post_data)
	# 	headers = {'x-li-format': 'json', 'Content-Type': 'application/json'}
	# 	params = {'oauth2_access_token': token}