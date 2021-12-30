Make and entr for code validation during editing
================================================

.. post:: 2021-12-30
   :author: Michal Bultrowicz
   :tags: Python, quality_assurance, CLI, CI/CD

For a while now, I've been wondering how to combine `entr <https://github.com/eradman/entr>`_
(which automatically runs commands on file changes)
with the way I setup project validation (both for CI/CD and for local developer usage) with Makefiles.
The best thing I got so far is the ``validate_continously`` target in
`my Makefile <https://github.com/butla/machine_setups/blob/master/Makefile>`_.

Here it is, with some annotations, and changes for the sake of clarity::

    # so we're sure what shell we're using.
    SHELL:=/bin/bash

    # The below commands require setting up a virtualenv,
    # activating it, and running `poetry install` in it.

    # "validate" - The command that can be used by the developers
    # locally to check that the changes they're working on are fine
    # and can be commited.
    # This should also be used by in the CI.
    # That way both the developers and the automation are always doing
    # the same quality checks and won't disagree
    # (as long as the tooling environment is kept similar enough).
    #
    # As for the order of the operations:
    # pylint can find errors in the code that can cause multiple tests
    # to error out (which would produce a lot of pytest output),
    # so we run it first. If we ran "test" first and got many
    # test errors because of issues detectable by Pylint,
    # analyzing the cause might take longer than if we saw the Pylint
    # output (which we wouldn't get, since "make" normally stops
    # processing on the first error).
    validate: pylint test isort_check

    # "validate_continously" runs all checks from "validate" when a
    # Python file is changed, but it doesn't quit on errors
    # ("--keep-going" option), so we can see the output of all commands,
    # for maximum information about what's wrong with the code.
    # If the tests are failing we can see which ones.
    #
    # This command works great with my Tmux-based "IDE view".
    # It should also be fine for developers comfortable with having
    # a terminal window open, and with the text output of the quality
    # assurance tools like pytest, pylint, etc.
    validate_continously:
        fd '\.py$$' the_code/ tests/ | entr -c make --keep-going validate

    test:
        # Each section that'll be part of "validate" echoes a header,
        # so we can better see where the output of one command ends,
        # and the other begins.
        @echo ===Tests===
        pytest -v tests

    pylint:
        @echo ===Pylint===
        # Your tests are code, so lint them as well.
        pylint the_code/ tests/

    isort_check:
        @echo ===Isort===
        isort -c .

Pylint is a bit slow, which gives an annoying lag before starting the tests, but I want to keep this order,
because it makes sense for running "validate" in CI.

My Tmux "IDE view" is started with
`this script <https://github.com/butla/machine_setups/blob/master/configs/host_agnostic/bin/tmux_ide_panel>`_,
while in Tmux, if you're interested.

As for the current set of static checks, I should add `mypy <https://pypi.org/project/mypy/>`_
and maybe `bandit <https://pypi.org/project/bandit/>`_ to the project.
Some automatic formatting with `yapf <https://pypi.org/project/yapf/>`_ might also be nice.

And before anybody recommends `black <https://pypi.org/project/black/>`_ - I don't like what does
with my intentionally formatted code.
And I don't like the clutter (and the hassle) created by having to add formatting exclusion comments.
Though I don't condemn using it for your project if you have different preferences, of course :)

By the way, I have another post about ``entr`` - :ref:`universal_reload_with_entr`
