from flask import Flask

from flask import request
from time  import sleep
from uuid import uuid4

import json
import time
import os
import sys
import requests

from config import *

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
def get_data(target_url, sw_trim=True):
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
					if sw_trim:
						trimed_job = {'title': job['title'], 'location': job['location'],
						'url': job['url'], 'date': job['date_new']}
						extract_list.append(trimed_job)
					else:
						extract_list.append(job)

		current_job_file = extract_list

	except requests.exceptions.RequestException as e:
		print(e)
		sys.exit(1)
	return extract_list

def build_posts(payload_raw):

	print("BUILD POSTS\n\n\n\n{}".format(len(payload_raw)))

	# Build post String
	posts = []
	post_string = ""
	for job in payload_raw:
		post_string = POST_TEMPLATE_P_ONE
		post_string = post_string + "{} {}\n{}".format(
			str(job["title"]), str(job["location"]), str(job["url"]))
		post_string = post_string + POST_TEMPLATE_P_ONE
		posts.append(post_string)
		post_string = ""

		print("build_posts # {}".format(len(posts)))

	return posts

	# # Format/Build LinkedIn post
	# for job_post in posts:
	# 	title="DBK JOB POSTING"
	# 	post_json = {"comment": job_post, "visibility": {"code": "anyone"} }
	# 	post_as_string = json.dumps(post_json)
	# 	# post = "{}{}{}".format("'{'comment': '", job_post, "','visibility': {'code': 'anyone'} }")

	# # response = requests.post("https://api.linkedin.com/v2/shares",data=post_data)
	# 	headers = {'x-li-format': 'json', 'Content-Type': 'application/json'}
	# 	params = {'oauth2_access_token': token}