Workstation setup with Ansible, the hu(/a)ssle
==============================================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux, system_administration, automation, journal

I was moving from my old Kubuntu 18.04 to Manjaro on my main workstation computer
(Alienware 15R3, now practically always docked on my desk (like the Mothership after the first Homeworld (TODO link)).
I decided to finally fully write down and automate that process.
So that setting up any new system won't be a hassle, because I'll be able to just tweak Ansible scripts.

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

This post is sort of a "journey" through my work/thought process.
These will be a bit just like stream of consciousness.
It'll have random stuff, might be hard to comprehend and it'll be hard to get through.
But hey, maybe it'll benefit somebody :) And it won't take me too long to push this out.

This whole Log thing would work well in a video format...
Gotta give that a try, finally. Maybe next log will be in video format.
I hope I won't spend too long editing :)
Gotta do some gesture or something when I'm putting in secrets or showing keepass, so I'll know to edit out all of those
instances... Or maybe I should see all the times that I press my keepass shortcut? (Super + 3).
We'll see :) Probably the simple thing with a (hand)signal on the video will be simple enough.
Hope I won't miss anything that way and it won't be too tiring.

The Ansible script coming out of it will be a better thing to study, I think.

Rename to something like "a script for keeping the software and configs of two laptops in sync".

Log / journal
-------------

(Log powinien mieć kawałek specjalnego HTMLa tłumaczący, czym jest, że to zapiski tego co robię, z których powstaje post.
Jak robi te swoje kropki Hynek?)
Funny, that these were kept by travelers (journal, journey)
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

Oh shit, I need ``entr``... Never-ending story xD I need that Ansible to never go through this again :)
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

**2021-09-09**

``$ yay ansible`` -> pick ``1 community/ansible 4.4.0-1``.

Gotta squash the commits in my ``machine_configs`` repo before I make it public.
There might me some encrypted keys there that I might still be using.
It's encrypted so it's not like anybody **should** be able to retrieve them.
But maybe it's better if I don't leave these encrypted blobs on public repos,
for indexing and use (and maybe exploitation) by some future cypher-craking efforts ¯\_(ツ)_/¯
Juuuuuust in case :)

Huh, running my ``shrug`` alias to paste in here - the system detected that I don't have ``xclip`` and offered
to install it. Nice of it to do that :) Oh, but pamac or something can't accept my "acceptation" :)
No stdin attached?::

     shrug              127 ✘  13s   1 
    ¯\_(ツ)_/¯ copied to clipboard...
    The application xclip is not installed. It may be found in the following packages:
      extra/xclip 0.13-3    /usr/bin/xclip
    Do you want to Install package xclip? (y/N)  y
    Executing command: pamac install xclip
    Preparing...
    Synchronizing package databases...
    Resolving dependencies...
    Checking inter-conflicts...
    
    To upgrade (1):
      thunderbird  91.1.0-0.1  (78.14.0-0.1)  extra  66.5 MB
    To install (1):
      xclip        0.13-3                     extra  15.3 kB
    
    Total download size: 66.5 MB
    Total installed size: 21.9 MB
    
    Apply transaction ? [y/N]
    Transaction cancelled.

``$ yay xclip`` -> "1", and then::

    shrug                   ✔  8s   1 
    ¯\_(ツ)_/¯ copied to clipboard...

You'll see it used above :) I do backtrack a small bit in this "log" :)

Ok, so gotta squash the commits, put the repo up on Github.
And then, I'll replace most of the old various machine setup scripts with a single new one for the machine
I'm working on right now (my main workhorse).
Different "machines" are:

- my main machine
- my old Raspberry PI
- some arbitrary in-between ones that might, and might have not, have been used on some cloud instances

If I'll have automation for different machines, it'll be extracted (and refactored)
from the monolithic script for the setup of my workstation.

**squashing commits / pushing to a new repository**

.. code-block::

    ~/development/machine_configs    master !1  git remote -v      ✔  1 
   origin  git@bitbucket.org:butla/machine_configs.git (fetch)
   origin  git@bitbucket.org:butla/machine_configs.git (push)

That's my private repo (now you know it exists, OMG! :) ).

Soft-reset to the first commit of that repo (hell, I'm gonna even leave the message, cause it'll be a nice trace :) )::

    git reset bf8963456ef42a24a0356cfe95ccb9771d724cbe

Stage all the files for the commit::

    git add .

Add everything to the original commit::

    git commit --amend

Now, there's just a single commit::

     ~/dev/machine_configs    master ⇣128⇡1  git log                   ✔  1 
    commit 9599e326ca16836b8b1b632505fd6f309c033e70 (HEAD -> master)
    Author: Michal Bultrowicz <michalbultrowicz@gmail.com>
    Date:   2017-07-02 13:32:12 +0200
    
        Initial commit, moved from Bitbucket with squashing of history
    
        Before Bitbucket, the stuff was at https://github.com/butla/utils

