Debugging Python in Docker with CLI
===================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python

* add ``stdin_open: true`` and ``tty: true`` to the container ``docker-compose.yml``.
* put ``breakpoint()`` in code where you want to enter the debugger
* recreate the container
* ``docker attach`` to the container (``docker-compose ps`` to show container names)
* trigger the code with the breakpoint

pdbpp recommended. Or pudb / ipdb. But pdbpp doesn't upset anything.
