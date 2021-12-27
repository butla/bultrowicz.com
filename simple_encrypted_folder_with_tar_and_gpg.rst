Simple encrypted Linux folders with TAR and GPG
===============================================

.. post:: 2021-12-27
   :author: Michal Bultrowicz
   :tags: Linux, CLI, security

What's the simplest way of encrypting a folder in Linux?
Combining ``tar`` with ``gpg``, it seems.

Let's say you have some files in a folder called ``secret_files``.
To encrypt them you can run::

    tar cvzf - secret_files/ | gpg -c > secret_files.tar.gz.gpg

This creates a compressed (with gzip) TAR archive [#1]_ of your files,
which is then symmetrically encrypted by GPG.
I advise to create and store the passphrase you'll be asked for with a password manager like KeePassXC.

To decrypt the files run::

    gpg -d secret_files.tar.gz.gpg | tar xvzf -

What do you need this for?
--------------------------

You can use that for whatever you need encrypted files for :)

This isn't a trick that I'll start using often, but it may come in handy on some occasions,
like sending private files through third parties, when I don't even want the file names to leak.
Password-protected ZIPs still present the filenames for example (see ``unzip -l password_protected.zip``).

Sources
-------

Just for the record, these are the URLs I got (and used) when I was "researching" [#2]_
the topic of encrypting folders on Linux:

- https://linuxconfig.org/how-to-create-compressed-encrypted-archives-with-tar-and-gpg
- https://superuser.com/questions/370389/how-do-i-password-protect-a-tgz-file-with-tar-in-unix

.. rubric:: Footnotes

.. [#] Yup, I know "TAR archive" would get expanded to "Tape ARchive archive",
   but maybe somebody won't know what a TAR is ¯\\_(ツ)_/¯
.. [#] By "research" I mean "googling" with DuckDuckGo. DuckDuckGoing?
