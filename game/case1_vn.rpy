# ------------------------------------------------------------------------
# Case 1
# ------------------------------------------------------------------------
label case1_vn:
    $ _skipping = True # enable skipping option
    $ show_quick_menu = True
    $ case = "case1"
    $ somnia_name = "???"
    $ remerie_name = "Remerie"
    $ marcella_name = "???"
    $ renpy.start_predict(
        "images/sprites/somnia_*.png",
        "images/sprites/remerie_*.png",
        "images/sprites/marcella_*.png",
        "images/sprites/bg_dreamoffice.png",
        "images/sprites/bg_storefront.png",
    )
    stop music fadeout(2.0)
    scene black with dissolve
    pause 2.0

    call titlezone from _call_titlezone

    dr """
    When the curtain of the night lifts, a sleepy town wakes by the gentle glow of morning.

    The townsfolk go about their days, shedding the patchwork quilt of a night's myriad of dreams.

    However... When the townsfolk fall in a deep slumber once more, the visions of night come out to play.

    The fantasies of wondrous reverie entertain those who have nothing to worry about.

    Yet, the troubled fear how their nighttime tales will unfold.

    Luckily, in a quiet corner of the town lies {ii}Café Nemo{/ii}. A cozy café that greets anyone who visits with a warm meal and a warmer atmosphere.

    Their dreamy dishes and a mellow milieu offer a soothing repose from troubled, busy lives.

    Should any uneasy lives trail the starlit streets for the café's incandescent aromas, they'll find two cooks with open arms.
    """

    pause 1.0
    show outside:
        xpos 0 ypos -1000
        parallel:
            xalign 0.5 yalign 1.0
            linear 2.0 zoom 1.2
        parallel:
            linear 2.0 alpha 0.0
    pause 4.0
    $ show_quick_menu = True
    scene storefront with dissolve
    s "Hm hmm... Spoonful of sugar~... {mn}"
    s "… in a most delightful way~!"
    u "{i}Ding!{/i}"
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
    r "Mmrph! {w=0.5}{nw}" with shake()
    $ remexpr = "pe"
    r "Mmrrph! Mmrhh nmrph!" with shake()
    show somnia at right with ease
    $ somexpr = "ne"
    s "How is it?"
    r "{ii}Somnia{/ii}! That's hot!"
    r "I can grab my own, you know?"
    $ somnia_name = "Somnia"
    $ somexpr = "th"
    s "Do you think I used too much jam?"
    $ remexpr = "th"
    r "... No, the portions are well-balanced."
    r "The jam you made this time has a better consistency, so the tart shells held together nicely."
    r "You also took my advice on making a thicker, lighter tart shell, huh... Good work."
    $ somexpr = "ne"
    s "Aw, you flatterer! Your tips are always topnotch!"
    $ somexpr = "de"
    s "I can always count on your sharp palate for tasting, {i}Remi{/i}~!"
    $ remexpr = "fl"
    r "Well, o-of course...!"
    r "Regardless, you should know better than to handle tarts that are too hot to touch!"
    r "{th}(Despite that, I can’t say no to Somnia’s desserts!){/th}"
    $ somexpr = "ne"
    $ remexpr = "si"
    r "*sigh*"
    $ somexpr = "sh"

    s "My, Remi, you've been at inventory count for quite a while. Allow me to finish it up instead while you take a breather!"
    $ remexpr = "th"
    r "It's fine, Somnia. I know you think it's a bore to count everything-{w=0.6}{nw}"
    $ somexpr = "ne"
    s "I won't take no for an answer, Remerie! You've been preparing since 5 AM!"
    $ somexpr = "gr"
    s "Besides, we seem to be early on setting up shop, anyway. There's no harm in taking breaks, is there?"
    s "So if you would... Please sit down, relax, and enjoy a fresh tart made with love~!"
    $ remexpr = "fl"
    r "I... If you insist."
    $ remexpr = "si"
    r "There's no arguing, is there..."
    $ remexpr = "ne"
    r "Here, I just have the last page to check off on."
    $ somexpr = "de"
    s "Yes, ma'am! Hm hmm~... {mn}"
    hide remi with easeoutleft
    show somnia at center with ease
    $ somexpr = "sh"
    s "Oh? There are only three things left to check."
    $ somexpr = "gr"
    s "Done, done, and done!"
    s "If that's all, I'll go flip the sign outside for any early birds to arrive."
    $ somexpr = "gr"
    s "Hmm hm~... {mn}"
    s "Hm~... A merry tune to toot-"
    $ somexpr = "bi"
    stop music
    s "AH!" with shake()
    r "What’s wrong?"
    s "T-there’s a person fallen over on the pavement outside!"
    show somnia at right with ease
    show marchiecollapse at truecenter with Dissolve(0.8)
    $ remexpr = "pe"
    show remi at left with dissolve
    r "We can’t have bodies blocking the door for potential customers."
    $ somexpr = "sh"
    s "Oh dear, are they okay?"
    ml "{th}Hrn...{/th}"
    $ remexpr = "bi"
    r "Are they... {ii}d-dea-{/ii}{w=0.5}{nw}"
    ml "{th}... I-I’m alive...{/th}"
    ml "Snrk... {i}*snore...*{/i}" with shake()
    play music weird
    $ remexpr = "si"
    r "......"
    $ somexpr = "th"
    s "......"
    $ remexpr = "ne"
    r "... We should bring them in. It won't do us any good having someone lying on the floor in front of our store."
    scene black with dissolve
    play sound welcomedoor
    with Pause (1.0)

    $ somexpr = "ne"
    $ remexpr = "ne"
    scene storefront with dissolve
    show remi at left
    show somnia at right
    with dissolve
    show mar with easeinbottom

    ml "So sorry...! A thousand apologies for the concern... "
    $ marexpr = "ya"
    play sound yawn
    extend "{cps=10}*yaaaaawn...*" with shake()
    $ remexpr = "sh"
    r "{th}(They were napping?!){/th}"
    $ somexpr = "sh"
    s "{th}(Were they... sleeping on the pavement outside...?){/th}"
    $ marexpr = "ne"
    $ remexpr = "ne"
    ml "Um... Let’s see... Would you happen to know a café around here called {ii}Café Nemo{/ii}?"
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
    ml "It’s been, what, {ii}five years{/ii}? It’s been so long, I can hardly contain my... {nw}"
    play sound yawn
    extend "{cps=10}*yaaawn*{/cps} ...excitement..."
    $ somexpr = "th"
    s "{th}(Five years? Why, that's around the time when {ii}she{/ii}... Hmm...){/th}"
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
    r "Welcome to {ii}Slumberworks{/ii}. Here, we specialize in investigating strange sleep patterns and behavior."
    $ remexpr = "ne"
    r "Tell us, what ails you?"
    $ marexpr = "fr"
    ml "Um... Well, first, I would like to ask if {ii}Miss Nemo{/ii} is... present?"
    $ remexpr = "sh"
    $ somexpr = "sh"
    s "... Oh! {w=0.5}{nw}"
    $ somexpr = "di"
    extend "Um..."
    $ marexpr = "ne"
    $ somexpr = "th"
    s "Unfortunately, she is currently away. We are her apprentices who’ll be taking care of the store while she's gone."
    $ somexpr = "ne"
    s "However, you're in good hands! We provide this specialty service as partners."
    $ remexpr = "gr"
    r "I'm Remerie, {ii}dreams specialist{/ii}."
    $ somexpr = "gr"
    s "And I'm the {ii}connoisseur of nightmares{/ii}, Somnia!"
    $ marexpr = "gr"
    ml "It's a pleasure to meet you two. I'm {ii}Marcella Lapin{/ii}."
    $ marcella_name = "Marcella Lapin"
    $ marexpr = "ne"
    ml "I wasn't aware she left behind apprentices, but..."
    $ marexpr = "ya"
    play sound yawn
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
    ml "It’s been absolutely exhausting to do anything... or get anywhere... {nw}"
    play sound yawn
    extend "*yawn* I just want to sleep…"
    $ marexpr = "ne"
    ml "Sleeping pills, music, exercise and such have done nothing in my favor..."
    ml "I’m a very busy person, see. I have a lot on my plate... But..."

    $ marexpr = "wo"
    ml "I-I don’t know what will become of me at this rate…!"
    $ somexpr = "sh"
    s "Oh dear. That sounds like a strong case of insomnia."
    $ somexpr = "th"
    s "I wonder... could it be a nightmare? Something vexing pulling at the heartstrings?"
    $ somexpr = "de"
    s "Dreams made by a sleepless client... My, I wonder how they'll taste!"
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
    ml "A bed... Despite how comfortable it might be, I'm afraid I won't be able to fall asleep in it..."
    $ remexpr = "gr"
    r "Don’t worry, we have ways of making you sleep."
    $ somexpr = "gr"
    $ marexpr = "ne"
    s "If you would please, relax. I’ll be lighting some incense now~!"
    $ remexpr = "ne"
    $ somexpr = "ne"
    play sound incense
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

    show enterdream with dissolve:
        xanchor 0 yanchor 0
        xpos 0 ypos -2000


    dr """The aromatic wisps that rolled out shimmered lazily against the glint of the office's few lamps, and seemed to be made of a dream itself.

	As the smoke swirled up lazily into the air, the two, cooks just a moment ago, now began their work as {ii}dream eaters{/ii}.
    """
    call intodream from _call_intodream

    pause (2.0)
    $ renpy.stop_predict(
        "images/sprites/somnia_*.png",
        "images/sprites/remerie_*.png",
        "images/sprites/marcella_*.png",
        "images/sprites/bg_dreamoffice.png",
        "images/sprites/bg_storefront.png",
        )
    jump expression case+"_dream"

