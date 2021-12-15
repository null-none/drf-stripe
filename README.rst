======================
drf-stripe
======================

Django REST Framework wrapper of the payments Django app for Stripe

Install
======================
* pip install drf-stripe
* Add 'payments' to INSTALLED_APPS
* Add to urls.py: ``url(r"^api/stripe/", include("payments.api.urls"))``

Endpoints
======================
* current-user/ (GET)
* subscription/ (GET/POST)
* change-card/  (GET/POST)
* charges/      (GET)
* invoices/     (GET)
* plans/        (GET)
* events/       (GET)
* webhook/      (POST)
* cancel/       (POST)
