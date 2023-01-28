# __Introduction__

This readme file will guide you through the process of deploying a social media bot on OpenShift, a free and open-source platform as a service provided by Red Hat. The bot will automatically take images and videos from a list of subreddits that it randomly picks and post them on a Twitter account with the same title of the video/image it got from the subreddit. It will run every day at 1am, 10am, 10pm, and 1pm, and will pick only one subreddit from the list, once a subreddit has been picked, it will not pick it again that day.

## __Prerequisites__

Before you begin, make sure you have:

• An OpenShift account
• Python 3.6 or later installed on your local machine
• A Twitter account and developer account, with the appropriate API keys and tokens
• A Reddit account and developer account, with the appropriate API keys and tokens

# __Setting up the Environment__

1) Create a new project in OpenShift by logging into the OpenShift web console and clicking on the "Create Project" button.

2) Create a new Python 3.6 or later application by selecting the appropriate template in the "Add to Project" section.

3) Add the necessary environment variables to the application by navigating to the "Environment" tab and clicking on the "Edit" button. Add the following environment variables:

•REDDIT_CLIENT_ID
•REDDIT_CLIENT_SECRET
•REDDIT_USER_AGENT
•TWITTER_CONSUMER_KEY
•TWITTER_CONSUMER_SECRET
•TWITTER_ACCESS_TOKEN
•TWITTER_ACCESS_TOKEN_SECRET

4) Create a new file named ".env" in the root of your project and add the environment variables created in step 3.

# __Deploying the Application__

1) Clone the repository to your local machine using git.
`bash`
`git clone https://github.com/<mannysoye>/<TheCloudFeed>.git`

2) Change into the project directory.
`bash`
```cd <the-repository>```

3) Create a new file named "requirements.txt" in the root of your project and add the following dependencies:
```
tweepy
praw
python-dotenv
```

4) Use the OpenShift command-line interface (CLI) to deploy the application.
`css`
```oc new-app --name <your-application-name> --image-stream <your-image-stream> --env-file .env```

5) Expose the application to the internet by creating a route.
`php`
```oc expose service <your-application-name>```

6) Finally, create a new cron job in OpenShift that will run the run_bot() function in the bot.py script every day at 1am, 10am, 10pm, and 1pm.
`bash`
``` oc create-cron-job <your-cron-job-name> --image <your-image> --schedule "0 1,10,22 * * *" --command "python bot.py"```


# __Conclusion__

You have successfully deployed a social media bot on OpenShift. The bot will now automatically take images and videos from a list of subreddits and post them on a Twitter account at the specified times.

If you have any problems creating a Openshift project, look for a tutorial on how to do so. Just look at the OpenShift docs too,  https://www.openshift.com/.
