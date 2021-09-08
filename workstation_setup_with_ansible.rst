Workstation setup with Ansible, the hu(/a)ssle
==============================================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux, system_administration, automation, journal

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

this is also a guide to my setup for people who are looking for guidance or inspiration.

some distilled articles may come from this in the future, but not just yet. Other priorities.

these will be a bit just like stream of consciousness.
It'll have random stuff, might be hard to comprehent and it'll be hard to get through.
But hey, maybe it'll benefit somebody :) And it won't take me too long to push this out.

The Ansible script coming out of it will be a better thing to study, I think.

Log / journal
-------------

(Log powinien mieć kawałek specjalnego HTMLa tłumaczący, czym jest, że to zapiski tego co robię, z których powstaje post.
Jak robi te swoje kropki Hynek?)
Funny, that these were kept by travellers (journal, journey)
or sailors (logs, wonder if they were written on logs first xD).


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
Carrying on with ranger config updates - created default configs,
comparing them to mine with ``meld``.

  - that should be done every now and then - post about it?

Nope, can't finish ranger, gotta set up my aliases and functions so I can use the computer more normally.
``$ meld .zshrc .zshrc.the_link``
``.zshrc`` is what Manjaro Architect set up for me when I said I wanted ZSH as my shell.
It gives me Powerline with nice command statuses and execution times
(something I was getting with plugins from Oh My ZSH).

I want to merge that into my config later, but I need stuff in the shell to work right now, to help me with my actual work
(automation of my work setup creation - including "stuff in the shell").

How much more time I'm spending on this (writing down the "log" / diary) compared to how much time I would spend doing
just the Ansible and immediate manual setups (that will be added to Ansible by the time I'm done)?

But maybe, if I wanna blog, then keeping this "log" will be a quicker way of pushing out my "content"
(I have Luke Smith saying that in my head now).
The slower way would be what I usually do, which is edit the posts to make them as succinct and information-packed as possible. Sometimes, at least :)
I would like to rant a bit more, from time to time, though...
People sometimes enjoy these (rants) in real life.

I have to keep the log in tidy English, though. Like I would use when I was writing to a work colleague.
That requires bits of editing, but, I try to just do them per paragraph.
Once the paragraph is done, it's done (at least that's the approach I'm testing in practice right now :) ).

What I normally use in my personal notes is this weird mix of Polish and English.
You know, some thoughts flow quicker in English, some in Polish.
Depends on where I have the most practiced vocabulary :)

Keeping a log (with exact bits of scripts) should be a good way to backtrack during a debug session.
Can't do that if you're in an emergency that requires urgency, though.
Guess you can look at your shell history if you need to backtrack in those situations.

Anyway, back to the ``**meld**``.
I'm getting everything from my config that will be useful, but will not break.
So probably that'll be everything like basic settings, and scripts and aliases from my
`configs_and_scripts <https://github.com/butla/configs_and_scripts>`_ repo.
Still, that'll be a lot of help :)

That's how the file looks like now::

    # Use powerline
    USE_POWERLINE="true"
    # Source manjaro-zsh-configuration
    if [[ -e /usr/share/zsh/manjaro-zsh-config ]]; then
      source /usr/share/zsh/manjaro-zsh-config
    fi
    # Use manjaro zsh prompt
    if [[ -e /usr/share/zsh/manjaro-zsh-prompt ]]; then
      source /usr/share/zsh/manjaro-zsh-prompt
    fi

    # Butla config
    # If you come from bash you might have to change your $PATH.
    export PATH=$HOME/bin:$HOME/.local/bin:/snap/bin:$HOME/.local/lib/node_modules/bin:$HOME/.cargo/bin:$HOME/go/bin:$PATH

    export EDITOR='vim'

    # enable vim mode
    bindkey -v

    # normal delete and backspace with VIM mode
    bindkey "^D" delete-char-or-list
    bindkey "^?" backward-delete-char

    source ~/.config/zsh/aliases.zsh
    source ~/.config/zsh/functions.zsh

    # fd configuration, mainly so that FZF works more to my liking
    export FZF_DEFAULT_COMMAND='fd --type f --hidden --follow --exclude .git'

    # if less than one screen worth of output, just print it on stdout
    # Without this Git on ZSH was trying to put everything through a pager.
    export PAGER="less -F -X"

Huh, I noticed that my old config has this note in it::

    # TODO remove after alacritty fix? https://github.com/jwilm/alacritty/issues/2515
    # Needed to make apps start in the foreground
    unset DESKTOP_STARTUP_ID

Shitf+clicked the link above with Alacritty :)

Looks like `it got fixed <https://github.com/alacritty/alacritty/pull/2525>`_, merged into master on Jun 16, 2019,
so I bet I have that installed :)
And basically, they do that for me, so I can remove the code bit. Also, I won't be using KDE anymore.

Removed that bit of config while in ``meld``. ``configs_and_scripts`` repo notices the update because of the link.
Saved both the files (both got updated) and closed ``meld``.

Installed ``xsel`` so I can copy file names from my ``ranger`` in my "development view", while writing this post.
Need the copy, so I can paste image file paths into ``workstation_setup_with_ansible.rst`` with ``nvim``.
installed_xsel.png

.. image:: /_static/workstation_setup_with_ansible/installed_xsel.png

