App tests in containers
=======================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, quality_assurance

I usually put tests outside of the container (they run in the local environment),
so that it's easy to run and debug them.
But there are some usecases where they would be included in the container, e.g. if you don't want local virtualenvs.
Also, there can be test containers that are separate from the app, that could be used to run functional tests
against the app container.
