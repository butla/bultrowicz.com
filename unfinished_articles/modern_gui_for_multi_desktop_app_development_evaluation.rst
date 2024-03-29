Search for a Python-friendly multi-platform GUI toolkit
=======================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, GUI, Windows, Linux, MacOS

I'm building a for-profit multi-platform [#1]_ GUI application.
Because I like making informed decisions I had to look around the ecosystem to see what's available.
In the end I went with Kivy, but before that I evaluated a few tools (some more obscure).
Here are the notes from that endevour.

I didn't spend equal time on all the tools. I had to pick the ones more promising for me.

Looking for GUIs
----------------

There's a lot of articles that regurgitate similar lists (just search for "python gui list")
without any real insight. Looks like people writing the articles don't even try to use the tools.
They just skim the documentation (which sometimes can be propaganda,
or omits that the author had a very narrow use case).

Common themes in GUIs
---------------------

Projects that wanna look native, so they delegate to platform specific toolkits:
- complexity
- different problems on different platforms
- wxPython, Toga, something else?

GUIs that don't look native, but look the same everywhere.

JS/electron

My development background
-------------------------

The last couple of years in my career was about the web (with emphasis on the backends),
but I was maintaining some GUIs (desktop and mobile) at the beginning of my career.

My long-term goals
------------------

I want:

- less centralization
- for people to own their data
- companies to not have access to their customers' data (it's even safer for them, cause they can't leak it)
- to be able to put software in people's hands no matter what platform they're on

Why not JS
----------

It seems that JS is dominating the GUI scene. It's really easy on the app distribution as well.
You just go to an URL and there's your app!
No need to download or install, or do any other time consuming things.
Also, they're relatively safe.

I could've chosen Javascript, but I knew I would miss a lot of the freedom I have with Python.
I'm very good with Python and I know it. JS - not so much
(bits here and there, read a book, some work on a React app during the previous contract).

If I went with something that requires JS, I wouldn't want to mix it with Python and I would've went with JS
all the way. I probably won't need typically Python tools like numpy.

To check
--------

- zadanie:
  - tabela użytkowników
  - kliknięcie, żeby otworzyć zdjęcie
  - zaznaczanie punktów na zdjęciu, wyświetlanie kątów między nimi
- polskie znaki
- async HTTP request with httpx
- przeskakiwanie tabem lub strzałkami po elementach gui?
- wpinanie się debuggerem
- reakcja GUI na jakieś asynchroniczne zdarzenie
  - z innego wątku/event loopa
  - z innego elementu GUI
- ile zajmuje apka na windowsie/MacOS/Linuxie?



DearPyGui
---------

Problems
~~~~~~~~

- polish characters in the inputs don't work? Might be an issue for internationalization
- file selector
  - Jak wygląda na windowsie?
  - mogę wołać po prostu filedialog systemu?
  - można z takim żyć?
- chyba trochę słabo robieniem rzeczy asynchronicznie https://github.com/hoffstadt/DearPyGui/issues/407
- faktycznie bardziej dla dodawanie opcji pod skrypty, raczej nie wyświetlę tabelarycznych danych

Positives
~~~~~~~~~

- beautiful simplicity

App size
~~~~~~~~

- dear_py_gui/lib/python3.8/site-packages/dearpygui -- 152M



NanoGui
-------

Problems
~~~~~~~~

- trochę mają wylane w dokumentację, https://github.com/mitsuba-renderer/nanogui/issues/60. Albo po prostu faktycznie
  maja zdecydowanie za mało czasu
- biblioteka bardziej dla dodawanie opcji pod wizualizacje, raczej nie wyświetlę tabelarycznych danych
- nie widzę opcji, żeby stworzyć nowe okno wyskakujące. Wszystko w obrębie jednego okna.


Positives
~~~~~~~~~

Notes
~~~~~

- can just install with pip, no compilation needed
- can run "detached" easily. Whatever that means
- prawdziwy przykładowy kod w pythonie jest tu https://github.com/mitsuba-renderer/nanogui/tree/master/src/python

App size
~~~~~~~~

- nano_gui/lib/python3.8/site-packages/nanogui -- 4,2M



cefpython
---------

Problems
~~~~~~~~

- latest version built only for Windows https://github.com/cztomczak/cefpython/issues/609
- releases don't seem very regular (might not be a problem if it's stable) https://pypi.org/project/cefpython3/66.0/#history
- have to code in both JS and Python and manage interactions between them - too much cognitive overhead.
- python3.8 and higher not supported, at least in 66.0

