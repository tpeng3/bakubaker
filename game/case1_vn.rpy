# Case 1
# ------------------------------------------------------------------------
label case1_vn:
    $ case = "case1"
    $ somnia_name = "???"
    $ remerie_name = "Remerie"
    $ marcella_name = "???"

    scene black with dissolve
    dr """
    When the curtain of the night lifts, a certain sleepy town is awaken by the gentle glow of morning.

    The patchwork quilt of the prior night's myriad dreams is kicked off, and the townsfolk go about their day.

    But, alas... When night falls again and the townsfolk begin dreaming, their struggles are laid bare once more.

    Meanwhile, in a quiet corner of the town lies a peculiar café, {ii}cafe name{/ii}.

    Warm dishes and a cozy atmosphere greets anyone who has the pleasure to stop by, but beyond that is an even deeper desire to heal what ails the subconscious.

    Should any sleepy lives follow the café's sweet and savory aroma down the starlight-dusted streets, two busy cooks will await them with open arms.
    """

    scene storefront with dissolve
    s "Hm hmm... Spoonful of sugar~... ♫"
    s "… in a most delightful way~!"
    "Ding!"
    $ somexpr = "gr"
    show somnia
    s "{ii}Rem~er~ie~! ♫{/ii}"
    $ somexpr = "ex"
    s "Take a look! The tarts are done!"
    show somnia at right with ease
    $ remexpr = "th"
    show remi at left
    r "... In a minute."
    s "I’ll go ahead and set some on the display. Would you like to taste one?"
    $ remexpr = "si"
    r "Later, please. I- {w=0.5}{nw}"
    $ somexpr = "de"
    $ remexpr = "sh"
    r "Mmrph!" with sshake
    $ remexpr = "pe"
    r "Mmrrph! Mmrhh nmrph!" with sshake
    $ somexpr = "ne"
    s "How is it?"
    r "{ii}Somnia{/ii}! That's hot!"
    r "I can grab my own, you know?"
    $ somnia_name = "Somnia"
    $ somexpr = "th"
    s "Do you think maybe I used too much jam?"
    $ remexpr = "th"
    r "... No, it was good. The sweet jam you used was less watery this time, so the tart crust held together well."
    $ somexpr = "ne"
    s "I see. I'm glad they turned out better this time!"
    $ somexpr = "de"
    s "I can always count on your sharp palate for tasting, {i}Remi{/i}~!"
    $ remexpr = "fl"
    r "Well, o-of course...!"
    # rth "I can’t say no to Somnia’s desserts!"
    $ remexpr = "ne"
    r "If you’re all done baking, we ought to open up shop."
    show somnia
    s "Sure! I’ll go flip the sign outside."
    hide remi with easeoutleft
    $ somexpr = "gr"
    show somnia at center with ease
    s "Hmm hm~... ♫"
    s "Hm~... A merry tune to toot-"
    $ somexpr = "sh"
    s "AH!" with sshake
    r "What’s wrong?"

# NOTE Cynthia vn shenanigans bookmark
    scene black with flash
    u "Cynthia's only gotten {ii}this{/ii} far in adding all the images n stuff! The following will cont awkwardly. Proceed with caution."

    # Client is passed out on the floor in front of the store
    s "T-there’s a person fallen over on the pavement outside!"
    s "Oh dear, are you okay?"
    r "We can’t have bodies blocking the door for potential customers."
    ml "Hrn..."
    r "Are they... dea-"
    ml "... I-I’m alive..."
    ml "Snrk... *snore...*"
    r "... We should bring them in. It won't do us any good having someone lying on the floor in front of our store."

    scene black with dissolve
    with Pause (1.0)
    scene storefront with dissolve

    show remi at left
    show somnia at right
    # client sprite slowly rises from below
    show marchie with easeinbottom
    ml "So sorry...! A thousand apologies for the concern... *yawn*"
    r "They were napping?!"
# TODO cafe name lol
    ml "Um... Let’s see… Would you happen to know a café around here called {ii}cafe name{/ii}?"
    "..."
    s "Welcome!"
    r "... Welcome."
    s "We’re technically not open yet, but is there anything we can get started for you?"
    ml "Oh... yes! I heard rumors that the shop recently opened again."
    ml "It’s been, what, five years? It’s been so long, I can hardly contain my... *yawn* ...excitement..."
    # s "Five years... what would they happen to know?"
    ml "Let’s see, now... I’ll have... this cherry tart and the..."
    ml "...{ii}Egg pudding pasta with strawberry chives.{/ii}"
    # Somnia and Remerie both perk up with a !
    ml "T-that’s the special menu item of the day, right?"
    s "Yes, you are correct."
    r "Would you like your order for here or to go?"
    ml "For... here."
    r "Alright. Luckily there's still a half hour before the store opens proper so we have time to fulfill your request."
