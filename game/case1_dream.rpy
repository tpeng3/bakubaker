label tina:
    menu:
        "Dream Investigation":
            jump case1_dream
        "Hell's Kitchen":
            jump case1_cook

label case1_dream:
    python:
        case = "case1" # remove later since it's in vn
        bg = "wonderland2" # background image
        page_width = 1720 # screen page width
        total_pages = 3 # total pages in investigation
        inventory = Inventory()
        # itr_list = [t_client, t_clocktower, t_strawberry] # starting interactions, it should actually be blank for case1
        interactions = Interactions()
        
        unlocked_pages = 0 # default is 0
        finished = False # default is false, but true for testing
    scene black
    show screen dream()
    window hide
    dreamSom "Woah…!"
    dreamRem "Geez, it's a mess in here."
    dreamSom "Our client must really have a hard time arranging their thoughts..."
    dreamRem "Sounds like someone I know."
    dreamRem "Don’t think I didn’t catch you this morning rearranging our already labeled pastry display!"
    dreamSom "Aww, but it looks better when it’s arranged by jam color!"
    dreamRem "*Sigh* Anyways, we need to find our client. Where are they?"
    $ interactions.unlock([t_marcella_start])
    show expression t_marcella_start.image with Dissolve(0.8)
    # [# Client fades into appearance on the first screen]
    # # Client "Oh no, I’m late. I’m late! I have to hurry!"
    # # Client "This assignment is due... and I have to fill out the report for... oh, I need to pick up the..."
    dreamSom "Oh, there they are, practically up to their nose in paperwork!"
    dreamRem "The client can’t see us in their dream, but let’s tail them."
    jump dream_start

label marcella_talk_start:
    # Client "...And there's the kids' practice... I need to arrange the bouquet... class has been cancelled but..."
    hide expression t_marcella_start.image with Dissolve(0.8)
    show expression t_bunnysquad.image with Dissolve(0.8)
    $ interactions.complete([t_marcella_start])
    $ interactions.unlock([t_bunnysquad])
    dreamRem "Darn, they're too fast...!"
    dreamRem "What’s with these bunnies?!"
    dreamSom "Ooh, they are so cute!!"
    dreamRem "Now what? We can't start cooking under these conditions..."
    dreamSom "How about we take a look around? Maybe we can learn something from these adorable dream whip cream fluffles~"
    jump dream_start

label bunnies_talk_som:
    dreamSom "Hi there cuties! Would you mind letting us pass? We have an important mission and need to speak with our client up ahead."
    # Bunnies: "Mission? Mission…! Do you know big sis Marchie? So cool!!" 
    dreamSom "We sure do! Your older sister asked us for help, and I’ll need your assistance in order to help them."
   # Bunnies: "Marchie’s the greatest! They do so much! They’re the hardest worker ever!"
   # Bunnies: "We’re gonna work hard too! Let’s support big sis!"
    hide expression t_bunnysquad.image with Dissolve(0.8)
    $ interactions.complete([t_bunnysquad])
    $ interactions.unlock([t_strawberry])
    $ unlocked_pages += 1
    $ inventory.add(c_bunnyapples)
   # [Get ingredient: bunny-cut apples]
    "As the bunnies left, a bundle of clouds manifested itself along the path of the two intrepid dream eaters. A shape that came out to be..."
    # [Dream apple close up shot?]
    "...A selection of apple slices, daintily cut in the shape of bunnies."
    dreamRem "Our first ingredient is freshly cut apples?"
    dreamSom "Oooh, I wonder if we get to bake a pie with this!"
    dreamRem "We'll just have to see what we got to work with as we find other ingredients."
    dreamSom "I'll pocket this sweet snack for now, thank you very much~"
    jump dream_start

label bunnies_talk_rem:
    dreamRem "Hey… Can you move aside?"
    # Bunnies: "...Move? Why? Who are you?"
    dreamRem "It’s… not important. But you guys are in the way."
    # Bunnies: "...We don’t wanna. Say no to strangers!"
    dreamRem "(...This is why I’m no good with talking to kids.)"
    dreamSom "Aww cheer up, Remi. How about I give it a go?"
    jump dream_start

label strawberry_look:
    dreamRem "The moon looks awfully peculiar… Is that a strawberry?!"
    dreamSom "Could it be? An ingredient? Let’s extract it!"
    "Remerie watched as dreamSom reached out her hand and carefully plucked the strawberry out of the night sky."
    # [Get Creamy Strawberry!]
    $ inventory.add(c_strawberry)
    jump dream_start