Notes
~~~~~

- it would be nice to be able to use HTML and CSS to create the UI since they're very good at it, but the price
  (JS for UI logic, binaries' size) is too high
- other approaches to embedding Chromium are mentioned here https://medium.com/@abulka/electron-python-4e8c807bfa5e

App size
~~~~~~~~

- cefpython/lib/python3.8/site-packages/cefpython3 -- 212M



pyglet
---------

Problems
~~~~~~~~

- default controls look dated and a bit ugly
- no example of how to create a button without an image, dunno if it's possible

Positives
~~~~~~~~~

- API seems nicely Pythonic

Notes
~~~~~

- it's not for building GUIs, I think

App size
~~~~~~~~

- /home/butla/.virtualenvs/pyglet_/lib/python3.8/site-packages/pyglet -- 8,8M



Toga / Briefcase
----------------

Questions
~~~~~~~~~

- can I make the test app label be centered?

Problems
~~~~~~~~

- no clue where it installs all the packages (like JDK for android development) and python packages
- ``briefcase create`` on Linux gives me a Python 3.6 project, doesn't say how to change the version
- didn't find info on how to specify the "support package" (Python version)
  - had to delete ``linux`` folder created with ``briefcase build`` to see the URL it's getting the packages from
- dependency python modules not available when doing ``briefcase dev``
- ``briefcase run`` fails with python3.9 support. Docker gets created with 3.6 anyway...

- running Pillow from within the AppImage::

    from PIL import Image as PilImage
      File "/tmp/.mount_BeewarvaKxjQ/usr/app_packages/PIL/Image.py", line 114, in <module>
        from . import _imaging as core
    ImportError: libtiff-102594ad.so.5.7.0: ELF load command address/offset not properly aligned
    https://github.com/beeware/briefcase/issues/458

- running from a virtualenv could be documented better. There is ``pip install --pre toga-demo``, in the README, but I was
  too slow to figure out that I need that (well, ``install --pre toga-gtk`` for Linux, really)


Positives
~~~~~~~~~

- includes application building that works (at least for Linux) and the sample AppImage is under 30MB, which is
  acceptable (see how much all the Electron apps are taking)
- przeskakiwanie tabem lub strzałkami po elementach gui działa (przynajmniej w GTK)
- ctrl+f do wyszukiwania w tabeli działa (przynajmniej w GTK)


Notes
~~~~~

- Kinda dislike this approach of doing everything through magical commands (like ``briefcase dev/run``)
- Alpha status and warning about stuff not being fully supported on Windows scares me.
- do I want the standard top menu for the application? Isn't it better to have separate screens?
- doesn't reuse system-wide tools like Android SDK
- I have to run export JAVA_HOME=/home/butla/.briefcase/tools/java before running commands from
  ~/.briefcase/tools/android_sdk/tools/bin like avdmanager
- numpy doesn't work. It might work with PyOxidizer

App size
~~~~~~~~

- AppImage is around 29 MB
- /home/butla/.virtualenvs/beeware_toga_test_app/lib/python3.8/site-packages -- 9,4M
- the minimal app on Android takes 90.57 MB



PySide6
-------

Problems
~~~~~~~~

- ImportError: ``/lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.28' not found
  (required by /home/butla/.virtualenvs/pyside6_app/lib/python3.8/site-packages/PySide6/Qt/lib/libQt6Core.so.6)``

Positives
~~~~~~~~~


Notes
~~~~~


App size
~~~~~~~~

- 560M    PySide6



Azul
----

Problems
~~~~~~~~

- from https://azul.rs/guide/nightly/Installation - "the precompiled library is dependency-free".
  That's not true, ldd shows the .so file is dependent on other libs, and it failes with segfault because of linking.
- I wanted to compile it myself, but it's complaining that there are no "features" like "python3".
- no tags, build is failing even without "features"
- on Manjaro I get ``ImportError: dynamic module does not define module export function (PyInit_azul)``
- I guess the project is too immature. I'm gonna go with the warnings from
  https://raphlinus.github.io/rust/druid/2020/09/28/rust-2021.html

Positives
~~~~~~~~~

- looks to be very minimalistic in setup - no tools, no reliance on frameworks, just a file to use from Python.
- up to me to package it up the best way possible (WiX? PyInstaller? That Rust compiling solution? Cython + rust?)

Notes
~~~~~

- zgłoś poprawki do docsów

App size
~~~~~~~~

- libazul.so -- 11.1 M


Kivy
----

TODO
~~~~

- recycleview dla tabeli?

Questions
~~~~~~~~~

- how much can I style components? https://github.com/kivy/kivy/wiki/Theming-Kivy
- can I make scroll bars always visible if something is scrollable?
  I need people using the app for the first time to know what's happening and what they can do.
- can I disable the right-click behavior? I think it ads a holding touch right now

Problems
~~~~~~~~

- default widgets might not be familiar to people not used to touch interfaces.
  Hidden scroll bars, for example.
  I want my UIs to be understandable even to "non-tech" people.
- no widget for tabular data
- licensing stuff stresses me out https://kivy.org/doc/stable/guide/licensing.html
- kinda hard to figure out how to produce a table of data
- made with touch interfaces in mind, little support for mouse and keyboard.
  Double click in file chooser would be nice

Positives
~~~~~~~~~

- app can be run with asyncio as the event loop, so doing async stuff should be easy
- nice documentation
- lots of examples
- looks actively maintained (so does Toga), but this is commercially used (at least according to their own
  docs/propaganda :))
