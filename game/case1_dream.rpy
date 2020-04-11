label case1_dream:
    show screen focus_dialogue
    $ bun_name = "Dream bunnies"
    $ _skipping = False # disable skipping option

    python:
        bg = "images/BG/bg_wonderland.png" # background image
        page_width = 1720 # screen page width
        total_pages = 3 # total pages in investigation
        inventory = Inventory() # initialize inventory
        interactions = Interactions( # starting interactions
            [t_somrem_start]
        )
        unlocked_pages = 0 # default is 0
        finished = False # default is false
        renpy.start_predict_screen("dream")
        renpy.start_predict(
            "images/BG/bg_wonderland.png",
            "images/interactables/case1/*.png",
            "side dreamSom *",
            "side dreamRem *",
            "gui/frame_*.png", # dream hover textboxes
            "gui/textbox_*.png" # dream talk textboxes
        )
    scene cloud
    show screen dream() with Dissolve(2.0)
    pause(1.0)
    play sound trip
    dreamSom sh "W-whoa...!" with sshake
    dreamRem ne "I got you. Watch your step, it's a mess in here."
    dreamRem ne "A dream would reflect a person's inner headspace, after all."
    dreamSom th "Our client must really have a hard time arranging their thoughts, among other things..."
    dreamRem si "Sounds like someone I know."
    dreamRem pe "Don't think I didn't catch you this morning rearranging our already labeled pastry display!"
    dreamSom gr "Aww, but it looks better when it's arranged by jam color!"
    dreamRem si "*sigh* Anyway, we need to find our client. Where are they?"
    $ interactions.unlock([t_marcella_start])
    # play appear sfx?
    pause(1.0)
    dreamMar "Oh no, I'm late. I'm late! I have to hurry!"
    dreamMar "This assignment is due... and I have to fill out the report for... Oh, I need to pick up the..."
    dreamSom sh "My, there's Marcella, practically up to their nose in paperwork!"
    dreamRem ne "The client can't see us in their dream, but let's tail them."
    play music dream1 fadein(0.4)
    jump dream_start
    hide screen focus_dialogue

label somrem_start_talk:
    if t_somrem_start.state == "start":
        dreamSom gr "This dream... My, it's like a wonderland!"
        dreamRem fl "Don't get lost now Soms. Here, take my hand."
    elif t_somrem_start.state == "postMar":
        dreamSom de "Oh~ I could just stare at those cutie bunnies all night~"
        dreamRem th "It's a shame, but the incense will only last so long before our client wakes up."
        dreamSom ex "Hey Remi, we should go to a petting zoo for our next date!"
        dreamRem gr "That sounds like a good idea, but first, let's focus our on job."
    elif t_somrem_start.state == "middle":
        dreamSom th "This busybee Marcella is quite a change from the Marcella we had found earlier lying on the sidewalk." #WORDING HELP
        dreamRem ne "They did mention that they haven't slept in several days. That can't possibly do anyone good."
        dreamRem th "What could be the reason for their lack of sleep?"
    elif t_somrem_start.state == "end":
        dreamRem th "TODO!!!"
    jump dream_start

label marcella_talk_start:
    dreamMar "... And there's the kids' practice... I need to arrange the bouquet... Class has been cancelled but..."
    $ interactions.complete([t_marcella_start])
    hide expression t_marcella_start.image with Dissolve(0.8)
    $ interactions.unlock([t_bunnysquad])
    dreamRem pe "Darn, they're too fast...!"
    dreamRem "And what's with these {ii}bunnies?!{/ii}"
    dreamSom gr "Oooh, they are so cute!"
    dreamRem si "Now what? We can't start cooking, much less collect any ingredients in this condition."
    dreamSom gr "Well maybe we can learn something from these adorable dream whip cream fluffles~..."
    $ interactions.update(t_somrem_start.updateState("postMar"))
    jump dream_start

label bunnies_talk_som:
    dreamSom de "Hello there, cuties! Would you mind letting us pass?"
    dreamSom de "We have an important mission and need to speak with our client up ahead."
    bun "Mission? {ss}Mission…!{/ss} Do you know big sib Marchie? {ss}So cool!{/ss}"
    dreamRem th "{ii}\"Marchie\"{/ii}? Could they be talking about Marcella?"
    dreamSom gr "We sure do! Your sibling asked us for help and we need to reach them. May I ask you dearies to kindly scoot over?"
    bun "Marchie's the greatest! {ss}They do so much!{/ss} They're the hardest worker ever!"
    bun "We're gonna work hard too! {ss}Let's support big sib!{/ss}"
    $ interactions.complete([t_bunnysquad])
    hide expression t_bunnysquad.image with Dissolve(0.8)
    dr "The bunnies scampered off, kicking up clouds along the two intrepid dream eaters's path in the shape of..."
    show screen get_ingredient("apple") with Dissolve(0.8)
    play sound itemget
    dr "... a selection of apple slices. Each slice's ruby skin was daintily cut to mimic the adorable silhouette of a bunny."
    hide screen get_ingredient
    dreamRem th "Our {ii}first ingredient{/ii} is freshly cut apples?"
    dreamSom gr "Oooh, I wonder if we get to bake a pie with this!"
    dreamRem ne "We'll see exactly what we can work with once we find more ingredients."
    dreamSom gr "I'll pocket this sweet snack for now, thank you very much~!"
    $ interactions.unlock([t_strawberry, t_clockface1, t_marcella_mid])
    $ inventory.add(c_bunnyapples)
    $ unlocked_pages += 1
    jump dream_start