label marcella_talk_mid1:
    # # Client: "And I have to find my report… and buy the medicine for little Whitney... Oooh and this whole place has been a mess!"
    dreamRem "Marcella sure has a lot on their plate."
    dreamSom "Then perhaps we can help them out!"
    dreamSom "Let’s see… they’re looking for their report… trying to give medicine to their little sister… Oh! And they want to clean up this entire area!"
    dreamRem "That last task sounds like a bit of a handful…"
    dreamSom "Oh come on Remi, it’ll be fun! After all ~🎶, spoonful of sugar-"
    dreamRem "...Helps the medicine go down, I know. It’s your favorite song. Let's just get to work."
    $ interactions.unlock([t_report, t_debris4, t_medicine, t_bunny1, t_bunny2, t_bunny3, t_bunny4, t_bunny5])
    jump dream_start

label marcella_talk_mid2:
    # Marcella "And I have to do this… and don’t forget that… Oh and I need to…"
    dreamRem "Looks like Marcella’s frozen in their thoughts."
    jump dream_start

label report_find:
    dreamSom "Could this be the report Marcella was looking for?"
    dreamRem "I don’t think this looks to be a report as much as it is a… planner?"
    dreamSom "Wow, look at this calendar, it’s been filled to the brim with events!"
    dreamRem "How could you tell? All the pages are a complete mess!"
    dreamRem "I can’t even read the handwriting!"
    dreamRem "I guess even in a dream, our client doesn’t feel very organized with their life."
    dreamSom "Let’s return the planner to Marcella after we finish the other tasks."
    $ interactions.complete([t_report])
    jump dream_start

label pile_clean:
    dreamRem "Urk… The client’s going to be awake by the time we clean through this mess."
    dreamSom "How about we ask Marchie’s little siblings to help out?"
    dreamRem "Well, it’s definitely worth a shot."
    python:
        interactions.update(t_bunny1.enable("bunny1_help"))
        interactions.update(t_bunny2.enable("bunny2_help"))
        interactions.update(t_bunny3.enable("bunny3_help"))
        interactions.update(t_bunny4.enable("bunny4_help"))
        interactions.update(t_bunny5.enable("bunny5_help"))
    jump dream_start

label medicine_get:
    dreamSom "This looks to be the medicine we have to give to Marcella's sister. The label says \"Drink Me\"."
    dreamRem "The question is… which of their siblings need a dose?"
    dreamSom "I guess we’ll just have to go around and ask!"
    dreamRem "I’ll… let you do the talking."
    python:
        inventory.add(c_medicine)
        interactions.complete([t_medicine])
        interactions.update(t_bunny1.enable("bunny1_give"))
        interactions.update(t_bunny2.enable("bunny2_give"))
        interactions.update(t_bunny3.enable("bunny3_give"))
        interactions.update(t_bunny4.enable("bunny4_give"))
        interactions.update(t_bunny5.enable("bunny5_give"))
    jump dream_start

# Quiet Bunny
label bunny1_talk:
    "aaaa flavor text"
    jump dream_start
label bunny1_give:
    "bruh"
    jump dream_start
label bunny1_help:
    "mayb i'll help"
    # code here about debris
    jump dream_start
label bunny1_chat:
    "what's up"
    jump dream_start
label bunny1_time:
    "it's 420 blaze it"
    jump dream_start

# Energetic Bunny (the sick one)
label bunny2_talk:
    "aaaa flavor text"
    jump dream_start
label bunny2_give:
    "No…! NO! I don’t want to take my medicine!"
    dreamSom "Now now… You have to be strong so you can be healthy and play outside."
    dreamSom "Open up~"
    "It… It doesn’t taste all that bad."
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
    jump dream_start
label bunny2_help:
    "i can't help im sick"
    # code here about debris
    jump dream_start
label bunny2_chat:
    "what's up"
    jump dream_start
label bunny2_time:
    "zzz..."
    jump dream_start

# Peevish Bunny
label bunny3_talk:
    "Our little sis hasn’t been feeling well lately, but she’s weak to the taste of medicine so she tries to lie her way out of it. How spoiled!"
    jump dream_start
label bunny3_give:
    "Medicine? Me? I’m not the sick one! Give it to Little Whitney!"
    jump dream_start
label bunny3_help:
    "mayb i'll help"
    # code here about debris
    jump dream_start
label bunny3_chat:
    "what's up"
    jump dream_start
label bunny3_time:
    "it's 420 blaze it"
    jump dream_start

# Studious Bunny
label bunny4_talk:
    "Our parents are really busy so Marchie took up the job to take care of all of us in their stead. I’m the second oldest but recently I’ve been away for school."
    "I hope Marchie is doing alright…"
    jump dream_start
label bunny4_give:
    "Oh are you looking for Little Whitney? She’s an outgoing kid so you’d probably find her somewhere more open."
    jump dream_start
label bunny4_help:
    "mayb i'll help"
    # code here about debris
    jump dream_start
label bunny4_chat:
    "what's up"
    jump dream_start
label bunny4_time:
    "it's 420 blaze it"
    jump dream_start

