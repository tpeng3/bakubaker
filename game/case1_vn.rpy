# Case 1
# ------------------------------------------------------------------------
label case1_vn:
    $ case = "case1"

    scene black with dissolve
    dr """
    On a fresh, early morning day like any other, we begin the story in the quiet corner of {ii}name{/ii}, a modest and cosy bakery.

    The aroma of baked goods fills the store and the alleys, warming anyone who has the pleasure to stop by.

    Should any sleepy lives follow their nose into the bakery, two busy cooks will await them with open arms.
    """

    scene storefront with dissolve
    show somnia gr
    u "Hm hmm... Spoonful of sugar hm~♫"
    u "… in a most delightful way~"
    "Ding!"
    show somnia
    u "{ii}Rem~er~ie~♫!{/ii}"
    show somnia ex
    u "Take a look! The tarts are done!"
    show somnia ex at right with ease
    show remi th at left
    r "...In a minute."
    show somnia
    u "I’ll go ahead and set some on the display. Would you like to taste one?"
    show remi si
    r "Later, please. I- {w=0.5}{nw}"
    show somnia de
    show remi bsh
    r "Mmrph!" with sshake
    show remi pe
    r "Mmrrph! Mmrhh nmrph!" with sshake
    show somnia
    u "How is it?"
    r "{ii}Somnia{/ii}! That's hot!"
    r "I can grab my own, you know?"
    show somnia th
    s "Do you think maybe I used too much jam?"
    show remi th
    r "...No, it was good. The sweet jam you used was less watery this time, so the tart crust held together well."
    show somnia
    s "I see. I'm glad they turned out better this time!"
    show somnia de
    s "I can always count on your sharp palate for tasting, {i}Remi{/i}~."
    show remi fl
    r "Well, o-of course...!"
    rth "I can’t say no to Somnia’s desserts!"
    show remi
    r "H-how about we open the shop now if you’re all done baking."
    show somnia
    s "Yup~ I’ll go flip the sign outside."
    hide remi with easeoutleft
    show somnia gr at center with ease
    s "Hmmm hm~ ♫"
    s "Hm~ A merry tune to toot-"
    show somnia bsh
    s "AH!" with sshake
    r "What’s wrong?"

# NOTE Cynthia vn shenanigans bookmark
    scene black with flash
    u "Cynthia's only gotten {ii}this{/ii} far in adding all the images n stuff! The following will cont awkwardly. Proceed with caution."

    # Client is passed out on the floor in front of the store
    s "There’s a person fallen over outside."
    s "Oh dear, are you okay?"
    r "We can’t have bodies blocking the door for potential customers."
    uml "Hrn…"
    r "Are they… dea-"
    uml "...I-I’m alive..."
    uml "Snrk... {ii}...Snore...{/ii}"
    r "We should bring them in, it won't do us any good having someone lying on the floor in front of our store."

    scene black with dissolve
    with Pause (1.0)
    scene storefront with dissolve

    show remi at left
    show somnia at right
    # client sprite slowly rises from below
    show marchie with easeinbottom
    u "So sorry, apologies for the concern. *yawn*"
    r "They were napping?!"
