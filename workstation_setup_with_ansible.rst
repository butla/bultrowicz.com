Workstation setup with Ansible
==============================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux

Long time ago I created an Ansible script for setting up my machine.
I didn't keep it up to date and I thought it didn't make sense to maintain it, since I
had multiple OSes (Kubuntu and Manjaro).
But now that both my computers are on Manjaro I decided to try this trick once more to create
something that will allow me to just turn any Manjaro install into my workstation.

Before I had dreams of making that script support multiple OSes, that dream is still holding on.
Though I won't implement that just yet :)

Ansible has changed and I have changed, so I'm giving this another try.

My notes
--------

TODO
----

- set up ZSH (.zshrc)
  - keep powerline with process times and status
- install Ansible
- change XFCE theme while looking at what a config window is changing with strace, add those config to ``configs_and_scripts`` (blog post out of that)
  - hide window headings
- alacritty doesn't render to the side - some XFCE scrollbars?
- go through TODOs in machine_configs
  - signal settings
- mention manual steps
  - enable sync in Brave, extend it to extensions, settings, history, theme, open tabs
  - syncing Signal
