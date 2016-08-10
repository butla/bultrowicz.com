Continuous Delivery of a Python library with AngularJS commit convention
========================================================================

.. post::
   :tags: Python

I got tired of having to manually build and upload my library
(`Mountepy <https://pypi.org/project/mountepy/>`_) to PyPI, so I decided to do what any sane
programmer would do - set up automation.
But how would my scripts know whether they need to just update the README on PyPI and when to
push a new version of the library?
Thanks to the `AngularJS commit conventions <https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit>`_!
Oh, and `Snap CI <https://snap-ci.com/>`_ will run the whole thing.

Motivation
----------

Let's say that you have a Python library and that you follow `semantic versioning <http://semver.org/>`_.
If you introduce a change to the code you probably want to ship it to PyPI.
When you're introducing a fix or implementing a new feature it's quite straightforward - you bump
the version, create new artifacts (probably a wheel and a tar.gz) and then you push to PyPI.
But what if you only refactored a few tests? Then you don't need to do anything with PyPI.
And when you updated the readme or docs? The version shouldn't change
(it's still exactly the same library as before the commit) but your documentation site
(e.g. the README page on PyPI) needs to be updated.
Gdybys nie mial semver, to teoretycznie mozna wywalac wszystko z inną wersją, ale to brzmi słabo i wprowadza użytkowników biblioteki w błąd.

change readme - just update the docs and page on pypi
change tests - still the same version
change library code - new library version

Let's just say that you're not a big project that needs to go through beta, etc
(but maybe their tests just aren't good enough? Or they deal with so many clients from different OSes and they want to be nice to them...).
But this can be fine for uploading development versions for people to try out.
Or even

I was inspired by this article about `PyPI deployments with Travis <https://www.appneta.com/blog/pypi-deployment-with-travis-ci/>`_.
But I had a few problems with it and with Travis (explained later).

Trochę było uciążliwe, że jak coś zmieniałem, to albo musiałem robić upload albo register. Raz jeszcze zamiast zuploadować wheela, to wziąłem output z bdist.
Automat musi być w stanie robić to za mnie. No i robienie automatów to świetna zabawa (po co odwiedzić znajomych, których nie widziało się od dwóch miesięcy,
skoro można siedzieć przy komputerze?).

Parsing AngularJS-style commits
-------------------------------

* I decided that my commits will follow AngularJS commit conventions (https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit)
* I created scripts that parse commit messages.
* Based on the commit type I either update the documentation (which can really do nothing) or upload a new version of the library to PyPI.

### Chosing a CI service
Of course I wanted something hosted and integrated with Github.

Zaczęło się od tego, że travisowe buildy Mountepy zaczęły czasem failować
z powodu jakiejś zwiechy między testami. Raz na jakiś czas (w końcu wziąłem się za naprawienie tego).
No i Travis jak to Travis nie umożliwia żadnego debugu.
No to zacząłem patrzeć na alternatywy.

Travis nie miał debugu - słabo. Ale miał Dockera. No i wsparcie dla OS X, które może bym tam użył.
Circle miał debug po ssh normalnie, miał też docker i OS X - no super. Ale nie udało mi się przez 10 minut zrobił,
żeby mój biuld działał. A miałem build z Dockerem (PyDAS).

A no i Circle podobno ma cztery darmowe buildy jednocześnie.

Travis też ma dobre opcje deploymentów (https://www.appneta.com/blog/pypi-deployment-with-travis-ci/) ale nie jest to tak banalnie proste,
jak odpalenie po prostu linijek basha w Snapie.

Snap miał dockera i debug, ale bez OS X (i tak mi się nie chiało),
a Docker był na życzenie tylko. Ale ogarnęli się w try miga.
No i pipeline'y to po prostu polecenia, żadnej magii i czytania dokumentacji (co i tak nie pomogło mojemu toxowemu buildowi pydasa).
Fakt, że opis buildu nie jest trzymany z kodem (co też jest fajną formą dokumentacji), ale wyglądają przejrzyście, są proste w ustawianiu
i dają bardziej wyklarowane kroki (a nie odpalanie jednego monolitycznego skryptu dla trochę bardziej złożonego zachowania.
Chociaż to muszę zweryfikować, bo tych stadiów odpalania trochę jest w Circlu i Travisie.

After I finished anything I've stumbled upon Codeship, although I've heard about it before.
It's supposed to be really cool, Docker and all, but I found setting the tests clunky and I didn't have the initiative to try to get to know it, since I was perfectly happy with Snap.
But you can find it to your liking, I don't know...

* I chose Snap CI because it supports Docker, enables build debug and has powerful build pipeline setup.

  ### Build pipeline
Te automatyczne deploye będą tylko na masterze, ustawię sobie, żeby na pull requesty były tylko testy i sprawdzenie poprawności commita.
W ogóle będę developował na masterze. Fakt, że na razie tylko ja tam commituje (ale wiecie, może znajdziecie coś do poprawy, obczajcie na githubie, dajcie gwiazdkę, czy coś),
więc dużego ruchu nie będzie. Ale nie bezpieczniej robić sobie feature branche, puszczać CI na nich i dopiero wtedy przerzucać na mastera?
Co jeśli popsuję build i na githubie i pypi pojawi się ośmieszające "build failed"?? Cóż, po prostu lepiej mieć się na baczności, żebym tego nie zrobił.
U mnie też nierobienie feature-branchy wywoływało strach, ale chodzą słuchy, że to może być "the way to go" (https://www.thoughtworks.com/insights/blog/enabling-trunk-based-development-deployment-pipelines).

Ale jakby co, to nic się nie bójcie, w Snapie można ustawić dokładnie jak mają być sprawdzane pull requestach i branche (domyślnie nie są wcale ruszane).

W ogóle poszczególne fazy można restartować, nie trzeba całego buildu.

#### Tests
There's no build step in most Python libraries. So our first pypeline stage runs the tests:
```
pip install tox
tox
pip install coveralls
coveralls
```
I like when my tests keep the developers (only me, in this case) in check, so my tox configuration not only runs my tests,
but also checks that test coverage is at 100% and that there are no unknown Pylint issues.

I like to show off that my project has the mythical full coverage, so I use coveralls. BLABLABLA użyje .coverage musi już być, a powstaje w trakcie testów.

Following the instructions from https://pypi.python.org/pypi/coveralls I've set `COVERALLS_REPO_TOKEN` as a secret environment variable in coveralls step.

A i jak mamy w toxie pythona 3 i 2, to znajduje Pythona 2 na środowisku 3.4 (według Snapa). Bo można tylko jednego Pythona na cały pipeline.
Ale nawet, gdyby czegoś brakowało, to niby można [doinstalować youmem] (https://docs.snap-ci.com/faq/)

#### Pypi upload
W sumie tym commitu dyktuje, co powinno się zrobić. Czy wrzucam nową wersję, czy nie (ale np. updatuje dokumentację przez register).
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

### Wydzielanie skryptów, żeby były uniwersalne
Zrobiłem sobie repo. Wywaliłem skrypty z ci/ tam. Teraz ustawiam Gitowy submodule w mountepy i zaraz przestawię konfigurację w Snapie, bo będzie inny folder.
`git submodule add adres`
no i ściągać teraz trzeba przez `git clone --recursive adred`, bo tox polega na jednym, z tych skryptów.

Przerób skrypty i biuld na Snapie, żeby użytkownik pypi też był dostarczany przez argument. Żeby ludzie mogli od razi używać.

### Podsumowanie
Co zrobiłem? Jak wygląda teraz mój proces?

Jak robie jakieś zmiany, to robię jakiś commit, czekam, klikam w snapie jakby co i działa.

Jak macie jakieś pomysły na usprawnienia albo widzicie tu jakieś problemy to komentujcie.

