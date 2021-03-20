Minimal Flask demo for debugging
================================

Installation
------------

.. code-block:: bash

    git clone https://github.com/starzel/flask.git
    cd flask
    python -m venv .
    pip install -r requirements


Run application
---------------

.. code-block:: bash

    env FLASK_APP=demo.py flask run


Run in debug-mode

.. code-block:: bash

    env FLASK_APP=demo.py FLASK_ENV=development flask run

Open in http://localhost:5000
