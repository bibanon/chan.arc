Supplier ID Registry
====================

Abstract
--------
This document specifies the format of a ``Supplier ID Registry``. This is required so that users of the ``chan`` URI specification know which imageboards map to which Supplier ID, so they know which archives act as a third-party backup for which resources, and to prevent name collisions in the specification.

These supplier IDs have been created due to the transient nature of image board culture, and the need to provide useful information for all sorts of suppliers on the internet.

Version Numbers
---------------
The Supplier ID Registry version number refers to the format of the supplied JSON file. The content of the registry should be assumed to be in flux, and therefore a version number on this content is not feasable.

This version number matches that of the ``chan.arc`` specification, and will be the same as the that specification.

Format
------
The Supplier ID Registry consists of a JSON file, one called ``registry.json`` and the other called ``historical.json``. ``registry.json`` provides information to allow rewriting ``chan`` URIs into valid HTTP URIs, if possible, as well as the status, existing archives, and other sorts of information about valid suppliers.

**unfinished**
