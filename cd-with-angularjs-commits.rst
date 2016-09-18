Continuous delivery of a Python library with AngularJS commit convention
========================================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python

I got tired of having to manually build and upload my library (`Mountepy`_) to PyPI,
so I decided to do what any sane programmer would do - set up automation [#1]_.
But how would my scripts know whether they need to just update the README on PyPI and when to
assemble and push a new version of the library?
Thanks to the `AngularJS commit convention`_!
Oh, and `Snap CI`_ will run the whole thing.
Why Snap, you ask? See my previous article - :ref:`choosing-a-ci`.

Motivation
----------

Let's say that you have a Python library and that you follow `semantic versioning`_.
Let's also assume that when your tests pass you have sufficient certainty that your software is
ready for release (and you should have it) and you don't require any pre-releases,
beta versions or whatever.
I'm sure it's easier said than done for those important projects that many people depend upon,
but it has to be doable.

If you introduce a change to the code you probably want to ship it to PyPI.
When you're introducing a fix or implementing a new feature it's quite straightforward - you bump
the version, create new artifacts (probably a wheel and a source archive) and then you push to PyPI.

But what if you only refactored a few tests? Then you don't need to put anything on PyPI.
And when you updated the readme or docs? The version shouldn't change
(it's still exactly the same library as before the commit) but your documentation site
(e.g. the project's page on PyPI) needs to be updated.
If you don't care about any sane versioning (please, care), you could just create a new version
of the library for every commit, but otherwise you need to be able to distinguish
between the commits that affect the production code and those that don't [#2]_. 

This is where AngularJS commit convention helps out.
It's originally for automatic changelog generation, but in essence it allows to distinguish
between commit types of commits.
It requires some work on the human part, of course, but I think that this work is not much more
then the good practice of doing commits that are about a single change.


The build pipeline
------------------

SnapCI build setup
^^^^^^^^^^^^^^^^^^

It's straightforward to add a build configuration for any of your GitHub repositories in Snap,
so I won't go into it.
When you add it you are sent to page that looks like the one below.

.. image:: /_static/cd-with-angularjs-commits/bare_build_config.png

You can change the version of Python in "Languages and Database", you could even pick a different
technology stack, like NodeJS.
You may notice that you can only pick one language, but fear not if you need a mixed environment!
Additional (language) packages can simply be installed with ``yum``
(as mentioned in `Snap CI FAQ`_) in "Commands to be executed in this stage".

About that section commands - it's one of the best things about Snap in my opinion.
You simply type in shell commands that you want to run for the given stage, and that's it!
As familiar and flexible a setup method as you can get.

Real-life tests stage
^^^^^^^^^^^^^^^^^^^^^

What you probably want to do in every CI is to build the code and run the tests.
Most Python libraries don't have to build anything, so just running the tests is enough,
and this is what I did in the first stage of my build, uninspiredly named "TESTS" [#3]_
(I've just renamed the default EDITME):

.. code-block:: bash

    pip install tox # install Tox
    tox # run it

Outside of running the tests and measuring test coverage my Tox setup does other things to check if
the code is OK, and you'll see that later.

The stage could end right there, but I also want to upload the coverage data gathered during
tests to `Coveralls`_ to get that sweet 100% coverage badge on GitHub [#4]_:

.. code-block:: bash

    pip install tox
    tox
    pip install coveralls
    coveralls

For Coveralls to work, it needs to have the repo token allowing it to upload data to your profile.
It will look for it in ``COVERALLS_REPO_TOKEN`` environment variable.
Thankfully, Snap allows to set secure (secret) variables that will be cut out the logs.

.. image:: /_static/cd-with-angularjs-commits/secure_variable.png

Parsing AngularJS-style commits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As I've mentioned at the start of this article a commit message convention can be used
to distinguish different kinds of commits and react to them properly
(deploy a new version? update docs? do nothing?).
`AngularJS commit convention`_ dictate that the messages look like this:

.. code-block:: bash

    <type>(<scope>): <subject>
    <BLANK LINE>
    <body>
    <BLANK LINE>
    <footer>

So, for example (from Mountepy):

.. code-block:: bash

    docs(README): Measuring coverage in mountepy tests

    Also pointed to PyDAS for examples.

The available commit types and their meanings:

* feat - new feature (hopefully with tests)
* fix - a bug fix (also hopefully with tests)
* docs - documentation
* style - formatting, missing semi colons, etc.
* refactor - some refactoring, optimization, etc.
* test - adding missing tests
* chore - project maintainance like build scripts, small tools, etc.

I've created a script (``get_commit_action.sh``) that can identify the commit type and dictate
the action that should be taken (by printing it):

.. code-block:: bash

    #!/bin/bash
    # If some command in this script fails then the commit was probably
    # malformed and an error code should be returned.
    set -e

    # Taking the summary (first line) of the last commit's message.
    COMMIT_SUMMARY=$(git log -1 --format=%s)
    # Type of the commit is located before the mandatory parens
    # explaining location of the chanhe.
    COMMIT_TYPE=$(echo $COMMIT_SUMMARY | cut -d "(" -f 1)

    case $COMMIT_TYPE in
        # These commits change the library code,
        # so they must result in a new release.
        feat|fix|refactor|perf) printf build_code;;
        # Here, the actual library code isn't changed, so a new
        # library version can't be released. But if we host the docs
        # somewhere (library's README page on PyPI also counts),
        # we should rebuild and upload them.
        # Also, documentation updates sometimes go on the same commit
        # with other minor tweaks, so we should (and don't risk
        # anything by) re-release the docs just to be sure.
        docs|style|test|chore) printf build_docs;;
        # If the type isn't recognized,
        # we raise an error and print to the error stream.
        *) >&2 echo "Invalid commit format! Use AngularJS convention."; exit 2;
    esac

Automatic deployment to PyPI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

So let's say that I'm using AngularJS commit convention and have the script to identify them.
Now comes the part we've been waiting for - actually publishing (deployment of) the library to PyPI.
The script to do that looks like this:

.. code-block:: bash

    #!/bin/bash
    set -ev

    # Running the previous script to decide if we'll be uploading
    # a new version or just updating the docs.
    COMMIT_ACTION_SCRIPT=$(dirname $0)/get_commit_action.sh
    COMMIT_ACTION=$($COMMIT_ACTION_SCRIPT)

    if [ $COMMIT_ACTION == build_code ]; then
        # Building source and binary distributions to upload later on,
        # and setting the action that will be performed by Twine (PyPI
        # upload tool) later in the script.
        python3 setup.py sdist bdist_wheel
        TWINE_ACTION=upload
    else
        # Only building the source distribution to update the package
        # description on PyPI.
        # If I had documentation on readthedocs.org I would rebuild it
        # here. Sadly, I don't have it (yet).
        python3 setup.py sdist
        TWINE_ACTION=register
    fi

    # The file that contains repositories configuration for Twine.
    # For me, it points to the official and test PyPI
    # This script's first argument specifies which one to use.
    PYPIRC=$(dirname $0)/pypirc

    # Depending on the commit type this will either upload the
    # distribution files (upload) or update the package's metadata
    # (register).
    # PYPI_PASSWORD will be stored in a secure environment variable in
    # Snap, like the Coveralls token.
    twine $TWINE_ACTION -r $1 -p $PYPI_PASSWORD --config-file $PYPIRC dist/*
       
One thing to note about uploading a new version of the library:
if the version number in setup.py isn't incremented, then it will fail,
because files on PyPI can't be overwritten.
A human is needed to change the version because we're using semantic versioning.
And if said human forgets to do that when he should, he can fix the CI
build with a "fix" type commit bumping the version.

But you can say that, since were can automatically understand commit types, a machine
could incerement the last version number (patch) on "fix", "refactor", and "perf"
commits, and the second version number (minor) on "feat".
I won't do that, because I have bad experience with automatic commits made by CI [#5]_.
I think that the commit log starts to look ugly and gets twice as long with
a version-bumping commit done after every normal one.
A crazy to idea once popped into my head to make the CI just ammend the bumped
version onto the last commit to make the log look nicer, but it would force a developer
to ``pull --rebase`` after each push to origin, so it's... crazy.

So, finally, the step that uses the above script in my Snap setup looks like this:

.. code-block:: bash

    pip install twine
    # pypitest is a label in pypirc file with URL of,
    # you've guessed it, test PyPI.
    pypi_upload.sh pypitest

Why do I interact ith test PyPI and not the real one?
Well, to test stuff... I dunno.
I can check if the files really get there, whether the README looks OK, etc.
And only after that I trigger (manually) the next and last pipeline step:

.. code-block:: bash

    pip install twine
    # This time uploading/registering with the real PyPI.
    # I've also got a different $PYPI_PASSWORD, an approach I recommend.
    # You can store the passwords in KeePass, or something.
    pypi_upload.sh pypi

Triggering a pipeline step manually can also come in handy when your code needs to go through
some out-of-band (out-of-Snap) checks, like Windows tests on AppVeyor or some legal mumbo-jumbo
before you can release the next iteration.

A bit of a warning - if you rerun the step or the whole build that succesfully uploaded some
artifacts, then it'll fail, due to file collision on PyPI.
I don't see any real need to rerun them, though.

When introducing all of this to Mountepy I've put the CI scripts in `another repository`_
at attached them as a `Git submodule`_ to be able to reuse them in other projects
and develop them independently.

Trunk-based development
^^^^^^^^^^^^^^^^^^^^^^^

To dobre podejście, dzięki niemu muszę tylko rozpatrywać jeden commit na raz.
No i continuous delivery tak jakby je zakłada.

My commit parser assumes pushing one commit at a time to master, but that's actually the preferred way in trunk-based development.

Żeby nie było skuchy to Tox sprawdza, czy ostatni commit jest wporzo (odpalając tamten skrypt,
jeśli on się nie wywali to jest spoko).
Dobrze puścić zatem Toxa po commicie. No i od razu wyjdzie w buildzie CI.

To, że jest trunk-based development sprawia, że zawsze możemy rozpatrywać tylko pojedynczy commit.
Jakby przyszły dwa różne i trzeba zdecydować co robić, to byłoby ciut bardziej skomplikowanie

W ogóle będę developował na masterze. Fakt, że na razie tylko ja tam commituje (ale wiecie, może znajdziecie coś do poprawy, obczajcie na githubie, dajcie gwiazdkę, czy coś),
więc dużego ruchu nie będzie. Ale nie bezpieczniej robić sobie feature branche, puszczać CI na nich i dopiero wtedy przerzucać na mastera?
Co jeśli popsuję build i na githubie i pypi pojawi się ośmieszające "build failed"?? Cóż, po prostu lepiej mieć się na baczności, żebym tego nie zrobił.
U mnie też nierobienie feature-branchy wywoływało strach, ale chodzą słuchy, że to może być "the way to go" (https://www.thoughtworks.com/insights/blog/enabling-trunk-based-development-deployment-pipelines).

Tox sprawia, że nie powinno nic jebnąć

Ale jakby co, to nic się nie bójcie, w Snapie można ustawić dokładnie jak mają być sprawdzane pull requestach i branche (domyślnie nie są wcale ruszane).

Additional stuff
^^^^^^^^^^^^^^^^

I like when my tests keep the developers (only me, in this case) in check, so my tox configuration not only runs my tests,
but also checks that test coverage is at 100% and that there are no unknown Pylint issues.

### Wydzielanie skryptów, żeby były uniwersalne
Zrobiłem sobie repo. Wywaliłem skrypty z ci/ tam. Teraz ustawiam Gitowy submodule w mountepy i zaraz przestawię konfigurację w Snapie, bo będzie inny folder.
`git submodule add adres`
no i ściągać teraz trzeba przez `git clone --recursive adred`, bo tox polega na jednym, z tych skryptów.

Przerób skrypty i biuld na Snapie, żeby użytkownik pypi też był dostarczany przez argument. Żeby ludzie mogli od razi używać.

Conventional commits can be later used to generate changelogs.

Pipeline overview (conclusions)
-------------------------------
Co chcę ogólnie powiedzieć? Że CD jest fajne? Że powinno się robić małe testowalne zmiany
i mieć z głowy uploady i deploymenty?
Co zrobiłem? Jak wygląda teraz mój proces (screen shot z pipelinea)?

Jak robie jakieś zmiany, to robię jakiś commit, czekam, klikam w snapie jakby co i działa.

Jak macie jakieś pomysły na usprawnienia albo widzicie tu jakieś problemy to komentujcie.

The overall configuration looks like this.

.. image:: /_static/cd-with-angularjs-commits/full_build_config.png

W ogóle poszczególne fazy buildu można restartować, nie trzeba całego buildu.

Konfiguracja buildowa ze wszystkim dostępna tu https://snap-ci.com/butla/mountepy/branch/master


.. rubric:: Footnotes

.. [#] If you want to get fancy you can also call this automation a `continuous delivery`_ pipeline.
.. [#] At least that's the granurality that worked for me, you can go more in depth if you want.
.. [#] I've also changed Python to 3.4 from the default 2.7.
.. [#] I could put Coveralls invocation in another stage, but then I would need to pass ``.coverage`` file as an artifact (TODO to tak sie robi??), because different stages are not guaranteed to run in the same environment (virtual machine).
.. [#] I'm mainly looking at you, ``mvn release``...

.. _another repository: https://github.com/butla/ci-helpers
.. _AngularJS commit convention: https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit
.. _continuous delivery: https://www.thoughtworks.com/continuous-delivery
.. _Coveralls: https://coveralls.io
.. _Git submodule: https://git-scm.com/book/en/v2/Git-Tools-Submodules 
.. _Mountepy: https://pypi.org/project/mountepy/ 
.. _semantic versioning: http://semver.org/
.. _Snap CI: https://snap-ci.com/
.. _Snap CI FAQ: https://docs.snap-ci.com/faq/
