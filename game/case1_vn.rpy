# Case 1
# ------------------------------------------------------------------------
label case1_vn:
    $ case = "case1"
    $ somnia_name = "???"
    $ remerie_name = "Remerie"
    $ marcella_name = "???"

    scene black with dissolve
    # add nighttime sfx (like soft wind)
    dr """
    When the curtain of the night lifts, a sleepy town is awaken by the gentle glow of morning.

    The patchwork quilt of the prior night's myriad dreams is kicked off, and the townsfolk go about their day.

    But, alas... Once night falls again and the townsfolk begin dreaming, their struggles are laid bare once more.

    Luckily, in a quiet corner of the town lies {ii}Cafe Nemo{/ii}, a cozy café that greets anyone who visits with warm meals and a warmer atmosphere.
    """
    dr "Should any sleepy lives follow the café's sweet and savory aroma down the starlight-dusted streets, they'll find two busy cooks awaiting with open arms."
    pause 1.0
    play music storefront
    pause 2.0
    scene storefront with dissolve
    s "Hm hmm... Spoonful of sugar~... {mn}"
    s "… in a most delightful way~!"
    "Ding!"
    $ somexpr = "gr"
    show somnia with dissolve
    s "{ii}Rem~{w=.1}er~{w=.1}ie~! {mn}{/ii}"
    $ somexpr = "ex"
    s "Take a look! The tarts are done!"
    show somnia at right with ease
    $ remexpr = "th"
    show remi at left with dissolve
    r "... In a minute."
    $ somexpr = "ne"
    s "I’ll go ahead and set some on the display. Would you like to taste one?"
    $ remexpr = "si"
    r "Later, please. I- {w=0.5}{nw}"
    $ somexpr = "de"
    show somnia at center with ease
    $ remexpr = "sh"
    r "Mmrph! {w=0.5}{nw}" with sshake
    $ remexpr = "pe"
    r "Mmrrph! Mmrhh nmrph!" with sshake
    show somnia at right with ease
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
    r "Regardless, you should know better than to handle tarts that are too hot to touch!"
    $ somexpr = "ne"
    $ remexpr = "si"
    r "*Sigh*"
    r "{i}(Despite that, I can’t say no to Somnia’s desserts!){/i}"
    $ remexpr = "ne"
    r "If you’re all done baking, we ought to open up shop."
    show somnia
    s "Sure! I’ll go flip the sign outside."
    hide remi with easeoutleft
    $ somexpr = "gr"
    show somnia at center with ease
    s "Hmm hm~... {mn}"
    s "Hm~... A merry tune to toot-"
    $ somexpr = "bi"
    stop music
    s "AH!" with sshake
    r "What’s wrong?"
    s "T-there’s a person fallen over on the pavement outside!"
    $ somexpr = "sh"
    s "Oh dear, are you okay?"
    show somnia at right with ease
    $ remexpr = "pe"
    show remi at left with dissolve
    r "We can’t have bodies blocking the door for potential customers."
    ml "Hrn..."
    $ remexpr = "bi"
    r "Are they... dea-"
    ml "... I-I’m alive..."
    ml "Snrk... {i}*snore...*{/i}" with sshake
    play music weird
    $ remexpr = "si"
    r "......"
    $ somexpr = "th"
    s "......"
    $ remexpr = "ne"
    r "... We should bring them in. It won't do us any good having someone lying on the floor in front of our store."

    scene black with dissolve
    with Pause (1.0)

    $ somexpr = "ne"
    $ remexpr = "ne"
    scene storefront with dissolve
    show remi at left
    show somnia at right
    with dissolve
    show mar with easeinbottom

    ml "So sorry...! A thousand apologies for the concern..."
    $ marexpr = "ya"
    extend "{cps=10}*yaaaaawn*" with sshake
    $ remexpr = "sh"
    r "(They were napping?!)"
    $ somexpr = "sh"
    s "(Were they... sleeping on the pavement outside...?)"
    $ marexpr = "ne"
    $ remexpr = "ne"
    ml "Um... Let’s see… Would you happen to know a café around here called {ii}Café Nemo{/ii}?"
    $ _last_say_who = "None"
    u "..."
    $ somexpr = "de"
    s "Welcome!"
    r "... Welcome."
    $ somexpr = "ne"
    s "We’re technically not open for the day yet, but since you're here, is there anything we can get started for you?"
    $ marexpr = "gr"
    ml "Oh... yes! I heard rumors that the café recently reopened for business again."
    $ marexpr = "ya"
    ml "It’s been, what, {ii}five years{/ii}? It’s been so long, I can hardly contain my... {cps=10}*yawn* ...excitement...{/cps}"
    $ somexpr = "th"
    s "(Five years... what would they happen to know?)"
    $ marexpr = "ne"
    ml "Let’s see, now... I’ll have... this cherry tart and the..."
    $ remexpr = "sh"
    $ somexpr = "bi"
    ml "...{ii}Egg pudding pasta with strawberry chives.{/ii}" with flash
    $ marexpr = "fr"
    ml "T-that’s the special menu item of the day, right?"
    $ somexpr = "gr"
    $ remexpr = "ne"
    s "Yes, you are correct."
    $ remexpr = "th"
    r "Would you like your order for here or to go?"
    $ marexpr = "th"
    ml "For... here."
    $ remexpr = "ne"
    r "Alright. Luckily there's still a half hour before the store opens proper so we have time to fulfill your request."
    $ somexpr = "ex"
    s "Kindly please follow us to the back~!"
    stop music fadeout (2.0)
    hide somnia with easeoutright
    hide remi with easeoutleft
    hide mar with dissolve
    pause(1.0)

    show storefront:
        xalign 0.5 yalign 0.5
        alpha 1.0
        pause 0.5
        parallel:
            linear 3.0 zoom 2 truecenter
        parallel:
            linear 3.0 alpha 0.0
    pause(1.0)
    scene black with dissolve
    pause (1.0)
    play music dreamoffice fadein(2.0)
    pause(2.0)
    scene dreamoffice with dissolve

    dr """
    Beyond the café's inconspicious backdoor and past the checkered tiles of the kitchen was a curious room, simultaneously deep and light, unfamiliar yet intimate.

    It was an office of sorts. Dimly lit, it housed a bed as its centerpiece, a decorative mirror to taste, and a long olden cabinet.

    The two cooks shut the door after their client, and the three of them became enveloped in the velvety deep.

    It was time to begin.
    """

    $ remexpr = "ne"
    $ somexpr = "ne"

    show mar at center with dissolve
    show remi at left
    show somnia at right
    with dissolve
    $ marexpr = "gr"
    ml "This place...!"
    $ marexpr = "th"
    ml "Wow, it looks much more different than what I remember."
    $ remexpr = "de"
    r "Welcome to the {ii}Dream Service{/ii}. Here, we specialize in investigating strange sleep patterns and behavior."
    $ remexpr = "ne"
    r "Tell us, what ails you?"
    $ marexpr = "fr"
    ml "Um... Well, first, I would like to ask if {ii}Madam Nemo{/ii} was... present?"
    $ remexpr = "sh"
    $ somexpr = "sh"
    s "... Oh! {w=0.5}{nw}"
    $ somexpr = "di"
    extend "Um..."
    $ marexpr = "ne"
    $ somexpr = "th"
    s "Unfortunately, she is currently away. We are her apprentices who’ll be taking care of the store while she's gone."
    $ remexpr = "gr"
    r "I'm Remerie, dreams specialist."
    $ somexpr = "gr"
    s "And I'm the connoisseur of nightmares, Somnia!"
    $ marexpr = "gr"
    ml "It's a pleasure to meet you two. I'm {ii}Marcella Lapin{/ii}."
    $ marcella_name = "Marcella Lapin"
    $ marexpr = "ne"
    ml "I wasn't aware she left behind apprentices, but..."
    $ marexpr = "ya"
    ml "*yawn* That’s fine. If possible, I would like you two to help me as she once did."

    $ marexpr = "ne"
    $ remexpr = "ne"
    $ somexpr = "ne"
    ml "You see, I’ve been having problems sleeping the past several nights."
    ml "I would come home exhausted from work, climb into bed..."
    $ marexpr = "fr"
    ml "... Only to endlessly toss and turn until morning comes, unable to catch even a wink of shut-eye!"
    ml "It was fine at first... I’ve pulled all-nighters before, but it has now been two weeks…"
    ml "I don’t think my body can keep up with my brain anymore."
    $ marexpr = "ya"
    ml "It’s been absolutely exhausting to do anything... or get anywhere... *yawn* I just want to sleep…"
    $ marexpr = "ne"
    ml "Sleeping pills, music, exercise and such have done nothing in my favor..."
    ml "I’m a very busy person, see. I have a lot on my plate... But..."

    $ marexpr = "wo"
    ml "I-I don’t know what will become of me at this rate…!"
    $ somexpr = "sh"
    s "Oh dear. That sounds like a strong case of insomnia."
    $ somexpr = "th"
    s "I wonder... could it be a nightmare? Something vexing pulling at the heartstrings?"
    $ somexpr = "ex"
    s "Dreams made by a dreamless client... My, I wonder how they'll taste!"
    $ marexpr = "ne"
    ml "What was that?"
    # s (Maybe a nightmare or @#$%…!)
    $ remexpr = "si"
    r "Don't mind her. For now, we'll get our investigation started."
    # s(I hope it’s a gruesome dream. Those are absolutely scrumptious!)
    $ remexpr = "ne"
    $ somexpr = "ne"
    r "Marcella, I’m going to need you to lie on this bed."
    $ marexpr = "fr"
    ml "A bed... I'm afraid I won't be able to fall asleep in it..."
    $ remexpr = "gr"
    r "Don’t worry, we have ways of making you sleep."
    $ somexpr = "gr"
    $ marexpr = "ne"
    s "If you would please, relax. I’ll be lighting some incense now~!"
    $ remexpr = "ne"
    $ somexpr = "ne"

    dr """
    Somnia carefully lit an incense stick, blew it, and placed it in a ceramic holder.

    The insomniac was skeptical to believe incense would work this time, but with nothing left to lose, they closed their eyes nonetheless.
    """

    s "When we count to three, you shall fall into a deep sleep..."
    show black with dissolve:
        linear 2 alpha 0.15
    u "1...{w=0.5}{nw}"
    show black:
        linear 2 alpha 0.40
    extend "{w=1.0}2...{w=0.5}{nw}"
    show black:
        linear 2 alpha 0.80
    extend "{w=1.0}3......{w=0.5}{nw}"
    show black:
        linear 2.0 alpha 1.0
    extend "{w=1.0}...{w=0.5}{nw}"
    scene black with dissolve
    pause (2.0)

    stop music fadeout (5.0)
    dr """The aromatic wisps that rolled out shimmered lazily against the glint of the office's few lamps, and seemed to be made of a dream itself.

	As the smoke swirled up lazily into the air, the two, cooks just a moment ago, now began their work as {ii}dream eaters{/ii}.
    """
    pause (2.0)
    jump expression case+"_dream"

