label case2_dream:
    "hi"
#     python:
#         bg = "images/BG/bg_wonderland_WIP.png" # background image
#         page_width = 1720 # screen page width
#         total_pages = 2 # total pages in investigation
#         inventory = Inventory()
#         interactions = Interactions()

#         unlocked_pages = 0 # default is 0
#         current_page = 0 # start at 0
#         finished = False # default is false, but true for testing
#     scene black
#     show screen dream()
#     show screen focus_dialogue()
# # NOTE SFX: something falling, sfx for Somnia tripping
#     dreamSom sh "W-whoa...!" with sshake
#     dreamRem ne "I got you. Watch your step, it's a mess in here."
#     dreamRem ne "A dream representing the client's outward appearance..."
#     dreamSom th "Our client must really have a hard time arranging their thoughts, among other things..."
#     dreamRem si "Sounds like someone I know."
#     dreamRem pe "Don't think I didn't catch you this morning rearranging our already labeled pastry display!"
#     dreamSom gr "Aww, but it looks better when it's arranged by jam color!" with flash
#     dreamRem si "*sigh* Anyway, we need to find our client. Where are they?"
#     play music dream1
#     $ interactions.unlock([t_marcella_start])
#     show expression t_marcella_start.image with Dissolve(0.8)
#     dreamMar "Oh no, I'm late. I'm late! I have to hurry!"
#     dreamMar "This assignment is due... and I have to fill out the report for... Oh, I need to pick up the..."
#     dreamSom sh "My, there's Marcella, practically up to their nose in paperwork!"
#     dreamRem ne "The client can't see us in their dream, but let's tail them."
#     jump dream_start
#     hide screen focus_dialogue


# label marcella_talk_start:
#     dreamMar "... And there's the kids' practice... I need to arrange the bouquet... Class has been cancelled but..."
#     $ interactions.complete([t_marcella_start])
#     hide expression t_marcella_start.image with Dissolve(0.8)
#     $ interactions.unlock([t_bunnysquad])
#     show expression t_bunnysquad.image with Dissolve(0.8)
#     dreamRem pe "Darn, they're too fast...!"
#     dreamRem "And what's with these {i}bunnies?!{/i}"
#     dreamSom gr "Oooh, they are so cute!"
#     dreamRem si "Now what? We can't start cooking, much less collect any ingredients in this condition."
#     dreamSom ne "How about we take a look around? Maybe we can learn something from these adorable dream whip cream fluffles~..."
#     jump dream_start

# label bunnies_talk_som:
#     dreamSom de "Hello there, cuties! Would you mind letting us pass? We have an important mission and need to speak with our client up ahead."
#     bun "Mission? {ss}Mission…!{/ss} Do you know big sib Marchie? {ss}So cool!{/ss}"
#     dreamRem th "{ii}\"Marchie\"{/ii}? Could they be talking about Marcella?"
#     dreamSom gr "We sure do! Your sibling asked us for help and we need to reach them. May I ask you dearies to kindly scoot over?"
#     bun "Marchie's the greatest! {ss}They do so much!{/ss} They're the hardest worker ever!"
#     bun "We're gonna work hard too! {ss}Let's support big sib!{/ss}"
#     $ interactions.complete([t_bunnysquad])
#     hide expression t_bunnysquad.image with Dissolve(0.8)
#    # [Get ingredient: bunny-cut apples]
#     dr "The bunnies scampered off, kicking up clouds along the two intrepid dream eaters's path in the shape of..."
#     # [Dream apple close up shot?]
#     dr "... a selection of apple slices. Each slice's ruby skin was daintily cut to mimic the adorable silhouette of a bunny."
#     $ inventory.add(c_bunnyapples)
#     dreamRem th "Our first ingredient is freshly cut apples?"
#     dreamSom gr "Oooh, I wonder if we get to bake a pie with this!"
#     dreamRem ne "We'll see exactly what we can work with once we find more ingredients."
#     dreamSom gr "I'll pocket this sweet snack for now, thank you very much~!"
#     $ interactions.unlock([t_strawberry, t_marcella_mid])
#     $ unlocked_pages += 1
#     jump dream_start

