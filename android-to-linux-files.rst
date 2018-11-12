A battle with Android-to-Linux photo transfer
=============================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, Android


The longish intro to the story
------------------------------

This article will tell my recent story about trying to figure out for myself how to deal
with Android - Linux file transfer without the trouble and unusability of some commercial
ways, and without using the privacy breaking public clouds. We Linux people want to have the
best user interface ever - not doing a thing. Our automation should do the work, not we, even
with the nicest GUIs.

I think this story will be familiar to any "Linux adventurer", who likes to make his life a little
less tedious (there are people who even play various games of which the only aspect is tediousness,
weird; like those clicky-microtransactiony mobile game) from time to time using the powers
of this great and open (...sadly not entirely free) OS!
This will be a story with many adventures, monsters, bugs, and treasures.
Well, at least some.

Oh and I'm not trying to rip off this (great) article (TODO Jiriu Davis o naprawianiu DNS).
I just though about it right now after writing that small intro :)

This post may be marked by ignorance, but I welcome everyone who can clarify any information in here.
And I guess that all of us sometimes encounters ignorance in himself in this form
(meme I have no idea what I'm doing pies)

Oh, and I dislike the overuse of memes in technical presentations, but this one is just so good
and relatable. And it's almost the Socratean "The only thing I know is that I know nothing",
so its meaning must be deep and stuff :)

I think I'll be focusing more on in-depth, slightly dry, technical articles in the future, but
one of these may pop up from time to time after I find a moment to hack on something for myself
(and try to maintain the journalling / blogging discipline :) ).

TODO do chapters with adequately sounding names that will show people what tools and topics are
touched. Może na rozpisce powinny być wydzielone rozdziały [technical] od całej reszty.
I konkretne przepisy na temat konretnych narzędzi tylko tam.
Co myślicie o takim układzie artykułu? Może powinien być u góry przełącznik
(powiązany z linkiem) oczywiście, do przełączania mędzy trybem tylko technicznym,
a pełnym/literackim?

This is long, but do you need multiple parts in an article
if you can bookmark permalinks in chapter headers?


MTP on the cable
----------------

