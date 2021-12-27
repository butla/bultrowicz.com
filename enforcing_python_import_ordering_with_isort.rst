Enforcing Python imports' order with isort, Makefiles, and Vim
==============================================================

.. post:: 2021-12-27
   :author: Michal Bultrowicz
   :tags: Python, Linux, CLI, Vim

I finally integrated `isort <https://pypi.org/project/isort/>`_ into my toolbox.
I think that the job of changing code files belongs to the editor (or an IDE),
so I made Vim run ``isort`` automatically,
while the import order enforcement in a project is done via Makefile
(which can be run the same way by developers and the CI/CD pipeline).

This post may be a bit chaotic, but it should give a glimpse of how I like to set up automation
around quality assurance (like tests, linting, static checks, etc.) in my projects.
I'd like to produce more comprehensive write-ups at some point in the future.

isort installation
------------------

First, the ``isort`` Python package needs to be available for your editor and the ``make`` commands wherever
you are working, so:

- add ``isort`` to your project's dependencies and virtualenv.
  I use `poetry <https://pypi.org/project/poetry/>`_ for that: ``poetry add --dev isort``
- make ``isort`` available outside of any virtualenv (e.g. for small scripts),
  by installing it for your user. I use `pipx <https://pypi.org/project/pipx/>`_ for that: ``pipx install isort``

VIM (editor) setup
------------------

If you're not using Vim you'll probably still find an ``isort`` plugin for your editor.
Or maybe your IDE has import ordering built-in, like
`Pycharm <https://www.jetbrains.com/pycharm/guide/tips/optimize-imports/>`_.

You'll need a Vim plugin - `ALE <https://github.com/dense-analysis/ale>`_ - to run ``isort``.
I recommend `vim-plug <https://github.com/junegunn/vim-plug>`_ as the plugin manager.
You can see how I set it up at the top of my
`.vimrc <https://github.com/butla/machine_setups/blob/master/configs/host_agnostic/.vimrc>`_.

You can add the plugin by adding ``Plug 'dense-analysis/ale'`` in the right place in your ``.vimrc``,
and then issuing the ``:PlugUpdate`` command to Vim.

Then, add some more config into ``.vimrc``::

    " make ALE use isort
    let g:ale_fixers = { 'python': ['isort'] }

    " this will make :ALEFix, and thus import fix to run on file save
    let g:ale_fix_on_save = 1

Configuring isort
-----------------

Know that you can `configure some aspects <https://pycqa.github.io/isort/docs/configuration/options.html>`_
of how ``isort`` works.
For example, I like to sort all my imports alphabetically on the referenced packages,
without separating ``import XXX`` and ``from XXX import YYY`` statements.
So I put this in my `pyproject.toml <https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/>`_::

    [tool.isort]
    force_sort_within_sections = true

Use in project's Makefile
-------------------------

I like to have a ``validate`` Makefile target that runs all tests and static code checks.
That target should be run by developers and the CI/CD pipeline.

``isort`` can work as one of the static checks, if used with ``-c`` flag.

So we can have a Makefile looking like this::

    validate: static_checks test

    test:
        pytest -v tests/

    static_checks:
        isort -c the_code
        pylint the_code


Bonus: automatic imports fixer for Vim
--------------------------------------

One of the features I'm missing from Pycharm is automatic adding of missing imports.
There's a plugin called `vim-nayvy <https://github.com/relastle/vim-nayvy>`_ that can do that,
but I wasn't able to get it to work with anything other than standard library imports.
That is, it wouldn't fix imports of third-party packages from ``site-packages`` or project/local packages.

Maybe that has something to do with me not having a Python `Language Server <https://langserver.org/>`_
running with NeoVim... I'll see about that some other time.