# TODO cafe name lol
    uml "Uh… Let’s see… Would you happen to know a cafe around here called {ii}cafe name{/ii}."
    "..."
    s "Welcome!"
    r "...Welcome."
    s "We’re technically not open yet, but is there anything we can get started for you?"
    uml "Yes, I heard rumors that the shop recently opened again."
    uml "It’s been what, 5 years? It’s been so long I could hardly contain my *yawn* excitement…"
    # s "Five years... what would they happen to know?"
    uml "Let’s see now… I’ll have… this cherry tart and the…"
    uml "...{ii}Egg pudding pasta with strawberry chives.{/ii}"
    # Somnia and Remerie both perk up with a !
    uml "T-that’s the special menu item of the day, right?"
    s "Yes, you are correct."
    r "Would you like your order for here or to go?"
    uml "For… here."
    r "Alright. Luckily there's still a half hour before the store opens proper so we have time to fulfill your request."
    s "Kind sir, please follow us to the back~"
    uml "Alright…"

    scene dreamoffice
    dr """
    Through the back of the store, and only a short few feet away from the kitchen, was an intimate, deep-colored room.

    The dimly lit office housed a bed as its centerpiece, a decorative mirror to taste, and a long olden cabinet.

    Shutting the door behind them, the three guests, enveloped in the velvety deep, began.
    """

    uml "This place…!"
    uml "Wow, it looks much more different than what I remember."
    r "Welcome to the {ii}Dream Service{/ii}. Here, we specialize in investigating strange sleep patterns and behavior."
    r "Tell us, what ails you?"
    uml "Um.. Is {ii}Madam{/ii}... present?"
    s "... Oh! Um..."
    s "Unfortunately, she is currently away on a trip. We are her apprentices who’ll be taking care of the store while she’s gone."
    r "I'm Remerie, dreams specialist."
    s "And I'm the connoisseur of nightmares, Somnia!"
    uml "Pleasure to meet you two, I'm {ii}Marcella Lapin{/ii}."
    ml "Err, I wasn't aware she left behind apprentices..."
    ml "But… {i}yawns{/i} that’s fine… If possible, I would like you two to help me as she once did…"

    ml "You see, I’ve been having problems sleeping the past several nights."

    ml """
    I would come home exhausted from work, climb into bed...

    ... Only endlessly toss and turn until morning comes, unable to catch even a wink of shut-eye!

    It was fine at first… I’ve pulled all-nighters before, but it has now been two weeks…

    I don’t think my body can keep up with my brain anymore.

    It’s been absolutely exhausting… to do anything… or get anywhere… *yawn* I just want to sleep…

    Sleeping pills, music, exercise and such have done nothing in my favor...

    I’m a very busy person, see. I have a lot on my plate… But...

    I-I don’t know what will become of me at this rate…!
    """

    s "Sounds like a strong case of insomnia."
    s "I wonder… could it be a nightmare? Something vexing pulling at the heartstrings?"
    s "Dreams made by a dreamless client… My, I wonder how they'll taste!"
    ml "What was that?"
    # s (Maybe a nightmare or @#$%…!)
    r "Don't mind her. For now, let’s get our investigation started."
    # s(I hope it’s a gruesome dream. Those are absolutely scrumptious!)
    r "Marcella, I’m going to need you to lie on this bed."
    ml "A… bed… I don’t think I would be able to fall asleep in it…"
    r "Don’t worry, we have ways of making you sleep."
    s "If you would please, relax… I’ll be lighting some incense now~"
    s "When we count to three, you shall fall into a deep sleep…"
    "1… 2… 3…"

    scene black with dissolve
    dr """
    Somnia carefully lit an incense at the tip, blew it out, and fanned the smoke out, spreading the aroma across the office.

    The insomniac was skeptical to believe incense would work this time, but with nothing left to lose, they closed their eyes nonetheless.

    The smoke swirled lazily up into the air, and the two, cooks just a moment ago, now began their work as dream eaters.
    """

    jump expression case+"_dream"

