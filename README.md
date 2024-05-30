# Web Status Scraper

This is a site status scraper: it sends requests to sites and checks their status code.

- 200: site is up.
- 400: site is down.
- 300: waits until it gets a 200/400. If it gets a 200 then checks the html image's and looks for an alt property with an 'error' code.

If there are any down sites, it sends an email with the list.

## Run

```
# to start virtual environment
$ python3 -m venv myenv
$ source myenv/bin/activate
$ python3 main.py
# to exit environment:
$ deactivate
```
