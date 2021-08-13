style credits:
    xalign .5


screen choice_language():
    add "gui/bg_credits.png"

    vbox:
        align .5, .5
        text __("Choose your language")
        for name, switch in languages:
            textbutton name:
                if not isinstance(switch, NullAction):
                    action [switch, Return()]
                else:
                    action switch
screen credits():
    zorder 120
    modal True

    default await_time = 10
    default isFrame = "credits"
    default credits_naming = ((__("Game Design"), ("Ataraxic Games and Novels", "A. K. Fagan")),
                              (__("Programming"), ("Various", )), (__("Art"), ("mmm_sheva", )),
                              (__("Music"), ("trufata", )), (__("Writing"), ("A. K. Fagan", )),
                              (__("Portuguese Translation"), ("Samuel Finezi", ("Copyright © 2021 Alexa Fagan. All Rights Reserved."))))

    add "gui/bg_credits.png"

    if isFrame == "credits":
        frame at Move((.5, 3.), (.5, .0), await_time, repeat=False, bounce=False, xanchor="center", yanchor="bottom"):
            background None
            vbox:
                text __("Credits") style "credits" size 80
                null height 35
                for category, names in credits_naming:
                    text category style "credits" size 40
                    null height 10
                    for name in names:
                        text name style "credits" size 50
                    null height 35
                text __("Engine") style "credits" size 40
                text __("Ren'py") style "credits" size 50
                text __("7.4.3") style "credits" size 50
    elif isFrame == "toBe":
        text __("To Be Continued...") align .5, .5 size 100
    elif isFrame == "look":
        vbox:
            align .5, .5
            text __("Thanks for playing! Too bad it didn't end so well for you...") align .5, .5 size 50
            text __("Look forward to more on my Patreon in the upper right corner!") align .5, .5 size 50

    vbox:
        align 1., 0.
        textbutton __("Patreon"):
            text_xalign .5
            text_size 52
            xysize 358, 100
            action OpenURL("https://www.patreon.com/ataraxicgamesandnovels")

        add "gui/logo.png" size 344, 200

    timer await_time:
        action SetScreenVariable("isFrame", "toBe"), With(Dissolve(1.))

    timer await_time+5:
        action SetScreenVariable("isFrame", "look"), With(Dissolve(1.))

    timer await_time+25:
        action Return(), With(Dissolve(1.))

label credits:
    scene black #replace this with a fancy background
    with dissolve
    call screen credits with dissolve
    return
