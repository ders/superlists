Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

e.g., on Ubuntu:

    $ sudo apt-get install nginx git python3 python3-pip
    $ sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g. superlists-staging

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, e.g. superlists-staging

## Folder structure:
Assume we have a user account at /home/ubuntu

/home/ubuntu
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv
