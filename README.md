# Dollar Bank Jobs on LinkedIn
Automated Post Generator which collects, organizes, generates and shares Dollar Bank Job Openings on your personal LinkedIn feed.

# Program Description and Summary
As of 08/31/2018 job listings at Dollar Bank are available as a json file at [https://dollarbankcareers.jobs/feed/json](https://dollarbankcareers.jobs/feed/json). This program downloads this listing and extracts all IT related jobs. With abbreviated list, the data is organized into strings which will act as posts when they are shared to LinkedIn. After making a connection to LinkedIn and passing OAuth2 the program will make at least X posts in X intervals. Post limits and interval values as a precaution, more research is needed to verify what kind of limitations the LinkedIn API has for numbner of calls and their frequency.

# Installation
As of 08/31/2018 this project is still under development. This section will be fillout once there is a stable release.

# Schedule - Development Plan
1.  ~~YOLO code - proof of concept.~~
2. __Compartmentalize.__

    Additional Features

    * Add URL encoding (config redirect url -> main.py)
    * Add cli script that clean copies(no sensitive data) copy of the prod config file into main dir.
3. Screen cast development tutorial.
4. Add run in background feature (scheduled runs)
5. Implemnt database and code previous job list checking.
5. Add mobile app remote feature (run command from mobile device)

Thanks for looking. Feel free to comment, flame, or contribute.

[Bio/Resume/CV Website](http://tekksparrow.info)
