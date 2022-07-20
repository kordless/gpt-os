# Mitta OS
Mitta OS creates an "operating system" for AI agents to crawl, index and search documents or URLs for use in interactive chats.

The infrastructred required to run this may be deployed onto Google Cloud. Scripts for server deployment may be reconfigured easily to run elsewhere.

The system uses OpenAI's GPT-3 language model and Google's Vision APIs. If you want to run other models, please consider contributing to this project.

Use is provided via Slack and API calls.

# Deploy a Grub Box on Google Cloud
Grub is a crawler, which outputs screenshots that can be passed to image models for text and object extraction purposes.

## Running Grub
Start by checking this repo out on your Google Cloud Shell terminal:

```
$ git clone https://github.com/kordless/mitta-os
```

### Create a secrets.sh file

```
$ vi secrets.sh
TOKEN=f00bar
:x
```


### Deploy
Deploy a Grub instance on Google cloud:

```
$ ./deploy-grub.sh
Password token is: f00bar
```

Instance will be running in 2.5 minutes, listening on port 8983.

Calls may be made to the Grub instance with the token: 

```
example
```

