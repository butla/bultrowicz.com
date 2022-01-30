Find out where do programs write their config files
===================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux, system_administration, Manjaro

TODO finish up configs_audit zsh function

Or, instead of that you can just use grep in the standard directory for configs.
That strategy works if the program works well together with the OS.
(look at osdirs in Python, that package that gives you standard config/data/log envs)

So after QBittorent's theme broke after an update from Manjaro's ``pacman``.
I fired ``qt6ct`` as `this helpful thread
<https://forum.manjaro.org/t/qbittorrent-ignores-the-desktop-theme-after-update/100338/4>`_
recommended.
I checked which "theme" is a dark one I like. I only had 4.
Picked "kvantum-dark".
Looked for that string in the usual configs dir:

```
grep -rni kvantum-dark ~/.config``
```

I found ``/home/butla/.config/qt6ct/qt6ct.conf``.
