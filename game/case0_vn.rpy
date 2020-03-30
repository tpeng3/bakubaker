# Time to BREAK EVERYTHING
# Ultimate lab for bullshit
# -----------------------------------------------------------------------------
init:
    define flash = Fade(.10, 0.0, .20, color="f8dfd2")

label booktest:
    show starry:
        xpos 0 ypos 0
        linear 40.0 xpan 360 ypan -360
        xpan 0 ypan 0
        repeat
    show book:
        zoom 0.50

label cynthia:

    menu:
        "Case 1 VN":
            jump case1_vn
        "Ultimate Lab":
            jump lab

label lab:
    scene dreamoffice

    dr """
    I wonder what Cynthia is going to break this time...
    """

    call booktest from _call_booktest

    show somnia at right
    s "Test!"
    show remi at left
    r "Test???"
    s "Remi is hiding in the shadows..."
    r "..."

    # NOTE Dimming not applied to different expression sprites
    show somnia ex
    s "Test!!!!!!!"
    show remi sh
    r "Test?!"
    s "Callie is a part of the Squid Sisters pop idol duo and a former host of Inkopolis News, along with her cousin Marie. Her signature color is magenta. {ii}Staaay fresh!{/ii} {ss}That's her catchphrase!{/ss}"
    r "Marie is a part of the Squid Sisters pop idol duo and a host of Inkopolis News, alongside her cousin Callie. Her signature color is lime green. {ss}Please don't make me say the catchphrase...{/ss}"

    # NOTE Checking how the dreambox + side image looks
    dreamSom sh "Oh Remi, don't be so shy! You have nothing to be ashamed about for loving the Squid Sisters!"
    dreamSom ex "Woomy!" with flash
    dreamRem sh "...??!" with hpunch
    dreamRem fl "{ss}(Th-that was really cute...){/ss}"

    u "Looks like we're done here! Check out the other shenanigans."
    jump start

return
