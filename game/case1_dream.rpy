# TODO:
    # - checks for debris(?)
    # - progress check is a bit difficult rn bc I want the label to start when the player goes to the 2nd screen
    # - update flags with view so no repeating flags
    # - b-b-b-bugs..
    # - current bug where screen naturally drifts left upon loading

label tina:
    "tina basement is empty right now... (come back later)"
    return

label case1_dream:
    python:
        bg = "wonderland2" # background image
        page_width = 1720 # screen page width
        total_pages = 3 # total pages in investigation
        inventory = Inventory()
        interactions = Interactions()

        unlocked_pages = 0 # default is 0
        current_page = 0 # start at 0
        finished = False # default is false, but true for testing
    scene black
    show screen dream()
    window hide
    dreamSom "Woah…!"
    dreamRem "I've got you. Watch your step, it's a mess in here."
    dreamSom "Our client must really have a hard time arranging their thoughts..."
    dreamRem "Sounds like someone I know."
    dreamRem "Don't think I didn't catch you this morning rearranging our already labeled pastry display!"
    dreamSom "Aww, but it looks better when it's arranged by jam color!"
    dreamRem "*Sigh* Anyways, we need to find our client. Where are they?"
    $ interactions.unlock([t_marcella_start])
    show expression t_marcella_start.image with Dissolve(0.8)
    ml "Oh no, I'm late. I'm late! I have to hurry!"
    ml "This assignment is due... and I have to fill out the report for... oh, I need to pick up the..."
    dreamSom "My, there they are, practically up to their nose in paperwork!"
    dreamRem "The client can't see us in their dream, but let's tail them."
    jump dream_start


label marcella_talk_start:
    ml "...And there's the kids' practice... I need to arrange the bouquet... class has been cancelled but..."
    $ interactions.complete([t_marcella_start]) 
    hide expression t_marcella_start.image with Dissolve(0.8)
    $ interactions.unlock([t_bunnysquad])
    show expression t_bunnysquad.image with Dissolve(0.8)
    dreamRem "Darn, they're too fast...!"
    dreamRem "What's with these bunnies?!"
    dreamSom "Ooh, they are so cute!!"
    dreamRem "Now what? We can't start cooking, much less start collecting ingredients in this condition."
    dreamSom "How about we take a look around? Maybe we can learn something from these adorable dream whip cream fluffles~"
    jump dream_start

label bunnies_talk_som:
    dreamSom "Hi there cuties! Would you mind letting us pass? We have an important mission and need to speak with our client up ahead."
    "Mission? {ss}Mission…!{/ss} Do you know big sis Marchie? {ss}So cool!{/ss}" 
    dreamSom "We sure do! Your older sister asked us for help, and I'll need your assistance in order to help them."
    "Marchie's the greatest! {ss}They do so much!{/ss} They're the hardest worker ever!"
    "We're gonna work hard too! {ss}Let's support big sis!{/ss}"
    $ interactions.complete([t_bunnysquad])
    hide expression t_bunnysquad.image with Dissolve(0.8)
   # [Get ingredient: bunny-cut apples]
    "As the bunnies left, a bundle of clouds manifested itself along the path of the two intrepid dream eaters. A shape that came out to be..."
    # [Dream apple close up shot?]
    "...A selection of apple slices, daintily cut in the shape of bunnies."
    $ inventory.add(c_bunnyapples)
    dreamRem "Our first ingredient is freshly cut apples?"
    dreamSom "Oooh, I wonder if we get to bake a pie with this!"
    dreamRem "We'll just have to see what we got to work with as we find other ingredients."
    dreamSom "I'll pocket this sweet snack for now, thank you very much~"
    $ interactions.unlock([t_strawberry, t_marcella_mid])
    $ unlocked_pages += 1
    jump dream_start

label bunnies_talk_rem:
    dreamRem "Hey… Can you move aside?"
    "...Move? Why? {ss}Who are you?{/ss}"
    dreamRem "It's… not important. But you guys are in the way."
    "...We don't wanna. {ss}Say no to strangers!{/ss}"
    dreamRem "(...This is why I'm no good with talking to kids.)"
    dreamSom "Aww cheer up, Remi. How about I give it a go?"
    jump dream_start

