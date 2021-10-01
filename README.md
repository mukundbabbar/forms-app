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

Open app url in browser

<img width="346" alt="Screen Shot 2021-10-01 at 8 44 43 PM" src="https://user-images.githubusercontent.com/5012739/135607597-42020886-587d-439d-9da0-bb11ede2428c.png">



- The application takes a phone number as the input and sends a sms to this number. 
- It checks if the number is valid

Invalid phone number

<img width="350" alt="Screen Shot 2021-10-01 at 8 44 28 PM" src="https://user-images.githubusercontent.com/5012739/135607814-9123d255-2386-4434-82a4-30d9f8cf0e62.png">


SMS Sent succesfully 

<img width="395" alt="Screen Shot 2021-10-01 at 8 44 55 PM" src="https://user-images.githubusercontent.com/5012739/135607562-787c754d-bc68-4d2b-bd48-d6665246a49f.png">