Now, I have to create an empty repo on Github.
I'd like to move everything to Gitlab one day and make Github repos into mirrors,
I don't like Microsoft handling most of the world's open source...

Switch the ``origin`` to the new repo::

       ~/dev/machine_configs    master ⇣128⇡1  git remote set-url origin git@github.com:butla/machine_setups.git
       ~/dev/machine_configs    master ⇣128⇡1  git remote -v             ✔  1 
    origin  git@github.com:butla/machine_setups.git (fetch)
    origin  git@github.com:butla/machine_setups.git (push)

And push it out to GitHub with ``$ git push``.

I also added a note on the Bitbucket repo (in the repo description) pointing to the new repo.
I'm not removing the repo from Bitbucket, in case I ever need to consult the old git log.

----

Man... there's a lot of old TODOs I left for myself in that repo.
It's a bit overwhelming. They'll need to get purged.
I'm either solving the problem or letting it go.
All of the Kubuntu-specific TODOs can go, fortunately.
The ones about config files as well (because of ``configs_and_scripts``).
And a lot of complexity with getting the software (PPAs, downloading and compiling myself),
goes out of the window because of how rich and up-to date the Manjaro (and Arch) repos are.
Also, there's AUR.

The repo right now is basically bitrotten old Ansible for systems I'm not using anymore and a bunch of TODOs and notes.
Well, I gotta change that into Ansible that'll actually run on both Manjaro laptops.

We'll see if it won't be too much of a hassle to keep the laptop's software in-sync with Ansible...
Hopefully it won't, and I'll have a forever-up-to-date resource that can recreate my workstation with one command.
And it'll be the perfect documentation of my setup.

Anyway, gotta create the new blank-slate playbook and start putting everything that's useful from around the repo into it.
Maybe I'll consult the updated Ansible best-practices first...
Dunno if there's a page like that anymore.
Ansible's documentation sure got more confusing. Do I look at "community", "core", or which docs?
There's overlap between them as well...
Well, I guess "community" is the way to go.

They sure added a lot of stuff in. And made commands more clunky with the namespaces
(e.g. ``command`` -> ``ansible.builtin.command``).

Should I even bother with Ansible? It looks like it's gotten so big.
And I probably wouldn't use it in production now (I'd like immutable VMs with Terraform, Docker, Packer).
But maybe there will still be some utility to it.
It looks like you create playbooks and roles pretty much the same way as you did it two years ago
(last time I wrote any Ansible).
So let's see if can create this script in a relatively painless manner.

If not, my setups will just be maintained with bash scripts :)
I do think Ansible is nice with the idempotence (and rerunning not breaking stuff), though.
But maybe the overhead is too big... Dunno.

Ok, starting with a single role - ``main_machine``.
First, just install all the packages I need (I'll gather them from the repo and notes).
Gotta look into the docs to see the Ansible module for that on Manjaro (there was a universal one).

Ok, Ansible is too much to handle for me ATM.
Writing stuff in it requires me to just go the docs too often.
I don't think I need it in my toolbox anymore. So long, friend...
Let's see how will the environment setup look as a Bash script.
I won't be able to just rerun it on both laptops to keep everything in sync, but it probably won't be a big problem
to run the updates selectively.

Woah, Manjaro automatically found my printer/scanner in the local network, and I can scan/print without setting anything up.
So civilized :) I've heard that even Debian got some driverless scanning/printing support nowadays.
Linux is making progress, I guess :)

OK, I've deleted the old Ansible scripts, pulled their logic into the shell script (almost).
This is going to be so much simpler, although I'll need to implement small functions for idempotent setups of certain things, like pulling git repos. I don't have to go too overboard with it, though.
It'll be way easier to maintain than Ansible, I think.

**2021-09-10**

Working on the script.
All of the python tools that I used to install with `pip install --user` I now have taken either from Manjaro repos
(with ``pacman``) or from AUR (with ``yay``).
We'll see if this works well for me. If not, I'll try to use ``pipx`` for maintaining them.

Too bad that ``yay`` `doesn't have an option to skip what it's already installed <https://github.com/Jguer/yay/issues/1552>`_.
I'm working on a workaround for that, though.
My initial idea isn't working for some reason, so I'll leave it for when I have the full setup done.
It looks like I'm only missing NeoVim and ZSH configs, and plugins for NeoVim, ZSH and ranger.

I love how much software is available as packages on Manjaro (and Arch, most probably) and how recent they are.
Finally, a distro that doesn't lag behind the software I use.
Ubuntu did that. And something would always break for me when upgrading the whole OS, so I just stayed with the LTSes.

