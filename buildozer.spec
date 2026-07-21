[app]
title = Bac Calc Bot
package.name = baccalcbot
package.domain = org.bot
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pyTelegramBotAPI,certifi,urllib3,idna,charset-normalizer,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
#android.sdk = 33
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
