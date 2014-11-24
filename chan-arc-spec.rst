.chan.arc File Format
=====================

Unfinished Spec
---------------
This specification is in ``draft`` status and **is by no means final**. It is still being written and drafted. Please expect things to change, as per the Version Strings section in the ``chan.arc`` specs.

Abstract
--------
This document specifies the ``chan.arc`` file extension. This format is designed to provide a simple, standard way to represent and transport archives of imageboard threads.

This format has been created primarily for 4chan threads, but aims to cleanly store threads from other decently compatible image boards (as well as from other imageboard archives themselves).

Status of This Document
-----------------------
This is an early draft specification, and is **not yet recommended for production use**.

Because of the early nature of this draft, the version string of this specification is ``"0.1-draft"``.

Introduction
------------
Image boards have proved themselves important parts in the creation of internet culture. However, some of the primary image boards in use today have been founded on ephemerality. This leaves the job of archiving and saving content to third parties or to the users themselves.

Many completely seperate methods of archiving image board threads have been developed, from a user simply going to "Save Page" in their browser to complex scripts and programs designed for backing up content. Because each of these is independently developed, there has not been a standard way to browse or to transfer thread backups from one system to another.

With ``chan.arc``, we hope to create a standard way to store and archive image board thread content. With a standard format, we hope to be able to seamlessly transfer thread information between different archives, give tools that want to analyse and look at imageboard threads a standard format to be able to parse and look through, and give users a filetype that lets them store the thread content and the metadata surrounding it for the future!

Because of the historical importance of this data, we should have a standard format we can use and look back on in some years' time. Something that won't just be lost or unimportable if we can't setup and run the archival software anymore or if a database layout changes.

The most important thing to store, in our eyes, is the user-generated content – what the users have themselves posted inside threads. The specific stylings and layout of the specific imageboard itself are less important, which is why our standard (required) information files place more focus on the content and posts themselves than the page layout, structure, or theme/design of the specific imageboard. However, direct grabs of these files can be downloaded and stored in ``WARC`` files in the provided ``warc/`` folder.

Version Strings
---------------
Versions of the ``chan.arc`` specification are strings, specified as such in ABNF `(RFC5234) <http://www.ietf.org/rfc/rfc5234.txt>`_::

    version_string = version [ "-" status ]
    version = major "." minor
    major = NUMBER
    minor = NUMBER
    status = "draft" | "alpha" | "beta" | "pre"

    NUMBER = 1 * DIGIT

Major and Minor
^^^^^^^^^^^^^^^
The ``version`` at the front of ``version_string`` above refers to the major and minor versions of the chan-arc and Supplier ID Registry specifications.

Both specifications are based around JSON files for interchanging information, and they shall follow the constraints below:

* If keys are only added to the existing JSON information files, then the minor version number shall be incremented.

* If more major changes are made (such as new JSON information files, changing the meaning of keys, renaming or deleting keys) to either the JSON files or the file/folder layout structure of the ``chan.arc`` archive, the major number version shall be incremented.