label case1_vn_end(result=0):
    stop music fadeout (2.0)
    scene dreamoffice
    with dissolve
    show somnia at right
    show remi at left
    with dissolve
    play music dreamoffice
    $ somexpr = "de"
    s "The omelette came out great!"
    $ remexpr = "si"
    r "Not my best work considering how much I was scrambling back there, but I admit, it does look enticing..."
    $ somexpr = "ne"
    s "Why don't you have it?"
    $ remexpr = "bi"
    r "...!" with flash
    $ somexpr = "de"
    s "We both know dreams are harder to come by than nightmares, so please... Help yourself!"
    $ remexpr = "fl"
    r "I... Thank you, Somnia."
    $ somexpr = "gr"
    s "What's with that sad look? Eat up and enjoy!"
    $ remexpr = "gr"
    r "I... I will. Thanks for the meal. Mmrph."
    $ remexpr = "th"
    r "Mm... Soft, warm eggs wrapped in a delicate fold and perfectly sweetened."
    $ remexpr = "gr"
    r "The freshly cut fruit serves as a crisp, light flavor in contrast to the richness of the eggs."
    r "This is sure to brighten up anyone’s morning, especially if they had a tiring night before."
    $ remexpr = "th"
    r "I hope with this, we were able to eat away some of Marcella’s worries."
    $ somexpr = "gr"
    s "Hehe~... I hope so too!"

    dr """
    The dream eater feasted on the hearty dish conjured from the client's suppressed worries and anxieties.

    Somnia prepared an inspired dish in the adjacent kitchen, in eager anticipation for the client to wake from their repose.

    Slowly, Marcella rose from the bed as the incense fizzled out to a small ember.
    """

    $ marexpr = "ya"
    show mar with dissolve
    ml "*Yaaaawn...*" with sshake
    $ somexpr = "gr"
    s "Good morning! How are you feeling after that little nap?"
    $ marexpr = "ne"
    ml "Um..."
    $ marexpr = "th"
    ml "Hungry..."
    $ somexpr = "de"
    s "You're in luck! We've prepared a dish specially for you."
    $ somexpr = "ne"
    s "If you would please follow me back out to the front..."

    scene storefront with dissolve

    show mar
    show somnia at right
    show remi at left
    $ marexpr = "aw"
    ml "Oh, this is delicious!"
    if result == 1:
        $ marexpr = "th"
        ml "It reminds me of when I first came here and had sleep consulting with, um... what's her name again...?"
        s "Ms. Nemo!!"
        r "Ms. Nemo."
        $ marexpr = "aw"
        ml "Y-yeah! This dish really takes me back..."
        s "Can you tell us how you two met?"
        $ marexpr = "la"
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