label strawberry_look:
    dreamRem "The moon looks awfully peculiar… Is that a strawberry?!"
    dreamSom "Could it be? An ingredient? Let's extract it!"
    "RRRemerie watched as dreamSom reached out her hand and carefully plucked the strawberry out of the night sky."
    # [Get Creamy Strawberry!]
    $ inventory.add(c_strawberry)
    $ interactions.complete([t_strawberry])
    jump dream_start

label marcella_talk_mid1:
    ml "And I have to find my report… and buy the medicine for little Whitney... Oooh and this whole place has been a mess!"
    dreamRem "Marcella sure has a lot on their plate."
    dreamSom "Then perhaps we can help them out!"
    dreamSom "Let's see… they're looking for their report… trying to give medicine to their little sister… Oh! And they want to clean up this entire area!"
    dreamRem "That last task sounds like a bit of a handful…"
    dreamSom "Oh come on Remi, it'll be fun! After all ~♪, spoonful of sugar-"
    dreamRem "...Helps the medicine go down, I know. It's your favorite song. Let's just get to work."
    $ interactions.unlock([t_debris, t_medicine, t_bunny1, t_bunny2, t_bunny3, t_bunny4, t_bunny5])
    $ interactions.update(t_marcella_mid.enable("marcella_talk_mid2"))
    $ interactions.update(t_marcella_mid.disable("marcella_talk_mid1"))
    jump dream_start

label marcella_talk_mid2:
    ml "And I have to do this… and don't forget that… Oh and I need to…"
    dreamRem "Looks like Marcella's frozen in their thoughts."
    dreamSom "Let's see… they're looking for their report… trying to give medicine to their little sister… Oh! And they want to clean up this entire area!"
    dreamRem "Hah... Let's get to work."
    jump dream_start

label pile_inspect:
    if t_debris.state == 0:
        jump march_continue
    elif t_debris.viewed and t_debris >= 0:
        dreamSom "Let's see if we can get Marchie's little siblings to help us out."
    else:
        dreamRem "Urk… The client's going to be awake by the time we clean through this mess."
        dreamSom "How about we ask Marchie's little siblings to help out?"
        dreamRem "Well, it's definitely worth a shot."
        dreamRem "Hang on, there's a blue book in the pile of random papers…"
        dreamSom "There's a name written inside- \"Maddie\"."
        dreamRem "Do you think that's one of the bunnies' names?"
        dreamSom "Cute! We should hang on to it, just in case."
        python:
            interactions.update(t_debris.view())
            interactions.update(t_bunny1.enable("bunny1_help"))
            interactions.update(t_bunny2.enable("bunny2_help"))
            interactions.update(t_bunny3.enable("bunny3_help"))
            interactions.update(t_bunny4.enable("bunny4_help"))
            interactions.update(t_bunny5.enable("bunny5_help"))
            inventory.add(c_bluebook)
            interactions.update(t_debris.updateState(4)) # you got 4 bunnies to ask for help
    jump dream_start

label medicine_find:
    dreamSom "This looks to be the medicine we have to give to Marcella's sister. The label says \"Drink Me\"."
    dreamRem "The question is… which of their siblings need a dose?"
    dreamSom "I guess we'll just have to go around and ask!"
    dreamRem "I'll… let you do the talking."
    python:
        inventory.add(c_medicine)
        interactions.complete([t_medicine])
        interactions.update(t_bunny1.enable("bunny1_give"))
        interactions.update(t_bunny2.enable("bunny2_give"))
        interactions.update(t_bunny3.enable("bunny3_give"))
        interactions.update(t_bunny4.enable("bunny4_give"))
        interactions.update(t_bunny5.enable("bunny5_give"))
    jump dream_start

label report_find:
    dreamSom "Could this be the report Marcella was looking for?"
    dreamRem "I don't think this looks to be a report as much as it is a… planner?"
    dreamSom "Wow, look at this calendar, it's been filled to the brim with events!"
    dreamRem "How could you tell? All the pages are a complete mess!"
    dreamRem "I can't even read the handwriting!"
    dreamRem "I guess even in a dream, our client doesn't feel very organized with their life."
    dreamSom "Let's return the planner to Marcella after we finish the other tasks."
    $ inventory.add(c_redbook)
    $ inventory.drop(c_bluebook)
    jump dream_start