label bunnies_talk_rem:
    dreamRem ne "Hey... Can you move aside?"
    bun "...Move? Why? {ss}Who are you?{/ss}"
    dreamRem pe "It's not important. You guys are in the way."
    bun "...We don't wanna. {ss}Say no to strangers!{/ss}"
    dreamRem pe "{th}(This is why I'm no good with talking to kids...){/th}"
    dreamSom gr "Aw~, cheer up, Remi. How about I give it a go?"
    jump dream_start

label strawberry_look:
    dreamRem th "Doesn't that moon look peculiar? Those weird spots and pinkish hue... Is it a strawberry?!"
    dreamSom ex "Could it be? An ingredient? Let's extract it!"
    dr "Squinting up against the moonlight, Somnia reached and placed her hand against the night sky, pinching the distant moon between her fingers."
    dr "Like a manipulation of perspective, or a magic trick, one pluck was all it took for Somnia to retrieve the strawberry."
    $ inventory.add(c_strawberry)
    $ interactions.complete([t_strawberry])
    show screen get_ingredient("strawberry") with Dissolve(0.8)
    play sound itemget
    dr "You got a {ii}Creamy Strawberry!{/ii}"
    hide screen get_ingredient
    jump dream_start

label clock1_talk:
    dreamRem sh "What an odd-looking clocktower...!"
    dreamSom sh "I wonder just how long it goes..."
    dreamSom th "Unfortunately, the bottom of the tower is obscured by the clouds."
    jump dream_start

label clock2_talk:
    dreamSom sh "Could this be... part of the same clocktower from earlier?"
    dreamRem ne "With all its curves and twists, it really is a sight to behold."
    jump dream_start

label marcella_talk_mid:
    if not t_marcella_mid.viewed:
        dreamMar "And I have to find my report... and buy the medicine for little Whitney... Ohhh, and this whole place is an absolute mess!"
        dreamRem sh "Marcella sure has a lot on their plate."
        dreamSom gr "Perhaps we can help them out!"
        dreamSom th "Let's see... They're looking for a {ii}report{/ii}, trying to get {ii}medicine{/ii} to one of the siblings..."
        dreamSom gr "Oh! And they want to {ii}clean up this entire area!{/ii}"
        dreamRem pe "That last task sounds like a bit of a handful..."
        dreamSom gr "Oh, come on Remi! It'll be fun!"
        dreamSom gr "After all~ A spoonful of sugar...{wmn}"
        dreamRem si "Helps the medicine go down, I know. It's your favorite song. Let's just get to work."
        $ interactions.unlock([t_debris, t_medicine, t_bunny1, t_bunny2, t_bunny3, t_bunny4, t_bunny5, t_clockface2])
        $ interactions.update(t_marcella_mid.view())
        $ interactions.update(t_somrem_start.updateState("middle"))
    else:
        dreamMar "And I have to do this... and don't forget that... Oh, and I need to..."
        dreamRem th "Looks like Marcella's frozen in their thoughts."
        if [c_herbs, c_redbook] in inventory.items: # if first two tasks are done
            dreamSom th "Well, we managed to finish all the tasks Marcella listed earlier."
            if t_debris.state == 0: # progress is all done, just need to check pile
                dreamSom de "Now what's left is to check on the pile their siblings helped us clean up!" #WORDING HELP...
            else:
                dreamSom ex "Now all that's left is to {ii}clean up this mess!{/ii}"
                dreamRem si "Let's see if we can get more of those little guys to help us out."
        else:
            dreamSom th "If I remembered correctly..."
            if c_herbs in inventory.items and c_redbook not in inventory.items: # medicine is done but report isn't
                dreamSom th "We were able to give Whitney her medicine, but we still need to help look for Marcella's missing {ii}report{/ii}."
            elif c_herbs not in inventory.items and c_redbook in inventory.items: # report found but no medicine
                dreamSom th "We found Marcella's missing report, but we still need to find little Whitney and give her the {ii}medicine.{/ii}"
            else:
                dreamSom th "They're looking for a {ii}report{/ii}, trying to get {ii}medicine{/ii} to one of the siblings..."
            dreamSom gr "And don't forget, we need to find a way to {ii}clean up this entire area!{/ii}"
            dreamRem si "Hahhh... Let's get to work."
    jump dream_start