# NOTE change sir to something else?
    s "Kindly please follow us to the back~!"

    scene dreamoffice
    dr """
    Beyond the café's inconspicious backdoor and past the checkered tiles of the kitchen was a curious room, simultaneously deep and light, unfamiliar yet intimate.

    It was an office of sorts. Dimly lit, it housed a bed as its centerpiece, a decorative mirror to taste, and a long olden cabinet.

    The two cooks shut the door after their client, and the three of them became enveloped in the velvety deep.

    It was time to begin.
    """

    ml "This place...!"
    ml "Wow, it looks much more different than what I remember."
    r "Welcome to the {ii}Dream Service{/ii}. Here, we specialize in investigating strange sleep patterns and behavior."
    r "Tell us, what ails you?"
    ml "Um... Well, first, I would like to ask if {ii}Madam{/ii} was... present?"
    s "... Oh! Um..."
    s "Unfortunately, she is currently away. We are her apprentices who’ll be taking care of the store while she's gone."
    r "I'm Remerie, dreams specialist."
    s "And I'm the connoisseur of nightmares, Somnia!"
    ml "It's a pleasure to meet you two. I'm {ii}Marcella Lapin{/ii}."
    $ marcella_name = "Marcella Lapin"
    ml "I wasn't aware she left behind apprentices, but..."
    ml "*yawn* That’s fine. If possible, I would like you two to help me as she once did."

    ml "You see, I’ve been having problems sleeping the past several nights."

    ml """
    I would come home exhausted from work, climb into bed...

    ... Only to endlessly toss and turn until morning comes, unable to catch even a wink of shut-eye!

    It was fine at first... I’ve pulled all-nighters before, but it has now been two weeks…

    I don’t think my body can keep up with my brain anymore.

    It’s been absolutely exhausting to do anything... or get anywhere... *yawn* I just want to sleep…

    Sleeping pills, music, exercise and such have done nothing in my favor...

    I’m a very busy person, see. I have a lot on my plate... But...

    I-I don’t know what will become of me at this rate…!
    """

    s "Oh dear. That sounds like a strong case of insomnia."
    s "I wonder... could it be a nightmare? Something vexing pulling at the heartstrings?"
    s "Dreams made by a dreamless client... My, I wonder how they'll taste!"
    ml "What was that?"
    # s (Maybe a nightmare or @#$%…!)
    r "Don't mind her. For now, we'll get our investigation started."
    # s(I hope it’s a gruesome dream. Those are absolutely scrumptious!)
    r "Marcella, I’m going to need you to lie on this bed."
    ml "A bed... I'm afraid I won't be able to fall asleep in it..."
    r "Don’t worry, we have ways of making you sleep."
    s "If you would please, relax. I’ll be lighting some incense now~!"
    s "When we count to three, you shall fall into a deep sleep..."
    "1… 2… 3…"

    scene black with dissolve
    dr """
    Somnia carefully lit an incense stick, blew it, and placed it in a ceramic holder.

    The insomniac was skeptical to believe incense would work this time, but with nothing left to lose, they closed their eyes nonetheless.

    The aromatic wisps that rolled out shimmered lazily against the glint of the office's few lamps, and seemed to be made of a dream itself.

	As the smoke swirled up lazily into the air, the two, cooks just a moment ago, now began their work as dream eaters.
    """

    jump expression case+"_dream"