# Quiet Bunny
label bunny1_talk:
    if not t_bunny1.state:
        dreamRem "Hey."
        "..."
        dreamRem "..."
        dreamRem "Can they not hear me?"
        dreamSom "They look like they're occupied in trying to find something…"
        "I can't find my favorite book…"
        dreamRem "A blue book, huh."
        if c_bluebook in inventory.items:
            dreamRem "Well, we found this book in the pile of papers over there earlier. Are you Maddie?"
            "Oh! Oh yes!"
            "Yay! You saved the day!"
            dreamRem "... I did huh..."
            dreamSom "Aww Remi you look so happy! How sweet~"
            dreamRem "D-don't look at me right now."
            "I had mistakened my book for another. Here you can have the other one!"
            $ interactions.update(t_bunny1.updateState(True))
            jump report_find
    else:
        "Thank you again for the book!"
        "Whitney has to go to bed early tonight- she needs to get her rest." 
        "She would have been so sad if I couldn't read her favorite stories before bed…"
    jump dream_start
label bunny1_give:
    "My name is Maddie, not Whitney! Even though I'm smaller than her, I'm older!"
    jump dream_start
label bunny1_help:
    dreamSom "Hey there, auntie Som needs some help with cleaning, would you mind helping?"
    if not t_bunny1.state:
        "..."
        dreamSom "..."
        "I can't find my favorite book…" 
        "It's blue and has my name on the inside…"
        dreamSom "Hm... A blue book you say..."
        if c_bluebook in inventory.items:
            dreamSom "Maddie, is this what you're looking for?"
            "Oh! Oh yes!"
            "Yay! You saved the day!"
            dreamRem "Could've just asked for our help instead of ignoring me."
            dreamSom "Oh, Remi don't be so grumpy!"
            dreamRem "I-I'm not..."
            "I had mistakened my book for another. Here you can have the other one!"
            $ interactions.update(t_bunny1.updateState(True))
            jump report_find
    else:
        dreamRem "It looks like Maddie is too focused on her book now to answer."
        dreamSom "Oh I know that feeling!"
        dreamSom "Maybe we can try asking again later."
    jump dream_start
label bunny1_chat:
    "Whitney has to go to bed early tonight- she needs to get her rest." 
    "She would have been so sad if I couldn't read her favorite stories before bed…"
    jump dream_start
label bunny1_time:
    "It's 9 o' clock! I just finished reading Whitney her favorite bedtime stories."
    jump dream_start

# Energetic Bunny (the sick one)
label bunny2_talk:
    "Wheee! Wheeeee!"
    dreamSom "That little one is going to get hurt, jumping around like that…!"
    dreamRem "I'm sure she knows what she's doing."
    "Whee- OUCH!"
    dreamRem "OW! Watch it!"
    dreamSom "Oh, sweetie, slow down and please be careful!"
    "I'm fine! Hehe, wheee!"
    dreamRem "Kids, theses days..."
    dreamSom "Now now~"
    jump dream_start
label bunny2_give:
    dreamSom "Little Whitney? I heard someone's not feeling good and needs to take her medicine."
    "What? I'm fine! Look how fast I can run!"
    dreamRem "The only running I see is your high fever."
    "No…! NO! I don't want to take my medicine!"
    dreamSom "Now now… You have to be strong so you can be healthy and play outside."
    dreamSom "Open up~"
    "It… It doesn't taste all that bad."
    dreamSom "See? What a good girl! I hope you feel better soon."
    "Thanks, lady!"
    dreamRem "...Let me guess, you added some sugar."
    dreamSom "Hmmm hm~ ♫"
    python:
        interactions.update(t_bunny1.disable("bunny1_give"))
        interactions.update(t_bunny2.disable("bunny2_give"))
        interactions.update(t_bunny3.disable("bunny3_give"))
        interactions.update(t_bunny4.disable("bunny4_give"))
        interactions.update(t_bunny5.disable("bunny5_give"))
        interactions.update(t_bunny2.updateState(True))
    jump dream_start
