
Pinning requirements vs. keeping them updated
=============================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python

allgreed [Yesterday at 3:53 PM]
in #python
@P. Sto Tak, ale wtedy trzeba manualnie lurkować update'y, bo czasami są znajdowane luki i wtedy klops, bo ktoś używa niezabezpieczonej werjsi paczki ;)


10 replies
P. Sto [18 hours ago]
True, dlatego zazwyczaj jedziemy na najnowszych i hardkodujemy wersje tylko wtedy, jesli pojawia sie jakig powazny bugol, albo zmiana wywolana przez libke wymaga od nas wiekszych zmian a nie ma na nie w tej chwili czasu.


butla [16 hours ago]
@P. Sto @allgreed A ja bym powiedział że powinno się bezwględnie przypinać przypinać każdą wersję biblioteki w drzewie zależności. Też zależności testowe (pytest, jego pluginy pylint, coverage). No chyba, że ktoś lubi marnować czas i pieniądze na naprawianie losowycyh błędów na produkcji lub wyjebujących się buildów w CI :slightly_smiling_face:

@allgreed Jeśli chodzi o monitorowanie update'ów pod kontem dziur bezpieczeństwa, to są usługi w stylu https://requires.io/ i Gemnasium.
requires.io
requires.io | Monitor your dependencies
Stay Up-to-date! Stay secure! Requires.io monitors your Python projects dependencies, and notify you whenever any of your dependency is out-of-date or outright insecure.
 


allgreed [16 hours ago]
I Snyk!


butla [16 hours ago]
o, nie znałem, dzięki


upgrade [2 hours ago]
+3 do shitstorm - a ja uważam że to bardzo zależy. W przypadku np. aplikacji webowych, a szczególnie w czasach dockera, packera i wypalania AMI tudzież obrazów na inną chmurę według mnie lepiej jest mieć requirementsy zawsze nastawione na najnowsze. Dlaczego UPGrade chcesz marnować pieniądze ? Po co ci ten ciągły process naprawiania czegoś? Otóż po to właśnie mam CI. Aby po każdym commit sprawdził wszystko , puścił unity i funcjonalne testy, zbudował "artefakt" jakim jest obraz dockera dla przykładu, i ten obraz wypchnął. A jak coś się sypnie, to to naprawie w procesie "developmentu" jakiegoś "ficzera". Tak, marnuje czasem trochę czasu, ale wiem że moja aplikacja przynajmniej w obszarze zależności jest wolna od długu technicznego. Zbyt wiele razy widziałem projekty gdzie nie da się podnieść wersji jakiejś biblioteki bo za dużo już teraz kodu trzeba było by orać, więc robi się hacki, które emulują rzeczy poprawione w frameworkach w nowych wersjach. 

Inny zupełnie temat - tworzenie bibliotek. Tutaj problem jest dużo większy gdyż jeśli ustawimy ==1.0.0 w naszej zależności, to nasza biblioteka może kolidować z inną biblioteką której inny developer chce użyć ktora na tej samej wspólnej zależności ma ustawione >=1.1.0. Tutaj powstaje problem jak testować libki? Czy instalować je i odpalać testy w wersjach minimalnych jakie mamy wpisane, + najnowszych? Czy może jeszcze w pośrednich? Przemnożyć to przez wersje pythona? Wiem że tox tutaj pomaga  i np taki trawis CI ma wbudowane opcje do właśnie tego rodzaju testów. 

Reasumując mój "wall of text" wydaje mi się że przy tej dyskusji pominięty został najważniejszy element - kontekst. Czy mówimy o bibliotece, apce, i dla kogo jest skierowana :slightly_smiling_face:


upgrade [2 hours ago]
o ch### naprawde wall of text... dopiero ogarnąłem jak nacisnąłem enter  :stuck_out_tongue:

upgrade [1 hour ago]
(ps moja wypowiedz głównie kierowana była do @butla :stuck_out_tongue: )

