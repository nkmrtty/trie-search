trie-search
===========

Trie-search is a package for text pattern search using
`marisa-trie <https://github.com/pytries/marisa-trie>`__.

Installation
------------

::

    $ pip install trie-search

Usage
-----

Create trie dictionary
~~~~~~~~~~~~~~~~~~~~~~

Before using this package, you need to create trie dictionary, or
prepare a list of patterns.

The following example simply creates trie dictionary of
``marisa_trie.Trie`` from list of article titles in English version of
Wikipedia, and saves it to ``./example/triedict``.

::

    $ cd ./example
    $ curl https://dumps.wikimedia.org/jawiki/20170101/enwiki-20170101-all-titles-in-ns0.gz | gzcat | python create_triedict.py

**NOTICE** : This script will consume more than 2GB memory.

trie\_search.TrieSearch
~~~~~~~~~~~~~~~~~~~~~~~

Create an instance, and load dictionary:

.. code:: python

    >>> import trie_search
    >>> trie = trie_search.TrieSearch(filepath='./example/triedict')

If you have ``list`` or ``tuple`` object of patterns, you can create an
instance as follows:

.. code:: python

    >>> patterns = [u'pattern1', u'pattern2', u'pattern3']
    >>> trie = trie_search.TrieSearch(patterns)

TrieSearch.search\_all\_patterns
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Search all patterns in an input text:

.. code:: python

    >>> text = (u'in computer science , a trie , also called digital tree and '
    ...         u'sometimes radix tree or prefix tree ( as they can be searched '
    ...         u'by prefixes ) , is a kind of search tree - an ordered tree data '
    ...         u'structure that is used to store a dynamic set or associative array '
    ...         u'where the keys are usually strings .')
    >>> for pattern, start_idx in trie.search_all_patterns(text):
    ...     print pattern, start_idx
    ...
    in 0
    computer 3
    computer science 3
    science 12
    , 20
    a 22
    trie 24
    , 29
    also 31
    called 36
    digital 43
    ... skipped ...
    array 246
    where 252
    where the 252
    the 258
    the keys 258
    keys 262
    are 267
    usually 271
    strings 279 

-  The text is the 1st sentence of https://en.wikipedia.org/wiki/Trie.
   For normalization, remove capitalizations and add single white space
   before/after symbols.
-  ``search_all_patterns`` returns an iterator. Each searched pattern is
   represented as a tuple ``(pattern_string, pattern_start_index)``. The
   results are sorted by the start index. If you want to get the result
   as a ``list`` object, use ``list`` function as follow:

   .. code:: python

       >>> patterns = list(trie.search_all_patterns(text))

TrieSearch.search\_longest\_patterns
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Search longest patterns in an input text:

.. code:: python

    >>> for pattern, start_idx in trie.search_longest_patterns(text):
    ...     print pattern, start_idx
    ...
    in 0
    computer science 3
    , 20
    a 22
    trie 24
    , 29
    also 31
    called 36
    digital tree 43
    and 56
    sometimes 60
    radix tree 70
    or 81
    prefix tree 84
    ( 96
    as 98
    they 101
    can 106
    be 110
    by 122
    prefixes 125
    ) 134
    , 136
    is a 138
    kind 143
    of 148
    search tree 151
    - 163
    an 165
    ordered tree data structure 168
    that 196
    is 201
    used to 204
    store 212
    a 218
    dynamic set 220
    or 232
    associative array 235
    where the 253
    the keys 259
    are 268
    usually 272
    strings 280

-  ``search_all_patterns`` also returns an iterator. The result sorted
   by the length of patterns. In the above example, the result is
   re-sorted by the start index.

trie\_search.RecordTrieSearch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``trie_search.RecordTrieSearch`` is a sub class of
``marisa_trie.RecordTrie``, which maps unicode keys to data tuples.

The functions, ``search_all_patterns`` and ``search_longest_patterns``,
are also implemented in ``trie_search.RecordTrieSearch``.