# Clumsy Bunny
label bunny5_talk:
    "aaaa flavor text"
    jump dream_start
label bunny5_give:
    "C-cherry medicine…?! Oh no thank you, I’m glad I’m not the sick one this time."
    jump dream_start
label bunny5_help1:
    "Oh before that, can I ask for a favor as well?"
    dreamSom "Sure sweetie, what is it?"
    "You see, I wanted to give big sis Marchie a gift for all that she’s done for us."
    "Big sis Marchie’s favorite color is red! But all the flowers here are white…!"
    "I brought some paint earlier, could you help me color 7 flowers?"
    dreamSom "What a lovely idea! We’ll be sure to do that."
    dreamRem "Painting… the flowers?"
    dreamRem "Well I guess it’s the thought that counts."
    python:
        interactions.update(t_bunny5.disable("bunny5_help1"))
        interactions.update(t_bunny5.enable("bunny5_help2"))
        interactions.update(t_flower1.enable("flower1_paint"))
        interactions.update(t_flower2.enable("flower2_paint"))
        interactions.update(t_flower3.enable("flower3_paint"))
        interactions.update(t_flower4.enable("flower4_paint"))
        interactions.update(t_flower5.enable("flower5_paint"))
        interactions.update(t_flower6.enable("flower6_paint"))
        interactions.update(t_flower7.enable("flower7_paint"))
    jump dream_start
label bunny5_help2:
    "There still number of flowers left to be painted"
    jump dream_start
label bunny5_help3:
    " ok I'll help"
    # code here about debris
    jump dream_start
label bunny5_chat:
    "what's up"
    jump dream_start
label bunny5_time:
    "it's 420 blaze it"
    jump dream_start

# magic to flower paint is that the bg will have red flowers and we'll remove the interaction when they're painted
label flower1_paint:
    hide expression flower1.image with Dissolve(0.8)
    $ interactions.complete([t_flower1])
    jump dream_start
label flower2_paint:
    hide expression flower2.image with Dissolve(0.8)
    $ interactions.complete([t_flower2])
    jump dream_start
label flower3_paint:
    hide expression flower3.image with Dissolve(0.8)
    $ interactions.complete([t_flower3])
    jump dream_start
label flower4_paint:
    hide expression flower4.image with Dissolve(0.8)
    $ interactions.complete([t_flower4])
    jump dream_start
label flower5_paint:
    hide expression flower5.image with Dissolve(0.8)
    $ interactions.complete([t_flower5])
    jump dream_start
label flower6_paint:
    hide expression flower6.image with Dissolve(0.8)
    $ interactions.complete([t_flower6])
    jump dream_start
label flower7_paint:
    hide expression flower7.image with Dissolve(0.8)
    $ interactions.complete([t_flower7])
    jump dream_start

# need a check for progress before jumping to dream_start
label check_tasks_progress:
    "aaaa TODO"

label march_continue:
    dreamSom "We did it…! The place looks so much nicer now."
    dreamRem "How is Marcella feeling?"
    Marchie "Urgh and I still have to remember to go there… and pick up that… and call the…"
    dreamRem "There’s more tasks to do?!"
    dreamSom "Remi, look!"
    "To the dismay of the investigative duo, the oppressive atmosphere of debris returned."
    "Undoing all the progress made, the two dream eaters paused to gather their bearings as they became overwhelmed, once more, in the clutter."
    dreamRem "All our hard work…!"
    dreamRem "What could we be doing wrong?"
    dreamSom "Even in the planner, the pages are just getting filled up with more and more scribbles."
    dreamSom "Maybe it’s not the tasks themselves that are the problem…"
    dreamRem "What- So they don’t want our help?"
    # Client "Help…? Why would I need help? These are my responsibilities!"
    # [# Client fades away again]
    dreamRem "Ack! There they go again…!"
    dreamSom "Let’s go Remi, we mustn’t leave them!"
    $ interactions.unlock([t_marcella_end])

