# About

sipwping-django is a Django based web frontend for [SIPwPing server](https://github.com/saghul/SIPwPing-server) 
It allows users to query the availability of a SIP endpoint from a simple web form.


# Installation (for local development)

Assuming you already have SIPwPing server up and running (and listening on local port 8889) this is what needs to be done:

    git clone http://github.com/saghul/sipwping-django
    cd sipwping-django
    mkdirtualenv --no-site-packages sipwping-django
    pip install -r requirements.txt

I assume you are using virtualenv + virtualenvwrapper. If you are not, you should.


# Configuration

The only thing that needs to be configured is the URL for the *SIPwPing server*. This can be done by setting 
the `SIPWPING_SERVER_URL` variable in the settings.py file:

    SIPWPING_SERVER_URL = 'http://127.0.0.1:8889/options'


# Like it?

Cool, thanks!


# Hate it?

Sorry, this is my first Django project :-) Fork it, improve it, send a pull request!


# License

See LICENSE file.


# Author

saghul - saghul @ gmail . com