butla [1 hour ago]
A, zapomniałem dać adnotacje, że chodzi mi o zależności do aplikacji. Tak, przy bibliotekach nie wolno dawać konkretnych wersji.

A co do rośnięcia długu związanego z niepodciąganiem wersji, to tak, jest to ważna rzecz. Ale według mnie lepiej używać usługi która monitoruje zależności i robić update np. raz w tygodniu rano (można sobie ustawić cykliczne wydarzenie w kalendarzu). A nie w środku nocy, kiedy szef robi demo w Stanach, chce wypchnąć drobną zmianę, a coś się mu gdzieś wypierdala, bo jakaś biblioteka postanowiła walnąć regresję.

Jak wiem, że mam całkowicie powtarzalne buildy/deploymenty to dosłownie mogę spać spokojnie :slightly_smiling_face:. Fakt, że moje problemy zaostrzają się przez nasz styl pracy - kilka projektów zmienianych w nieregularnych odstępach czasu przez ludzi w innych strefach czasowych.

Co do medytacji nad powtarzalnymi buildami itp, to polecam Continous Delivery (książkę). Była pisana jeszcze przed chmurową rewolucją (2007, chyba), ale goście w niej sensownie kminią (choć nie zgadzam się że wszystkim, oczywiście).

@upgrade A oto moja ściana tekstu stworzona na kiblu :grin:


butla [3 minutes ago]
Jeszcze więcej przemyśleń i kontekstu:
- Mam mały team, więc czas jest bardzo cenny
- docker + CI dają odtwarzalność buildów, bo możesz zobaczyć co dokładnie jest w image'u, ale nie dają powtarzalności, bo nowy build może się wyjebać
- nieprzypinanie zależnosci pogarsza jakość testów

Więcej o tym ostatnim punkcie z testami. Jak pewnie wiecie uwielbiam swoje testy i lubię, kiedy dają dużo pewności, że aplikacja będzie faktycznie działać na produkcji. Zdarzyło się parę razy, że coś miałem nieprzypięte. I teraz taki scenariusz, który naprawdę miał miejsce: inny ziomek, który też ma mało czasu chce zmienić małą pierdółkę. Dodaje unit testa (bo indoktrynuję wszystkich o tym, jak ważne są testy), puszcza toxa i wypierdala się coś niezwiązanego z tym co robił. I teraz myśli sobie - ej, te testy to są zjebane i w sumie nie można na nich polegać, Michał, zjebałeś. I ma racje.

Myślę o testach jako o aplikacji dla delevoperów, którzy nie zawsze muszą być bardzo ogarnięci w danym projekcie. Jeśli aplikacja losowo się wypierdala, to jest z nią coś nie tak.

Updatowanie zależności jest ważnym problemem, ale myślę, że nie lepiej go nie rozwiązując generując inny problem :slightly_smiling_face: Będę musiał ogarnąć współpracę Pipenva i Pipfile'a z Toxem, bo te dwa pierwsze właśnie mają bardzo ładny model analizy i przypinania zależności. Teraz jak chcesz zupdatować zależności w requirementsach to jest to wykonalne przy użyciu paru komend pipa i może tyci Bash-fu, ale nie jest proste dla każdego. Też komplikuje to podział na zależności produkcyjne (normalne requirements.txt), testowe (requirements-test.txt) i deweloperskie (requirements-dev.txt, jedyne, których nie przypinam, bo nie mają wpływu na działanie kodu i testy; np. ptpython, pipdeptree), bo nie można zrobić po prostu upgrade i `pip freeze > requirements.txt`

Kurde, dobry materiał do rozkmin na blogasku :slightly_smiling_face: Muszę wrócić do jego pisania. Mam pełno draftów, a nic nie opublikowałem od półtora roku :smile:


butla [2 minutes ago]
Te same uwagi co o testach (że nie powinny się wypierdalać) oczywiście też powinny się tyczyć deploymentu.

https://before-you-ship.18f.gov/infrastructure/pinning-dependencies/