label pile_inspect:
    if t_debris.state == 0:
        jump march_continue
    elif t_debris.viewed and t_debris >= 2:
        dreamSom "Let's see if we can get Marcella's little siblings to help us out."
    elif t_debris.viewed and t_debris >= 0:
        dreamRem sh "I can't believe it. I think I see the floor to this place!"
        dreamSom gr "The bunny siblings have been absolute sweethearts in helping us. Let's see if we can get the rest of them to pitch in~"
    else:
        dreamRem pe "Urk... The client's going to be awake by the time we clean through this mess."
        dreamSom th "How about we ask these bunnies... Marcella's little siblings, to help out?"
        dreamRem th "Well, it's definitely worth a shot."
        dreamRem sh "Hang on, there's a book in the pile of papers."
        dreamSom sh "There's a name written inside- {ii}Maddie.{/ii}"
        dreamRem th "Do you think that's one of the bunnies' names?"
        dreamSom gr "How cute! We should hang on to it, just in case."
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
    dreamSom sh "This must be the medicine we have to give to Marcella's sister! The label says {ii}\"Drink Me\".{/ii}"
    show screen get_ingredient("ooze") with Dissolve(0.8)
    play sound itemget
    dr "You got the {ii}Cherry Medicine!{/ii}"
    hide screen get_ingredient
    dreamRem th "The question is just which of these siblings need a dose."
    dreamSom gr "I guess we'll just have to go around and ask!"
    dreamRem pe "... I'll let you do the talking."
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
    dreamSom sh "Could this be the report Marcella was looking for?"
    dreamRem sh "I don't think this looks to be a report as much as it is a... planner?"
    dreamSom bi "Gosh, just look at this calendar. It's been filled to the brim with events!"
    dreamRem "You can tell those are supposed to be events? All the pages are a complete mess!"
    dreamRem "I can't even read the handwriting!"
    dreamRem th "I guess even in a dream, our client doesn't feel very organized with their life."
    dreamSom ne "Let's return the planner to Marcella after we finish the other tasks."
    dreamSom sh "Hm?"
    dreamSom "Something fell out of the pages..."
    dreamRem th "Looks like a family photo..."
    dreamRem "Marcella smiling while surrounded by their five younger siblings."
    dreamSom gr "Isn't that just the sweetest thing!"
    show screen get_ingredient("herbs") with Dissolve(0.8)
    play sound itemget
    dr "You got some {ii}Fine Herbs!{/ii}"
    hide screen get_ingredient
    $ inventory.add(c_redbook)
    $ inventory.drop(c_bluebook)
    jump dream_start

# Quiet Bunny
label bunny1_talk:
    $ bun_name = "Quiet Bunny"
    if not t_bunny1.state:
        dreamRem ne "Hey."
        bun "..."
        dreamRem si "..."
        dreamRem pe "Can they not hear me?"
        dreamSom sh "They look like they're occupied in trying to find something..."
        bun "I can't find my favorite book..."
        dreamRem th "A blue book, huh."
        if c_bluebook in inventory.items:
            dreamRem th "Well, we found this book in that pile of papers over there earlier. Are you Maddie?"
            bun "Oh! Oh, yes!"
            $ bun_name = "Maddie"
            bun "Yay! You saved the day!"
            dreamRem gr "... I did, huh..."
            dreamSom de "Aw, Remi you look so happy! How sweet~!"
            dreamRem fl "L-let's just focus on the task at hand, alright?"
            bun "I mixed up my book for another one. Here, you can have it!"
            $ interactions.update(t_bunny1.updateState(True))
            jump report_find
    else:
        $ bun_name = "Maddie"
        bun "Thank you again for the book!"
        bun "Whitney has to go to bed early tonight since she needs to get her rest."
        bun "She would have been so sad if I couldn't read her favorite stories before bed..."
    jump dream_start
label bunny1_give:
    $ bun_name = "Maddie"
    bun "My name is Maddie, not Whitney! Even though I'm smaller than her, I'm older!"
    jump dream_start
label bunny1_help:
    dreamSom ne "Hello, there! Auntie Som needs some help with cleaning, would you mind helping?"
    if not t_bunny1.state:
        dreamRem ne "Hey."
        bun "..."
        dreamRem si "..."
        dreamRem pe "Can they not hear me?"
        dreamSom sh "They look like they're occupied in trying to find something..."
        bun "I can't find my favorite book..."
        bun "It's blue and has my name on the inside."
        dreamSom "Hm... A blue book, you say..."
        if c_bluebook in inventory.items:
            dreamSom ne "Maddie, is this what you're looking for?"
            bun "Oh! Oh, yes!"
            bun "Yay! You saved the day!"
            dreamRem pe "Could've just asked for our help instead of ignoring me."
            dreamSom gr "Oh, Remi, no need to be such a grumpster!"
            dreamRem fl "I-I'm not..."
            bun "I mixed up my book for another one. Here, you can have it!"
            $ interactions.update(t_bunny1.updateState(True))
            jump report_find
    else:
        dreamRem sh "It looks like Maddie is too focused on her book now to answer."
        dreamSom gr "Oh, I know that feeling!"
        dreamSom th "Maybe we can try asking again later."
    jump dream_start
label bunny1_chat:
    bun "Thanks again for the book!"
    bun "Now I get to share my favorite bedtime stories with Whitney."
    jump dream_start