label bunny2_help:
    if not t_bunny2.state:
        "Wheee! Wheee!"
        dreamSom "It seems a bit difficult to catch this little one's attention right now."
    else:
        dreamSom "We can't ask Little Whitney to help! The thing she needs right now is some proper rest!"
        "E-excuse me...!"
        dreamRem "Hm? Oh it's the bunny that wanted the blue book."
        dreamSom "Hi there, Maddie. What's wrong?"
        "Since little Whitney is sick, I can help clean up instead!"
        "I just finished my book, I'll be right over!"
        dreamSom "My, how responsible! Thank you, darling~"
        # momentary fade effect
        python:
            interactions.update(t_bunny1.disable("bunny1_help"))
            interactions.update(t_bunny2.disable("bunny2_help"))
            interactions.update(t_debris.updateState(t_debris.state - 1))
    jump dream_start
label bunny2_chat:
    "zzz..."
    jump dream_start
label bunny2_time:
    "zzz..."
    dreamSom "Aww... She's fast asleep now."
    dreamRem "(How do you fall sleep inside a dream?)"
    jump dream_start

# Peevish Bunny
label bunny3_talk:
    "Our little sis hasn't been feeling well lately, but she's weak to the taste of medicine so she tries to lie her way out of it. How spoiled!"
    jump dream_start
label bunny3_give:
    "Medicine? Me? I'm not the sick one! Give it to Little Whitney!"
    jump dream_start
label bunny3_help:
    dreamSom "Hello, could you help us move some of that big pile of papers for your dear big sis Marchie?"
    "Hmph… If it helps big sis Marchie out…"
    python:
        interactions.update(t_bunny3.disable("bunny3_help"))
        interactions.update(t_debris.updateState(t_debris.state - 1))
    jump dream_start
label bunny3_chat:
    "what's up"
    jump dream_start
label bunny3_time:
    "What time is it? Well, it's obviously 9 o' clock!"
    jump dream_start

# Studious Bunny
label bunny4_talk:
    "Our parents are really busy so Marchie took up the job to take care of all of us in their stead. I'm the second oldest but recently I've been away for school."
    "I hope Marchie is doing alright…"
    jump dream_start
label bunny4_give:
    "Oh are you looking for Little Whitney? She's an outgoing kid so you'd probably find her somewhere more open."
    jump dream_start
label bunny4_help:
    "Why yes, I'd love to help if that would be okay!"
    python:
        interactions.update(t_bunny4.disable("bunny4_help"))
        interactions.update(t_debris.updateState(t_debris.state - 1))
    jump dream_start
label bunny4_chat:
    "what's up"
    jump dream_start
label bunny4_time:
    "It's 9 o'clock, my younger siblings should be going to bed around now."
    jump dream_start

# Clumsy Bunny
label bunny5_talk:
    "aaaa flavor text"
    jump dream_start
label bunny5_give:
    "C-cherry medicine…?! Oh no thank you, I'm glad I'm not the sick one this time."
    jump dream_start
label bunny5_help1:
    if t_bunny5.state == -1:
        "Oh before that, can I ask for a favor as well?"
        dreamSom "Sure sweetie, what is it?"
        "You see, I wanted to give big sis Marchie a gift for all that she's done for us."
        "Big sis Marchie's favorite color is red! But all the flowers here are white…!"
        "I brought some paint earlier, could you help me color 7 flowers?"
        dreamSom "What a lovely idea! We'll be sure to do that."
        dreamRem "Painting… the flowers?"
        dreamRem "Well I guess it's the thought that counts."
        $ interactions.unlock([t_flower1, t_flower2, t_flower3, t_flower4, t_flower5, t_flower6, t_flower7])
        $ interactions.update(t_bunny5.updateState(7))
    if t_bunny5.state == 0:
        "yay! ok I'll help"
        $ interactions.update(t_bunny5.disable("bunny5_help"))
        $ interactions.update(t_debris.updateState(t_debris.state - 1))
    if t_bunny5.state > 0:
        "There still [t_bunny5.state] of flowers left to be painted."
    jump dream_start
