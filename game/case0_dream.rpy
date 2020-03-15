label tina:
    menu:
        "Dream Investigation":
            jump case0_dream
        "Hell's Kitchen":
            jump case0_cook

label case0_dream:
    python:
        case = "case0"
        bg = "wonderland2" # background image
        page_width = 1720 # screen page width
        total_pages = 3 # total pages in investigation
        unlocked_pages = 2 # default is 0 but set to 2 for testing purposes
        inventory = Inventory()
        # itr_list = [t_client, t_clocktower, t_strawberry] # starting interactions, it should actually be blank for case0
        interactions = Interactions(itr_list)

        finished = True # default is false, but true for testing

    scene black
    "Case 1 (tutorial) dream"
    show screen dream()
    jump dream_start1

label case0_enter:
    dreamSom "Woah…!"
    dreamRem "Geez, it's a mess in here."
    dreamSom "Our client must really have a hard time arranging their thoughts..."
    dreamRem "Sounds like someone I know."
    dreamRem "Don’t think I didn’t catch you this morning rearranging our already labeled pastry display!"
    dreamSom "Aww, but it looks better when it’s arranged by jam color!"
    dreamRem "*Sigh* Anyways, we need to find our client. Where are they?"
    show expression t_marcella_start.image with Dissolve(0.8)
    $ interactions.unlock([t_marcella_start])
    # [Client fades into appearance on the first screen]
    # Client "Oh no, I’m late. I’m late! I have to hurry!"
    # Client "This assignment is due... and I have to fill out the report for... oh, I need to pick up the..."
    dreamSom "Oh, there they are, practically up to their nose in paperwork!"
    dreamRem "The client can’t see us in their dream, but let’s tail them."
    jump dream_start

label marcella_talk_start:
    Client "...And there's the kids' practice... I need to arrange the bouquet... class has been cancelled but..."
    hide expression t_marcella_start.image with Dissolve(0.8)
    show expression t_bunnysquad.image with Dissolve(0.8)
    $ interactions.complete([t_marcella_start])
    $ interactions.unlock([t_bunnysquad])
    Rem "Darn, they're too fast...!"
    Rem "What’s with these bunnies?!"
    Som "Ooh, they are so cute!!"
    Rem "Now what? We can't start cooking under these conditions..."
    Som "How about we take a look around? Maybe we can learn something from these adorable dream whip cream fluffles~"
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
    Rem "Our first ingredient is freshly cut apples?"
    Som "Oooh, I wonder if we get to bake a pie with this!"
    Rem "We'll just have to see what we got to work with as we find other ingredients."
    Som "I'll pocket this sweet snack for now, thank you very much~"
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
    "Remerie watched as Somnia reached out her hand and carefully plucked the strawberry out of the night sky."
    # [Get Creamy Strawberry!]
    $ inventory.add(c_strawberry)
    jump dream_start

label marcella_talk_mid:
    # Client: "And I have to find my report… and buy the medicine for little Whitney... Oooh and this whole place has been a mess!"
    dreamRem "Marcella sure has a lot on their plate."
    dreamSom "Then perhaps we can help them out!"
    dreamSom "Let’s see… they’re looking for their report… trying to give medicine to their little sister… Oh! And they want to clean up this entire area!"
    dreamRem "That last task sounds like a bit of a handful…"
    Som "Oh come on Remi, it’ll be fun! After all ~🎶, spoonful of sugar-"
    Rem "...Helps the medicine go down, I know. It’s your favorite song. Let's just get to work."
    $ interactions.unlock([t_report, t_debris4, t_medicine, t_bunny1, t_bunny2, t_bunny3, t_bunny4, t_bunny5])
    jump dream_start