label bunny1_time:
    bun "It's 9 o' clock! I just finished reading Whitney her favorite bedtime stories."
    jump dream_start

# Energetic Bunny (the sick one)
label bunny2_talk:
    $ bun_name = "Energetic Bunny"
    if not t_bunny2.state:
        bun "Wheee! Wheeeee!"
        dreamSom bi "That little one is going to get hurt, jumping around like that...!"
        dreamRem si "I'm sure she knows what she's doing."
        bun "Whee- OUCH!" with sshake
        dreamRem pe "OW! Watch it!" with sshake
        dreamSom sh "Oh, sweetie, slow down and please be careful!"
        bun "I'm fine! Hehe, wheee!"
        dreamRem "Kids theses days..."
        dreamSom gr "Now, now~"
    else:
        bun "*Yaaaawn*"
        bun "I feel kinda sleepy now after the medicine..."
    jump dream_start
label bunny2_give:
    $ bun_name = "Little Whitney"
    dreamSom ne "Little Whitney? I heard someone's not feeling good and needs to take her medicine."
    bun "What? I'm fine! Look how fast I can run!"
    dreamRem si "The only running I see is your high fever."
    bun "No...! NO! I don't want to take my medicine!"
    dreamSom "Now, now... You have to be strong so you can be healthy and play outside."
    dreamSom gr "Open up~!"
    bun "It... It doesn't taste all that bad."
    dreamSom de "See? That's a good girl! I hope you feel better soon."
    bun "Thanks, lady!"
    dreamRem gr "... Let me guess, you added some sugar."
    dreamSom de "Hmmm hm~ {wmn}"
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
        $ bun_name = "Energetic Bunny"
        bun "Wheee! Wheee!"
        dreamSom th "It seems a bit difficult to catch this little one's attention right now."
    else:
        dreamSom sh "We can't ask little Whitney to help! The thing she needs right now is some proper rest!"
        $ bun_name = "Maddie"
        bun "E-excuse me...!"
        dreamRem sh "Hm? Oh, it's the bunny that wanted the blue book."
        dreamSom gr "Hi there, Maddie. What's wrong?"
        bun "Since little Whitney is sick, I can help clean up instead!"
        bun "I just finished my book, I'll be right over!"
        dreamSom de "My, how responsible! Thank you, darling~!"
        show black with Dissolve(0.8)
        pause(1.0)
        hide black with Dissolve(0.8)
        python:
            interactions.update(t_bunny1.disable("bunny1_help"))
            interactions.update(t_bunny2.disable("bunny2_help"))
            interactions.update(t_debris.updateState(t_debris.state - 1))
            interactions.update(t_debris.updateImage("/images/interactables/case1/debris{}.png".format(t_debris.state)))
    jump dream_start
label bunny2_chat:
    $ bun_name = "Little Whitney"
    bun "Zzz..."
    jump dream_start
label bunny2_time:
    $ bun_name = "Little Whitney"
    bun "Zzz..."
    dreamSom de "Aww... She's fast asleep now."
    dreamRem th "{th}(How do you fall asleep inside a dream?){/th}"
    jump dream_start

# Peevish Bunny
label bunny3_talk:
    $ bun_name = "Peevish Bunny"
    bun "Our younger sis hasn't been feeling well lately, but she's weak to the taste of medicine so she tries to lie her way out of it."
    bun "How spoiled!"
    jump dream_start
label bunny3_give:
    $ bun_name = "Peevish Bunny"
    bun "Medicine? Me? I'm not the sick one! Give it to Little Whitney!"
    jump dream_start
label bunny3_help:
    $ bun_name = "Peevish Bunny"
    dreamSom "Hello, could you help us move some of that big pile of papers for your dear big sib Marchie?"
    bun "Hmph... I guess if it's to help out big sib Marchie then..."
    python:
        interactions.update(t_bunny3.disable("bunny3_help"))
        interactions.update(t_debris.updateState(t_debris.state - 1))
        interactions.update(t_debris.updateImage("/images/interactables/case1/debris{}.png".format(t_debris.state)))
    # play debris cleaning sfx
    show expression t_debris.image with Dissolve(0.8)
    jump dream_start
label bunny3_chat:
    $ bun_name = "Peevish Bunny"
    bun "What's up."
    jump dream_start
label bunny3_time:
    $ bun_name = "Peevish Bunny"
    bun "What time is it? Well, it's obviously 9 o' clock!"
    jump dream_start

# Studious Bunny
label bunny4_talk:
    $ bun_name = "Studious Bunny"
    bun "Our parents are really busy so Marchie's been taking care of us in their stead. I'm the second oldest, but recently I've been away for school."
    bun "I hope Marchie is doing alright..."
    jump dream_start
label bunny4_give:
    $ bun_name = "Studious Bunny"
    bun "Oh, are you looking for Little Whitney? She's an outgoing kid so you'd probably find her somewhere more open."
    jump dream_start