# label bunnies_talk_rem:
#     dreamRem ne "Hey... Can you move aside?"
#     bun "...Move? Why? {ss}Who are you?{/ss}"
#     dreamRem pe "It's not important. You guys are in the way."
#     bun "...We don't wanna. {ss}Say no to strangers!{/ss}"
#     dreamRem pe "(This is why I'm no good with talking to kids...)"
#     dreamSom gr "Aw~, cheer up, Remi. How about I give it a go?"
#     jump dream_start

# label strawberry_look:
#     dreamRem th "Doesn't that moon look peculiar? Those weird spots and pinkish hue... Is it a strawberry?!"
#     dreamSom th "Could it be? An ingredient? Let's extract it!"
#     dr "Squinting up against the moonlight, Somnia reached and placed her hand against the night sky, pinching the distant moon between her fingers."
#     dr "Like a manipulation of perspective, or a magic trick, one pluck was all it took for Somnia to retrieve the strawberry."
#     # [Get Creamy Strawberry!]
#     $ inventory.add(c_strawberry)
#     $ interactions.complete([t_strawberry])
#     jump dream_start

# label marcella_talk_mid:
#     if not t_marcella_mid.viewed:
#         dreamMar "And I have to find my report... and buy the medicine for little Whitney... Ohhh, and this whole place is an absolute mess!"
#         dreamRem sh "Marcella sure has a lot on their plate."
#         dreamSom gr "Perhaps we can help them out!"
#         dreamSom th "Let's see... They're looking for a report, trying to get medicine to one of the siblings... Oh! And they want to clean up this entire area!"
#         dreamRem pe "That last task sounds like a bit of a handful..."
#         dreamSom gr "Oh, come on Remi! It'll be fun! After all~... {mn} A spoonful of sugar-"
#         dreamRem si "Helps the medicine go down, I know. It's your favorite song. Let's just get to work."
#         $ interactions.unlock([t_debris, t_medicine, t_bunny1, t_bunny2, t_bunny3, t_bunny4, t_bunny5])
#         $ interactions.update(t_marcella_mid.view())
#     else:
#         dreamMar "And I have to do this... and don't forget that... Oh, and I need to..."
#         dreamRem th "Looks like Marcella's frozen in their thoughts."
#         dreamSom th "Let's see... They're looking for a report, trying to get medicine to one of the siblings... Oh! And they want to clean up this entire area!"
#         dreamRem si "Hahhh... Let's get to work."
#     jump dream_start

# label pile_inspect:
#     if t_debris.state == 0:
#         jump march_continue
#     elif t_debris.viewed and t_debris >= 0:
#         dreamSom "Let's see if we can get Marcella's little siblings to help us out."
#     else:
#         dreamRem pe "Urk... The client's going to be awake by the time we clean through this mess."
#         dreamSom th "How about we ask these bunnies... Marcella's little siblings, to help out?"
#         dreamRem th "Well, it's definitely worth a shot."
#         dreamRem sh "Hang on, there's a book in the pile of papers."
#         dreamSom sh "There's a name written inside- \"Maddie\"."
#         dreamRem th "Do you think that's one of the bunnies' names?"
#         dreamSom gr "How cute! We should hang on to it, just in case."
#         python:
#             interactions.update(t_debris.view())
#             interactions.update(t_bunny1.enable("bunny1_help"))
#             interactions.update(t_bunny2.enable("bunny2_help"))
#             interactions.update(t_bunny3.enable("bunny3_help"))
#             interactions.update(t_bunny4.enable("bunny4_help"))
#             interactions.update(t_bunny5.enable("bunny5_help"))
#             inventory.add(c_bluebook)
#             interactions.update(t_debris.updateState(4)) # you got 4 bunnies to ask for help
#     jump dream_start

# label medicine_find:
#     dreamSom sh "This looks to be the medicine we have to give to Marcella's sister! The label says \"Drink Me\"."
#     dreamRem th "The question is just which of these siblings need a dose."
#     dreamSom gr "I guess we'll just have to go around and ask!"
#     dreamRem pe "... I'll let you do the talking."
#     python:
#         inventory.add(c_medicine)
#         interactions.complete([t_medicine])
#         interactions.update(t_bunny1.enable("bunny1_give"))
#         interactions.update(t_bunny2.enable("bunny2_give"))
#         interactions.update(t_bunny3.enable("bunny3_give"))
#         interactions.update(t_bunny4.enable("bunny4_give"))
#         interactions.update(t_bunny5.enable("bunny5_give"))
#     jump dream_start