- polskie znaki działają :)
- I like that I have options for creating the root widget for the app and loading of the .kv file,
  there's no holy opinionated way that the framework forces me to use (or keeps to other ways more obscure,
  like Django does)
- drawing stuff is quite straightforward

Notes
~~~~~

- should be straightforward to build for macs starting from Catalina, which should be 75% of them
  https://www.statista.com/statistics/944559/worldwide-macos-version-market-share/
- implementing tab-switching can be done with the FocusBehavior
  https://kivy.org/doc/stable/api-kivy.uix.behaviors.focus.html?highlight=focus#module-kivy.uix.behaviors.focus

App size
~~~~~~~~

- todo



wxPython
--------

To check
~~~~~~~~

- async HTTP request with httpx (start an event loop in another thread before running wxPython's main loop?)
  - or maybe https://github.com/sirk390/wxasync ??
- jak wygląda na windowsie?

Questions
~~~~~~~~~

- wxPython zaciąga GTK. Jak bym dystrybuował binarkę z GTK, to czy nie muszę publikować kodu?
  Poszukaj na jakiś grupach.

Problems
~~~~~~~~

- not too much happening in the commits. Is the project inactive, or so much feature-complete?
- pip install wxPython took /24m-8,1s, 12m-12,7s on my main laptop
- I think it's very bad that running constructors for widgets adds them to the layout.
  Same problem as Tkinter. Can't nicely create stuff in functions and then bind it into a UI.
- non-pythonic API (uppercase)
- wiki (https://wiki.wxpython.org/) seems to have a lot of outdated examples, but it looks like there's a more modern
  tutorial mentioned there (https://zetcode.com/wxpython/)
- why do I have to add widgets both to parent widgets (Panel, Frame) and to Sizers?
- sizers have a weird mechanic of merging of flags for border width, widget alignment, and space expansion (size hints
  in Kivy seem nicer)
- ListCtrl (table):
    - quite clunky method of adding rows
    - thing with mixins is a bit awkward
    - can't put a button in there (controls are nice and full featured, but rigid)
- I can't just register for touch events from a simple image widget and draw on it - it works on Linux,
  but not on Windows (and somebody on stack overflow says it doesn't work on Mac as well)

- delegates to

Positives
~~~~~~~~~

- polskie znaki działają :)
- mature and full-featured

Notes
~~~~~

- translates to native GUI elements like Toga, it seems

App size
~~~~~~~~

- todo


More tools that might be good to look at
-----------------------------------------


https://github.com/ChrisKnott/Eel
From its README.
"Eel is not as fully-fledged as Electron or cefpython - it is probably not suitable for making full blown applications like"
Dunno why is that. What does full Electron give? If you can use HTML, CSS, JS and normal Python that should be good
enough.

.. rubric:: Footnotes

.. [#] Windows and MacOS is a must (most customers there), but I want to normalize releasing on Linux as well.
       Also, if you have a truly multi-platform solution, it should just work anywhere.
       Even on Android and iOS.
       but I'm sure I'll iron the script out once I need to setup another system or when I'll boot a live install.