label bunny4_help:
    $ bun_name = "Studious Bunny"
    dreamSom gr "Hello there! Would you mind helping us clean up these papers for your big sib Marchie?"
    bun "Why yes, I'd love to help!"
    bun "Marchie already has a lot on their plate, so this is the least I could do!"
    python:
        interactions.update(t_bunny4.disable("bunny4_help"))
        interactions.update(t_debris.updateState(t_debris.state - 1))
        interactions.update(t_debris.updateImage("/images/interactables/case1/debris{}.png".format(t_debris.state)))
    # play debris cleaning sfx
    show expression t_debris.image with Dissolve(0.8)
    jump dream_start
label bunny4_chat:
    bun "It sure is tough keeping an eye on everyone. I wonder how Marchie manages it?"
    jump dream_start
label bunny4_time:
    bun "Oh, do you need the time? It's currently 9 o'clock. My younger siblings should be going to bed around now."
    jump dream_start

# Clumsy Bunny, needs talk and chat text
label bunny5_talk:
    $ bun_name = "Clumsy Bunny"
    bun "I have my paint but..."
    bun "Where to start?"
    dreamRem ne "Looks like this one's a little preoccupied with talking to themselves."
    jump dream_start
label bunny5_give:
    $ bun_name = "Clumsy Bunny"
    bun "C-cherry medicine…?! Oh, no thank you. I'm not the sick one this time, thankfully."
    jump dream_start
label bunny5_help:
    $ bun_name = "Clumsy Bunny"
    if t_bunny5.state == -1:
        dreamSom ne "Hi! Would you mind helping us clean this place up for your big sib?"
        bun "Oh, before that, can I ask for a favor as well?"
        dreamSom ne "Sure sweetie, what is it?"
        bun "You see, I wanted to give big sib Marchie a gift for all that she's done for us."
        bun "Big sib Marchie's favorite color is red! But all the flowers here are white...!"
        bun "I brought some paint earlier, but I'm not sure where to start..."
        bun "Could you help me {ii}color seven flowers?{/ii}"
        dreamSom gr "What a lovely idea! We'll be sure to do that."
        dreamRem th "Painting... the flowers?"
        dreamRem si "Well, I guess it's the thought that counts."
        python:
            interactions.unlock([t_flower1, t_flower2, t_flower3, t_flower4, t_flower5, t_flower6, t_flower7])
            interactions.update(t_bunny5.updateState(7))
            interactions.update(t_bunny5.disable("bunny5_talk"))
    elif t_bunny5.state == 0:
        bun "Oh, thank you, thank you! The red roses are so pretty!"
        bun "I hope big sib Marchie likes them!"
        bun "And I didn't forget your request- I can help clean up, too!"
        python:
            interactions.update(t_bunny5.disable("bunny5_help"))
            interactions.update(t_bunny5.enable("bunny5_chat"))
            interactions.update(t_debris.updateState(t_debris.state - 1))
            interactions.update(t_debris.updateImage("/images/interactables/case1/debris{}.png".format(t_debris.state)))
        # play debris cleaning sfx
        show expression t_debris.image with Dissolve(0.8)
    elif t_bunny5.state > 0:
        bun "I think there's still [t_bunny5.state] of the flowers left to be painted. Good luck!"
    jump dream_start
label bunny5_chat:
    $ bun_name = "Clumsy Bunny"
    bun "I would've paint the flower myself but last time I painted anything, I spilled the whole bucket all over the floor!"
    bun "Big sib Marchie told me it was okay and that accidents happen, but I felt bad since they had to clean up my mess..."
    jump dream_start
label bunny5_time:
    $ bun_name = "Clumsy Bunny"
    bun "What time is it? Um... The longer needle is the minute hand so it's... 9 o' clock!"
    jump dream_start

# magic to flower paint is that the bg will have red flowers and we'll remove the interaction when they're painted
label flower1_paint:
    $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
    $ interactions.update(t_flower1.disable("flower1_paint"))
    $ interactions.update(t_flower1.updateImage("/images/interactables/case1/flower1red.png"))
    # play paint sfx
    show expression t_flower1.image with Dissolve(0.8)
    jump flower_check
label flower2_paint:
    $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
    $ interactions.update(t_flower2.disable("flower2_paint"))
    $ interactions.update(t_flower2.updateImage("/images/interactables/case1/flower2red.png"))
    # play paint sfx
    show expression t_flower2.image with Dissolve(0.8)
    jump flower_check
label flower3_paint:
    $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
    $ interactions.update(t_flower3.disable("flower3_paint"))
    $ interactions.update(t_flower3.updateImage("/images/interactables/case1/flower3red.png"))
    # play paint sfx
    show expression t_flower3.image with Dissolve(0.8)
    jump flower_check
label flower4_paint:
    $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
    $ interactions.update(t_flower4.disable("flower4_paint"))
    $ interactions.update(t_flower4.updateImage("/images/interactables/case1/flower4red.png"))
    # play paint sfx
    show expression t_flower4.image with Dissolve(0.8)
    jump flower_check
label flower5_paint:
    $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
    $ interactions.update(t_flower5.disable("flower5_paint"))
    $ interactions.update(t_flower5.updateImage("/images/interactables/case1/flower5red.png"))
    # play paint sfx
    show expression t_flower5.image with Dissolve(0.8)
    jump flower_check