* For the ``0.x`` versions, each minor version number should be assumed to have major changes and breakages (eg: some of the JSON keys that existed in ``0.2`` may not exist in ``0.3``. This is to be able to rapidly introduce new features and get a decent set of features worked out before a 'production' release. When this standard reaches a sufficient level of stability, the major version number will be upgraded from 0 to 1, and the rules above will apply.

The reasoning for such is this: If I have a chan.arc reader that natively supports ``"1.0"``, and it opens a file of version ``"1.2"``, it should be able to find all the keys it expects and be able to parse and read information from the new chan.arc file with relative parity compared to ones of the old ``"1.0"`` format.

Status
^^^^^^

* "draft" status means the specification is in extreme flux, and may change entirely. At this point, it is recommended to contribute and to read the specification, but not to implement code based on it.

* "alpha" and "beta" are simply various stages of development and a sign that development focus is shifting from implementing and speccing out new features to focusing on what's already made it in. One or both of these stages may be skipped if it is deemed acceptable, but it is recommended to spend at least a week at each stage if possible to allow for proper feedback. At this stage, library authors may start trying to update their implementations, but features may still change at this point.

* "pre" refers to a preliminary release of the standard. This is a (hopefully) entirely finished specification to let the library authors and other parties both prepare for the full release, and point out any bugs that have gotten overlooked or deficiencies that have yet to be corrected.

At the point of a preliminary release, library authors are recommended to try implementing the specification and to provide feedback. If enough feedback is given and it is deemed necessary, the specification may be sent back to any of the prior stages.

As an example, for version "1.2", the drafting process is expected to result in the following version strings before, during development, and for the final release::

    "1.2-draft"  ->  "1.2-alpha"  ->  "1.2-beta"  ->  "1.2-pre"  ->  "1.2"
    ->  "1.3-draft"  ->  ...

Compression
-----------
The ``.arc`` part of the standard name refers to a compression format. The two standard forms of compression used with ``.chan.arc`` are listed below:

* ``7zip``

    This format refers to 7zip, a very efficient open source compression format. Due to the high level of compression of this format, this is the recommended way to compress ``chan.arc`` archives. Archives compressed with this format shall have the file extension ``chan.7z``.

* ``zip``

    This format refers to PKZIP, the standard compression format for Windows-based systems. While this format has not proven itself the absolute best for compression's sake, there is a large ecosystem of tools and libraries already familiar with this format, and it is quite simple to decompress and extract files from this. Archives compressed with this format shall have the file extension ``chan.zip``.

Other compression formats may be used if required, but this is not recommended as most software will not be able to open them.

Folder and File Structure
-------------------------
This lays out the standard folder structure of an archived thread. The specific files and folders are described in-detail below.

This is a reference example of an archived thread::

    /thread.json
    /thumbs
        /12345.jpg
        /23456.jpg
        /spoiler-etc.jpg
        /filetype-mp3.jpg
    /files
        /12345.jpg
        /23456.gif
        /23484.webm
        /23484.mp3

    /index.html
    /template
        /template.css
        /template.js
        /template.png

    /resources
        /banner_etc.jpg
        /favicon.png
        /index.html
        /css
            /embedded_file_a.css
            /embedded_file_b.css
        /embedded_file.js
    /warc
        warc_01.warc.gz
        warc_01.cdx
    /raw
        api.json
        raw_file_a.ext
        raw_file_b.ext


thread.json
^^^^^^^^^^^
This file stores and describes the thread information including metadata, posts, files – everything we want to store. It includes a variety of details including the thread ID, sticky/locked, site banner, information about where the thread was started and where it was archived from.

This file shall be in UTF-8 encoding, with no BOM.

As this file is designed to hold human-readable information, this file should be 'pretty-printed'. That is to say, it should be formatted in a human-readable way, similar to the example shown below. While recommended, this is not required.

A typical ``thread.json`` file is laid out as such:

.. code:: json

    {
        "version": "0.1-draft",
        "software": "BASC-Archiver",
        "timestamp": 9867378547236,
        "thread": {
            "id": 1234234,
            "subject": "Thread Title",
            "sticky": false,
            "locked": false
        },
        "source": [
            {
                "site": "4chan",
                "banner": "banner_etc.jpg",
                "board": {
                    "id": "etc",
                    "name": "Cool Guys Here!"
                }
            },
            {
                "site": "archive.moe",
                "software": "FoolFuuka",
                "timestamp": 1234567890
            }
        ],
        "posts": {
            "op": {
                "post_id": 1234234,
                "timestamp": 1398264918,
                "subject": "Thread Title",
                "poster": {
                    "type": "administrator",
                    "name": "Some Guy",
                    "email": "a@example.com",
                    "tripcode": "#coolDuD3",
                    "hash": "Nbm21HN4",
                    "country": "AU"
                },
                "file": [
                    {
                        "original_name": "good-guy.webm",
                        "path": "1234234.webm",
                        "image": { "w": 0, "h": 0 },
                        "hash": "?????????????????",
                        "duration": 1232,
                        "spoiler": true,
                        "thumb_path": "spoiler-etc.jpg",
                        "thumb": { "w": 0, "h": 0 }
                    }
                ],
                "content": "Does anyone else enjoy imageboard archiving?"
            },
            "replies": [
                {
                    "post_id": 1234568,
                    "timestamp": 1398264918,
                    "poster": {
                        "name": "Anonymous",
                        "hash": "0fSGrhH4"
                    },
                    "content": "No, go away"
                },
                {
                    "post_id": 1234583,
                    "timestamp": 1398264918,
                    "poster": {
                        "name": "Anonymous",
                        "hash": "SHDGr24D"
                    },
                    "file": [
                        {
                            "original_name": "really_cool.gif",
                            "path": "1234583.gif",
                            "image": { "w": 0, "h": 0 },
                            "hash": "?????????????????",
                            "thumb_path": "1234583.jpg",
                            "thumb": { "w": 0, "h": 0 }
                        }
                    ],
                    "content": "Oh cool, another archivist!\n[green][post=1234568]>>1234568[/post] is just lame[/green]",
                    "references": [1234568]
                },
                {
                    "post_id": 1234624,
                    "poster": {
                        "name": "Anonymous",
                        "hash": "92feDBtW"
                    },
                    "file": [
                        {
                            "original_name": "cool_paper.pdf",
                            "path": "1234624.pdf",
                            "hash": "?????????????????",
                            "thumb_path": "type-pdf.jpg",
                            "thumb": { "w": 0, "h": 0 }
                        }
                    ],
                    "file": "paper.pdf",
                    "content": "Look at this cool paper on archiving!\n[green][url=chan:4chan/etc/2534321]>>>2534321[/url] is also cool![/green]",
                    "deleted": true
                },
                {
                    "post_id": 1234626,
                    "poster": {
                        "type": "moderator",
                        "name": "CoolDude",
                        "hash": "902gSgbY"
                    },
                    "content": "Yay, people are using my imageboard!"
                },
                {
                    "post_id": 142,
                    "supplier": "archive.moe",
                    "poster": {
                        "type": "ghost",
                        "name": "Anonymous",
                        "hash": "g3rTsvrS"
                    },
                    "content": "Look, I'm a ghost! Also, this is a nice old thread!"
                }
            ]
        }
    }

**version**

This key lists the version of the ``chan.arc`` format that this archive conforms to, as listed above.

**software**

This key lists the software that created this ``chan.arc`` archive. If the software has a version identifier, it is to be attached to the end of this value with a space and then the version.

**timestamp**

This is a unix timestamp representing the time of archival. This is a machine-readable representation, and is recommended to be in Coordinated Universal Time (UTC).

**thread**

This contains information about the thread. These should be generated at archive time. Subkeys may be excluded if the information does not or cannot be extracted at archive time. This key itself may be excluded if there are no subkeys.

    * ``id``

        This is the ID of the given thread.

    * ``subject``

        This contains the subject of the OP post. It is a string, containing any characters necessary.

    * ``sticky``

        This boolean represents whether the thread is a 'sticky'. That is, whether the site management has kept it stuck to the top of the image board. It may contain the values ``true`` or ``false``, and is generated at archive time.

    * ``locked``

        This boolean represents whether the thread is 'locked'. That is, whether the thread has been forced to accept no new replies. It may contain the values ``true`` or ``false``, and is generated at archive time.

**source**

This contains a list of sources where the thread has been, and has been downloaded from.

The first source will be the site the thread was created on. It lists the board the thread was created on, the thread's ID and a timestamp of it was created.

Any other sources will be other archives the thread was downloaded to and archived from. That is, archives where the thread was read from the previous source, imported into that archive's backend, and then a ``chan.arc`` file was created from that archive's backend data, rather than from the original source directly.

**Initial Source**

The initial source has the following special keys, which are not applied for later sources.

    ``board``

    This contains information about the board this thread was posted to. This should be generated at archive time.

    * ``id``

        This is the id of the current board, which is normally the "url slug" of the given board. This key must be written.

    * ``name``

        This is the long-form human-readable name of the board. On most imageboards, this is listed at the top. This key is optional, but is recommended as it can provide very valuable historical insight.

    * ``banner``

        This is the filename of an image under ``resources/``, which is the banner at the top of the page at archive time. This is shown at the top of most image boards. This key is recommended.

**Follow-on Sources**

    * ``timestamp``

    This is a unix timestamp representing the time the source archived this thread from the previous supplier. This is a machine-readable representation, and is recommended to be in Coordinated Universal Time (UTC). This key is optional, if the timestamp is not available.

**Standard Source Keys**

    * ``site``

        This is a Supplier ID, as specified in the `Supplier ID Registry <supplier-id-registry.rst>`_, representing the original source or an archive.

    * ``board``

        This represents the 'board' the thread was archived from. For instance, ``/tg/`` would be represented as ``tg``, ``/g/`` would be represented as ``g``. This is usually the url slug the board occupies. The first and last slashes are recommended to be removed from this.

        If an image board implements recursive sub-boards or other similar features, this is recommended to be represented with slashes in the board name, such as ``tch/cmp``. However, if the board does support slashes within board names, this should be represented as a list such as ``['tch/cmp', 'g']``.

        This may contain any characters necessary to represent the board, but is recommended to be lowercase letters, numbers, and dashes and underscores if required.

    * ``thread_id``

        This is the id of the thread. Generally, this is the id of the topic post (OP), or the first post of the thread. This is an integer.

    * ``software``

        This identifies the software running on each supplier. This may be the imageboard software itself, on the initial source, or software such as Fuuka or FoolFuuka on follow-on suppliers. This key is optional.


**posts**

This key represents the posts in the archived thread. We create this file because HTML formats change continuiously, and if we force future archives to read the downloaded thread HTML directly they will need to read a million different formats. It's much easier for the archival application to extract this machine-readable information at archive time, rather than putting the raw HTML file in and forcing future applications to parse it.

We try to obtain as much information as we can during archiving, because this is how the thread will be represented to future applications.

* ``op``

    This contains a post object containing information about the post that created the thread. These may be excluded if the information does not exist or cannot be extracted, but this is not recommended. The subkeys are detailed below.

* ``replies``

    This contains a list of post objects, in sequential order from the earliest reply to the latest reply, representing what was posted in the thread.

A post object can contain the following keys:

* ``poster``

    This contains information about who made the post.

    * ``name``

        This key contains the name of the poster, sans any tripcode.

    * ``email``

        This key contains what is in the ``email`` field of this post. This is a string and can contain any characters the original site supports in its name field. It is important to note that this may contain a string that is not a valid email address. This is by design, as some sites let users post with this in their email field.

        This key is optional and not required if the poster has not set an email.

    * ``type``

        This is a 'type' or a privilidge the poster has. The default allowed values for this string are as follows: ``["owner", "developer", "administrator", "moderator", "janitor", "ghost"]``.

        Owner, Admin, Mod, and Janitor are fairly self-evident, mostly coming from the 4chan moderation system. Other values can be put into this key, but they will not be understood by most software and it is recommended to try and add them to the specification as an 'official' allowed value.

        Ghost represents that the given post has been added at a later supplier, and is not part of the thread from the original supplier.

        This key is optional, if the poster has no special types to declare.

    * ``tripcode``

        This key contains what the ``tripcode`` of the topic post of the thread is displayed as. This may contain a standard tripcode or a secure tripcode, depending on what is supported by the original supplier and what the post contains. This is a string that can contain any characters necessary to represent the generated tripcode, but is expected to conform to standard tripcode formats. Leading and trailing whitespace should be stripped from this field.

        This key is optional, if the poster has no tripcode.

    * ``hash``

        This refers to imageboards that assign a specific hash-like ID to posters, usually based off their IP address or some other defining feature. This allows users to generally see who has made duplicate posts in a thread.

        This key is optional, and can contain any characters the original supplier supports.

    * ``country``

        Some imageboards allow users to declare themselves from a certain country, which puts a small flag next to their name.

* ``post_id``

    This key contains the identifier given to this post by the source image board. This may or may not be board-specific, depending on how the source imageboard specifies its post IDs.

* ``file``

    This key contains a list of files attached to this post. It is a list because some imageboards support attaching multiple files to a single post. The keys in a 'file object' are listed below:

    * ``original_name``

        This key contains the original name of the file, as reported by the imageboard. Note that the actual file itself in the ``files/`` directory should not be named this. This key is optional, if not known at archive time or if the imageboard does not support original names.

    * ``path``

        This key contains the actual path of the image file, in the ``files/`` directory.

    * ``hash``

        Some imageboards also supply a 'hash' of the file. This key is optional, and contains the hash value supplied by the imageboard if applicable.

    * ``spoiler``

        Whether this file is 'spoilered', or the real thumbnail is not displayed, in place of a generic "spoilered" thumbnail. This may contain the value ``true`` or ``false``, and is optional if the key is ``false``.

    * ``thumb_path``

        This contains the name of the thumbnail file in the ``thumbs/`` directory.

    * ``thumb``

        This contains the width and height of the thumbnail for this file.

    In addition, there are several mediatype-specific keys, as below:

    * ``image``

        This contains the width and height of the file, if it is an image file.

    * ``duration``

        This contains the duration, in seconds, of the file, if it is a music or video file. Note that this key is optional if the imageboard does not supply this information, but still recommended.

* ``supplier``

    Some imageboard archives allow posting on their archived versions of threads, after the thread has been deleted from the source imageboard. For instance, after archiving a thread on ``archive.example``, that website may allow its users to post on the threads they have archived. This is often called 'ghost mode' or names similar.

    If a post has been added on/by a provider that is not the original source of the thread, this key shall contain the ``site`` identifier of where the post originated. (Site identifiers are specified above, in the ``manifest.json`` section)

* ``content``

    This key contains the content of this post in BBCode format. This key is required.

    Inter-board and links to other imageboards' threads are very transient – most of them not having a specified lifetime. The links to other threads on the same or on different image boards shall be replaced with a ``chan:`` URI representing the same content. For instance, if a link in content originally points to ``http://boards.4chan.org/etc/thread/123234/something#263543``, it shall be replaced with the standardised ``chan://4chan/etc/123234#263543``. These are rewritten to valid URLs on creation of the ``index.html``. For exact specifications, please see the `chan URI Specification <chan-uri-spec.rst>`_.

    Because of the disjointed nature of the way imageboards implement things like greentext, spoilers, and URLs, there are some standard replacements that must be made below. This is to provide conformance between different imageboard post content.


                "content": "Look at this cool paper on archiving!\n[green][url=chan:4chan/etc/2534321]>>>2534321[/url] is also cool![/green]"

    * Italics/Bold

        These shall be replaced with the standard BBCode tags ``[i][/i]`` and ``[b][/b]``.

    * Greentext

        "Greentext", or text that is coloured green and generally starts the line with the character ``">"``, shall be represented with the BBCode tag ``[green][/green]``.

    * Spoilered Text

        Spoilered text is text whose background and foreground both appear black. When they are hovered over, the text turns lighter and shows what the message says. These spoilers can be nested. The standard tag to represent this is ``[spoiler][/spoiler]``.

    * Ban Messages

        Ban messages generally appear as all-red, bold, and sometimes in a slightly bigger font than the rest of the text. The typical message that appears as 'ban' text is as such: ``"(USER WAS BANNED FOR THIS POST)"``.

        These messages shall be inside the tag ``[banned][/banned]``.

    * Internal post links

        Links to other posts in the same thread (usually shown/performed as something like ``>>123123``) should be in the following format: ``[post=123234]>>123234[/post]``. If the link is shown as green in an unhovered state on the original website, it should be inside a ``[green]`` tag.

        The full example would be given as such: ``[green][post=123234]>>123234[/post] is cool[/green]``

    * External thread links

        Links to other threads (usually shown as something like ``>>>123123``) should be in the following format: ``[url=chan:4chan/etc/123231#123234]>>>123234[/url]``. If the link is shown as green in an unhovered state on the original website, it should be inside a ``[green]`` tag.

        The full example would be given as such: ``[green][url=chan:4chan/etc/123231#123234]>>>123234[/url] is cool[/green]``

* ``content_raw``

    This key is optional and only recommended if the post content could not be cleanly or completely translated to BBCode format as above. It contains the raw HTML content of the post, with no processing performed.

* ``references``

    This shows which other posts this post references. This is normally captured as an internal ``>>123234`` style link in the content.

files/
^^^^^^
This folder contains the original files posted in the thread (on most imageboards, these are images). This folder may be excluded, but this is not recommended as it reduces the archive's value.

Files in this folder will be named from the post ID followed by the file extension of the image, or of the form ``postid-filenumber.ext`` if there are multiple files attached to a single post, unless they are special files as described below.

If there are special post files, an example being board or imageboard-specific spoiler files that are linked in the thread, they may be named ``spoiler.ext``, ``spoiler-something.ext``, or whatever best represents the file. They must be put these in this folder if a post object in ``posts.json`` will refer to these in their ``image`` key.

Keep in mind that the files attached to posts are not restricted to image content. Some image boards let users attach files of other formats such as ``webm``, ``pdf``, ``mp3`` to their posts, and these may exist in this folder as well.

thumbs/
^^^^^^^
This folder contains the original thumbnails posted in the thread. This folder must be included if possible.

Images in this folder will be named by the post ID followed by the file extension of the image, or of the form ``postid-filenumber.ext`` if there are multiple files attached to a single post, unless they are special files as described below.

However, if there are special thumbnails, such as board or imageboard-specific spoiler thumbs that are linked in the thread, they may be named ``spoiler.ext``, ``spoiler-something.ext``, or whatever best represents the file. They must be put these in this folder if a post object in ``posts.json`` will refer to these in their ``thumb`` key.


index.html
^^^^^^^^^^
This is a purely human-readable file. It is created at archive time, and is essentially a file users can double-click on and view the thread that has been archived. This should be statically generated by the chan.arc library being used, from ``manifest.json`` and ``posts.json``, using standard templates.

If generating a html file is not possible, this may be a download of the original imageboard's html with the required file, thumbnail and resource urls changed. How ``index.html`` is generated will affect which files will be put under the ``resources/`` folder at archive time.

resources/
^^^^^^^^^^
This folder contains resources linked by the ``index.html`` file. This folder may have subdirectories. It is only recommended to create subdirectories if the created folder will have more than a single file. The recommended subdirectories include ``css``, ``js``, and ``images``. If the favicon is a single file, it should be put in the root ``resources/`` directory as shown. If there are multiple favicon files, they should be put in a ``resources/favicons/`` folder.

If the ``index.html`` file is generated by the ``chan.arc`` library, using the template in this repo's ``templates/`` folder, the resources folder inside there should be copied to here at archive time, when the ``index.html`` file is generated.

If the ``index.html`` file is a 'grab' directly from the image board with URLs replaced, the required page resources should be put inside this folder, following the above recommendations.


warc/
^^^^^
This folder is for storing files in the Web ARChive file format. These files may take any file name deemed appropriate, depending on how the archiver downloads and stores these files. Storing WARC files allow external archives such as the `Wayback Machine <http://archive.org/web/>`_ to import thread information and allow users to browse the thread exactly as it existed at archive time. Users may download and store ``.warc`` grabs of the thread HTML directly from the source, as well as other resources that are linked on that page.

raw/
^^^^
This folder is for storing files which may be of use and importance, but are not described in this specification. It is also for storing files which have been described, but are site-specific and do not have widespread enough adoption to warrant putting them in another location.

**List of files officially available under the raw/ directory**

* ``api.json`` (4chan)

Assumptions Made
----------------
Whenever creating a format like this, assumptions must be made. If these are invalidated in the future, core sections of the standard may need to be updated or reworked.

* Post IDs and Thread IDs will always be integers.

    I haven't yet seen an imageboard that uses something other than integers for post and thread IDs. I consider it a fairly core part of being an imageboard. If this is invalidated, the ``chan`` URI specification will also need to be updated
