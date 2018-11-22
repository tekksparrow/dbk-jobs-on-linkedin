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

	# Authroization
	#
	# Step 1: Determine which host site the program needs to seek permission
	# Step 2: Else/If statement will build the necessary request link - must be a better way to do this?
	# Step 3: Redirect user with authorization url, which will allow them to grant access to the program.
	link_base = HOST_SITE_AUTH_URL[str_host_site]