label flower6_paint:
    $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
    $ interactions.update(t_flower6.disable("flower6_paint"))
    $ interactions.update(t_flower6.updateImage("/images/interactables/case1/flower6red.png"))
    # play paint sfx
    show expression t_flower6.image with Dissolve(0.8)
    jump flower_check
label flower7_paint:
    $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
    $ interactions.update(t_flower7.disable("flower7_paint"))
    $ interactions.update(t_flower7.updateImage("/images/interactables/case1/flower7red.png"))
    # play paint sfx
    show expression t_flower7.image with Dissolve(0.8)
    jump flower_check

label flower_check:
    if t_bunny5.state == 0:
        dreamRem gr "There! That should be the last rose we needed to paint."
        dreamSom de "Oh they're beautiful Remi!"
        dreamRem fl "Honestly it wasn't that bad since it was like adding decorations to a dish." # I wanted to say icing on a cake but this is remi hhh rose icings... what food does it... minus cake WORDING HELP
        dreamRem de "Now let's go check on the bunny who asked the favor."
    jump dream_start

label march_continue:
    dreamSom de "We did it! The place looks so much nicer now~."
    dreamRem th "How is Marcella feeling?"
    dreamMar "Urgh... and I still have to remember to go there... and pick up that... and call the..."
    dreamRem bi "There's {b}more{/b} tasks to do?!"
    dreamSom bi "Remi, look!"
    $ interactions.complete([t_debris])
    hide expression t_debris with Dissolve(0.8)
    dr "To the dismay of the investigative duo, the oppressive atmosphere of has debris returned, undoing all the progress they had made."
    dr "The two dream eaters paused to gather their bearings as they became overwhelmed, once more, by the clutter."
    dreamRem "All our hard work!"
    dreamRem pe "What could we be doing wrong?"
    dreamSom th "Even in the planner, the pages are just becoming covered with more and more scribbles."
    dreamSom "Perhaps... it's not the tasks themselves that are the problem."
    dreamRem sh "What- So they don't want our help?"
    dreamMar "{ii}Help...?{/ii} Why would I need help? These are my responsibilities! I-I took on the tasks, so I can finish the job myself!"
    $ interactions.complete([t_marcella_mid])
    hide expression t_marcella_mid.image with Dissolve(0.8)
    dreamRem bi "Ack! There they go again...!"
    stop music fadeout 5.0
    dreamSom bi "Let's go, Remi! We mustn't lose them!"
    $ interactions.unlock([t_marcella_end])
    $ unlocked_pages = 2
    jump dream_start

label marcella_talk_end:
    if not t_marcella_end.viewed:
        play music dream2 fadein 2.0
        $ bun_name = "Rowdy bunnies"
        dreamMar "I-I... I can't keep up with this anymore."
        dreamMar "My list keeps growing and growing... but the little ones! They're all depending on me!"
        bun "Big sib! Big sib! We're hungry...! {ss}Hungry!{/ss}"
        dreamRem sh "The bunnies here... They're not acting like the ones from earlier..."
        # [Bunnies that are surrounding Marchie]
        bun "Big sib... Do you know where my shirt is? {ss}It has to be my favorite shirt!{/ss}"
        dreamMar "The kids are growing up... and that means their needs are growing too..."
        dreamMar "I can't let them down but there simply isn't enough time in the world to get all these things done!"
        dreamMar "I can't afford to fall asleep, there's too work much left to be finished!"
        bun "Big sib, can we go to the park? {ss}No, I want to go to the movies!{/ss}"
        dreamMar "Resting now means I'll be wasting my time!"
        bun "Big sib Marchie is the oldest, so they can do everything!"
        dreamMar "I HAVE to keep going!!!" with sshake
        # [# Client collapses in dream?!]
        dreamSom di "Oh, dearie. So the issue with cleaning wasn't the problem after all."
        dreamRem th "Yes, it seems much deeper than that."
        dreamRem "The root of the issue lies in the sibling bunnies."
        dreamSom bi "Remerie, how could you! Don't you dare blame these sweet children!"
        dreamRem pe"I'm not {i}blaming them{/i}, I'm just thinking out loud."
        dreamRem th "We have to consider why the bunnies are in the client's worried dreams to begin with."
        dreamRem "Marcella obviously cares a lot about their siblings, but their perception here is different from our previous interactions."
        dreamRem "Our client has been so focused on meeting everyone's demands that they haven't had the time to sleep."
        dreamRem bi "... Time!"
        dreamRem sh "Somnia, the clocks! Let's go check on all the clocks!"
        dreamSom sh "You're right, there certainly were a lot of clocks in this dream."
        python:
            interactions.unlock([t_clockface1, t_clockface2, t_clockface3, t_clockface4])
            interactions.update(t_marcella_end.view())
            interactions.update(t_bunny1.enable("bunny1_time"))
            interactions.update(t_bunny2.enable("bunny2_time"))
            interactions.update(t_bunny3.enable("bunny3_time"))
            interactions.update(t_bunny4.enable("bunny4_time"))
            interactions.update(t_bunny5.enable("bunny5_time"))
            interactions.update(t_bunny1.disable("bunny1_talk"))
            interactions.update(t_bunny2.disable("bunny2_talk"))
            interactions.update(t_bunny3.disable("bunny3_talk"))
            interactions.update(t_bunny4.disable("bunny4_talk"))
            interactions.update(t_bunny5.disable("bunny5_talk"))
    else:
        dr "Marcella seems to be unconscious at the moment."
    jump dream_start

