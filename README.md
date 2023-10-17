# Marktplaats Messages python client


## Setup

```
python3 -m venv .venv
. .venv/bin/activate
pip install poetry
```

### Development install

```
poetry install
```


## Run

### Authentication

For now the only supported way is to steal cookies from the browser session. Find assistance from [header-hunter](https://github.com/aleksandr-vin/header-hunter).

Open https://marktplaats.nl and log in, open Developer Tools > Network tab and right-click on any request to marktplaats.nl (after you log-in), choose Save as Curl.
That will copy full request command (with cookies) to clip buffer.

Run next command to extract cookies and place them in *.env*:

```
header-hunter > .env
```

### No you can use client

... [TBD]