You used to be able to just plug in the Android phone like external storage, everything was perfect.
It seems they just removed that. It stopped working after some update to my Xperia Z3 Compact
(or was it Z5? I don't remember)

This explains the reasons why MTP is everywhere and why Mass Storage mode was cut
https://www.reddit.com/r/linux/comments/3ff1rm/why_does_everything_use_mtp_these_days_mtp_sucks/

When I plug in my phone to Kubuntu I have options including opening in the file explorer or in
Gwenview, though I need to be mindful of popups on the phone requesting access etc, cause I'll
just see cryptic errors on my laptop.

Browsing the files seems to work for a second but then it doesn't.
Gwenview seems to work (sometimes) despite transient errors popping up,
but it wants to load ALL the photos, which is needlessly time consuming.
And I'd like to have a scripting option.

So it seems that all my problems are just due to implementation of MTP in KDE's Dolphin.
So if I have a good implementation (maybe
https://www.fossmint.com/android-file-transfer-for-linux/
or jmptfs) my MTP problems might be gone.
More tools discussed here
https://wiki.debian.org/mtp

go-mtpfs is installable with apt (I don't want to set a GOPATH and compile anything in Go,
even though, theoretically, it's so easy; it's never just that). It seemed to work great,
but then it turned out that sometimes it couldn't even enable copying of a single file
because of libusb errors.
Is that always the case? Will it work sometimes? Can the errors be mitigated somehow?
Is that error related to something with Samsung they called out in android-file-transfer?


ADB
---

Connecting over ADB seems to work for read/write in the internal storage, and even on the SD card.

Scripting it would require some tricks with adb shell, push, and pull, though. But might be doable.


Airdroid
--------

Slow Airdroid, when the transfer broke I didn't have anything, had to click around the interface
again... Maybe try that a few times. And it's always all or nothing.


KDE Connect and the Wi-Fi issue
-------------------------------

It was crashing from time to time, but that looks like it's because of the phone's Wi-Fi??
Or is the app doing something bad with the Wi-Fi? Or is the Samsung system interrupt Wi-Fi
because it thinks the download looks suspicious?
Pings to the phone weren't getting through only after the crash.
Pings just left on their own don't stop working by themselves.

I try to run the script right after pairing.
Also, I need to first access the phone file system and access the Internal Storage (or the SD card)
with the file explorer for it to be mounted.
I have to mount it some other way, but it's not clear enough for me how to do that, and I don't
have the time to read about that now.

KDE Connect uses SFTP under the hood for file transfer (at least that's what the app says).
I couldn't get any SSH server to work with external storage with the newer Androids.

TODO add screenshots, compare with AirDroid downloads from 20180803_211056.jpg

KDE - had to pair again from time to time. Access from the file explorer. And at times, I had to
try to pair again and again... I have to repair, open a new Dolphin (KDE file xplorer) window,
and go into the storage to attach it. Wouldn't it be way easier with SSHD? How does Dophin see
the device when it's not mounted? How can I do that programmatically?
Damn, my PC lost the Internet connection once as well, even though Wi-Fi didn't pick anything up.
Maybe it's my router?? 
This shady looking motherfucker (TODO photo of the router, see the metadata first,
put some stuff in it. Have a script for that?)...
Hmm... Spooky... You can't trust anything anymore...

Anyway, back to reconnecting.
Repair, reopen dolphin, devices, phone, internal storage...
And start the script. So, not ideal for automation yet.

Maybe there was a way to fix that to find the solution in the KDE wiki, like the app suggested?
Nah, I didn't have time this time.

Huh! Running a ping to both the phone and the internet
(and a ping to the internet in Termux on the phone) showed me that after all, the phone,
not the computer might be disconnected from the Internet.

And of course, I sometimes have to touch on the KDE app on Android, cause it was sounding, but
not showing the pair notification...

Well, I guess that this painful process is not acceptable as my automation...

Running the script again. Looking at the network graphs from the system monitor, of course (TODO
screenshots). Flatline again (I'm switching between the glog Tmux window and photo/script/CLI
Tmux window; oh and between Chrome and Spotify for music switching).
Maybe it's finally done?

Fuck.

Another error. Let's see how far I got in the pictures...::

    Removing the partially downloaded file: /data/zdjęcia_i_filmiki/z_telefonu_mego/samsung_s7/20180922_172620.mp4

Damn, a still a couple of more days of vacation left, a lot of pictures. But I think we're already
two months further than before this whole shenanigans.
Must... get... the pictures... off of the phone... Then find some better way... (I already probed
a couple of approaches before writing this. I might need less parallelism in the future and focus
more on the output of single cores...)

Actually, I only moved a couple of minutes on this run. It seems that now, it was the PC that got
disconnected again. Oh well, reconnect to Wi-Fi and once more unto the breach!
I think I'd be contemplating my options more and not just rushing if I wasn't sleepy, and at night.

Is it the router? Or the app? Who is responsible, I wonder, fearing of my safety after
I close my eyes and go to sleep with the possible culprits in the same room with me...

I know what to do. The mantra. I try again. Maybe waiting some time between the attempts
lengthens the download window? It seems that earlier they were longer... Hmm... That would point
to some weird throttling mechanism in the router... And is it even possible for an app to break
the WiFi connection both on Linux AND Android? Seems implausible. But then again, reality is
sometimes strange (remember JavaScript Meltdown? (link)).

One more day of photos grabbed from the Network's grasp. Again! Charge with the same prayer
"check pings (both of them running on panes in a separate Tmux window, of course),
restart network, re-pair, accept pairing, reopen dolphin, access the dir, run script!"

Hell is this cargo cult-y...

Ranger (in another pane of the window with the code and CLI) showing the files popping up...

Maybe killing the app on the phone and starting again helped in the app? The PC app piccked up,
that the phone disconnected for the first time when I did that.

AAAaaaand my PC got disconnected from the network. WTF.
Nothing seems to be happening with the router. This is all weird. And there's a weird scratching
in the fireplace (without fire). What the hell?
Alright! Reconnect your PC Wi-Fi and focus!
Ok! Both pings both on-line.

Happy thoughts, happy thoughts... (some picture from Alien TODO maybe put pictures from
horror movies in here? Children of the Corn with the router and phone)

Shit, forgot to remount. Had to start Dolphin. But it's running again.
Oh my God... (some horror / alien photo) I thing I've made more photos than ever in Portugal...
(z drinem w Lizbonie)
Zipping this up before upload is the only way... but that has to be done on the phone's side.
I think I'm trying for the last time tonight... I deserve some chill-out.

I'll won't see how deep is this rabbit whole, but there are other adjacent wholes that I'd
like to visit, if not explore completely.

Tomorrow, we try the other ways!

Fuck, refreshing Chrome made the pings go through on the Android that required reconnecting.
Probably fucking wakelocks, weird resource management with power savings mode, etc.
Why you can't be a normal Linux, Android? (Why you can't be normal meme.
Damn, I'm falling to the meme dark side;... maybe if I were sober I wouldn't?...)

This is like the last (fifth?) season of Bojack Horseman a bit.

I have to look at some dmesg or Wi-Fi demon logs, on both machines...

Another day, on the train, after watching Apocalypse Now, right before getting to Gdańsk.
I tried connecting over the phone's Wi-fi, and there are no interruptions!
The connection isn't that fast, but it simply carries on.

So the task of getting the photos there is done. But this still requires me clicking
around and doing stuff. It's not even "one-click", and it's the "zero-click" that I want.

TODO filmik z Malcolm in the Middle jak koleś wszystko naprawia po kolei.

Oh, and I published my script here (TODO in experiments)

TODO końcówka irlandzka I want my tears back jako piosenka sukcesu.
TODO link do fragmentu utworu Rhapsody (albo Lotr?) z YouTube jako soundtracku do przygody?
TODO gdzieś link do soundtracku z diuny

And now KDE connect remote filesystem stopped working. I just can't open no phone storage
in Dolphin...


Syncthing, maybe?
-----------------

It's supposed to sync arbitrary files automatically. Let's check that.

But does it phone as a one-way sync? I want my photos to be uploaded to a place on the PC, but when
I move the files on the PC to a proper place I don't want them deleted from the phone.

Seems a bit flimsy, I never new when stuff will sync, how to get a new shared folder from the
phone to start syncing. Turns out I needed to restart the service. Well that's crappy.
I can't set pull only on a folder, and I can't set where will the files be saved... fuck.
There's no way to change the target of the folders on the PC... Ridiculous.
https://github.com/syncthing/syncthing/issues/4309

Install syncthing (apt install)
and enable it start for the user:
systemctl --user enable syncthing.service
systemctl --user start syncthing.service


Magic wormhole on Termux and why it can't work right now
--------------------------------------------------------

I could just zip whatever files I need and send it through the wormhole.
As of now the route through termux and magic-wormhole, it's dependent on specifics of cryptography
https://github.com/warner/magic-wormhole/issues/217#issuecomment-426646526

Enable termux storage
https://wiki.termux.com/wiki/Termux-setup-storage
apt update && apt upgrade
termux-setup-storage

pip install --upgrade pip
apt install clang libffi-dev openssl-dev
pip install magic-wormhole


S3 / DigitalOcean with Termux?
------------------------------

Maybe S3 / Digital Ocean Spaces upload is an option, but installing Android Studio, assembling
a Gradle project with https://aws.github.io/aws-sdk-android/ seems like too much of a hassle.
I could write full automation for that. Android would send the files if on Wi-Fi,
my PC would download them. I could encrypt them before sending (link to the cloudonaut article
about encryption), so no photos could've been seen by a third party.

Maybe try awscli installed in termux with pip?

Can I use pyjnius to do something with Android?

https://github.com/termux/termux-app/issues?q=is%3Aissue+cron+is%3Aclosed
https://github.com/termux/termux-app/issues/14


QPython sucks
-------------

QPython seems to be a Python-focused alternative to termux, but I never felt at home using it.
I just didn't see, from it's website and documentation, that it could be used for something more
advanced than just writing and running scripts isolated from the device.

https://stackoverflow.com/questions/51725405/schedule-a-qpython-script-to-run-daily-on-android-device
https://stackoverflow.com/questions/52319266/launch-python-script-on-android-using-adb

community, doesn't seem to be very active.

Seems not documented enough.
