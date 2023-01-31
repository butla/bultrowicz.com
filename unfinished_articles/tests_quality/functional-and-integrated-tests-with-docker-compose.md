---
blogpost: true
author: Michał Bultrowicz
language: English
tags: Python, quality_assurance
---

Functional and integrated tests with Docker Compose
===================================================

Using containers (docker-compose with Docker, to be specific; it's not only docker) in tests revolutionizes not only QA,
but also the way you develop (and even design) software.

If you can reliably test more. You can really treat external apps as part of your app. Like DBs. Or Redis.

Some patterns (like ORM because it lets you test) become less appealing, as well. Show the tests with triggers.
Why bother? Locking is good, etc.

Pokaż od razu na przykładzie SQLowej bazy (postgresa), żeby było trochę trudniej.
Jeszcze integracja apek przez kolejkę z redpandą???
Albo Redpanda zamiast SQLa (w miejscu tworzenia kolejek możecie np. puszczać migracje bazy).

Follow up do moich rzeczy z 2016. Widzę, że nadal się nie zestarzały bardzo.

Testy z composem powinny używać tylko zewnętrznych interfejsów.
No, czasem trzeba się trochę namęczyć, żeby strzyknąć faile. Ale często można to wykombinować.
Np przez wstrzykiwanie złych rzeczy do DB, kolejki, mountebanka.

Kod wrzuć gdzieś w experiments. Folder `testing__qa`.

O testach w CI też napisz.

Funkcjonalne testy z composem powinny używać tylko zewnętrznych interfejsów.
No, czasem trzeba się trochę namęczyć, żeby strzyknąć faile.
Ale często można to wykombinować.
Np przez wstrzykiwanie złych rzeczy do DB, kolejki, mountebanka.

Używanie jak największej ilości produkcyjnego kodu w testach.
Jeśli coś jest trudne do testowania, to można tymczasowo zastępować jakimiś fakeowymi implementacjami
(clean architecture) i dla testów configurować odpowiednio.
