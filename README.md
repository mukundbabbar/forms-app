# forms-app

This repository is for forms-app microservice. 

## Prereq - 
Configure following environment variables

```
CALLBACK_URL

FROM_PHONE_NUMBER

TWILIO_ACCOUNT_SID

TWILIO_AUTH_TOKEN
```

## Start web app

Once env variables are configured, start the webapp using following command or use Heroku or other PaaS to deploy the app. 

`python app.py runserver`

- The application takes a phone number as the input and sends a sms to this number. 
- It checks if the number is valid