# label report_find:
#     dreamSom sh "Could this be the report Marcella was looking for?"
#     dreamRem sh "I don't think this looks to be a report as much as it is a... planner?"
#     dreamSom bi "Gosh, just look at this calendar. It's been filled to the brim with events!"
#     dreamRem "You can tell those are supposed to be events? All the pages are a complete mess!"
#     dreamRem "I can't even read the handwriting!"
#     dreamRem th "I guess even in a dream, our client doesn't feel very organized with their life."
#     dreamSom ne "Let's return the planner to Marcella after we finish the other tasks."
#     $ inventory.add(c_redbook)
#     $ inventory.drop(c_bluebook)
#     jump dream_start

# # Quiet Bunny
# label bunny1_talk:
#     $ bun_name = "Quiet bunny"
#     if not t_bunny1.state:
#         dreamRem "Hey."
#         bun "..."
#         dreamRem "..."
#         dreamRem "Can they not hear me?"
#         dreamSom "They look like they're occupied in trying to find something..."
#         bun "I can't find my favorite book..."
#         dreamRem "A blue book, huh."
#         if c_bluebook in inventory.items:
#             dreamRem "Well, we found this book in that pile of papers over there earlier. Are you Maddie?"
#             bun "Oh! Oh, yes!"
#             $ bun_name = "Maddie"
#             bun "Yay! You saved the day!"
#             dreamRem gr "... I did, huh..."
#             dreamSom de "Aw, Remi you look so happy! How sweet~!"
#             dreamRem fl "L-let's just focus on the task at hand, alright?"
#             bun "I mixed up my book for another one. Here, you can have it!"
#             $ interactions.update(t_bunny1.updateState(True))
#             jump report_find
#     else:
#         $ bun_name = "Maddie"
#         bun "Thank you again for the book!"
#         bun "Whitney has to go to bed early tonight- she needs to get her rest."
#         bun "She would have been so sad if I couldn't read her favorite stories before bed..."
#     jump dream_start
# label bunny1_give:
#     $ bun_name = "Maddie"
#     bun "My name is Maddie, not Whitney! Even though I'm smaller than her, I'm older!"
#     jump dream_start
# label bunny1_help:
#     dreamSom ne "Hello, there! Auntie Som needs some help with cleaning, would you mind helping?"
#     if not t_bunny1.state:
#         bun "..."
#         dreamSom th "..."
#         bun "I can't find my favorite book..."
#         bun "It's blue and has my name on the inside."
#         dreamSom "Hm... A blue book, you say..."
#         if c_bluebook in inventory.items:
#             dreamSom ne "Maddie, is this what you're looking for?"
#             bun "Oh! Oh, yes!"
#             bun "Yay! You saved the day!"
#             dreamRem pe "Could've just asked for our help instead of ignoring me."
#             dreamSom gr "Oh, Remi, no need to be such a grumpster!"
#             dreamRem fl "I-I'm not..."
#             bun "I mixed up my book for another one. Here, you can have it!"
#             $ interactions.update(t_bunny1.updateState(True))
#             jump report_find
#     else:
#         dreamRem sh "It looks like Maddie is too focused on her book now to answer."
#         dreamSom gr "Oh, I know that feeling!"
#         dreamSom th "Maybe we can try asking again later."
#     jump dream_start
# label bunny1_chat:
#     bun "Whitney has to go to bed early tonight- she needs to get her rest."
#     bun "She would have been so sad if I couldn't read her favorite stories before bed..."
#     jump dream_start
# label bunny1_time:
#     bun "It's 9 o' clock! I just finished reading Whitney her favorite bedtime stories."
#     jump dream_start

