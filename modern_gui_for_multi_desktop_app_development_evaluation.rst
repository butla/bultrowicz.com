Evaluation: using modern Python GUI libraries for multi-platform app development
================================================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, GUI, Windows, Linux, MacOS

To check
--------

- zadanie:
  - muszę coś kliknąć albo otworzyć plik
  - pojawia się zdjęcie, zaznaczam coś na nim, wyświetlam kąty, najlepiej na obrazku
  - mogę je otworzyć znowu ze wszystkim zaznaczonym
  - drugi ekran z listą pacjentów
- dodanie pythonowej paczki do zależności
- polskie znaki
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

- przykład 1 nie działa, bo brakuje (przynajmniej) GLShader (https://raw.githubusercontent.com/wjakob/nanogui/master/python/example1.py) nie działają,
- w przykładzie 2 trzeba było zmienić nazwy na snake case z camel case


Positives
~~~~~~~~~

Notes
~~~~~

- can just install with pip, no compilation needed
- can run "detached" easily. Whatever that means

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

Positives
~~~~~~~~~

- includes application building that works (at least for Linux) and the sample AppImage is under 30MB, which is
  acceptable (see how much all the Electron apps are taking)

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
