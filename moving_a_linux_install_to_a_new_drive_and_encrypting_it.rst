Moving a Linux installation to a new drive and encrypting it
============================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux, computer_maintenance

Plan zakłada zrobienie obrazu dysku kiedy system jest wyłączony (zbootowany z pendrivea albo innego systemu),
stworzenie zaszyfrowanego kontenera z tą sztuczną hierarchią partycji i zgranie aktualnej partycji tam.
Potem naprawienie GRUBa (on leży na partycji EFI) i wszystko powinno śmigać.

Zaczynam od zrobienia pełnego obrazu dysku z m2 na zewnętrzny.
Gdybym miał jakąś przejściówkę do m2 to mógłbym włożyć nowy dysk i po prostu przekopiować.
Widziałem tylko m2 do sata, ale dla tych słabych m2. Wiem, że interfejsy są inne i musiałby być jakiś aktywny adapter,
ale zastanawiam się dlaczego to nie powstało.