# Clock under the column on the first page
label clock1_inspect:
    dr "A large clock something something flavor text after seeing the clock drawn"
    dr "The hour hand is facing {b}[t_clockface1.state]{/b}, while the minute hand is stuck facing {b}down{/b}."
    if not t_clockface1.viewed:
        python:
            interactions.update(t_clockface1.view())
            interactions.update(t_clockface1.enable("clock1_up"))
            interactions.update(t_clockface1.enable("clock1_down"))
            interactions.update(t_clockface1.enable("clock1_left"))
            interactions.update(t_clockface1.enable("clock1_right"))
    jump dream_start
label clock1_up:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}up{/b}, while the minute hand is stuck facing {b}down{/b}."
    $ interactions.update(t_clockface1.updateState("up"))
    jump check_clocks
label clock1_down:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}down{/b}, while the minute hand is stuck also facing {b}down{/b}."
    $ interactions.update(t_clockface1.updateState("down"))
    jump check_clocks
label clock1_left:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}left{/b}, while the minute hand is stuck facing {b}down{/b}."
    $ interactions.update(t_clockface1.updateState("left"))
    jump check_clocks
label clock1_right:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}right{/b}, while the minute hand is stuck facing {b}down{/b}."
    $ interactions.update(t_clockface1.updateState("right"))
    jump check_clocks

# giant clock on second page
label clock2_inspect:
    dr "A large clock something something flavor text after seeing the clock drawn"
    dr "The hour hand is facing {b}[t_clockface2.state]{/b}, while the minute hand is stuck facing {b}up{/b}."
    if not t_clockface2.viewed:
        python:
            interactions.update(t_clockface2.view())
            interactions.update(t_clockface2.enable("clock2_up"))
            interactions.update(t_clockface2.enable("clock2_down"))
            interactions.update(t_clockface2.enable("clock2_left"))
            interactions.update(t_clockface2.enable("clock2_right"))
    jump dream_start
label clock2_up:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}up{/b}, while the minute hand is stuck also facing {b}up{/b}."
    $ interactions.update(t_clockface2.updateState("up"))
    jump check_clocks
label clock2_down:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}down{/b}, while the minute hand is stuck facing {b}up{/b}."
    $ interactions.update(t_clockface2.updateState("down"))
    jump check_clocks
label clock2_left:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}left{/b}, while the minute hand is stuck facing {b}up{/b}."
    $ interactions.update(t_clockface2.updateState("left"))
    jump check_clocks
label clock2_right:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}right{/b}, while the minute hand is stuck facing {b}up{/b}."
    $ interactions.update(t_clockface2.updateState("right"))
    jump check_clocks

# first clock on last page
label clock3_inspect:
    if not t_clockface3.viewed:
        dreamRem th "The position of this clock is different from the other one in the room."
        dreamSom th "The numbers and ticks seems to be missing. I wonder how we can tell the time?"
        dreamRem "Hm... the minute hand's not moving... I think it's stuck. Oh, but it looks like I can move the hour hand."
        dreamRem si "Nothing seems to happen when I do, though."
        dreamSom ne "Let's check the other clocks, too."
        python:
            interactions.update(t_clockface3.view())
            interactions.update(t_clockface3.enable("clock3_up"))
            interactions.update(t_clockface3.enable("clock3_down"))
            interactions.update(t_clockface3.enable("clock3_left"))
            interactions.update(t_clockface3.enable("clock3_right"))
    else:
        dr "A large clock something something flavor text after seeing the clock drawn"
        dr "The hour hand is facing {b}[t_clockface3.state]{/b}, while the minute hand is stuck facing {b}right{/b}."
    jump dream_start
label clock3_up:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}up{/b}, while the minute hand is stuck facing {b}right{/b}."
    $ interactions.update(t_clockface3.updateState("up"))
    jump check_clocks
label clock3_down:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}down{/b}, while the minute hand is stuck facing {b}right{/b}."
    $ interactions.update(t_clockface3.updateState("down"))
    jump check_clocks
label clock3_left:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}left{/b}, while the minute hand is stuck facing {b}right{/b}."
    $ interactions.update(t_clockface3.updateState("left"))
    jump check_clocks
label clock3_right:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}right{/b}, while the minute hand is stuck also facing {b}right{/b}."
    $ interactions.update(t_clockface3.updateState("right"))
    jump check_clocks