# # Energetic Bunny (the sick one)
# label bunny2_talk:
#     $ bun_name = "Energetic bunny"
#     if not t_bunny2.state:
#         bun "Wheee! Wheeeee!"
#         dreamSom bi "That little one is going to get hurt, jumping around like that...!"
#         dreamRem si "I'm sure she knows what she's doing."
#         bun "Whee- OUCH!" with sshake
#         dreamRem pe "OW! Watch it!" with sshake
#         dreamSom sh "Oh, sweetie, slow down and please be careful!"
#         bun "I'm fine! Hehe, wheee!"
#         dreamRem "Kids theses days..."
#         dreamSom gr "Now, now~"
#     else:
#         bun "*Yaaaawn*"
#         bun "I feel kinda sleepy now after the medicine..."
#     jump dream_start
# label bunny2_give:
#     $ bun_name = "Little Whitney"
#     dreamSom ne "Little Whitney? I heard someone's not feeling good and needs to take her medicine."
#     bun "What? I'm fine! Look how fast I can run!"
#     dreamRem si "The only running I see is your high fever."
#     bun "No...! NO! I don't want to take my medicine!"
#     dreamSom "Now, now... You have to be strong so you can be healthy and play outside."
#     dreamSom gr "Open up~!"
#     bun "It... It doesn't taste all that bad."
#     dreamSom de "See? That's a good girl! I hope you feel better soon."
#     bun "Thanks, lady!"
#     dreamRem gr "... Let me guess, you added some sugar."
#     dreamSom de "Hmmm hm~ {mn}"
#     python:
#         interactions.update(t_bunny1.disable("bunny1_give"))
#         interactions.update(t_bunny2.disable("bunny2_give"))
#         interactions.update(t_bunny3.disable("bunny3_give"))
#         interactions.update(t_bunny4.disable("bunny4_give"))
#         interactions.update(t_bunny5.disable("bunny5_give"))
#         interactions.update(t_bunny2.updateState(True))
#     jump dream_start
# label bunny2_help:
#     if not t_bunny2.state:
#         $ bun_name = "Energetic bunny"
#         bun "Wheee! Wheee!"
#         dreamSom th "It seems a bit difficult to catch this little one's attention right now."
#     else:
#         dreamSom sh "We can't ask little Whitney to help! The thing she needs right now is some proper rest!"
#         $ bun_name = "Maddie"
#         bun "E-excuse me...!"
#         dreamRem sh "Hm? Oh, it's the bunny that wanted the blue book."
#         dreamSom gr "Hi there, Maddie. What's wrong?"
#         bun "Since little Whitney is sick, I can help clean up instead!"
#         bun "I just finished my book, I'll be right over!"
#         dreamSom de "My, how responsible! Thank you, darling~!"
#         # momentary fade effect
#         python:
#             interactions.update(t_bunny1.disable("bunny1_help"))
#             interactions.update(t_bunny2.disable("bunny2_help"))
#             interactions.update(t_debris.updateState(t_debris.state - 1))
#     jump dream_start
# label bunny2_chat:
#     $ bun_name = "Little Whitney"
#     bun "Zzz..."
#     jump dream_start
# label bunny2_time:
#     $ bun_name = "Little Whitney"
#     bun "Zzz..."
#     dreamSom de "Aww... She's fast asleep now."
#     dreamRem th "(How do you fall asleep inside a dream?)"
#     jump dream_start

# # Peevish Bunny
# label bunny3_talk:
#     $ bun_name = "Peevish bunny"
#     bun "Our younger sis hasn't been feeling well lately, but she's weak to the taste of medicine so she tries to lie her way out of it. How spoiled!"
#     jump dream_start
# label bunny3_give:
#     $ bun_name = "Peevish bunny"
#     bun "Medicine? Me? I'm not the sick one! Give it to Little Whitney!"
#     jump dream_start
# label bunny3_help:
#     $ bun_name = "Peevish bunny"
#     dreamSom "Hello, could you help us move some of that big pile of papers for your dear big sis Marchie?"
#     bun "Hmph... I guess if it's to help out big sib Marchie then..."
#     python:
#         interactions.update(t_bunny3.disable("bunny3_help"))
#         interactions.update(t_debris.updateState(t_debris.state - 1))
#     jump dream_start
# label bunny3_chat:
#     $ bun_name = "Peevish bunny"
#     bun "What's up."
#     jump dream_start
# label bunny3_time:
#     $ bun_name = "Peevish bunny"
#     bun "What time is it? Well, it's obviously 9 o' clock!"
#     jump dream_start

# # Studious Bunny
# label bunny4_talk:
#     $ bun_name = "Studious bunny"
#     bun "Our parents are really busy so Marchie's been taking care of us in their stead. I'm the second oldest, but recently I've been away for school."
#     bun "I hope Marchie is doing alright..."
#     jump dream_start
# label bunny4_give:
#     $ bun_name = "Studious bunny"
#     bun "Oh, are you looking for Little Whitney? She's an outgoing kid so you'd probably find her somewhere more open."
#     jump dream_start
# label bunny4_help:
#     $ bun_name = "Studious bunny"
#     bun "Why yes, I'd love to help if that would be okay!"
#     python:
#         interactions.update(t_bunny4.disable("bunny4_help"))
#         interactions.update(t_debris.updateState(t_debris.state - 1))
#     jump dream_start
# label bunny4_chat:
#     bun "It sure is tough keeping an eye on everyone. I wonder how Marchie manages it?"
#     jump dream_start
# label bunny4_time:
#     bun "It's 9 o'clock. My younger siblings should be going to bed around now."
#     jump dream_start