label case1_vn_end(result=0):
    $ marcella_name = "Marcella Lapin" # delete this before publishing
    $ _skipping = True # enable skipping option
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
    r "Not my best work, but I admit it does look enticing..."
    $ somexpr = "ne"
    s "Why don't you have it?"
    $ remexpr = "bi"
    r "...!"
    $ somexpr = "de"
    s "We both know dreams are harder to come by than nightmares, so... Help yourself!"
    $ remexpr = "fl"
    r "I... Thank you, Somnia."
    $ somexpr = "gr"
    s "What's with that sad look? Eat up and enjoy!"
    $ remexpr = "gr"
    r "I... I will. {i}Bonne nuit et bon appétit{/i}."
    $ remexpr = "th"
    r "Mm... Soft, warm eggs wrapped in a delicate fold and perfectly seasoned."
    $ remexpr = "gr"
    r "The freshly cut fruit serves as a crisp, light flavor in contrast to the richness of the eggs."
    r "This is sure to brighten up anyone’s morning, especially if they had a tiring night before."
    $ remexpr = "th"
    r "I hope with this, we were able to eat away some of Marcella’s worries."
    $ somexpr = "gr"
    s "Hehe~... I hope so too!"

    scene incenseout with Dissolve(2.0)

    dr """
    The dream eater feasted on the hearty dish conjured from the client's suppressed worries and anxieties.

    Somnia prepared an inspired dish in the adjacent kitchen, in eager anticipation for the client to wake from their repose.

    Slowly, Marcella rose from the bed as the incense fizzled out to a small ember.
    """
    pause (1.0)

    scene dreamoffice with fade

    $ marexpr = "ya"
    show mar with dissolve
    play sound yawn
    ml "*Yaaaawn...*" with shake()
    show mar at right with ease
    show remi at left with dissolve
    r "You're awake. How are you feeling after your nap?"
    $ marexpr = "ne"
    ml "Um..."
    $ marexpr = "th"
    ml "Hungry..."
    $ remexpr = "ne"
    r "That's to be expected. Fortunately, we've prepared a dish specially for you."
    r "If you would please follow me back out to the front..."
    stop music fadeout 2.0
    scene black with dissolve
    pause (2.0)
    play music storeend fadein 4.0
    scene storefront with dissolve

    $ remexpr = "ne"
    $ somexpr = "ne"
    $ marexpr = "aw"
    show mar with dissolve
    show somnia at right with easeinright
    show remi at left with easeinleft

    ml "Oh, this is delicious!" with flash
    if result >= 1:
        $ marexpr = "th"
        ml "It reminds me of when I first came here and had sleep consulting with, um... what's her name again...?"
        $ somexpr = "de"
        s "Miss Nemo!!"
        $ remexpr = "th"
        r "Miss Nemo."
        $ marexpr = "aw"
        ml "Y-yeah! This dish really takes me back..."
        $ somexpr = "th"
        s "Can you tell us how you two met?"
        $ marexpr = "la"
        ml "Well, it’s been a while ago now. The years have flown by in a blink of an eye..."
        $ marexpr = "th"
        ml "This is a bit of a personal story, but..."
        $ marexpr = "fr"
        $ somexpr = "ne"
        $ remexpr = "ne"
        ml "Five years ago, my family was going through a rough time. It was hard for our parents to be home, what with their odd jobs keeping them busy."
        ml "So I was given the responsibility of taking care of my younger siblings. But to be honest, it was pretty overwhelming."
        ml "I'm not that many years older than our second oldest child, but suddenly all of them were looking to me... to take care of them."
        $ marexpr = "wo"
        ml "What could I do? I couldn't turn my back on my family..."
        ml "The stress of it all led to a lot of sleepless nights. I was tired, sure, but that was nothing compared to letting my siblings down."
        ml "That’s when I stumbled across this café and meet {ii}Miss Nemo{/ii}."
        $ marexpr = "la"
        ml "In a similar fashion, really! There I was, stretched out on the pavement in front of {ii}Café Nemo{/ii}."
        $ marexpr = "fr"
        ml "When I woke up, I was inside the store, with a warm omelette and a comforting smile waiting for me."
        ml "It was difficult, balancing my responsibilities, but I felt a... a duty to take care of my siblings."
        ml "When she found me, she was so concerned! I didn't realize how hard I had been pushing myself until, well, my exhaustion got the best of me."
        $ marexpr = "la"
        ml "She really listened to my worries and offered me some words of wisdom. I was able to work hard and continue to support my siblings thanks to her advice."
        $ marexpr = "gr"
        ml "I also came back regularly to help myself to her specialty omelette!"
        $ marexpr = "wo"
        ml "B-but... here I am again. Falling asleep in odd places, being consumed by worries once more..."
        ml "I can't let this happen again. I need to find the time to take care of myself, so I can better take care of my siblings."
        $ marexpr = "gr"
        ml "I really can't thank you two enough for helping me with such kindness as Miss Nemo did years ago."
        $ marexpr = "aw"
        ml "Thinking back at it now, she did mention before she had taken on two kids of her own as apprentices. I suppose that must be the two of you."
        $ marexpr = "gr"
        ml "It's amazing how well you recaptured that flavor and nostalgia that I once felt years ago. I'm sure she would be proud."
        ml "We certainly had our fair share of caretaking stories. {ii}Miss Nemo{/ii} treasured you two the same I treasured my siblings."
        ml "She was a lovely soul. I hope she comes back soon, for your sake."
        $ somexpr = "di"
        s "That was a beautiful story..."
        $ remexpr = "th"
        r "..."
        $ remexpr = "ne"
        r "Do you think you could share more of your stories with us sometime?"
        $ somexpr = "sh"
        s "Yes, please...! We love and miss her a great deal!"
        $ somexpr = "gr"
        $ remexpr = "gr"
        $ marexpr = "aw"
        ml "I would love to hear your stories of {ii}Miss Nemo{/ii} as well. I'll definitely make space in my schedule for a short routine visit."
        $ marexpr = "gr"
        ml "Perhaps I'll even bring my siblings! Little Whitney doesn't care much for cherry flavored snacks, but no one could possibly deny your delectable cherry tarts!"
    $ somexpr = "ne"
    $ remexpr = "ne"
    $ marexpr = "th"
    ml "You know, when I took that nap earlier, I actually had what felt like a most wonderful, whimsical dream."
    ml "I don’t remember much of it now, but there were bits and pieces..."
    $ marexpr = "wo"
    ml "Oh no! I'm going to be late...!"
    $ marexpr = "th"
    ml "..."
    $ marexpr = "la"
    ml "Ah, you know what? If today's visit has told me anything, I think it's that I should take a day off to rest."
    ml "The flower shop can go without me for a day."
    ml "Rather than focus on trying to keep up, I honestly ought to step back and see if I can get help from my siblings with these tasks."
    $ marexpr = "la"
    ml "It's the silliest thing. I even dreamt of a messy tea party, and that my siblings were cleaning up the mess!"
    $ _last_say_who = "None"
    $ somexpr = "sh"
    $ remexpr = "sh"
    u "!!" with flash
    ml "But it’s true. They've grown up to be very capable... I think they might be able to help around the house and the floral shop!"
    $ marexpr = "aw"
    ml "Well, I should be going. Thank you so much for your services!"
    scene black with dissolve
    with Pause(2.0)

    scene storefront with dissolve
    $ somexpr = "gr"
    $ remexpr = "ne"
    show somnia at right with easeinright
    show remi at left with easeinleft
    s "Phew, all in a day's work! Right, Remi?"
    s "It’s funny, Marchie reminded me a little of you- working a little too hard at times..."
    s "You ought to take a card from Marchie’s book and take it easy- have some fun now and then!"
    $ remexpr = "si"
    r "I think you have enough fun for the both of us..."
    $ somexpr = "ex"
    s "Don't tell me you didn't have fun in that dream! The cute bunnies? Cooking up a yummy new dream dish?"
    s "It's been a dreadfully long time since we've had a client!" with flash
    $ remexpr = "gr"
    r "While I can't say the same about the {i}cute bunnies{/i}, I do have to agree that the dream dish was quite good…"
    $ somexpr = "bi"
    s "Hm? Do I spy a smile turning the corners of your mouth...?"
    $ remexpr = "bi"
    r "Wh-what?"
    $ somexpr = "de"
    s "I do! You really liked the dish, didn't you!"
    $ remexpr = "fl"
    r "O-of course! What's not to like about a dream dish? It's been quite some time since I've indulged in one."
    if result >= 1:
        $ remexpr = "gr"
        r "Your magic certainly added quite a sweet and tangy flavor that I didn't expect, but welcomed nonetheless."
        $ somexpr = "gr"
        s "Remi, you don't need to be so bashful about enjoying something!"
        s "You know I'd only ever make delicious treats for you~!"
        $ remexpr = "fl"
        r "T-thank you, Soms."

    $ somexpr = "di"
    s "*sigh...*"
    $ remexpr = "ne"
    s "It takes me back."
    s "It's been five years since {ii}Miss Nemo{/ii} disappeared..."
    $ remexpr = "th"
    r "..."
    $ remexpr = "gr"
    r "Starting the morning with a dish like this, it reminds me of when she would prepare fruit slices before opening."
    $ remexpr = "sh"
    s "Y-you remember something like that?"
    $ remexpr = "ne"
    r "Of course, the way you plated the fruit slices on the client's dish... It's just like how she did it."
    $ somexpr = "di"
    s "I... I suppose it is, isn't it."
    $ remexpr = "th"
    r "{th}(Does Somnia really not remember? Starting the day with small delights from our mentor only ever brightened up my day.){/th}"
    s "I suppose... I'm glad it reminded you of her, if only for a little bit."
    $ remexpr = "ne"
    r "You two were close, weren't you? It's only natural you'd pick up some of her tendencies."
    s "R... Right..."
    $ remexpr = "sh"

    dr """
    For the usually bubbly Somnia to fall silent... Well, it was certainly a rare sight to behold, and Remerie quickly took note.

    Providing comfort was far from Remerie's forte, but seeing Somnia so unusually despondent kindled a flame of determination within her.
    """
    $ remexpr = "th"
    r "Somnia..."
    $ somexpr = "sh"
    r "We agreed to watch the store and wait for her, right?"
    r "It's our duty to keep the store as warm and welcoming as it was before she left."
    $ somexpr = "ne"
    $ remexpr = "gr"
    r "I know it's hard to play the waiting game, but let's get to work... for the day she'll return."
    $ remexpr = "de"
    r "Until then, don't worry. You're not alone. I'll always stay by your side."
    $ somexpr = "de"
    s "Hehe..."
    s "Remi, you're such a charmer~..." with flash
    $ remexpr = "fl"
    r "A-ahem..."
    s "Aw, you're blushing!"
    r "Soms, please... W-we need to get the store ready." with shake()
    s "Whatever you say, {ii}Rem~{w=.1}er~{w=.1}ie~! {mn}{/ii}"

    dr "Chattering away, the dream eaters gathered their bearings for the start of another day."

    show outside with dissolve:
        xanchor 0 yanchor 0
        xpos 0 ypos -1080
        xalign 0.5 yalign 0.85
        zoom 3
        ease_quad 5 zoom 1

    dr """

    Another day, another chance to see their mentor.

    With that hope in their hearts, the two open up shop and await the return of their old friend.

    And so, Café Nemo resumes its day to day business, providing dreamy dishes to those whose hungers wish to be sated with delectable treats...

    ...And those whose who wander in with dreams composed of worries, fears, and woes will provide the same satisfaction to the {ii}dream eaters{/ii}.
    """
    call endscene from _call_endscene
    jump credits_start

    # return # change this to jump to credits page for demo
