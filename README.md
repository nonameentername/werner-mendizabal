Werner Mendizabal
=================

License
-------

All artwork is licensed under [CC BY-NC](cc-by-nc.md)

Requirements
------------

Uses Python Version 3.9.18

Install
-------

pip install -r requirements.txt

Run
----

Run local dev instance:

    PELICAN_DEV=true make html && make serve

Deploy
------

Publish to github:

    make html && make github