# # Clumsy Bunny, needs talk and chat text
# label bunny5_talk:
#     $ bun_name = "Clumsy bunny"
#     bun "aaaa flavor text"
#     jump dream_start
# label bunny5_give:
#     $ bun_name = "Clumsy bunny"
#     bun "C-cherry medicine…?! Oh, no thank you. I'm not the sick one this time, thankfully."
#     jump dream_start
# label bunny5_help:
#     $ bun_name = "Clumsy bunny"
#     if t_bunny5.state == -1:
#         bun "Oh, before that, can I ask for a favor as well?"
#         dreamSom ne "Sure sweetie, what is it?"
#         bun "You see, I wanted to give big sis Marchie a gift for all that she's done for us."
#         bun "Big sis Marchie's favorite color is red! But all the flowers here are white...!"
#         bun "I brought some paint earlier, could you help me color seven flowers?"
#         dreamSom gr "What a lovely idea! We'll be sure to do that."
#         dreamRem th "Painting... the flowers?"
#         dreamRem si "Well, I guess it's the thought that counts."
#         $ interactions.unlock([t_flower1, t_flower2, t_flower3, t_flower4, t_flower5, t_flower6, t_flower7])
#         $ interactions.update(t_bunny5.updateState(7))
#     elif t_bunny5.state == 0:
#         bun "Hmm? Sure, I can help out!"
#         $ interactions.update(t_bunny5.disable("bunny5_help"))
#         $ interactions.update(t_debris.updateState(t_debris.state - 1))
#     elif t_bunny5.state > 0:
#         "There's still [t_bunny5.state] of the flowers left to be painted."
#     jump dream_start
# label bunny5_chat:
#     $ bun_name = "Clumsy bunny"
#     bun "what's up"
#     jump dream_start
# label bunny5_time:
#     $ bun_name = "Clumsy bunny"
#     bun "What time is it? Um... the longer needle is the minute hand so it's... 9 o' clock!"
#     jump dream_start

# # magic to flower paint is that the bg will have red flowers and we'll remove the interaction when they're painted
# label flower1_paint:
#     $ interactions.complete([t_flower1])
#     $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
#     hide expression flower1.image with Dissolve(0.8)
#     jump dream_start
# label flower2_paint:
#     $ interactions.complete([t_flower2])
#     $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
#     hide expression flower2.image with Dissolve(0.8)
#     jump dream_start
# label flower3_paint:
#     $ interactions.complete([t_flower3])
#     $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
#     hide expression flower3.image with Dissolve(0.8)
#     jump dream_start
# label flower4_paint:
#     $ interactions.complete([t_flower4])
#     $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
#     hide expression flower4.image with Dissolve(0.8)
#     jump dream_start
# label flower5_paint:
#     $ interactions.complete([t_flower5])
#     $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
#     hide expression flower5.image with Dissolve(0.8)
#     jump dream_start
# label flower6_paint:
#     $ interactions.complete([t_flower6])
#     $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
#     hide expression flower6.image with Dissolve(0.8)
#     jump dream_start
# label flower7_paint:
#     $ interactions.complete([t_flower7])
#     $ interactions.update(t_bunny5.updateState(t_bunny5.state - 1))
#     hide expression flower7.image with Dissolve(0.8)
#     jump dream_start

