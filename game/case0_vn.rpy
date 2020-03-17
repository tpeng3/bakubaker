# Time to BREAK EVERYTHING
# Ultimate lab for bullshit
# -----------------------------------------------------------------------------
init:
    define flash = Fade(.10, 0.0, .20, color="f8dfd2")

label cynthia:

    menu:
        "Case 1 VN":
            jump case1_vn
        "Ultimate Lab":
            jump lab

label lab:
    window auto
    scene storefront

    dr """
    I wonder what Cynthia is going to break this time...
    """

    u "Testing: how much text I can shove in the dream box and how side images be lookin'."

    dreamSom gr "Callie is a part of the Squid Sisters pop idol duo and a former host of Inkopolis News, along with her cousin Marie. Her signature color is magenta. {ii}Staaay fresh!{/ii} {ss}That's her catchphrase!{/ss}"

    dreamRem fl "Marie is a part of the Squid Sisters pop idol duo and a host of Inkopolis News, alongside her cousin Callie. Her signature color is lime green. {ss}Please don't make me say the catchphrase...{/ss}"

    dreamSom sh "Oh Remi, don't be so shy! You have nothing to be ashamed about for loving the Squid Sisters!"
    dreamSom ex "Woomy!" with flash

    dreamRem sh "...??!" with hpunch
    dreamRem fl "{ss}(Th-that was really cute...){/ss}"

    u "Looks like we're done here! Check out the other shenanigans."
    jump start

return
