# Marktplaats Messages python client


## Setup

```
python3 -m venv .venv
. .venv/bin/activate
pip install poetry
```

### Install dependencies

```
sudo apt-get install python3-tk
```

### Development install

```
poetry install
```


## Run

### Sniff cookies

Open https://marktplaats.nl and log in, open Developer Tools > Network tab and right-click on any request to marktplaats.nl (after you log-in), choose Save as Curl.
That will copy full request command (with cookies) to clip buffer.

Run next command to extract cookies and place them in *.env*:

```
python -m marktplaats_messages.cookie_awareness > .env
```

### No you can use client

... [TBD]