Using formatted `time` for quick program measurements
=====================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux, CLI

Wanted to see how much resources will a program take without some fancy tools,
just initial quick rough measurements without nice graphs
or going into the stages or patterns in program's execution.

https://stackoverflow.com/questions/15261588/time-format-on-zsh

TIMEFMT

Sadly, I can't find the ``time`` binary, I just have the shell builtin.
I've looked for all the executables in ``/usr``::

    fd -t x 'time$' /usr

PS. finding ``man time`` cause of no help of the builtin.
Builtins should display help and usage if asked.
Maybe the benefit of learnability and discoverability is worth not being able to easily time programs called
``-h`` and ``--help``.

Or you can pair CLI utilities with help ones like ``<program's or builtin's command>-help``,
e.g. ``time-help``.
I wonder how easy or complicated it would be to contribute that and get it to my main distro (Manjaro).
