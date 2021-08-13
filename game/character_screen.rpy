
screen character_screen():
    python:
        global characters
        character = characters[character_number]
        character_img = character["img"]
        def change_character(direction):
            global character_number
            if direction == "next":
                character_number = (character_number + 1) % 4
            else:
                if character_number < 1:
                    character_number = 3
                else:
                    character_number = (character_number - 1) % 4

    add "gui/bg_character.jpg"

    add character_img xalign 0.8

    text "[character_number]" xalign 0.5 yalign 0.98

    textbutton _("Prev"):
        xalign 0.6 yalign 0.5
        action Function(change_character, "prev")

    textbutton _("Next"):
        xalign 0.95 yalign 0.5
        action Function(change_character, "next")

    textbutton _("Start"):
        xalign 0.8 yalign 0.98
        action Return(True)