label case1_vn_end(result=0):
    scene dreamoffice
    show somnia at right
    show remi at left
    s "The omelette came out great!"
    r "I admit, it does look enticing…"
    s "Why don't you have it?"
    r "...!!"
    s "We both know dreams are harder to come by than nightmares… So help yourself!"
    r "I… Thank you, Somnia."
    s "What's with that sad look? Eat up and enjoy!"
    r "I will… Thanks for the meal. Mmrph."
    r "Mm… Soft, warm eggs wrapped in a delicate fold and perfectly sweetened. The freshly cut fruit is served as a crisp, light contrast."
    r "This is sure to brighten up anyone’s morning, especially if they had a tiring night before."
    r "I hope with this, we were able to eat away some of Marcella’s worries."
    s "I hope so too~"

    dr """
    The dream eater feasted on the hearty dish conjured from the client's suppressed worries and anxieties.

    Somnia prepared an inspired dish in the adjacent kitchen, in eager anticipation for the client to wake from their repose.

    Slowly, Marcella rose from the bed as the incense fizzled out to a small ember.
    """

    show marchie
    ml "Yaaaawn..."
    s "Good morning! How are you feeling after that little nap?"
    ml "Um... hungry..."
    s "You're in luck! We've prepared a dish specially for you."
    s "If you would please follow me back out to the storefront..."

    scene storefront
    show marchie

    show somnia at right
    show remi at left
    ml "Oh, this is delicious!"
    if result == 1:
        ml "It reminds me of when I first came here and had sleep consulting with, um… what's their name again…?"
        # r and s pitch in with the mentor's name in excitement
        ml "Y-yeah! This dish really takes me back…"
        s "Can you tell us how you two met?"
        ml  "Well it’s been a while ago now… The years have passed in a blink of an eye…"
        ml "This is a bit of a personal story but well…"
        ml "F-Five years ago, my family was going through a rough time… It was hard for our parents to be home, what with their odd jobs keeping them busy."
        ml "So I was given the responsibility of taking care of my younger siblings. But to be honest, it was pretty overwhelming."
        ml "I wasn’t even that many years older, but suddenly they were looking to me to take care of them and asking me to take them to places."
        ml "What could I do? I couldn't turn my back on my family…"
    # TODO MENTOR NAME // BAKERY NAME
        ml "The stress of it all led to a lot of sleepless nights. And that’s when I happened to stumble across this bakery and meet {ii}mentor{/ii}."
        ml "In a similar fashion, really! There I was, stretched out on the pavement in front of {ii}bakery{/ii}."
        ml "When I woke up, I was inside the store, with a warm omelette and a comforting smile waiting for me."
        ml "It was difficult, balancing my responsibilities, but I felt a… a duty to take care of my siblings."
        ml "She really listened to my worries. I was able to work hard and continue to support my siblings thanks to her advice."
        ml "Thinking back at it now, she did mention before she had picked up two kids of her own. I guess that must be the two of you."
        ml "We certainly did have our fair share of caretaking stories… {ii}mentor{/ii} treasured you two the same I feel for my siblings."
        ml "She was a lovely soul. I hope she comes back soon, for your sake."
        r "Do you think you could share more of your stories with us sometime?"
        s "Yes, please…! We love and miss her a great deal!"
        ml "I would love to hear your stories of {ii}mentor{/ii} as well. I’ll try to become a regular when I have some time."
    ml "You know when I took that nap earlier, I actually had a wonderful dream."
    ml "I don’t remember much of it now, but there were bits and pieces…"
    # Marchie checks the time
    ml "Oh no! I'm going to be late…!"
    ml "..."
    ml "Ah, you know what? I think I should take a day off to rest."
    ml "The shop can go without me for a day."
    ml "Rather than focus on trying to keep up, I honestly ought to step back and see if I can get help from my siblings with these tasks."
    ml "Why, even in my dream, I saw them cleaning up some large piles of debris!"
    "!!"
    ml "But it’s true. They've grown up to be very capable… I think they might be able to help around the floral shop as well!"
    ml "But I must be going, thank you so much for your services!"
    scene black
    # ml leaves in their usual hurried disposition but with a happier energy in the steps. They look like they have an idea of what to do next…!

    scene storefront
    show somnia at right
    show remi at left
    s "Phew, all in a day's work, right Remi?"
    r "What do you mean? I had to clean up the mess you made out of that dish!"
    s "Hehe, I just wanted to impress you with a dash of whimsy!"
    s "It’s funny, Marchie reminded me a little of you- working a little too hard at times…"
    s "You ought to take a card from Marchie’s book and take it easy- have some fun now and then!"
    r "I think you have enough fun for the both of us..."
    s "Don't tell me you didn't have fun in that dream- the cute bunnies? Cooking the dream dish? It's been an awful long time since we've had a client!"
    r "While I can't say the same about the bunnies, I do have to agree that the dream dish was quite good…"
    s "Hm? Do I spy a smile turning the corners of your mouth…?"
    r "Wh-what?"
    s "I do! You really liked the dish, didn't you!"
    r "O-of course! I fixed it and made it delectable, no thanks to you!"
    # Somnia laughs lightly but her eyes are turned downward.
    s "Sigh..."
    s "It takes me back…"
    s "It's been five years since {ii}mentor{/ii} left…"
    r "..."
    r "Starting the morning with a dish like this, it reminds me of when she would prepare fruit slices before opening."
    s "Y-you remember something like that?"
    r "Of course, the way you plated the fruit slices on the client's dish... it's just like how she did it."
    s "I... I suppose it is, isn't it."
    r "Does Somnia really not remember? Starting the day with small delights from our mentor only ever brightened my day."
    s "I'm glad it reminded you of her, if only for a little bit."
    r "You two were close, weren't you? It's only natural you'd pick up some of her tendencies."
    s "R-right..."

    dr """
    It was abnormal for the bubbly Somnia to fall silent, but Remerie took note of the strange behaviour.

    Although condolences weren't Remerie's forte, she still cared for Somnia, making the attempt to bolster her spirit.
    """

    r "Somnia…"
    r "We agreed to watch the store and wait for her, right?"
    r "It's our duty to keep the store as welcoming as it was the day they left."
    r "I know it's hard to play the waiting game, but let's get to work… for their return."

    dr """
    Chattering away, the dream eaters gathered their bearings for the start of another day.

    Another day, another chance to see their mentor.

    With that hope in their hearts, the two open up shop and await their old friend with open arms.
    """
    return