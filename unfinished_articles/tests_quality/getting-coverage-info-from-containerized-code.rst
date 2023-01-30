Getting coverage info from containerized code
=============================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, quality_assurance

Do aplikacji muszą przychodzić sygnały, żeby były odpalone atexity (opisane tu
http://coverage.readthedocs.io/en/coverage-4.4.1/subprocess.html#signal-handlers-and-atexit).

Tutaj coś przydatnego o sygnałach w aplikacjach:
https://medium.com/@gchudnov/trapping-signals-in-docker-containers-7a57fdda7d86

Te zabawy z sygnałami wszystkie powinny działać na Unixach. Ja robię na GNU/Linuxie
(poprawna nazwa systemu, który ludzie, wliczając mnie, nazywają Linuxem; ale trzeba oddać
hołd Stallmanowi i całemu GNU, za wysiłek, którego dokonali).

Po pierwsze trzeba albo mieć zarejestrowany handler na SIGTERM (normalny, łagodny sygnał
zabicia). Robi się to przez signal.signal(signal.SIGTERM, handler) (link do dokumentacji).

Normalnie Python ogarnia SIGINT (ctrl+C) zamieniając go w KeyboardInterrupt.
Możecie powiedzieć Dockerowi albo docker-compose, żeby w celu łagodnego zabicia nie wysyłali
doomyślnego SIGTERM, a SIGINT dodając do Dockerfile'a ``STOPSIGNAL SIGINT``
(https://docs.docker.com/engine/reference/builder/#stopsignal), albo ustawiając to samo
w docker-compose (https://docs.docker.com/compose/compose-file/compose-file-v2/#stop_signal)

Generalnie wystarczy albo odpalać Pythona przez CMD command (to w nawiasach kwadratowych),
albo używać execa. Opisane też tutaj
https://docs.docker.com/engine/reference/builder/#exec-form-entrypoint-example

Można się opierać przed dodawaniem coverage do produkcyjnego, nie testowego kodu.
Wiem, że pewnie ze jakiś czas temu, kiedy byłem bardziej purystyczny a mniej pragmatyczny
sam bym to robił. Ale wbudowanie w kod możliwości introspekcji, która na dodatek nie
będzie mu w żaden sposób szkodzić, kiedy będzie chodził na produkcji, chyba nie jest zła.
To tak jak symbole debugowe przy kompilacji C. Nic nie spowolnią, zajmują co prawda ciut
miejsca, ale mogą się przydać. I często się przydają.

Commits fef56c678df40ebe1a83cac79c93330795d2ae31 and a07a4c66e56538dbe8f57ba020b34e1a9b292126

