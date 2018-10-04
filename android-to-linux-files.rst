A battle with Android-to-Linux photo transfer
=============================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, Android

Slow Airdroid.

This post may be marked by ignorance, but I welcome everyone who can clarify any information in here.

You used to be able to just plug in the Android phone like external storage, everything was perfect.
It seems they just removed that. It stopped working after some update to my Xperia Z3 Compact (or was it Z5? I don't remember)

KDE - had to pair again from time to time. Access from the file explorer.

KDE Connect uses SFTP under the hood for file transfer (at least that's what the app says).
I couldn't get any SSH server to work with external storage with the newer Androids.

-------------------

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

-----------------

Normal file explorer seems unreliable.

Gwenview seems to work despite transient errors popping up, but it wants to load ALL the photos,
which is needlessly time consuming.
And I'd like to have a scripting option.

-----------------

Maybe S3 / Digital Ocean Spaces upload is an option, but installing Android Studio, assembling
a Gradle project with https://aws.github.io/aws-sdk-android/ seems like too much of a hassle.
I could write full automation for that. Android would send the files if on Wi-Fi,
my PC would download them. I could encrypt them before sending (link to the cloudonaut article
about encryption), so no photos could've been seen by a third party.
