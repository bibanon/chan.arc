chan.arc File Format
====================
Imageboard thread archives come in a multitude of different formats: Plain WARC files, Fuuka database dumps, and most tools output their own unique format. This disjoined nature of the backup formats makes it difficult to transport thread dumps from one supplier to another, and even more difficult if you're looking to work with a bunch of different thread archives.

This is an attempt to standardize a file format that can be used to archive and store threads from all sorts of image boards. This should make it easier to create a tool that backs up threads, meaning we don't need to redo the same work of creating a format for our specific tool to use, and that everyone's archives can be imported and exported to a single, format.

The draft specification is available at `chan-arc-spec.rst <chan-arc-spec.rst>`_.

License
-------
The specification itself, as well as any reference code or libraries hosted here, are released into the public domain listed below::

    This is free and unencumbered software released into the public domain.

    Anyone is free to copy, modify, publish, use, compile, sell, or
    distribute this software, either in source code form or as a compiled
    binary, for any purpose, commercial or non-commercial, and by any
    means.

    In jurisdictions that recognize copyright laws, the author or authors
    of this software dedicate any and all copyright interest in the
    software to the public domain. We make this dedication for the benefit
    of the public at large and to the detriment of our heirs and
    successors. We intend this dedication to be an overt act of
    relinquishment in perpetuity of all present and future rights to this
    software under copyright law.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
    OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.

    For more information, please refer to <http://unlicense.org/>
