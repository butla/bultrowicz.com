There's always time for testing in a software project
=====================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, quality_assurance

Ok, maybe not if you're doing a hackathon, or if the project's gonna last a week,
but I'm not really sold even on that.

Nie ma czasu nie dbać o jakość: dev-QA-infra synergy
There's always time for quality - dev-QA-infra synergy

First off: not doing tests wastes your time, overall.

Nie dopuszczać do gnicia tech debt. Jakiś bandwidth musi być co sprint. Ilość tech debt (w story pointach, np.)
musi iść w dół, nie w górę.

Masz już projekt a testy kuleją - co robić?
- Apke musi się dać prosto odpalić - dokeryzacja, migracje.
- bardzo zgrubne testy dotykające dużej ilości kodu. Potem można refactorować jak już się ma te duże testy.

Testy po deploymentach

Seriously, if your project will take more than around 2 months (maybe even 1 month, my math isn’t very specific here)

przyjazne continuous testing / testability |  that makes you faster as you go

Targeted at mid-to-senior devs, managers, everybody who has input into ordering tasks on a software project.

Jeśli nie macie nikogo, kto umie narzędzia, to albo łapcie kogoś do teamu szybko, albo ktoś (od razu) zaczyna się
uczyć CI, Pulumi, testów. No ale jak tego nie macie, to jest to sygnał, że team nie jest dobrze zbudowany, według mnie.

continuous testing from day 1 makes all the difference, but you can start testing at any point.
Build very high level ones.

If you don’t have reproducible builds, and you don’t have tests, it's very bad.

Quality isn't only about testing - monitoring and alerting along with delivering features.


### Lacking quality controls make you slower

Jak nie dbasz o jakość to będzie cię to tylko spowalniać. Na początku jest git. Taki progres.
Ale dopóki jakość nie jest sprawdzana, to skąd wiesz, że to w ogóle działa?
Albo nie wywali się przy obciążeniu?

### Team organization that helps

Definition of done zawiera testy

Dev QA infra need to work together. It's best if you have delivery teams with all the capabilities.
Not a dev team, a QA team, an infra team.

Testing by other people has a huge problem - the code might be written so it's hard to test.
You should have separate testers, but these should be high level tests.
Or exploratory tests (if they find something, then the devs can replicate the tests in code)

### Misalignment is chaos

Misalignment - separate silos for dev/test/infra.

### Testing is important

Brak testów to chaos - raz na jakiś czas coś się wywali.
Planowana robota musi iść w odstawkę.
Naprawa niewiadomo ile zajmie. Czasem są "fixy", które czegoś naprawdę nie łatają i się ciągną.
Robisz krok do przodu i krok do tyłu przy developmencie wtedy. A tak to idziesz tylko do przodu, jak Moloch w Neuroshimie. Stabilnie.
