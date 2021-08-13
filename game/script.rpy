#screens
default languages = ((__("English"), Language(None)),
                     (__("Portuguese"), Language("portuguese")),
                     (__("Spanish"), Language("spanish")),
                     (__("Japanese"), Language("japanese")),
                     (__("Russian"), NullAction()))

default show_quick_menu = False

#Game points
define con = 0
define dubcon = 0
define noncon = 0

#Renpy character definitions
define pn = DynamicCharacter("playerName")
define s = Character("Strange Customer")
define d = Character("Damien")
define c1 = Character("Blonde Customer")
define c2 = Character("Overweight Patron")
define z1 = Character("Zac")
define b1 = Character("Barry")
define c3 = Character("Loud Customer")
define coS = Character("Shelly")
define coR = Character("Rick")
define k = Character("Kaley")
define st = Character("Stranger")

define config.main_menu_music = "audio/titlescreen.mp3"

default s_ch3_asked = None

label clearScene():
    scene black with dissolve
    $ stop_audio("sound", 1.)
    $ stop_audio("music", 1.)
    return

label showCenterText(t, size="100", color="#fff", font="BeyondWonderland.ttf"):
    show text "{font=[font]}{size=[size]}{color=[color]}[t]{/size}{/color}{/font}" at truecenter with dissolve
    return

label splashscreen:
    call screen choice_language
    return

label start:
    $ playerName = renpy.input(__("What's your name, darling?"), length=15, pixel_width=200)
    $ playerName = playerName.strip()

    $ stop_audio("music")

    call clearScene from _call_clearScene_5

    jump damien_demo