label case1_vn_end(result=0):
    scene dreamoffice
    show somnia at left
    show remi at right
    s "The omelette came out great!"
    r "Not my best work considering how much I was scrambling back there, but I admit, it does look enticing..."
    s "Why don't you have it?"
    r "...!"
    s "We both know dreams are harder to come by than nightmares, so please... Help yourself!"
    r "I... Thank you, Somnia."
    s "What's with that sad look? Eat up and enjoy!"
    r "I... I will. Thanks for the meal. Mmrph."
    r "Mm... Soft, warm eggs wrapped in a delicate fold and perfectly sweetened."
    r "The freshly cut fruit serves as a crisp, light flavor in contrast to the richness of the eggs."
    r "This is sure to brighten up anyone’s morning, especially if they had a tiring night before."
    r "I hope with this, we were able to eat away some of Marcella’s worries."
    s "Hehe~... I hope so too!"

    dr """
    The dream eater feasted on the hearty dish conjured from the client's suppressed worries and anxieties.

    Somnia prepared an inspired dish in the adjacent kitchen, in eager anticipation for the client to wake from their repose.

    Slowly, Marcella rose from the bed as the incense fizzled out to a small ember.
    """

    show marchie
    ml "*yaaaawn...*"
    s "Good morning! How are you feeling after that little nap?"
    ml "Um... Hungry..."
    s "You're in luck! We've prepared a dish specially for you."
    s "If you would please follow me back out to the front..."

    scene storefront
    show marchie

    show somnia at right
    show remi at left
    ml "Oh, this is delicious!"
    if result == 1:
        ml "It reminds me of when I first came here and had sleep consulting with, um... what's her name again...?"
        # r and s pitch in with the mentor's name in excitement
        ml "Y-yeah! This dish really takes me back..."
        s "Can you tell us how you two met?"
        ml "Well, it’s been a while ago now. The years have flown by in a blink of an eye..."
        ml "This is a bit of a personal story but, well..."
        ml "F-Five years ago, my family was going through a rough time. It was hard for our parents to be home, what with their odd jobs keeping them busy."
        ml "So I was given the responsibility of taking care of my younger siblings. But to be honest, it was pretty overwhelming."
        ml "I wasn’t even that many years older, but suddenly they were looking to me to take care of them and asking me to take them to places."
        ml "What could I do? I couldn't turn my back on my family..."
    # TODO MENTOR NAME // BAKERY NAME
        ml "The stress of it all led to a lot of sleepless nights. And that’s when I happened to stumble across this bakery and meet {ii}mentor{/ii}."
        ml "In a similar fashion, really! There I was, stretched out on the pavement in front of {ii}bakery{/ii}."
        ml "When I woke up, I was inside the store, with a warm omelette and a comforting smile waiting for me."
        ml "It was difficult, balancing my responsibilities, but I felt a... a duty to take care of my siblings."
        ml "She really listened to my worries. I was able to work hard and continue to support my siblings thanks to her advice."
        ml "Thinking back at it now, she did mention before she had taken on two kids of her own as apprentices. I suppose that must be the two of you."
        ml "We certainly had our fair share of caretaking stories. {ii}mentor{/ii} treasured you two the same I treasured my siblings."
        ml "She was a lovely soul. I hope she comes back soon, for your sake."
        r "..."
        r "Do you think you could share more of your stories with us sometime?"
        s "Yes, please...! We love and miss her a great deal!"
        ml "I would love to hear your stories of {ii}mentor{/ii} as well. If I ever had the time, I'd like to try dropping by more."
    ml "You know, when I took that nap earlier, I actually had what felt like a most wonderful, whimsical dream."
    ml "I don’t remember much of it now, but there were bits and pieces..."
    # Marchie checks the time
    ml "Oh no! I'm going to be late...!"
    ml "..."
    ml "Ah, you know what? I think I should take a day off to rest."
    ml "The shop can go without me for a day."
    ml "Rather than focus on trying to keep up, I honestly ought to step back and see if I can get help from my siblings with these tasks."
    ml "Why, I even dreamed I saw them cleaning up some large piles of debris!"
    "!!"
    ml "But it’s true. They've grown up to be very capable... I think they might be able to help around the floral shop as well!"
    ml "Well... I must be going. Thank you so much for your services!"
    scene black
    # ml leaves in their usual hurried disposition but with a happier energy in the steps. They look like they have an idea of what to do next…!

    scene storefront
    show somnia at right
    show remi at left
    s "Phew, all in a day's work! Right, Remi?"
    r "What do you mean? Don't forget the clean-up job you put me through after your little experiment on the dish!"
    s "Hehe~... I just wanted to impress you with a dash of whimsy!"
    s "It’s funny, Marchie reminded me a little of you- working a little too hard at times..."
    s "You ought to take a card from Marchie’s book and take it easy- have some fun now and then!"
    r "I think you have enough fun for the both of us..."
    s "Don't tell me you didn't have fun in that dream~! The cute bunnies? Cooking up a yummy new dream dish? It's been an awful long time since we've had a client!"
    r "While I can't say the same about the bunnies, I do have to agree that the dream dish was quite good…"
    s "Hm? Do I spy a smile turning the corners of your mouth...?"
    r "Wh-what?"
    s "I do! You really liked the dish, didn't you!"
    r "O-of course! I fixed it and made it delectable, no thanks to you!"
    # Somnia laughs lightly but her eyes are turned downward.
    s "*sigh...*"
    s "It takes me back."
    s "It's been five years since {ii}mentor{/ii} disappeared..."
    r "..."
    r "Starting the morning with a dish like this, it reminds me of when she would prepare fruit slices before opening."
    s "Y-you remember something like that?"
    r "Of course, the way you plated the fruit slices on the client's dish... It's just like how she did it."
    s "I... I suppose it is, isn't it."
    rth "Does Somnia really not remember? Starting the day with small delights from our mentor only ever brightened up my day."
    s "I'm glad it reminded you of her, if only for a little bit."
    r "You two were close, weren't you? It's only natural you'd pick up some of her tendencies."
    s "R... Right..."

    dr """
    For the usually bubbly Somnia to fall silent... Well, it was certainly a rare sight to behold, and Remerie quickly took note.

    Providing comfort was far from Remerie's forte, but seeing Somnia so unusually despondent kindled a flame of determination within her.
    """

    r "Somnia..."
    r "We agreed to watch the store and wait for her, right?"
    r "It's our duty to keep the store as welcoming as it was before she left."
    # would be cute if Somnia's expression changed gradually back to her neutral sprite throughout this convo
    r "I know it's hard to play the waiting game, but let's get to work... for the day she'll return."

    dr """
    Chattering away, the dream eaters gathered their bearings for the start of another day.

    Another day, another chance to see their mentor.

    With that hope in their hearts, the two open up shop and await the return of their old friend.
    """
    return