label bunny5_chat:
    "what's up"
    jump dream_start
label bunny5_time:
    "What time is it? Um… the longer needle is the minute hand so it's… 9 o' clock!"
    jump dream_start

# magic to flower paint is that the bg will have red flowers and we'll remove the interaction when they're painted
label flower1_paint:
    $ interactions.complete([t_flower1])
    $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
    hide expression flower1.image with Dissolve(0.8)
    jump dream_start
label flower2_paint:
    $ interactions.complete([t_flower2])
    $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
    hide expression flower2.image with Dissolve(0.8)
    jump dream_start
label flower3_paint:
    $ interactions.complete([t_flower3])
    $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
    hide expression flower3.image with Dissolve(0.8)
    jump dream_start
label flower4_paint:
    $ interactions.complete([t_flower4])
    $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
    hide expression flower4.image with Dissolve(0.8)
    jump dream_start
label flower5_paint:
    $ interactions.complete([t_flower5])
    $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
    hide expression flower5.image with Dissolve(0.8)
    jump dream_start
label flower6_paint:
    $ interactions.complete([t_flower6])
    $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
    hide expression flower6.image with Dissolve(0.8)
    jump dream_start
label flower7_paint:
    $ interactions.complete([t_flower7])
    $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
    hide expression flower7.image with Dissolve(0.8)
    jump dream_start

label march_continue:
    dreamSom "We did it…! The place looks so much nicer now."
    dreamRem "How is Marcella feeling?"
    ml "Urgh and I still have to remember to go there… and pick up that… and call the…"
    dreamRem "There's {b}more{/b} tasks to do?!"
    dreamSom "Remi, look!"
    "To the dismay of the investigative duo, the oppressive atmosphere of debris returned."
    "Undoing all the progress made, the two dream eaters paused to gather their bearings as they became overwhelmed, once more, in the clutter."
    dreamRem "All our hard work…!"
    dreamRem "What could we be doing wrong?"
    dreamSom "Even in the planner, the pages are just getting filled up with more and more scribbles."
    dreamSom "Maybe it's not the tasks themselves that are the problem…"
    dreamRem "What- So they don't want our help?"
    ml "Help…? Why would I need help? These are my responsibilities!"
    $ interactions.complete([t_marcella_mid])
    hide expression t_marcella_mid.image with Dissolve(0.8)
    dreamRem "Ack! There they go again…!"
    dreamSom "Let's go Remi, we mustn't leave them!"
    $ interactions.unlock([t_marcella_end])
    $ unlocked_pages = 2

label marcella_talk_end1:
    if not t_marcella_end.viewed:
        ml "I-- I can't keep up with this anymore…"
        ml "My list keeps growing and growing… but the little ones! They're all depending on me!"
        "Big sis! Big sis! We're hungry…! {ss}Hungry!{/ss}"
        dreamRem "The bunnies here… They're not acting like the ones from earlier..."
        # [Bunnies that are surrounding Marchie]
        "Big sis… Do you know where my shirt is? {ss}It has to be my favorite shirt!{/ss}"
        ml "The kids are growing up… and that means their needs are growing too…"
        ml "I can't let them down but there simply isn't enough time in the world to get all these things done!"
        ml "I can't afford to fall asleep, there's too work much to be done!"
        "Big sis, can we go to the park? {ss}No, I want to go to the movies!{/ss}"
        ml "Resting now means I'll be wasting my time!"
        "Big sis Marchie is the oldest, so they can do everything!"
        ml "I HAVE to keep going!!!"
        # [# Client collapses in dream?!]
        dreamSom "Oh dearie. So an issue with cleaning wasn't the problem after all."
        dreamRem "Yes, it seems much deeper than that."
        dreamRem "The root of the issue lies in the sibling bunnies."
        dreamSom "Remerie, how could you! Don't you dare blame these sweet children!"
        dreamRem "I'm not {i}blaming them{/i}, I'm just thinking out loud!"
        dreamRem "We have to consider why the bunnies are in the client's worried dreams to begin with."
        dreamRem "Marchie obviously cares a lot about their siblings, but their perception here is different from our previous interactions."
        dreamRem "Our client has been so focused on meeting everyone's demands that they haven't had the time to sleep."
        dreamRem "Time…!"
        dreamRem "Somnia, the clocks! Let's go check on all the clocks!"
        dreamSom "You're right, there certainly were a lot of clocks in this dream."
        python:
            interactions.unlock([t_clockface1, t_clockface2, t_clockface3, t_clockface4])
            interactions.update(t_marcella_end.view())
    else:
        "Marcella seems to be unconscious as of the moment."
    jump dream_start