# label march_continue:
#     dreamSom de "We did it! The place looks so much nicer now~."
#     dreamRem th "How is Marcella feeling?"
#     dreamMar "Urgh... and I still have to remember to go there... and pick up that... and call the..."
#     dreamRem bi "There's {b}more{/b} tasks to do?!"
#     dreamSom bi "Remi, look!"
#     dr "To the dismay of the investigative duo, the oppressive atmosphere of has debris returned, undoing all the progress they had made."
#     dr "The two dream eaters paused to gather their bearings as they became overwhelmed, once more, by the clutter."
#     dreamRem "All our hard work!"
#     dreamRem pe "What could we be doing wrong?"
#     dreamSom th "Even in the planner, the pages are just becoming covered with more and more scribbles."
#     dreamSom "Perhaps... it's not the tasks themselves that are the problem."
#     dreamRem sh "What- So they don't want our help?"
#     dreamMar "{ii}Help...?{/ii} Why would I need help? These are my responsibilities! I-I took on the tasks, so I can finish the job myself!"
#     $ interactions.complete([t_marcella_mid])
#     hide expression t_marcella_mid.image with Dissolve(0.8)
#     dreamRem bi "Ack! There they go again...!"
#     dreamSom bi "Let's go, Remi! We mustn't lose them!"
#     $ interactions.complete([t_debris])
#     $ interactions.unlock([t_marcella_end])
#     $ unlocked_pages = 2
#     jump dream_start

# label marcella_talk_end:
#     if not t_marcella_end.viewed:
#         $ bun_name = "Rowdy bunnies"
#         dreamMar "I-I... I can't keep up with this anymore."
#         dreamMar "My list keeps growing and growing... but the little ones! They're all depending on me!"
#         bun "Big sib! Big sib! We're hungry...! {ss}Hungry!{/ss}"
#         dreamRem sh "The bunnies here... They're not acting like the ones from earlier..."
#         # [Bunnies that are surrounding Marchie]
#         bun "Big sib... Do you know where my shirt is? {ss}It has to be my favorite shirt!{/ss}"
#         dreamMar "The kids are growing up... and that means their needs are growing too..."
#         dreamMar "I can't let them down but there simply isn't enough time in the world to get all these things done!"
#         dreamMar "I can't afford to fall asleep, there's too work much left to be finished!"
#         bun "Big sib, can we go to the park? {ss}No, I want to go to the movies!{/ss}"
#         dreamMar "Resting now means I'll be wasting my time!"
#         bun "Big sib Marchie is the oldest, so they can do everything!"
#         dreamMar "I HAVE to keep going!!!"
#         # [# Client collapses in dream?!]
#         dreamSom di "Oh, dearie. So the issue with cleaning wasn't the problem after all."
#         dreamRem th "Yes, it seems much deeper than that."
#         dreamRem "The root of the issue lies in the sibling bunnies."
#         dreamSom bi "Remerie, how could you! Don't you dare blame these sweet children!"
#         dreamRem pe"I'm not {i}blaming them{/i}, I'm just thinking out loud."
#         dreamRem th "We have to consider why the bunnies are in the client's worried dreams to begin with."
#         dreamRem "Marcella obviously cares a lot about their siblings, but their perception here is different from our previous interactions."
#         dreamRem "Our client has been so focused on meeting everyone's demands that they haven't had the time to sleep."
#         dreamRem bi "... Time!"
#         dreamRem sh "Somnia, the clocks! Let's go check on all the clocks!"
#         dreamSom sh "You're right, there certainly were a lot of clocks in this dream."
#         python:
#             interactions.unlock([t_clockface1, t_clockface2, t_clockface3, t_clockface4])
#             interactions.update(t_marcella_end.view())
#             interactions.update(t_bunny1.enable("bunny1_time"))
#             interactions.update(t_bunny2.enable("bunny2_time"))
#             interactions.update(t_bunny3.enable("bunny3_time"))
#             interactions.update(t_bunny4.enable("bunny4_time"))
#             interactions.update(t_bunny5.enable("bunny5_time"))
#             interactions.update(t_bunny1.disable("bunny1_talk"))
#             interactions.update(t_bunny2.disable("bunny2_talk"))
#             interactions.update(t_bunny3.disable("bunny3_talk"))
#             interactions.update(t_bunny4.disable("bunny4_talk"))
#             interactions.update(t_bunny5.disable("bunny5_talk"))
#     else:
#         dr "Marcella seems to be unconscious at the moment."
#     jump dream_start

