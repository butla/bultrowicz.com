Workstation setup with Ansible
==============================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux, system_administration, automation

Long time ago I created an Ansible script for setting up my machine.
I didn't keep it up to date and I thought it didn't make sense to maintain it, since I
had multiple OSes (Kubuntu and Manjaro).
But now that both my computers are on Manjaro I decided to try this trick once more to create
something that will allow me to just turn any Manjaro install into my workstation.

Before I had dreams of making that script support multiple OSes, that dream is still holding on.
Though I won't implement that just yet :)

Ansible has changed and I have changed, so I'm giving this another try.

Na tym Europythonie kiedyś już miałem pomysł configów w ansiblu.
Powiedziałem to jako komentarz po prezentacji, łysy koleś z brodą z Londynu mi przytaknął.

NixOS służy do tego samego co mój Ansible (utrzymywanie konfiguracji systemu w kodzie), i może robi to lepiej,
ale nie jestem gotowy przerzucać wszystko na NixOS.
Ansible jest jednak troszkę bardziej uniwersalny. Mogę używać go do wielu systemów.
Chociaż oczywiście byłoby super, gdyby producenci dystrybucji i programów szli w stronę configów,
które łatwo trzymać w gicie, i ogólnie prostej konfiguracji wszystkiego przez pliki, idempotencja też by była przydatna.

Log
---

(Log powinien mieć kawałek specjalnego HTMLa tłumaczący, czym jest, że to zapiski tego co robię, z których powstaje post.
Jak robi te swoje kropki Hynek?)

**2021-09-07**
What I've installed:

- mpv
- everything in the bootstrap script
- ranger
  - atool: for previews of archives
  - file: for determining file types [installed]
  - highlight: for syntax highlighting of code
  - libcaca: for ASCII-art image previews [installed]
  - mediainfo: for viewing information about media files
  - poppler: for pdf previews [installed]
  - python-chardet: in case of encoding detection problems [installed]
  - ueberzug (even though ranger mentions "python-ueberzug", that doesn't work, because it's under different python): w3mimgdisplay alternative
- the_silver_searcher
- dropbox
- dropbox-cli
- base-devel
- keepassxc

**2021-09-08**
- carrying on with ranger config updates - created default configs, comparing them to mine with ``meld``
  - that should be done every now and then - post about it?

TODO
----

- ranger - czy mogę wyjebać scope.sh? czy kiedyś go zmieniałem?
  - push configs_and_scripts
- skrypt datee dający mi datę w formacie jaki lubię (i wrzucający do schowka), do zapisków
- install Ansible
  - jakie są teraz best practices?
  - mieć wiele pliczków, każdy robiący dyskretną rzecz i na końcu ją jakoś testujący?
  - rób już w Ansiblu wszystko, dodawaj jak robisz (pisz to w logu), odpalaj Ansible na huwaweiu
- move machine_configs to github and make it public. Rename as machine_setup. Does it have private files in history?
  - maybe history needs to be dropped because of the private files
- set up ZSH (.zshrc)
  - keep powerline with process times and status
  - co jest potrzebne, żeby zainstalować powerline na huwaweiu?
- change XFCE theme while looking at what a config window is changing with strace, add those config to ``configs_and_scripts`` (blog post out of that)
  - hide window headings
- alacritty doesn't render to the side - some XFCE scrollbars? To samo ma huawei
- xfce favourites menu
- clock style
- autostart signal, (maybe slack, and discord?)
- xfce panel - get rid of workplace switcher?
- go through TODOs in machine_configs
- signal settings
- mention manual steps if the respective packages has been installed
  - Brave - enable sync for everything
  - Signal - sync with the phone
  - Dropbox - log into it
- keepassxc roaming config file kept in git https://github.com/keepassxreboot/keepassxc/issues/2666
- image viewer solution:
  - gthumb - solve zoom in problem (https://gitlab.gnome.org/GNOME/gthumb/-/issues/103)
    - sprawdź ``man gthumb``, może tam jest o pliku konfiguracyjnym
  - use gwenview but fix video playback to start immediately. How to skip to next if there's a video?
