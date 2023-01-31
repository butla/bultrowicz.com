Evolutionary code design and refactoring
========================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, quality_assurance, refactoring

Ewolucyjne podejście do refactorowania i wydzielania kodu - kawałek może rosnąć, dopóki nie jest "unwieldy".
Potem można go rozdzielić.
Albo jak dwie rzeczy chcą robić coś podobnego, to wtedy można wydzielać części wspólne kodu.
Nie najpierw pisać wspólną funkcjonalność, kiedy mamy jedno użycie.
Dopiero później, przy faktycznych przykładach będziemy widzieć co nadaje się do wydzielania.
Nie ma co się nad tym zastanawiać przed czasem.
No chyba, że boimy się, że kolejna osoba, która będzie zmieniać kod tego nie ogarnie.
(Ale może ten problem trzeba ogarnąć jakiś inaczej)

Don't write empty base classes. If you'll need base classes later, then write them then.
Base classes might be a bad idea anyway
https://hynek.me/articles/python-subclassing-redux/
https://www.sicpers.info/2018/03/why-inheritance-never-made-any-sense/

Don't write code without function, unless it's needed to communicate where you wanna go with the code.
Just be cautious about making assumptions about the future and the future direction of the code.
Maybe in a few weeks or months, as the code matures (and you with it :) ), your visioun of the future will change.