# # Clock under the column on the first page
# label clock1_inspect:
#     dr "A large clock something something flavor text after seeing the clock drawn"
#     dr "The hour hand is facing {b}[t_clockface1.state]{/b}, while the minute hand is stuck facing {b}down{/b}."
#     if not t_clockface1.viewed:
#         python:
#             interactions.update(t_clockface1.view())
#             interactions.update(t_clockface1.enable("clock1_up"))
#             interactions.update(t_clockface1.enable("clock1_down"))
#             interactions.update(t_clockface1.enable("clock1_left"))
#             interactions.update(t_clockface1.enable("clock1_right"))
#     jump dream_start
# label clock1_up:
#     dr "The hour hand has been moved to face {b}up{/b}, while the minute hand is stuck facing {b}down{/b}."
#     $ interactions.update(t_clockface1.updateState("up"))
#     jump check_clocks
# label clock1_down:
#     dr "The hour hand has been moved to face {b}down{/b}, while the minute hand is stuck also facing {b}down{/b}."
#     $ interactions.update(t_clockface1.updateState("down"))
#     jump check_clocks
# label clock1_left:
#     dr "The hour hand has been moved to face {b}left{/b}, while the minute hand is stuck facing {b}down{/b}."
#     $ interactions.update(t_clockface1.updateState("left"))
#     jump check_clocks
# label clock1_right:
#     dr "The hour hand has been moved to face {b}right{/b}, while the minute hand is stuck facing {b}down{/b}."
#     $ interactions.update(t_clockface1.updateState("right"))
#     jump check_clocks

# # giant clock on second page
# label clock2_inspect:
#     dr "A large clock something something flavor text after seeing the clock drawn"
#     dr "The hour hand is facing {b}[t_clockface2.state]{/b}, while the minute hand is stuck facing {b}up{/b}."
#     if not t_clockface2.viewed:
#         python:
#             interactions.update(t_clockface2.view())
#             interactions.update(t_clockface2.enable("clock2_up"))
#             interactions.update(t_clockface2.enable("clock2_down"))
#             interactions.update(t_clockface2.enable("clock2_left"))
#             interactions.update(t_clockface2.enable("clock2_right"))
#     jump dream_start
# label clock2_up:
#     dr "The hour hand has been moved to face {b}up{/b}, while the minute hand is stuck also facing {b}up{/b}."
#     $ interactions.update(t_clockface2.updateState("up"))
#     jump check_clocks
# label clock2_down:
#     dr "The hour hand has been moved to face {b}down{/b}, while the minute hand is stuck facing {b}up{/b}."
#     $ interactions.update(t_clockface2.updateState("down"))
#     jump check_clocks
# label clock2_left:
#     dr "The hour hand has been moved to face {b}left{/b}, while the minute hand is stuck facing {b}up{/b}."
#     $ interactions.update(t_clockface2.updateState("left"))
#     jump check_clocks
# label clock2_right:
#     dr "The hour hand has been moved to face {b}right{/b}, while the minute hand is stuck facing {b}up{/b}."
#     $ interactions.update(t_clockface2.updateState("right"))
#     jump check_clocks

# # first clock on last page
# label clock3_inspect:
#     if not t_clockface3.viewed:
#         dreamRem th "The position of this clock is different from the other one in the room."
#         dreamSom th "The numbers and ticks seems to be missing. I wonder how we can tell the time?"
#         dreamRem "Hm... the minute hand's not moving... I think it's stuck. Oh, but it looks like I can move the hour hand."
#         dreamRem si "Nothing seems to happen when I do, though."
#         dreamSom ne "Let's check the other clocks, too."
#         python:
#             interactions.update(t_clockface3.view())
#             interactions.update(t_clockface3.enable("clock3_up"))
#             interactions.update(t_clockface3.enable("clock3_down"))
#             interactions.update(t_clockface3.enable("clock3_left"))
#             interactions.update(t_clockface3.enable("clock3_right"))
#     else:
#         dr "A large clock something something flavor text after seeing the clock drawn"
#         dr "The hour hand is facing {b}[t_clockface3.state]{/b}, while the minute hand is stuck facing {b}right{/b}."
#     jump dream_start
# label clock3_up:
#     dr "The hour hand has been moved to face {b}up{/b}, while the minute hand is stuck facing {b}right{/b}."
#     $ interactions.update(t_clockface3.updateState("up"))
#     jump check_clocks
# label clock3_down:
#     dr "The hour hand has been moved to face {b}down{/b}, while the minute hand is stuck facing {b}right{/b}."
#     $ interactions.update(t_clockface3.updateState("down"))
#     jump check_clocks
# label clock3_left:
#     dr "The hour hand has been moved to face {b}left{/b}, while the minute hand is stuck facing {b}right{/b}."
#     $ interactions.update(t_clockface3.updateState("left"))
#     jump check_clocks
# label clock3_right:
#     dr "The hour hand has been moved to face {b}right{/b}, while the minute hand is stuck also facing {b}right{/b}."
#     $ interactions.update(t_clockface3.updateState("right"))
#     jump check_clocks