# second clock on last page
label clock4_inspect:
    if not t_clockface4.viewed:
        dreamRem sh "There're also no numbers on this clock. And the minute hand is stuck."
        dreamSom th "Maybe we need to get all the clock's time to match up?"
        dreamRem th "How can we do that if we can't move the minute hand?"
        dreamSom ex "We'll figure it out, Remi! There has to be a way!"
        python:
            interactions.update(t_clockface4.view())
            interactions.update(t_clockface4.enable("clock4_up"))
            interactions.update(t_clockface4.enable("clock4_down"))
            interactions.update(t_clockface4.enable("clock4_left"))
            interactions.update(t_clockface4.enable("clock4_right"))
    else:
        dr "A large clock something something flavor text after seeing the clock drawn"
        dr "The hour hand is facing {b}[t_clockface4.state]{/b}, while the minute hand is stuck facing {b}left{/b}."
    jump dream_start
label clock4_up:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}up{/b}, while the minute hand is stuck facing {b}left{/b}."
    $ interactions.update(t_clockface4.updateState("up"))
    jump check_clocks
label clock4_down:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}down{/b}, while the minute hand is stuck facing {b}left{/b}."
    $ interactions.update(t_clockface4.updateState("down"))
    jump check_clocks
label clock4_left:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}left{/b}, while the minute hand is stuck also facing {b}left{/b}."
    $ interactions.update(t_clockface4.updateState("left"))
    jump check_clocks
label clock4_right:
    play sound clocktwist
    dr "The hour hand has been moved to face {b}right{/b}, while the minute hand is stuck facing {b}left{/b}."
    $ interactions.update(t_clockface4.updateState("right"))
    jump check_clocks

label check_clocks:
    if t_clockface1.state == "right" and t_clockface2.state == "left" and t_clockface3.state == "up" and t_clockface4.state == "down":
        "tempO"
        stop music fadeout (2.0)
        pause (3.0)
        play sound clockring
        pause (4.0)
        play music clocktick
        dr "As the final clock struck nine, the machinery whirred to life, filling the air with the dull clanking of brass gears and spinning axles."
        dr "The various clock faces occupying the dream space seemed to react at once, winding their hands with incredible speed."
        dr "Finally settling on one time, the clock hands began to move in sync, once more."
        dr "The gentle ticking of each second echoing in unison was simply... harmonious."
        dreamSom sh "Remi, take a look! All the clocks are moving again."
        dreamSom th "Oh, and what's this? Another ingredient..."
        stop music fadeout 1.0
        show screen get_ingredient("egg") with Dissolve(0.8)
        play sound itemget
        dr "You got some {ii}Clockwork Eggs!{/ii}"
        hide screen get_ingredient
        dreamRem gr "That's a relief. My hunch was right after all."
        dreamRem th "So Marcella had a warped perception of time, which fueled their pressure to keep working at the cost of their sleep."
        dreamSom de "Time flies when you're having fun~!"
        dreamRem pe "I wouldn't describe our client's experience as \"fun\"."
        dreamSom th "Well, it sounds like dear Marchie needs a good break..."
        extend "fast."
        play sound rimshot
        dreamSom ex "Hehe..."
        dreamRem gr "Hah, hah. But you're right. It seems a brief respite from their busy life is in order."
        dreamRem th "And I have just the dish for this dream."
        dreamRem "Now with the Clockwork Eggs as the centerpiece..."
        dreamRem de "I believe we have the necessary ingredients for a proper morning dish."
        dreamSom de "Ooh, I'm so excited! Let us be off to the Wishing Kitchen!"
        dreamSom "I'll pocket these pretty eggs for now..."
        dreamSom sh "Ah!"
        dreamRem bi "Somnia! A-are you okay? What's the matter?!"
        dreamSom th "Some of these eggs... they have little stuffed bunnies in them!"
        dreamRem si "..."
        dreamRem "...Is that all? You really had me worried there for a second..."
        dreamSom sh "Yes, but that means we only have {ii}two Clockwork Eggs{/ii} to cook with..."
        dreamRem th "Only two eggs? I'll have to be cautious while I'm cooking..."
        dreamSom ex "I have total faith in you Remi! You can do it!"
        dreamRem gr "Heh, but of course!"

        python:
            inventory.add(c_clockegg)
            finished = True
            interactions.complete([t_clockface1, t_clockface2, t_clockface3, t_clockface4])
            interactions.update(t_bunny1.enable("bunny1_chat"))
            interactions.update(t_bunny2.enable("bunny2_chat"))
            interactions.update(t_bunny3.enable("bunny3_chat"))
            interactions.update(t_bunny4.enable("bunny4_chat"))
            interactions.update(t_bunny5.enable("bunny5_chat"))
            interactions.update(t_bunny1.disable("bunny1_time"))
            interactions.update(t_bunny2.disable("bunny2_time"))
            interactions.update(t_bunny3.disable("bunny3_time"))
            interactions.update(t_bunny4.disable("bunny4_time"))
            interactions.update(t_bunny5.disable("bunny5_time"))
            renpy.start_predict_screen("cooking")
            renpy.start_predict(
                "images/BG/starry.png",
                "images/BG/test_cookbook.png",
                "images/items/item_*.png",
                "images/items/dish_*.png",
            )
    else:
        dr "The clock hand was moved, but nothing happened."
    jump dream_start