**2021-09-14**

Rewritten the setup script to Python from Bash because
I've come across something that was problematic in Bash (picking AUR packages that weren't installed already).
That usually happens when you get slightly more complicated logic in scripts.
If it starts looking ugly and/or confusing in Bash, it might be time to switch your script.

**2021-09-15**

I was praising the great number of software packages available and how recent they are on Manjaro.
That's not always the case.
``oh-my-zsh``, for example, has last been updated in January (I know that from ``pacman -Si oh-my-zsh``).
I know that the manual install I have under ``~/.oh-my-zsh`` has updated itself many times since then.
So I guess I'll stick with it. Shame, I'd like to manage as much software as possible with just the package manager.

I'm merging my ``.zshrc`` with the one that was created for me by Manjaro Architect, when I chose ZSH.
I got some ZSH options out of it, and I will get that "powerlevel10k" theme, because it's just awesome - functional
and looking good. I'm discarding everything else.

Weird how I have the powerline fonts and icons on the machine setup with Manjaro Architect without having the packages
(``powerline-fonts``, ``awesome-terminal-fonts``)that provide them on the second laptop.
Looks like Architect has set me up with something non-standard?
It definitely adds ``manjaro-zsh-config`` package, but I don't see any fonts in it.
I should probably compare the installed packages to solve this.

I let powerlevel's config script (``p10k configure``) modify my ``.zshrc``.
I still needed to add sourcing of ``powerlevel10k.zsh-theme`` above sourcing of ``p10k.zsh``.

**2021-09-16**
My Python setup script is taking care of the idempotency on it's own.
Writing the necessary code is more natural and faster for me than dealing with Ansible.
Does it do some things less reliably than Ansible? (Like making sure that the repos I'm pulling are up to date?)
Yup. But it's enough for my use. And I can tweak it however I want without hurdles, browsing the docs, or writing
my own Ansible modules (I am writing my own "module" from the start).

I'm not putting in any tests (and I'm a testing fanatic),
but it won't be a problem to diagnose and fix the code when I'm using it.
Also, I'm the only user.
I am preparing myself for running this on a fresh Manjaro install, though.
I'm running all the code that I'm adding, and most of the changes I make are done with the code.
Sometimes I install/setup stuff manually, then tear it down and let the script do it.

Alacritty (or another terminal emulator) defines what colors like "blue", "light blue", etc. mean, most programs
say they want "blue", "light blue", etc. That's how you can tweak terminal colors in most programs
(ranger, ls, ZSH). You can also choose different colors in those programs.

I finally enabled KeepassXC to be a Secrets Service. That will prevent Brave (or Chromium) and pip from asking
me to put in my password for Gnome keyring every time I use them.
Dunno how to make Brave pull the passwords from KeePass, though, but that's not important now.

Magically, the KeePass on stopped putting temporary local configuration options (window size/position, last opened DB)
into ``~/.config/keepassxc/keepassxc.ini`` and started putting them into ``~/.cache/keepassxc/keepassxc.ini``.
Finally, I won't get any random changes in ``configs_and_scripts`` files.
`More info on the separation of configs <https://github.com/keepassxreboot/keepassxc/issues/2666>`_.

Different autostart programs for two of my laptops made me introduce host-specific configurations
into ``configs_and_scripts``. It was `quite simple to do <https://github.com/butla/configs_and_scripts/commit/9bbfe2a4ab87c0b9d3047a26e3d1992a0b93d89c#diff-cd9a14fe620c616e617225f9d9d6fee11f35f05950de741f88bfcc2dde2b6689>`_
with the way my code was set up.

**2021-09-17**

Now, I need to change some system settings (like desktop theme) and store that in ``configs_and_scripts``.
I want to get to the config files without having to dig through documentations of programs.
I can check what files the programs are modifying myself with ``strace``.

Getting a process ID related to a window you click: ``xprop _NET_WM_PID``.
Starting a trace of all the files being opened and closed by a process with a given PID:
``sudo strace -e open,close -p <PID>``.
Putting it together::

    sudo strace -e open,close -p $(xprop _NET_WM_PID | cut -d ' ' -f 3)

Huh... some config files are already opened by the time I attach, so I don't see their paths
(they only appear in "open" calls), but I can use ``lsof`` to see the files that the process has opened already.

Of course my plans are foiled again by software that just can't maintain its configuration in git-friendly text files...
Manjaro theme is being saved into ``~/.config/dconf/user``, which isn't a text file...
I guess I need to use ``dconf`` to be setting that correctly in an automated fashion.
So it'll go into ``machine_setups`` as a command I run, and not in ``configs_and_scripts`` as just, well, a config file.