# # second clock on last page
# label clock4_inspect:
#     if not t_clockface4.viewed:
#         dreamRem sh "There're also no numbers on this clock. And the minute hand is stuck."
#         dreamSom th "Maybe we need to get all the clock's time to match up?"
#         dreamRem th "How can we do that if we can't move the minute hand?"
#         dreamSom ex "We'll figure it out, Remi! There has to be a way!"
#         python:
#             interactions.update(t_clockface4.view())
#             interactions.update(t_clockface4.enable("clock4_up"))
#             interactions.update(t_clockface4.enable("clock4_down"))
#             interactions.update(t_clockface4.enable("clock4_left"))
#             interactions.update(t_clockface4.enable("clock4_right"))
#     else:
#         dr "A large clock something something flavor text after seeing the clock drawn"
#         dr "The hour hand is facing {b}[t_clockface4.state]{/b}, while the minute hand is stuck facing {b}left{/b}."
#     jump dream_start
# label clock4_up:
#     dr "The hour hand has been moved to face {b}up{/b}, while the minute hand is stuck facing {b}left{/b}."
#     $ interactions.update(t_clockface4.updateState("up"))
#     jump check_clocks
# label clock4_down:
#     dr "The hour hand has been moved to face {b}down{/b}, while the minute hand is stuck facing {b}left{/b}."
#     $ interactions.update(t_clockface4.updateState("down"))
#     jump check_clocks
# label clock4_left:
#     dr "The hour hand has been moved to face {b}left{/b}, while the minute hand is stuck also facing {b}left{/b}."
#     $ interactions.update(t_clockface4.updateState("left"))
#     jump check_clocks
# label clock4_right:
#     dr "The hour hand has been moved to face {b}right{/b}, while the minute hand is stuck facing {b}left{/b}."
#     $ interactions.update(t_clockface4.updateState("right"))
#     jump check_clocks

# label check_clocks:
#     if t_clockface1.state == "right" and t_clockface2.state == "left" and t_clockface3.state == "up" and t_clockface4.state == "down":
#         # clocktower ring sfx
#         dr "As the final clock struck nine, the machinery whirred to life, filling the air with the dull clanking of brass gears and spinning axles."
#         dr "The various clock faces occupying the dream space seemed to react at once, winding their hands with incredible speed."
#         dr "Finally settling on one time, the clock hands began to move in sync, once more."
#         dr "The gentle ticking of each second echoing in unison was simply... harmonious."
#         dreamSom sh "Remi, take a look! All the clocks are moving again."
#         dreamRem gr "That's a relief. My hunch was right after all."
#         dreamRem th "So Marcella had a warped perception of time, which fueled their pressure to keep working at the cost of their sleep."
#         dreamSom de "Time flies when you're having fun~!"
#         dreamRem pe "I wouldn't describe our client's experience as \"fun\"."
#         dreamSom th "Well, it sounds like dear Marchie needs a good break..."
#         extend "fast."
#         play sound rimshot
#         dreamSom ex "Hehe..."
#         # rimshot noise?!
#         dreamRem gr "Hah, hah. But you're right. And I have just the recipe for this dream."
#         dreamSom de "Ooh, I'm so excited! Let us be off to the Wishing Kitchen!"
#         python:
#             inventory.add(c_clockegg)
#             finished = True
#             interactions.complete([t_clockface1, t_clockface2, t_clockface3, t_clockface4])
#             interactions.update(t_bunny1.enable("bunny1_chat"))
#             interactions.update(t_bunny2.enable("bunny2_chat"))
#             interactions.update(t_bunny3.enable("bunny3_chat"))
#             interactions.update(t_bunny4.enable("bunny4_chat"))
#             interactions.update(t_bunny5.enable("bunny5_chat"))
#             interactions.update(t_bunny1.disable("bunny1_time"))
#             interactions.update(t_bunny2.disable("bunny2_time"))
#             interactions.update(t_bunny3.disable("bunny3_time"))
#             interactions.update(t_bunny4.disable("bunny4_time"))
#             interactions.update(t_bunny5.disable("bunny5_time"))
#     dr "The clock hand was moved, but nothing happened."
#     jump dream_start
