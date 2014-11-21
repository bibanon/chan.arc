``chan.arc`` File Format and ``chan`` URI
=========================================
Imageboard thread archives come in a multitude of different formats: Plain WARC files, Fuuka database dumps, and most tools output their own unique format. This disjoined nature of the backup formats makes it difficult to transport thread dumps from one supplier to another, and even more difficult if you're looking to work with a bunch of different thread archives.

This is an attempt to standardize a file format that can be used to archive and store threads from image boards. This should make it easier to create tools that create, import, export, and analyse thread archives.

Why a new standard?
-------------------
So we can all be talking the same language!

For example, most of the archives created by tools on users' computers end up unused (and relatively not too useful) beyond that user's hard drive because they can't go anywhere. Sure, you can post them on your website, throw them up on Github Pages or on somewhere like `Archive.org <https://archive.org/>`_, but they can't be imported into the other major thread archive sites. They also miss out on some useful information since their primary focus is just getting it to display when you double-click the HTML file.

If we have a standard format that can usefully define all this for us, we should be able to seamlessly transfer thread information between different archives, give tools that want to analyse and look at imageboard threads a standard format to be able to parse and look through, and give users a format that lets them store the thread content, as well as all the metadata surrounding it for the future!

This project has grown into several related specifications, which are required due to the nature of imageboard archiving. These are listed below:

* ``chan.arc`` Draft Specification: `chan-arc-spec.rst <chan-arc-spec.rst>`_
* ``chan`` URI Specification: `chan-uri-spec.rst <chan-uri-spec.rst>`_
* Supplier ID Registry Specification: `supplier-id-registry.rst <supplier-id-registry.rst>`_

**These specifications are still in heavy development, and we do not recommend using this yet**

**However, we would love to talk with any interested parties about these developments**

Contact
-------
If you want talk with us, our primary IRC channel is ``#bibanon`` on `Rizon.net <http://www.rizon.net/chat>`_, and ``danneh_`` is the primary author. He can also be reached `via email <mailto:daniel@danieloaks.net>`_.

Come and say hello, we're always interested in talking to other people about this spec. After all, that's how we find all of the current problems and create a good and useful standard for everyone!

License
-------
The specification itself, as well as any reference code or libraries hosted here, are released under the WTFPL::

               DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                       Version 2, December 2004

    Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

    Everyone is permitted to copy and distribute verbatim or modified
    copies of this license document, and changing it is allowed as long
    as the name is changed.

               DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
      TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

     0. You just DO WHAT THE FUCK YOU WANT TO.

Seriously, rip out parts of the spec and create something else, take the reference code and embed it directly in your application. Do whatever.

A link back to this project would be appreciated, but is not required.