# Clock under the column on the first page
label clock1_inspect:
    "A large clock something something flavor text after seeing the clock drawn"
    "The hour hand is facing {b}[t_clockface1.state]{/b}, while the minute hand is stuck to the {b}down{/b}."
    if not t_clockface1.viewed:
        python:
            interactions.update(t_clockface1.view())
            interactions.update(t_clockface1.enable("clock1_up"))
            interactions.update(t_clockface1.enable("clock1_down"))
            interactions.update(t_clockface1.enable("clock1_left"))
            interactions.update(t_clockface1.enable("clock1_right"))
    jump dream_start
label clock1_up:
    "The hour hand has been moved to face {b}upwards{/b}, while the minute hand is stuck facing {b}down{/b}."
    $ interactions.update(t_clockface1.updateState("up"))
    jump check_clocks
label clock1_down:
    "The hour hand has been moved to face {b}downwards{/b}, while the minute hand is stuck facing {b}down{/b}."
    $ interactions.update(t_clockface1.updateState("down"))
    jump check_clocks
label clock1_left:
    "The hour hand has been moved to face {b}left{/b}, while the minute hand is stuck facing {b}down{/b}."
    $ interactions.update(t_clockface1.updateState("left"))
    jump check_clocks
label clock1_right:
    "The hour hand has been moved to face {b}right{/b}, while the minute hand is stuck also facing {b}down{/b}."
    $ interactions.update(t_clockface1.updateState("right"))
    jump check_clocks

# giant clock on second page
label clock2_inspect:
    "A large clock something something flavor text after seeing the clock drawn"
    "The hour hand is facing {b}[t_clockface2.state]{/b}, while the minute hand is stuck to the {b}up{/b}."
    if not t_clockface2.viewed:
        python:
            interactions.update(t_clockface2.view())
            interactions.update(t_clockface2.enable("clock2_up"))
            interactions.update(t_clockface2.enable("clock2_down"))
            interactions.update(t_clockface2.enable("clock2_left"))
            interactions.update(t_clockface2.enable("clock2_right"))
    jump dream_start
label clock2_up:
    "The hour hand has been moved to face {b}upwards{/b}, while the minute hand is stuck facing {b}up{/b}."
    $ interactions.update(t_clockface2.updateState("up"))
    jump check_clocks
label clock2_down:
    "The hour hand has been moved to face {b}downwards{/b}, while the minute hand is stuck facing {b}up{/b}."
    $ interactions.update(t_clockface2.updateState("down"))
    jump check_clocks
label clock2_left:
    "The hour hand has been moved to face {b}left{/b}, while the minute hand is stuck facing {b}up{/b}."
    $ interactions.update(t_clockface2.updateState("left"))
    jump check_clocks
label clock2_right:
    "The hour hand has been moved to face {b}right{/b}, while the minute hand is stuck also facing {b}up{/b}."
    $ interactions.update(t_clockface2.updateState("right"))
    jump check_clocks

# first clock on last page
label clock3_inspect:
    if not t_clockface3.viewed:
        dreamRem "The position of this clock is different from the other one in the room."
        dreamSom "The numbers and ticks seems to be missing, I wonder how we can tell the time?"
        dreamRem "Hm… the minute hand's not moving… I think it's stuck. Oh! But it looks like I can move the hour hand."
        dreamRem "Nothing seems to happen when I do, though."
        dreamSom "Let's check the other clocks too."
        python:
            interactions.update(t_clockface3.view())
            interactions.update(t_clockface3.enable("clock3_up"))
            interactions.update(t_clockface3.enable("clock3_down"))
            interactions.update(t_clockface3.enable("clock3_left"))
            interactions.update(t_clockface3.enable("clock3_right"))
    else:
        "A large clock something something flavor text after seeing the clock drawn"
        "The hour hand is facing {b}[t_clockface3.state]{/b}, while the minute hand is stuck to the {b}right{/b}."
    jump dream_start
