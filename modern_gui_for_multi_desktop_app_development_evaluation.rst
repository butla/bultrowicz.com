Evaluation: using modern Python GUI libraries for multi-platform app development
================================================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, GUI, Windows, Linux, MacOS

To check
--------

- reakcja GUI na jakieś asynchroniczne zdarzenie
  - z innego wątku/event loopa
  - z innego elementu GUI
- zadanie:
  - muszę coś kliknąć albo otworzyć plik
  - pojawia się zdjęcie, zaznaczam coś na nim, wyświetlam kąty, najlepiej na obrazku
  - mogę je otworzyć znowu ze wszystkim zaznaczonym
  - drugi ekran z listą pacjentów
- ile zajmuje apka na windowsie? Czy da się spakować?
- przeskakiwanie tabem lub strzałkami po elementach gui?


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
