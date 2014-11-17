chan.arc File Format
====================
Imageboard thread archives come in a multitude of different formats: Plain WARC files, Fuuka database dumps, and most tools output their own unique format. This disjoined nature of the backup formats makes it difficult to transport thread dumps from one supplier to another, and even more difficult if you're looking to work with a bunch of different thread archives.

This is an attempt to standardize a file format that can be used to archive and store threads from all sorts of image boards. This should make it easier to create a tool that backs up threads, meaning we don't need to redo the same work of creating a format for our specific tool to use.

It may also become a specification for sharing threads between people. For instance, if you want to show someone a thread, you can just send them a ``.chan.arc`` of the thread and they'll have the whole thing ready to read!

The draft specification is available at `chan-arc-spec.rst <chan-arc-spec.rst>`_. **[ This specification is still in development ]**

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