label clock3_up:
    "The hour hand has been moved to face {b}upwards{/b}, while the minute hand is stuck facing {b}right{/b}."
    $ interactions.update(t_clockface3.updateState("up"))
    jump check_clocks
label clock3_down:
    "The hour hand has been moved to face {b}downwards{/b}, while the minute hand is stuck facing {b}right{/b}."
    $ interactions.update(t_clockface3.updateState("down"))
    jump check_clocks
label clock3_left:
    "The hour hand has been moved to face {b}left{/b}, while the minute hand is stuck facing {b}right{/b}."
    $ interactions.update(t_clockface3.updateState("left"))
    jump check_clocks
label clock3_right:
    "The hour hand has been moved to face {b}right{/b}, while the minute hand is stuck also facing {b}right{/b}."
    $ interactions.update(t_clockface3.updateState("right"))
    jump check_clocks

# second clock on last page
label clock4_inspect:
    if !clockface4.viewed:
        dreamRem "There's also no numbers on this clock. And the minute hand is stuck."
        dreamSom "Maybe we need to get all the clock's time to match up..."
        dreamRem "How can we do that if we can't move the minute hand?"
        dreamSom "We'll figure it out, Remi! There has to be a way!"
        python:
            interactions.update(t_clockface4.view())
            interactions.update(t_clockface4.enable("clock4_up"))
            interactions.update(t_clockface4.enable("clock4_down"))
            interactions.update(t_clockface4.enable("clock4_left"))
            interactions.update(t_clockface4.enable("clock4_right"))
    else:
        "A large clock something something flavor text after seeing the clock drawn"
        "The hour hand is facing {b}[t_clockface4.state]{/b}, while the minute hand is stuck to the {b}left{/b}."
    jump dream_start
label clock4_up:
    "The hour hand has been moved to face {b}upwards{/b}, while the minute hand is stuck facing {b}left{/b}."
    $ interactions.update(t_clockface4.updateState("up"))
    jump check_clocks
label clock4_down:
    "The hour hand has been moved to face {b}downwards{/b}, while the minute hand is stuck facing {b}left{/b}."
    $ interactions.update(t_clockface4.updateState("down"))
    jump check_clocks
label clock4_left:
    "The hour hand has been moved to face {b}left{/b}, while the minute hand is stuck facing {b}left{/b}."
    $ interactions.update(t_clockface4.updateState("left"))
    jump check_clocks
label clock4_right:
    "The hour hand has been moved to face {b}right{/b}, while the minute hand is stuck also facing {b}left{/b}."
    $ interactions.update(t_clockface4.updateState("right"))
    jump check_clocks

label check_clocks:
    if t_clockface1.state == "right" and t_clockface2.state == "left" and t_clockface3.state == "up" and t_clockface4.state == "down":
        # clocktower ring sfx
        "As the final clock struck nine, the sound of gears whirring filled the air."
        "The various clock faces occupying the dream space seemed to react at once, winding their hands with incredible speed."
        "Finally settling at one time, the clock hands began to move in sync, once more. The gentle click of each second echoing through the air was harmonious."
        dreamSom "Remi, take a look! All the clocks are moving again."
        dreamRem "That's a relief. My hunch was right after all."
        dreamRem "So Marcella had a warped perception of time, which fueled their pressure to keep working at the cost of their sleep."
        dreamSom "Time flies when you're having fun~"
        dreamRem "I wouldn't describe our client's experience as \"fun\"."
        dreamSom "Well, it sounds like dear Marchie needs a good break...fast."
        dreamRem "\"Hah Hah\", but you're right. And I have just the recipe we need to cook for this dream."
        dreamSom "Ooh, I'm so excited! Then let's go to the Wishing Kitchen."
        python:
            inventory.add(c_clockegg)
            finished = True
            interactions.complete([t_clockface1, t_clockface2, t_clockface3, t_clockface4]) 
    jump dream_start

