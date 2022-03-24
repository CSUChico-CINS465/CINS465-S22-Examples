#!/bin/bash

pylint --load-plugins pylint_django --disable=imported-auth-user --disable=django-not-configured --disable=missing-docstring ./mysite/mysite
pylint --load-plugins pylint_django --disable=imported-auth-user --disable=django-not-configured --disable=missing-docstring ./mysite/myapp