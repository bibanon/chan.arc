Supplier ID Registry
====================

Unfinished Spec
^^^^^^^^^^^^^^^
This specification is in ``draft`` status and **is by no means final**. It is still being written and drafted. Please expect things to change, as per the Version Strings section in the ``chan.arc`` specs.

Abstract
--------
This document specifies the format of a ``Supplier ID Registry``. This is required so that users of the ``chan`` URI specification know which imageboards map to which Supplier ID, so they know which archives act as a third-party backup for which resources, and to prevent name collisions in the specification.

These supplier IDs have been created due to the transient nature of image board culture, and the need to provide useful information for all sorts of suppliers on the internet.

Format
------
The Supplier ID Registry consists of JSON file, one called ``registry.json`` and the other called ``historical.json``. ``registry.json`` provides information to allow rewriting ``chan`` URIs into valid HTTP URIs, if possible. It also provides the status of suppliers, existing archives, and other sorts of information to make it easy for applications using ``chan.arc`` and the various standards around that format.

Version Numbers
---------------
The Supplier ID Registry version number refers to the format of the supplied JSON file. The content of the registry should be assumed to be in flux, and a version number referring to the actual content of the registry is not possible. For this purpose, please see the ``"last_updated"`` key.

The Supplier ID Registry version numbers match that of the ``chan.arc`` specification. They will be updated with that specification and keps in sync. For instance, version ``"2.3"`` of ``chan.arc`` will interact with and use version ``"2.3"`` Supplier ID Registry files.

Location
--------
Right now, Supplier ID Registry files are expected to be stored in the current location::

    http://chanarc.org/registry/<version>/registry.json
    http://chanarc.org/registry/<version>/historical.json

For instance, if a user wished to pull down the current registry in ``"1.2"`` format, they would go to::

    http://chanarc.org/registry/1.2/registry.json

As a special case, draft, alpha, beta and preliminary standard files will be removed shortly after the release of the final standard. For instance, if the user is testing ``chan.arc`` version ``1.4-pre``, they may access data files at the given address::

    http://chanarc.org/registry/1.4-pre/registry.json

However, this address is expected to be unavailable shortly after the release of the full ``1.4`` specification.

Trying to retrieve files that are unavailable should return a 404 response, in which case the application may try incrementing the minor version number of the standard and try again (As releases with incremented minor numbers mean that keys have only been added, and and removed or changed significantly).

We reserve the right to change the domain name here (``chanarc.org``) in the future, should it be required.

``registry.json`` Format
------------------------
This file aims to provide as much useful information as possible to help when users of the ``chan.arc`` specification, the ``chan`` URI, and hopefully other people who use imageboards.

First, an registry.json file with several example suppliers:

.. code:: json

    {
        "version": "0.1-draft",
        "suppliers": {
            "4chan": {

            },
            "archive.moe": {

            }
        }
    }
