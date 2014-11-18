chan URI Specification
======================

Abstract
--------
This document specifies the ``chan`` URI. This URI is designed to provide a simple, standard way to represent different imageboards, and represent the boards and threads on them.

This URI has been created due to the transient nature of image board culture, and the existence of multiple 'failover' archives from where backup information can be found. The transience of both image boards and of the HTTP URIs used to identify them – as well as the changes often found in imageboard's URL paths – require the creation of their own URI.

URI Scheme Syntax
-----------------
The syntax of ``chan`` URIs are detailed below in ABNF `(RFC5234) <http://www.ietf.org/rfc/rfc5234.txt>`_::

    uri = "chan:" supplier_ids "/" board_names "/" thread_idd [ "?" query ] [ "#" post_id ]

    supplier_ids = supplier_id * [ "-" supplier_id]
    supplier_id = 1 * SAFE_CHARS

    board_names = board_name * [ "-" board_name ]
    board_name = 1 * ALPHA_LOWER | DIGIT | ENCODED_CHAR

    query = qu * [ ";" qu ]
    qu = key [ "=" value ]
    key = ALPHA_LOWER
    value = SAFE_CHARS

    thread_ids = thread_id * [ "-" thread_id ]
    thread_id = 1 * DIGIT
    post_id = 1 * DIGIT

    SAFE_CHARS = ALPHA_LOWER | DIGIT | "."
    ENCODED_CHAR = "%" 1 * HEXDIG ";"
        ; encoded to represent characters we cannot represent in the given character range
        ; this is the UTF-8 hex value of the given character
    ALPHA_LOWER = %x61-7a

Examples::
    
    chan:4chan/etc/1234123#1234345
    chan:8chan/etc/7654345?ts=1396310400#7654567

Supplier ID
^^^^^^^^^^^
Supplier IDs must be defined in the Supplier ID Registry below. Otherwise, there is no way to know where the thread actually came from, and what supplier is being referred to.

The first supplier id (and usually the only id present) is the source of the thread. This should be a proper imageboard (such as ``4chan``), rather than an archiver. Other supplier IDs are archives that have grabbed the thread from the previous supplier and uploaded it onto their own website.

Standard Query Keys
^^^^^^^^^^^^^^^^^^^
There are several standard query keys, as specified below

* ``ts``

    ``ts`` is short for "timestamp", and refers to a unix timestamp referring to when the thread was available/active. This is not necessary on all thread links, but some imageboards have post numbers that can be reset.

    Eg: Post ``134`` might mean a specific post one day, and a few weeks later the board's post numbers have been reset or the board has been deleted and recreated, and post ``134`` for that same supplier and specific board now points towards a different post.

    Whether this key should be attached is detailed in the Supplier ID Registry as described below. By default, queried archives should return the first thread in their archives with that thread ID. If the ``ts`` key exists, however, they should return the thread that existed closest to that timestamp.

Board Names
^^^^^^^^^^^
This is fairly standard. In almost all cases, there will only be a single board name. However, the option for multiple board names exists if, for instance, a thread was moved from its original board by the administration of the original supplier.

Note that this refers to the boards the thread was on at the __original__ supplier. This is where the thread originated. The board names of later archives and suppliers are disregarded (I have yet to see a third-party supplier try to move threads into their own special board names anyway. Every single one I've seen just leaves it as-is).

Thread ID
^^^^^^^^^
This is the ID the source supplier used to identify the thread. For every image board I've seen, this is the ID of the originating post of the thread, though this is not a hard constraint.

The possibility for multiple thread IDs is linked to the multiple board names above. It is designed to handle the contingency of a thread that has been moved to a new board by the administration, and on the new board the thread's ID has changed from its original one.

Multiple thread IDs should not be required, but it is impossible to tell when/if someone will write a nonstandard imageboard implementation that does these things, so we have it here just in case.

Post ID
^^^^^^^
This is the ID of a specific post within the thread. When viewing a thread and this exists, the viewing application should 'snap' down to the given post. Examples of this occur on most image boards, and is where the inspiration for this URI section came from.
