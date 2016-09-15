Continuous delivery of a Python library with AngularJS commit convention
========================================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python

I got tired of having to manually build and upload my library (`Mountepy`_) to PyPI,
so I decided to do what any sane programmer would do - set up automation [#1]_.
But how would my scripts know whether they need to just update the README on PyPI and when to
assemble and push a new version of the library?
Thanks to the `AngularJS commit conventions`_!
Oh, and `Snap CI`_ will run the whole thing.

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

Choosing a CI service
---------------------

I host my code on GitHub, as probably many or you do [#3]_.
The easiest way to get my code automatically tested and published (only if there's a need for that)
is, of course, to use one of the integrated CI services.
`One thing to note`_ - some take the label of "continuous integration",
some "continuous delivery", but their capabilities are similar.
But there's still quite a few of them we have to choose...

Travis
^^^^^^

I don't know if it actually is, but for me it seems that Travis is the oldest,
most well known and most widely used from the bunch.
Because of that and because I didn't have any fancy requirements,
I was using it for Mountepy for some time (you'll see why this has changed).
Also, the article about `PyPI deployments with Travis`_ inspired me to create
the pipeline that is the subject of this article.

Travis has:

* Docker support, which I needed for my other project (`PyDAS`_);
* OS X builds, which I may need for Mountepy if and when I decide to support it [#4]_.

But Travis has one big problem - you have no easy way of debugging builds.
When I got strange test failures, it took a lot of guesswork
and a print-heavy version of my application to find their cause.
I knew that there had to be a better way, so it was time to look at other options [#5]_.

CircleCI
^^^^^^^^

Pros:

* You can SSH into the container that runs your builds/tests! (so there goes the debug problem)
* Docker support.
* OS X builds.

Cons:

* Hard to set up? Circle uses it's own build configuration YAML style (much like Travis).
  But I've struggled to get PyDAS tests (starting some processes, some Docker containers) working
  for about 5 or 10 minutes and I gave up [#6]_. I don't know...

Rumors(?):

* I've heard that it supports up to 4 parallel builds on the free plan but this is not what
  the `pricing page <https://circleci.com/pricing/>`_ says... [#7]_

Snap CI
^^^^^^^

This is the CI I chose. It provided what I needed (Docker, debug) and is really
straightforward to work with.

Pros:

* Docker support. Although it's in beta and I had to contact support to have it enabled
  (which was done in a few hours), my builds run smoothly.
* Build debug. Not through SSH, but with browser-based snap-shell. I think I'd prefer SSH,
  but being able to do it in the browser is also nice.
* Build steps defined in Bash. No custom configuration syntax to learn, just plain old scripts!
* Ability to group build steps into stages; even one's that need to be triggered manually
  (good for e.g. manual or exploratory tests).

Cons:

* No OS X builds (Travis and Circle have them).
* Build pipeline definitions are can't be easily copied between projects.
  With Travis you could just copy the config file,
  here it requires a bit more clicking around the web UI.
  Although you can still keep almost of your logic in script files
  and just run different ones in different stages

Codeship
^^^^^^^^

After I finished comparing Travis, Circle and Snap I've remembered that there's one more thing
(probably way more than that, but I don't have all the time in the world) to look at - Codeship.

It's supposed to be really cool and all, but I found setting up the tests clunky
and I didn't have the initiative to try to get to know it, since I was perfectly happy with Snap.
But you can find it to your liking, I don't know...

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
and this is what I did in the first stage of my build, uninspiredly named "TESTS" [#8]_
(I've just renamed the default EDITME):

.. code-block:: bash

    pip install tox # install Tox
    tox # run it

Outside of running the tests and measuring test coverage my Tox setup does other things to check if
the code is OK, and you'll see that later.

The stage could end right there, but I also want to upload the coverage data gathered during
tests to `Coveralls`_ to get that sweet 100% coverage badge on GitHub [#9]_:

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
`AngularJS commit conventions`_ dictate that the messages look like this:

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

I've created a script that can identify the commit type and dictate the action that should be
taken (by printing it):

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

**

Automatic deployment to PyPI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Na początku tylko do test, ale potem można dodać

Te automatyczne deploye będą tylko na masterze, ustawię sobie, żeby na pull requesty były tylko testy i sprawdzenie poprawności commita.

Wersję trzeba podbić ręcznie. Jak się nie podbije, to się wywali na uploadzie.

W sumie typ commitu dyktuje, co powinno się zrobić. Czy wrzucam nową wersję, czy nie (ale np. updatuje dokumentację przez register).
Jak zobaczymy coś w stylu konwencji AngularJS to można jakoś sygnalizować, co robi dany commit.
Dzięki temu będziemy mieli informację, czy trzeba zrobić upload czy tylko register.

Jakbym miał normalną HTMLową dokumentację, to wyglądałoby to podobnie. Po prostu bym przebudowywał i wrzucał na serwer.

Mam skrypt mały do parsowania commitów (pokaż). Mimo tego go wytestowałem (link do pliku), chociażby po to, żeby sobie poćwiczyć testowanie bashowych skryptów.
My commit parser assumes pushing one commit at a time to master, but that's actually the preferred way in trunk-based development.
Conventional commits can be later used to generate changelogs.

Step do uploadu,
```
pip install twine
ci/pypi_upload.sh pypitest
```
Skrypt uploadowy korzysta z poprzedniego.

Wrzucam z automatu na testpypi. Jak coś będzie nie tak, albo biblioteka będzie już istniała to będzie fail.
Jak się zapomni o podbiciu wersji, to trzeba zrobić kolejnego commita z "fix()".

Jako osobny krok mam wrzucanie na normalne pypi. Oznaczyłem jako krok ręczny, żeby zawsze móc jeszcze spojrzeć, czy na testowym dobrze wyświetla się README itp.
Sam opis w snapie wygląda tak samo jak poprzedni, tylko że zamiast `ci/pypi_upload.sh pypitest` jest `ci/pypi_upload.sh pypi`.
A no i oba przypadki używają tajnej zmiennej środowiskowej PYPI\_PASSWORD (mam różne tu i tu).

Rerun buildu, który wrzuca kod (fix, refactor, etc.) skończy się failem, bo będzie chciał wrzucić jeszcze raz pliki.
Na razie nie mam na to rozwiązania, chyba poprostu nie należy robić rerunów.

Wszystko dostępne tutaj https://snap-ci.com/butla/mountepy/branch/master

Ręczne odpalanie ostatecznego uploadu też jest dobre, jeśli np. czekacie na wyniki na Windowsie z AppVeyora (ale może to też da się zautomatyzować przez jakieś API).

To, że jest trunk-based development sprawia, że zawsze możemy rozpatrywać tylko pojedynczy commit.
Jakby przyszły dwa różne i trzeba zdecydować co robić, to byłoby ciut bardziej skomplikowanie

A word about branching
^^^^^^^^^^^^^^^^^^^^^^

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


Pipeline overview (conclusions)
-------------------------------
Co zrobiłem? Jak wygląda teraz mój proces (screen shot z pipelinea)?

Jak robie jakieś zmiany, to robię jakiś commit, czekam, klikam w snapie jakby co i działa.

Jak macie jakieś pomysły na usprawnienia albo widzicie tu jakieś problemy to komentujcie.

The overall configuration looks like this.

.. image:: /_static/cd-with-angularjs-commits/full_build_config.png

W ogóle poszczególne fazy buildu można restartować, nie trzeba całego buildu.


.. rubric:: Footnotes

.. [#] If you want to get fancy you can also call this automation a `continuous delivery`_ pipeline.
.. [#] At least that's the granurality that worked for me, you can go more in depth if you want.
.. [#] It's just more convenient and "social" than Bitbucket and GitLab. But I'm kind of afraid of its monopoly...
.. [#] I think that right now Mountepy should work on OS X, but you'll have to install Mountebank yourself. If you want the feature create a GitHub issue.
.. [#] And thanks to that you have the whole section about choosing a CI :)
.. [#] I didn't try that hard because by that point I've already taken a liking to Snap CI.
.. [#] If you're using Circle, please say how it is in the comments.
.. [#] I've also changed Python to 3.4 from the default 2.7.
.. [#] I could put Coveralls invocation in another stage, but then I would need to pass ``.coverage`` file as an artifact (TODO to tak sie robi??), because different stages are not guaranteed to run in the same environment (virtual machine).

.. _AngularJS commit conventions: https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit
.. _continuous delivery: https://www.thoughtworks.com/continuous-delivery
.. _Coveralls: https://coveralls.io
.. _Mountepy: https://pypi.org/project/mountepy/ 
.. _One thing to note: https://blog.snap-ci.com/blog/2016/07/26/continuous-delivery-integration-devops-research/
.. _PyDAS: https://github.com/butla/pydas
.. _PyPI deployments with Travis: https://www.appneta.com/blog/pypi-deployment-with-travis-ci/_ 
.. _semantic versioning: http://semver.org/
.. _Snap CI: https://snap-ci.com/
.. _Snap CI FAQ: https://docs.snap-ci.com/faq/