Now, how to use ``dconf`` to set this... I didn't want to search for stuff, but they forced me again...
I could just leave setting the dekstop theme as a manual step in ``machine_setups`` (at least it'll be documented),
but now I'm interested in seeing how much XFCE can be configured between different machines without GUIs.
`With KDE it seemed to be impossible.<https://unix.stackexchange.com/questions/438596/robust-command-line-cli-configuration-of-plasma-kde-applets>`_

I've searched for the theme name in ``~/.config``, turns out it's also saved in
``~/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml``.
Let's see what's modifying this file::

    sudo systemctl start auditd
    sudo auditctl -w ~/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml -p wa -k my_key
    # now modify the setting
    sudo ausearch -k my_key

Looks like the file is being modified by ``/usr/lib/xfce4/xfconf/xfconfd``. Of course it couldn't be that easy.

And that ``~/.config/dconf/user`` was being modified by ``/usr/lib/dconf-service``.
Jesus. A GUI program is talking to a daemon or two to save a config file.
Maybe they couldn't just use locks to synchronize saving the file?

But I see that my approach with following ``strace`` might not be universal.

Ok, so maybe a series of commands using ``xfconf`` will be the way to go.
Maybe that'll work better than ``dconf``? Who knows...
But now, how to figure out the option paths to use for ``xfconf``?

I'm looking at this file ``~/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml``...
Looks like the "channel" is ``xsettings``. Running ``xfconf-query -c xsettings -l`` gives me all properties,
and there's ``/Net/ThemeName``. Based on that I figure out::

    xfconf-query -c xsettings -p /Net/ThemeName -s Adapta-Nokto-Eta-Maia

It takes a moment for the setting to propagate to the file, but the theme change is visible immediately.
Ok, so setting of any XFCE config properties will have to be done like this in ``machine_setups``.

Actually, I'm already maintaining ``xfce4-keyboard-shortcuts.xml`` in ``configs_and_scripts``,
so maybe other configs will be good for that as well. They might require a restart to kick in, though.
Let's see. I'll compare the configs I have on my heavy/main laptop (new Manjaro) to the ones I have on the
light/secondary (old Manjaro) one.

Mounting the lighter one's filesystem over SSH will be handy (using hostnames from Avahi)::

    sshfs bl.local:/home/butla ~/bl_home

After looking at the files in ``~/.config/xfce4/xfconf/xfce-perchannel-xml/``
I've realised that ``xfwm4.xml`` and ``xsettings.xml`` both contain configuration options that I want, and don't
look to be polluted with often changing values.

Let's see if I can apply them, restart the session and see the changes take place.

It worked. The only other thing I want is the clock style.

And the QT apps (qBittorrent, kolourpaint, KeePassXC) styling... that'll be worse...
Ok, had to install one package (``kvantum-manjaro``), added one simple file to my configs, and added replacing of
one line (with regex) in another config to ``machine_setups``.

qBittorent won't be a good candidate for ``configs_and_scripts`` as it pollutes the configuration file with things
like "most recently used path" and last window position.

Ok, last config to set and find - the clock widget :)
Let's see if ``auditd`` will come in handy.
Running a broad search of all the configs::

    sudo auditctl -w ~/.config -p wa -k my_key

I hope the browser won't mess up the output too much. Let's see what I found::

    sudo ausearch -k my_key

Slack, Spotify, and Brave produced a lot of spam... I wonder when more developers will learn that ``~/.config``
is for config and ``~/.cache`` is for temporary data...

These can be filtered out::

    sudo ausearch -k my_key | grep name | grep -v spotify | grep -v Slack | grep -v Brave

So it's probably this file ``/home/butla/.config/xfce4/xfconf/xfce-perchannel-xml//xfce4-panel.xml``.
And of course, this config isn't reliably addressable with ``xfconf-query``, because it's just ``/plugins/plugin-1``,
``/plugins/plugin-2``, etc., and one of them happens to be the clock. I guess I could do that reliably by finding
the one with ``digital-format`` parameter, but at this point I want to be done with this whole setup.
It's going into "manual actions".

**2021-09-18**
A day off today, but I was annoyed by the login prompt style.
Turns out it's governed by LightDM (``$ lightdm-gtk-greeter-settings``).
And that has config stored globally, controlled by root under ``/etc/lightdm/lightdm-gtk-greeter.conf``.

So my revised config change search looks like this::

    sudo systemctl start auditd.service
    sudo auditctl -w ~/.config -p wa -k my_key
    sudo auditctl -w ~/.local -p wa -k my_key
    sudo auditctl -w /etc -p wa -k my_key
    sudo ausearch -k my_key | grep name | grep -v spotify | grep -v Slack | grep -v Brave

This config is going under ``manually_linked`` in my configs - I'd need to add something for setting root's configs,
like SSHD. Should be host-dependent.

TODO
----

- spellcheck this post
