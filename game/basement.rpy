label tina:
    scene black
    "Welcome to Tina's janky testing basement."
    "Please watch your step."
    scene dreamoffice with Dissolve(0.5)
    show remerie at left
    show somnia at right
    s "The omelette came out great!"
    r "Not my best work considering how much I was scrambling back there, but I admit, it does look enticing..."
    s "Why don't you have it?"
    r "...!"
    $ somexpr = "de"
    $ remexpr = "fl"
    s "We both know dreams are harder to come by than nightmares, so please... Help yourself!"
    r "I... Thank you, Somnia."
    s "What's with that sad look? Eat up and enjoy!"
    r "I... I will. Thanks for the meal. Mmrph."
    r "Mm... Soft, warm eggs wrapped in a delicate fold and perfectly sweetened."
    dreamSom sh "Oh Remi, don't be so shy! You have nothing to be ashamed about for loving the Squid Sisters!"
    dreamSom ex "Woomy!" with flash
    dreamRem sh "...??!" with hpunch
    dreamRem fl "{ss}(Th-that was really cute...){/ss}"
    return