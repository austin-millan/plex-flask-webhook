# plex-flask-webhook

An example Plex webhook.

To get started:

```bash
git clone https://github.com/austin-millan/plex-flask-webhook.git
```

Copy the `.env-example` file to `.env`, and then update it to match your environment.

## Run Locally

```bash
pip3 install flask
pip3 install plexapi
pip3 install pylogrus
python3 plex_webhook/plex_webhook.py
```

## Run With Docker

```bash
./build.sh
./run.sh
```