Now, I can paste the previous images I wanted to paste :)

So the one confirming that ``configs_and_scripts`` got updated when saving with ``meld``:

.. image:: /_static/workstation_setup_with_ansible/zshrc_is_updated_in_configs_and_scripts.png

And the one showing the diff itself:

.. image:: /_static/workstation_setup_with_ansible/zshrc_is_updated_-_the_diff.png

My work setup is slowly coming back to life :) Better than ever. Such a great feeling.

I had to find (remind myself how to) input images into `.rst` files :) With `ag` ("the silver searcher"), BTW :)

Ok, and now I wanna keep looking at my post, see how the images I've look.
So I'm gonna run some make commands in additional ``tmux`` panes:

.. image:: /_static/workstation_setup_with_ansible/tmux_panes_with_rebuilding.png

Oh shit, I need ``entr``... Neverending story xD I need that Ansible to never go through this again :)
Well, maybe for a few years, at least. And I'll have a better base for the new automation :)
Or maybe, I'll really keep updating it throughout the years.
Or I'll just never leave Manjaro :D Just keep expanding the script to more OSes
(wanna play around with Qubes on an additional partition).

``$ sudo pacman -S entr`` nice, it's in the ``community`` repos now.

Oh no! I need virtualenvs for the rebuilding to work xD
Ok, I gotta order food :) (time: 12:31+02:00)

Food will be ready for 14:00, around the time Monika (ze wife) comes back from work.
New restaurant opened at 7-minute-walk distance. Please God, let it be a good one :)

Back to no virtualenvs for rebuilding.
Had to run these to get the virtualenv running and activating without going through the ``virtualenvwrapper`` install just
yet (Ansible will do it later)::

    mkdir ~/.virtualenvs
    python -m venv ~/.virtualenvs/bultrowicz.com
    . ~/.virtualenvs/bultrowicz.com/bin/activate

Oh! Vim indicator is working in this Powerline setup! This is so nice :) I gotta have it.

Now that I'm in an activated virtual env (and I have ``fd`` and ``entr``), my ``make`` commands should run!
...Yeah, I need to install the python dependencies first :)::

       ~/dev/bultrowicz.com    master +2 !2 ?5  which pip
    /home/butla/.virtualenvs/bultrowicz.com/bin/pip
       ~/dev/bultrowicz.com    master +2 !2 ?5  pip install -r requirements.txt
    Collecting ablog==0.10.17
      Downloading ablog-0.10.17-py3-none-any.whl (55 kB)
         |████████████████████████████████| 55 kB 1.3 MB/s
    Collecting alabaster==0.7.12
      Downloading alabaster-0.7.12-py2.py3-none-any.whl (14 kB)
    Collecting Babel==2.9.0
      Downloading Babel-2.9.0-py2.py3-none-any.whl (8.8 MB)

I wonder how powerline fonts will get rendered after pasting into an ``rst`` code snippet...

``$ make build_continuously`` is working! I'm fixing the issues cropping up in this file there.
Once my NeoVim setup is done, I'll get these in the editor, directly.

13:01, time to get up from the computer, stretch (just a few seconds), and do some house chores :D
Hungry now, just had some apple today. Bao incoming in about 1h15m :)

Unpacking new "gear": window washer (for the dirty, Silesian windows) and a USB-C to micro-jack adapter,
for my sad Samsung phone (why did they have to go the Apple way?).

Need some music::

    yay spotify
    # picked: `3 aur/spotify 1:1.1.67.586-1 (+2219 31.11)`

And it's running. Logged in with data from ``keepassxc``.

I need my ``git`` aliases, so installing ``fzf``: ``$ sudo pacman -S fzf``.

Pushed ``configs_and_scripts`` `updates <https://github.com/butla/configs_and_scripts/commit/88776732be23242f3ef40f97a97325b8cc30bbc7>`_ with ranger stuff to ``origin``.

Checking if ``ranger`` is fine on the other laptop...
It wasn't. Ueberzug was crashing because of failing to load ``PIL``.
Turns out I had an outdated AUR package - ``python-pillow-simd`` - providing Pillow, instead of the usual ``python-pillow``.
Installed the latter, it replaced the former, everything is dandy.

TODO
----

- install Ansible
  - jakie są teraz best practices?
  - mieć wiele pliczków, każdy robiący dyskretną rzecz i na końcu ją jakoś testujący?
  - rób już w Ansiblu wszystko, dodawaj jak robisz (pisz to w logu), odpalaj Ansible na huwaweiu
- move machine_configs to github and make it public. Rename as machine_setup. Does it have private files in history?
  - maybe history needs to be dropped because of the private files
- set up ZSH (.zshrc)
  - keep powerline with process times and status
  - co jest potrzebne, żeby zainstalować powerline na huwaweiu?
- vim/zshrc config - wyświetlanie trybu VIMa działa z powerlinem. Nie spodziewałem się, że Powerline'owe prompty tak ładnie się chowają jeśli trzeba
- change XFCE theme while looking at what a config window is changing with strace, add those config to ``configs_and_scripts`` (blog post out of that)
  - hide window headings
- skrypt datee dający mi datę w formacie jaki lubię (i wrzucający do schowka), do zapisków
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
- przejrzyj log i zobacz co ijak było instalowane
