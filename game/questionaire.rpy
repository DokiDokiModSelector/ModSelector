## Tutorials.rpy
# This file isn't needed for DDLC modding and is just part of the tutorial
# of the DDLC Mod Template. BETA

init python:

    bestgirls = [
        (_("Yuri"),"yuri_bestgirl_selected"),
        (_("Monika"),"monika_bestgirl_selected"),
        (_("Sayori"),"sayori_bestgirl_selected"),
        (_("Natsuki"),"natsuki_bestgirl_selected"),
        (_("All Doki Best Doki"),"alldoki_bestgirl_selected")

    ]
    
    genres = [
        (_("Award Winning"),"genre_awarded"),
        (_("Action"),"genre_action"),
        (_("Romance"),"genre_romance"),
        (_("Horror"),"genre_horror"),
        (_("Good Ending"),"genre_goodend"),
        (_("NSFW"),"genre_nsfw")
        (_("NSFW"),"genre_comedy")
        
   ]
        
        

define adj = ui.adjustment()
define gui.tutorial_button_width = 500
define gui.tutorial_button_height = None
define gui.tutorial_button_tile = False
define gui.tutorial_button_borders = Borders(25, 5, 25, 5)

define gui.tutorial_button_text_font = gui.default_font
define gui.tutorial_button_text_size = gui.text_size
define gui.tutorial_button_text_xalign = 0.0
define gui.tutorial_button_text_idle_color = "#000"
define gui.tutorial_button_text_hover_color = "#fa9"

style tutorial_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing 5

style tutorial_button is default:
    properties gui.button_properties("tutorial_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style tutorial_button_text is default:
    properties gui.button_text_properties("tutorial_button")
    outlines []

screen tutorial_choice(items):
    style_prefix "tutorial"
    fixed:
        area (125, 40, 600, 450)

        viewport id "tu":
            #yadjustment adj
            mousewheel True
            has vbox

            for i_caption,i_label in items:
                textbutton i_caption:
                    action Return(i_label)

        vbar value YScrollValue(viewport="tu") style "vscrollbar" xalign -0.05

label tutorial_selection:
    stop music fadeout 2.0
    scene bg club_day
    with dissolve_scene_full
    play music t3
    
   

label bestgirl_selection_menu:
    $ ca = renpy.random.randint(1,4)
    if ca == 1:
        show sayori 4a at tcommon(950)
        s "Hey [player], you're here to find a new mod aren't you?"
        s "Well, you've come to the right place!"
        s "Just answer some questions and you'll be playing your perfect mod in no time!"
        s "Who out of the literature club is you favorite? I promise to keep it secret!"
    elif ca == 2:
        show natsuki 5a at tcommon(950)
        n "Hey [player], you're here to find a new mod aren't you?"
        n "Well, you've come to the right place!"
        n "Just answer some questions and you'll be playing your perfect mod in no time!" 
        n "Who out of the literature club is you favorite? I promise to keep it secret!"       
    elif ca == 3:
        show yuri 1a at tcommon(950)
        y "Hey [player], you're here to find a new mod aren't you?"
        y "Well, you've come to the right place!"
        y "Just answer some questions and you'll be playing your perfect mod in no time!"  
        y "Who out of the literature club is you favorite? I promise to keep it secret!"              
    else:
        show monika 2a at tcommon(950)
        m "Hey [player], you're here to find a new mod aren't you?"
        m "Well, you've come to the right place!"
        m "Just answer some questions and you'll be playing your perfect mod in no time!"        
        m "Who out of the literature club is you favorite? I promise to keep it secret!"
    window show
    $ mc(_("I love..."), interact=False)
    call screen tutorial_choice(bestgirls)
    window auto
    if _return == False:
        jump end_tutorial
    call expression _return from _call_expression
    scene bg club_day
    with wipeleft_scene
    jump bestgirl_selection_menu



label yuri_bestgirl_selected:
    hide yuri
    hide monika
    hide sayori
    hide natsuki
    scene club with wipeleft
    show yuri 1a at tcommon(950)
    $ bestgirl = "y"
    y "Why, I'm flattered. Thank you [player]."
    y "You know how I love a good horror novel, but what is your favourite genre?"
    jump genre_select
    
label natsuki_bestgirl_selected:
    hide yuri
    hide monika
    hide sayori
    hide natsuki
    scene club with wipeleft
    show natsuki 1ba at tcommon(950)
    $ bestgirl = "n"
    n "You're lucky you didn't pick one of the others, baka"
    n "Tell me what type of mod you like, and make it snappy!"
    jump genre_select
    
label monika_bestgirl_selected:
    hide yuri
    hide monika
    hide sayori
    hide natsuki
    scene club with wipeleft
    show monika 2a at tcommon(950)
    $ bestgirl = "m"
    m "I guess I did write the way into your heart!"
    m "You seem to like mods, so what type is your favourite?"
    jump genre_select
    
label sayori_bestgirl_selected:
    hide yuri
    hide monika
    hide sayori
    hide natsuki
    show sayori 3a at tcommon(950)
    $ bestgirl = "s"
    s "Eh? You're silly [player]!"
    s "Now I'm interested, what type of mod do you like?"
    jump genre_select
    
label genre_select:
       window show
       $ mc(_("I think my favourite is..."), interact=False)
       call screen tutorial_choice(genres)
       if _return == False:
          jump end_tutorial
       call expression _return from _call_expression
       jump genre_select
    
       
    
    


