# Alexa Skill API with MySQL DB in Docker
A dockerized Alexa Skill API using flask-ask with a MySQL database. This is a clean base template.


## Requirements
- amazon developer account (see https://developer.amazon.com/)
- noip Account (see https://www.noip.com/)

## Requirements on host system
- docker
- docker-compose
- openssl


## Usage

### Deploying the API

1. Create a NoIP Hostname on https://www.noip.com/ *(e.g. myapi.ddns.net)*
2. Navigate to the **api folder** of the repository
3. Create a self signed certificate (you may also see https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https)
```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```
4. Please fill the following prompts along your circumstances:
- Country Name (2 letter code) [AU]: DE
- State or Province Name (full name) [Some-State]: Saarland
- Locality Name (eg, city) []: Saarbrücken
- Organization Name (eg, company) [Internet Widgits Pty Ltd]: My ASK Business
- Organizational Unit Name (eg, section) []:
- Common Name (e.g. server FQDN or YOUR name) []: myapi.ddns.net *(**NoIP hostname** belongs here)*
- Email Address []:

5. Navigate back to the repository **root** and execute:
```
docker-compose up
```

### Deploying the Alexa Skill
1. Enter the amazon developer console
2. Create a new alexa skill
3. Enter the **skill name** (this is only the display name on your amazon developer console)
4. Choose a **default language** (this will be the language in which you communicate with alexa)
5. Choose a *model to add to your skill*: **Custom**
6. Choose a *method to host your skill's backend resources*: **Provision your own**
7. Select **Create Skill** (button)
8. Choose a *template*: **Strat From Scratch**
9. Select **Choose** (button)
10. Navigate to **JSON Editor**, delete the whole code and copy the following code:
```json
{
    "interactionModel": {
        "languageModel": {
            "invocationName": "<here comes your invocation name>",
            "intents": [
                {
                    "name": "AMAZON.FallbackIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.CancelIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.HelpIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.StopIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.NavigateHomeIntent",
                    "samples": []
                },
                {
                    "name": "YesIntent",
                    "slots": [],
                    "samples": [
                        "natürlich",
                        "ja"
                    ]
                },
                {
                    "name": "AnswerIntent",
                    "slots": [
                        {
                            "name": "first",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "second",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "third",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "{first} {second} and {third}",
                        "{first} {second} {third}"
                    ]
                }
            ],
            "types": []
        }
    }
}
```
11. Do not forget to change the **invocationName** in the JSON code (this will be the name to call your skill on alexa)
12. Select **Save Model** (button)
13. Navigate to **Endpoit**
14. For *Service Endpoint Type* check **HTTPS**
15. As *Default Region* enter your **NoIP hostname** (here: myapi.ddns.net)
16. For the *SSL certificate type* choose: *I will upload a **self-signed** certificate in X 509 fomat
17. Select **Save Endpoint** (button)
18. Select *Click here to upload your certificate* and provide the **cert.pem** in the api folder
19. Select **Save Endpoint** (button)
20. Navigate to **Invocation**
21. Select **Build Model**

### Testing Alexa Skill
1. Navigate to **Test** in your amazon developer console
2. Set *Skill testing is enable in* to *Developmet*
3. Hold the mic button and start talknig to Alexa!

## Database
When cloning this repo, the database will load a static table from the **db/init folder** of the repository.

**Warning**: At that time the database is **not** persistent. Every change to the database will be lost on container restart!

### Persistent database
After the first container start, copy the mysql data to localhost as follows:

1. Get the database container id using
```
docker ps
```
2. Navigate to the **repository root**
3. Copy mysql folder (unfortunately it is not possible to specify folder/* to copy all files from a folder):
```
docker cp r CONTAINER_ID:/var/lib/mysql db
```
4. Move files from within mysql into storage and remove the mysql folder:
```
mv -r db/mysql/* db/storage/ && rm -r mysql
```
5. Edit **docker-compose.yml**
6. Disable
```
  - ./db/init:/docker-entrypoint-initdb.d
  - /var/lib/mysql
```
7. Enable
```
  - ./db/storage:/var/lib/mysql:rw
```
8. **Save** the file and **restart** the containers

## Credits

https://developer.amazon.com/de/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask:-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development

https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https

https://github.com/johnwheeler/flask-ask
