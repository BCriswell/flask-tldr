===============================
Flask TLDR
===============================

A demo flask app that transforms a full-length article into a short, accurate summary... a TL;DR verssion.


Quickstart
----------

First, set your app's secret key as an environment variable. For example, example add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export TLDR_SECRET='something-really-secret'


Then run the following commands to bootstrap your environment.


::

    git clone https://github.com/bcriswell/tldr
    cd tldr
    pip install -r requirements/dev.txt
    python manage.py server

You should see a mostly blank home page. After generating some summaries, you will see them listed here.

Once you have installed your DBMS, run the following to create your app's database tables and perform the initial migration:

::

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py server



Deployment
----------

In your production environment, make sure the ``TLDR_ENV`` environment variable is set to ``"prod"``.


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``db``, and the ``User`` model.


Running Tests
-------------

To run all tests, run ::

    python manage.py test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands:
::

    python manage.py db migrate

This will generate a new migration script. Then run:
::

    python manage.py db upgrade

To apply the migration.

For a full migration command reference, run ``python manage.py db --help``.