label marcella_talk_end1:
    # Client "I-- I can't keep up with this anymore…"
    # Client "My list keeps growing and growing… but the little ones! They're all depending on me!"
    # Bunnies "Big sis! Big sis! We’re hungry…! Hungry!"
    dreamRem "The bunnies here… They’re not acting like the ones from earlier..."
    # [Bunnies that are surrounding Marchie]
    "Big sis… Do you know where my shirt is? It has to be my favorite shirt!"
    # Client "The kids are growing up… and that means their needs are growing too…"
    # Client "I can't let them down but there simply isn't enough time in the world to get all these things done!"
    # Client "I can’t afford to fall asleep, there’s too work much to be done!"
    "Big sis, can we go to the park? No, I want to go to the movies!"
    # Client "Resting now means I'll be wasting my time!"
    "Big sis Marchie is the oldest, so they can do everything!"
    # Client "I HAVE to keep going!!!"
    # [# Client collapses in dream?!]
    dreamSom "Oh dearie. So an issue with cleaning wasn't the problem after all."
    dreamRem "Yes, it seems much deeper than that."
    dreamRem "The root of the issue lies in the sibling bunnies."
    dreamSom "Remerie, how could you! Don't you dare blame these sweet children!"
    dreamRem "I'm not blaming them, I'm just thinking out loud!"
    dreamRem "We have to consider why the bunnies are in the client's worried dreams to begin with."
    dreamRem "Marchie obviously cares a lot about their siblings, but their perception has been warped."
    dreamRem "Our client has been so focused on meeting everyone’s demands that they haven’t had the time to sleep."
    dreamRem "Time…!"
    dreamRem "Somnia, the clocks! Let’s go check on all the clocks!"
    dreamSom "You’re right, there certainly were a lot of clocks in this dream."
    python:
        interactions.unlock([t_clockface1, t_clockface2, t_clockface3, t_clockface4])
        interactions.update(t_marcella_end.disable("marcella_end_talk1"))
        interactions.update(t_marcella_end.enable("marcella_end_talk2"))
    jump dream_start

# Clock under the column on the first page
label clock1_inspect1:
    "minute hand is stuck while hour hand is [t_clockface1.state]"
    jump dream_start
label clock1_up:
    "moved clockhand up"
    $ interactions.update(t_clockface1.updateState("up"))
    jump dream_start
label clock1_down:
    "moved clockhand down"
    $interactions.update(t_clockface1.updateState("down"))
    jump dream_start
label clock1_left:
    "moved clockhand left"
    $interactions.update(t_clockface1.updateState("left"))
    jump dream_start
label clock1_right:
    "moved clockhand right"
    $interactions.update(t_clockface1.updateState("right"))
    jump dream_start

# giant clock on second page
label clock1_inspect2:
    "minute hand is stuck while hour hand is [t_clockface2.state]"
    jump dream_start
label clock2_up:
    "moved clockhand up"
    $interactions.update(t_clockface2.updateState("up"))
    jump dream_start
label clock2_down:
    "moved clockhand down"
    $interactions.update(t_clockface2.updateState("down"))
    jump dream_start
label clock2_left:
    "moved clockhand left"
    $interactions.update(t_clockface2.updateState("left"))
    jump dream_start
label clock2_right:
    "moved clockhand right"
    $interactions.update(t_clockface2.updateState("right"))
    jump dream_start

# first clock on last page
label clock3_inspect3:
    "minute hand is stuck while hour hand is [t_clockface3.state]"
    jump dream_start
label clock3_up:
    "moved clockhand up"
    $interactions.update(t_clockface3.updateState("up"))
    jump dream_start
label clock3_down:
    "moved clockhand down"
    $interactions.update(t_clockface3.updateState("down"))
    jump dream_start
label clock3_left:
    "moved clockhand left"
    $interactions.update(t_clockface3.updateState("left"))
    jump dream_start
label clock3_right:
    "moved clockhand right"
    $interactions.update(t_clockface3.updateState("right"))
    jump dream_start

# second clock on last page
label clock1_inspect4:
    "minute hand is stuck while hour hand is [t_clockface4.state]"
    jump dream_start
label clock4_up:
    "moved clockhand up"
    $interactions.update(t_clockface4.updateState("up"))
    jump dream_start
label clock4_down:
    "moved clockhand down"
    $interactions.update(t_clockface4.updateState("down"))
    jump dream_start
label clock4_left:
    "moved clockhand left"
    $interactions.update(t_clockface4.updateState("left"))
    jump dream_start
label clock4_right:
    "moved clockhand right"
    $interactions.update(t_clockface4.updateState("right"))
    jump dream_start

# check clock progress, clock rings a tune when it's synced
label check_clock_progress:
    "As the final clock struck nine, the sound of gears whirring filled the air."
    "The various clock faces occupying the dream space seemed to react at once, winding their hands with incredible speed."
    "Finally settling at one time, the clock hands began to move in sync, once more. The gentle click of each second echoing through the air was harmonious."
    dreamSom "Remi, take a look! All the clocks are moving again."
    dreamRem "That’s a relief. My hunch was right after all."
    # [Obtain the Clockwork Egg]
    dreamRem "So Marcella had a warped perception of time, which fueled their pressure to keep working at the cost of their sleep."
    dreamSom "Time flies when you’re having fun~"
    dreamRem "I wouldn’t describe our client’s experience as \"fun\"."
    dreamSom "Well, it sounds like dear Marchie needs a good break...fast."
    dreamRem "\"Hah Hah\", but you’re right. And I have just the recipe we need to cook for this dream."
    dreamSom "Ooh, I’m so excited! Then let’s go to the Wishing Kitchen."
    $ finished = True
    jump dream_start

