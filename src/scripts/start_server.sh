#!/bin/bash

jupyter notebook --config='/config/jupyter_notebook_config.py' &

cd /home/hf/virt-assist/app
gunicorn --config=/config/gunicorn_config.py wsgi:flask_app
