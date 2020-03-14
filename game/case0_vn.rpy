# Time to BREAK EVERYTHING
# -----------------------------------------------------------------------------
label cynthia:

    """
    On a day like any other, we begin our story in the quiet corner of X, a modest and cosy bakery.

    The aroma of baked goods fills the store and the alleys, warming anyone who has the pleasure to stop by.

    Should any sleepy lives follow their nose into the bakery, two busy folks await them with open arms.
    """

    scene storefront

    show somnia
    s "Time to open up shop!"
    s "What the-"
    show somnia at right with ease
    show remi at left
    r "Is that person dead?"

    show client1
    bun "I-I'm alive..."
    bun "But I'm having HELLA trouble sleeping please help"
    s "Let's hit the dream room!"

    scene dreamoffice with fade
    show remi at left
    show somnia at right
    show client1
    bun "Wow!"
    s "You're feeling veryyyy sleepy..."
    scene black

    dreamSom neutral "Somnia used DARK VOID"
    dr "The CLIENT fell asleep!"
    dreamRem neutral "Remerie used DREAM EATER"

    scene black with fade
    jump dream_case1

return
