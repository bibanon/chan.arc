chan URI Specification
======================

Abstract
--------
This document specifies the ``chan`` URI. This URI is designed to provide a simple, standard way to represent different imageboards, and the boards and threads on them.

This URI has been created due to the transient nature of image board culture, and the existence of multiple 'failover' archives from where backup information can be found. The transience of both image boards and of the HTTP URIs used to identify them – as well as the changes often found in imageboard's URL paths – require the creation of their own URI.

URI Scheme Syntax
-----------------
The syntax of ``chan`` URIs are detailed below in ABNF `(RFC5234) <http://www.ietf.org/rfc/rfc5234.txt>`_::

    uri = "chan://" imageboard_id "/" board_names "/" thread_id [ "?" query ] [ "#" post_id ]

    imageboard_id = 1 * SAFE_CHARS

    board_names = board_name * [ "-" board_name ]
    board_name = 1 * ALPHA_LOWER | DIGIT | ENCODED_CHAR

    query = qu * [ ";" qu ]
    qu = key [ "=" value ]
    key = ALPHA_LOWER
    value = SAFE_CHARS

    thread_id = 1 * DIGIT
    post_id = 1 * DIGIT

    SAFE_CHARS = ALPHA_LOWER | DIGIT | "."
    ENCODED_CHAR = "%" 1 * HEXDIG ";"
        ; encoded to represent characters we cannot represent in the given character range
        ; this is the UTF-8 hex value of the given character
    ALPHA_LOWER = %x61-7a

Examples::
    
    chan://4chan/etc/1234123#1234345
    chan://8chan/etc/7654345?ts=1396310400#7654567

Standard Query Keys
^^^^^^^^^^^^^^^^^^^
There are several standard query keys, as specified below

* ``ts``

    ``ts`` is short for "timestamp", and refers to a unix timestamp referring to when the thread was available/active. This is not necessary on all thread links, but some imageboards have post numbers that can be reset.

    Eg: Post ``134`` might mean a specific post one day, and a few weeks later the board's post numbers have been reset or the board has been deleted and recreated, and post ``134`` for that same supplier and specific board now points towards a different post.

    Whether this key should be attached is detailed in the Imageboard ID Registry as described below. By default, queried archives should return the first thread in their archives with that thread ID. If the ``ts`` key exists, however, they should return the thread that existed closest to that timestamp.

Imageboard ID Registry
----------------------
A registry of Imageboard IDs (used in the URI as above) is to be maintained, both to prevent collisions in the namespace and to be able to provide useful information for applications implementing and using the ``chan`` URI (particularly the ``chan.arc`` specification).

** unfinished **
