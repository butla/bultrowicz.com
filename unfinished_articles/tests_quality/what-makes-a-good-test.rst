What makes a good test / What's the purpose of testing
======================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, quality_assurance

What's the purpose of tests? / How do good tests look? / What makes a good test.

What tests should be. What they don't need to be.
Writing stuff out

This doesn't exhaust all of my thoughts on the matter, but I wanted to push something out into the world.

TODO: look at some results from Google about good tests, the test pyramid, etc.

Nieposortowane
--------------

Reality is nuanced.
I'll focus on functional testing here (functional testing sometimes means e2e testing, that can be confusing, I know).
My view (stole that idea from someone on the Internet, I bet) is that tests make sure that some more
obvious (obviousnessness can be a wide spectrum) paths in the code work.
They also provide value by finding issues with the code (these can be functional or not).

Code is the source of bugs. Less code, less bugs :)


What should tests do, the purpose of testing
--------------------------------------------

Testy mają znaleźć nieprawidłowości w kodzie, który piszesz zanim kod trafi do użytku. Według mnie.

Jeśli test znajduje błędy to dobrze. Nawet jeśli nie jest dość "narrowly scoped".

Tests should prove that the code is doing what you want it to do (functional testing). And that it performs at expected levels, or has some required characteristics (non-functional tests). More or less. That's the ideal, at least.

Proving the code is correct with 100% certainty would be nice, but I don't know if that's possible. Proving correctnedd is the domain of both tests and functional programming (Haskell, Prolog, maybe Scala). You don't have to use a functional language to write functional code, BTW. Not having side-effects and long-lived state goes a long way to increase testability. But you'll have some advanced features in the languages dedicated to functionality.

Untested code can't be trusted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

bycie adwokatem diabła. Testy dla kodu. Napisałem koparkę, która robi 1BTC dziennie. Serio? "I'm fast at math, just not accurate." Pokaż. Udowodnij? Sam sprawdź dla siebie. Ale zademonstruj dowód.

Tests make you faster
~~~~~~~~~~~~~~~~~~~~~
Pisanie testów zjada czas. Ale jest efekt kuli śniegowej. Jestem coraz szybszy, pewniejszy, potężniejszy.



Make false positives highly improbable
--------------------------------------

W sumie czym jest test? Jak dobrze go ustawisz (żeby ciężko było o false-positive), to testy i kod nawzajem o siebie dbają. Żadnego nie dosięga bit-rot. Oba są zdrowe. No i kod robi to, co miał robić - to najważniejsze. JEŚLI testy są poprawne. To wymaga umiejętności, niestety. A zyskanie umiejętności wymaga praktyki i wyzwań.



Product code and test duality
-----------------------------

Testy - dualizm jest ważny. Jak w adversarial neural networks. Czy w każdym "wyścigu zbrojeń". Obie strony stają się silniejsze.
Ying yang.

Tension between things is needed.

The dualistic, antagonistic system. Making both better. Coevolution. The arms (challenges) race.

TDD jak klasztor. Miałem rację w tej dawnej pogadance. Dążenie do perfekcji. The power of incremental improvement.

Testy muszą rzucać wyzwanie dla kodu. Ten kod ma robić X. Sprawdź, że X się stało. Najlepiej jakoś niezależnie.
Łatwiej jest mieć kod funkcjonalny. Bo X jest zwracane.
I możesz zobaczyć, że zwrócone X jest tym, czego się spodziewałeś.
Ale rzeczy trywialne w stylu ustawiłem stałą, sprawdźmy jej wartość raczej nie mają sensu.


What about some common advice?
------------------------------

Single assert per test
~~~~~~~~~~~~~~~~~~~~~~

Też nie mieć twardych zasad w stylu jeden assert na test. Oszczędność czasu, pragmatyzm, yagni.
Keeping that single assert rule might give you a needless excess of test code, or might make the test suite too long.

Test only one thing - good, but sometimes it's pragmatic to have broader tests.

Had some heated debate about this in the past ;) (pozdrawiam Kubę)

Full repeatability
~~~~~~~~~~~~~~~~~~

Według mnie testy nie muszą być w pełni "repeatable" (full setup and teardown all the time).
Jeśli twoje testy są chaotyczne i niestabilne, to znaczy, że twój kod jest chaotyczny i niestabilny i trzeba go ogarnąć.
Niepisanie / nieutrzymywanie testów to jak zamiatanie rzeczy pod dywan.
Fakt, możesz nie dawać sobie rady z problemami w kodzie / nie ogarniasz jak napisać dobrze testy.
W takim razie - ucz się. Czytaj. Ćwicz. Aż będziesz umiał.
Podobał mi się mój tekst z przezentacji o TDD - TDD trzeba żyć. Jak mnich.
Czasem można naginać reguły.
Ale pokrycie sensownymi testami zawsze pomaga.

Test pyramid
~~~~~~~~~~~~

You don't really need more unit tests than other tests. That depends on your code.
E.g. if you're doing a lot of different communications with external systems, like a DB or hardware,
then it might make sense to have lots of integrated tests.


Bad tests
---------

Oczywiście mogą też być szkodliwe testy (np. te wypełnione mockami albo mirror tests - o nich osobny post - kinds of bad tests)

Nie, mirror-tests (sprawdzam, że odpaliły się linijki kodu) nie mają dużej wartości według mnie. Utrudniają zmiany w kodzie, to jest ich "feature". Więc dają Ci może chociaż to, że nad każdą zmianą musisz się zastanowić dwa razy, bo robisz ją dwa razy. Tą samą zmianę. Przykład mirror testu - zawołałem funkcję subprocess run z takimi parametrami. Przykład testu sprawdzającego, że coś się stało - odpal proces i zobacz output. O, ale to zabiera dużo czasu! Unit testy nie powinny odpalać innych procesów! Nie wszystkie testy muszą być unit testami. Testy powinny mieć ten poziom (unit/integrated/external) jaki jest dla nich odpowiedni.
Trello - stop writing "mirror tests".
Mention them, but redirect to the separate article.
