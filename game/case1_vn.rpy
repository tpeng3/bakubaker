# Case 1
# ------------------------------------------------------------------------
label case1_vn:

    dr """
    On a fresh, early morning day like any other, we begin the story in the quiet corner of {ii}name{/ii}, a modest and cosy bakery.

    The aroma of baked goods fills the store and the alleys, warming anyone who has the pleasure to stop by.

    Should any sleepy lives follow their nose into the bakery, two busy cooks will await them with open arms.
    """

    scene storefront
    show somnia
    u "Hm hmm... Spoonful of sugar hm~♫"
    u "… in a most delightful way~"
    "Ding!"
    u "Remerie~♫ Take a look! The tarts are done."
    r "...In a minute."
    u "I’ll go ahead and set some on the display. Would you like to taste one?"
    show somnia at right with ease
    show remi at left
    r "Later, please. I- Mmrph!"
    r "Mmrrph! Mmrhh nmrph!"
    u "How is it?"
    r "{i}Somnia{/i}! That's hot!"
    r "I can grab my own, you know?"
    s "Do you think maybe I used too much jam?"
    r "...No, it was good. The sweet jam you used was less watery this time, so the tart crust held together well."
    s "I see. I'm glad they turned out better this time!"
    s "I can always count on your sharp palate for tasting, {i}Remi{/i}~."
    r "Well, o-of course...!"
# TODO thinking character definition
    # r "I can’t say no to Somnia’s desserts!"
    r "H-how about we open the shop now if you’re all done baking."
    s "Yupp~ I’ll go flip the sign outside."
    s "Hmmm hm~ ♫"
    s "Hm~ A merry tune to toot- AH!"
    r "What’s wrong?"
    # Client is passed out on the floor in front of the store
    s "There’s a person fallen over outside."
    s "Oh dear, are you okay?"
    r "We can’t have bodies blocking the door for potential customers."
    "Hrn…"
    r "Are they… dea-"
    u "I-I’m alive… snore..."
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
    u "Uh… Let’s see… Would you happen to know a cafe around here called {ii}cafe name{/ii}."
    "..."
    s "Welcome!"
    r "...Welcome."
    s "We’re technically not open yet, but is there anything we can get started for you?"
    u "Yes, I heard rumors that the shop recently opened again."
    u "It’s been what, 5 years? It’s been so long I could hardly contain my *yawn* excitement…"
    # s "Five years... what would they happen to know?"
    u "Let’s see now… I’ll have… this cherry tart and the…"
    u "...{ii}Egg pudding pasta with strawberry chives.{/ii}"
    # Somnia and Remerie both perk up with a !
    u "T-that’s the special menu item of the day, right?"
    s "Yes, you are correct."
    r "Would you like your order for here or to go?"
    u "For… here."
    r "Alright. Luckily there's still a half hour before the store opens proper so we have time to fulfill your request."
    s "Kind sir, please follow us to the back~"
    u "Alright…"

    scene dreamoffice
    dr """
    Through the back of the store, and only a short few feet away from the kitchen, was an intimate, deep-colored room.

    The dimly lit office housed a bed as its centerpiece, a decorative mirror to taste, and a long olden cabinet.

    Shutting the door behind them, the three guests, enveloped in the velvety deep, began.
    """

    u "This place…!"
    u "Wow, it looks much more different than what I remember."
    r "Welcome to the {ii}Dream Service{/ii}. Here, we specialize in investigating strange sleep patterns and behavior."
    r "Tell us, what ails you?"
    u "Um.. Is {ii}Madam{/ii}... present?"
    s "... Oh! Um..."
    s "Unfortunately, she is currently away on a trip. We are her apprentices who’ll be taking care of the store while she’s gone."
    r "I'm Remerie, dreams specialist."
    s "And I'm the connoisseur of nightmares, Somnia!"
    u "Pleasure to meet you two, I'm {ii}Marcella Lapin{/ii}."
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

    # dreamSom neutral "Woah…!"
    # dreamRem neutral "I've got you. Watch your step, it's a mess in here."
    # dreamSom "Our client must really have a hard time arranging their thoughts..."
    # dreamRem "Sounds like someone I know."
    # dreamRem "Don’t think I didn’t catch you this morning rearranging our already labeled pastry display!"
    # dreamSom "Aww, but it looks better when it’s arranged by jam color!"
    # dreamRem "*Sigh* Anyways, we need to find our client. Where are they?"
    # # [Client fades into appearance on the first screen]
    # ml "Oh no, I’m late. I’m late! I have to hurry!"
    # ml "This assignment is due... and I have to fill out the report for... oh, I need to pick up the..."
    # dreamSom "Oh, there they are, practically up to their nose in paperwork!"
    # dreamRem "The client can’t see us in their dream, but let’s tail them."


    # [Rabbit client is still on the first screen, player should learn to click on them.]
    # Client "...And there's the kids' practice... I need to arrange the bouquet... class has been cancelled but..."
    # [--but the client fades/rushes off screen and a line of bunnies fade in and cross their path]
    #
    # r "Darn, they're too fast...!"
    # r "What’s with these bunnies?!"
    # s "Ooh, they are so cute!!"
    # r "Now what? We can't start cooking, much less start collecting ingredients in this condition."
    # s "How about we take a look around? Maybe we can learn something from these adorable dream whip cream fluffles~"
    #
    # Plot relevant Interactables
    # There are a number of essential objects (items that reveal client's situation) to be interacted with
    # (non plot relevant interactions flavor text will be in the interactables doc)
    #
    # Line of bunnies:
    # > Talk to bunnies (Somnia):
    # 	s "Hi there cuties! Would you mind letting us pass? We have an important mission and need to speak with our client up ahead."
    # 	Bunnies: "Mission? Mission…! Do you know big sis Marchie? So cool!!
    # 	s "We sure do! Your older sister asked us for help, and I’ll need your assistance in order to help them."
    # 	Bunnies: "Marchie’s the greatest! They do so much! They’re the hardest worker ever!"
    # 	Bunnies: "We’re gonna work hard too! Let’s support big sis!"
    # 	[Bunnies fade out/move out of the way and right arrow gets unlocked]
    # 	[Get ingredient: bunny-cut apples]
    # As the bunnies left, a bundle of clouds manifested itself along the path of the two intrepid dream eaters. A shape that came out to be...
    # [Dream apple close up shot?]
    # ...A selection of apple slices, daintily cut in the shape of bunnies.
    # r "Our first ingredient is freshly cut apples?"
    # s "Oooh, I wonder if we get to bake a pie with this!"
    # r "We'll just have to see what we got to work with as we find other ingredients."
    # s "I'll pocket this sweet snack for now, thank you very much~"
    #
    # > Talk to bunnies (Remerie):
    # 	r "Hey… Can you move aside?"
    # 	Bunnies: "...Move? Why? Who are you?"
    # 	r "It’s… not important. But you guys are in the way."
    # 	Bunnies: "...We don’t wanna. Say no to strangers!"
    # 	r (...This is why I’m no good with talking to kids.)
    # 	s "Aww cheer up, Remi. How about I give it a go?"
    #
    # Strawberry:(purple text for the optional stuff, on the first screen)
    # 	r "The moon looks awfully peculiar… Is that a strawberry?!"
    # 	s "Could it be? An ingredient? Let’s extract it!"
    # Remerie watched as Somnia reached out her hand and carefully plucked the strawberry out of the night sky.
    # [Get Creamy Strawberry!]
    #
    #
    # [After getting past the line of bunnies, the client is in view again but behind the pile of debris, the image doesn’t do the amount of actual debris needed justice]
    #
    # u "And I have to find my report… and buy the medicine for little Whitney... Oooh and this whole place has been a mess!"
    # r "Marcella sure has a lot on their plate."
    # s "Then perhaps we can help them out!"
    # s "Let’s see… they’re looking for their report… trying to give medicine to their little sister… Oh! And they want to clean up this entire area!"
    # r "That last task sounds like a bit of a handful…"
    # s "Oh come on Remi, it’ll be fun! After all ~🎶, spoonful of sugar-"
    # r "...Helps the medicine go down, I know. It’s your favorite song. Let's just get to work."
    #
    # Report (found back on the first page, the red book):
    # 	s "Could this be the report Marcella was looking for?"
    # 	r "I don’t think this looks to be a report as much as it is a… planner?"
    # 	s "Wow, look at this calendar, it’s been filled to the brim with events!"
    # 	r "How could you tell? All the pages are a complete mess!"
    # 	r "I can’t even read the handwriting!"
    # 	r "I guess even in a dream, our client doesn’t feel very organized with their life."
    # 	s "Let’s return the planner to Marcella after we finish the other tasks."
    #
    # Mounds of Papers (found all around the second page, this might be a bit of effort, but it’d be nice if like, there are several versions of debris piles several times and progression is when the pile fades into an image of a smaller debris pile)
    # 	> Clean up Debris
    # 		r "Urk… The client’s going to be awake by the time we clean through this mess."
    # 		s "How about we ask Marchie’s little siblings to help out?"
    # 		r "Well, it’s definitely worth a shot."
    # 		(unlocks option for bunnies to "Ask for Help")
    # 		r "Hang on, there's a blue book in the pile of random papers…"
    # 		s "There's a name written inside- 'Rosie'."
    # 		r "Do you think that's one of the bunnies' names?"
    # 		s "Cute! We should hang on to it, just in case."
    #
    # Medicine (found on the second page next to client):
    # 	s "This looks to be the medicine we have to give to Marcella's sister. The label says "Drink Me"."
    # 	r The question is… which of their siblings need a dose?"
    # 	s "I guess we’ll just have to go around and ask!"
    # 	r "I’ll… let you do the talking."
    # [Obtained Cherry Medicine, fake ingredient ajfkle;jwt]
    #
    # [after bunnies dispersed, they spreaded out to different parts of the map. I would say there’s like 5 bunnies. Player has to talk to each of them to deduce which rabbit is the correct sibling.]
    #
    # Bunny1: (first page, leftmost near where the two entered the dream):
    # 	> Talk to Bunny
    # 		r "Hey."
    # 		"..."
    # 	r "..."
    # 		r "Can they not hear me?"
    # 	s "They look like they're occupied in trying to find something…"
    # 	"I can't find my favorite book…"
    # r "A blue book, huh."
    # (convo ends if you dont have the book)
    # 	> Give the Medicine
    # 		"Hm? I don't need medicine."
    # 		"I need to find my favorite book…"
    # 	> Ask for help
    # 		s "Big sis sneeds some help with cleaning, would you mind helping?"
    # 		"..."
    # 		s "..."
    # 	"I can't find my favorite book…"
    # 		"It's blue and has my name on the inside…"
    # 			if no book: bunny convo ends
    # 			if book:
    # s "Hello Rosie, is this what you're looking for?"
    # "Oh! Oh yes!"
    # "Yay! You saved the day!"
    # "Whitney has to go to bed early tonight- she needs to get her rest."
    # "She would have been so sad if I couldn't read her favorite stories before bed…"
    # r "Could've just asked for our help instead of ignoring me."
    # s "Oh, Remi don't be so grumpy!"
    # r "I-I'm not..."
    # 		"Okay, since you helped me find my book, I'll help clean up!"
    #
    #
    # Bunny2: (first page, next to the clock column)
    # 	> Talk to Bunny
    # 		"Wheee! Wheeeee!"
    # 		s "That little one is going to get hurt, jumping around like that…!"
    # 		r "I'm sure she knows what she's doing."
    # 		"Whee- OUCH!"
    # 		r "OW! Watch it!"
    # 		s "Oh, sweetie, slow down and please be careful!"
    # 		"I'm fine! Hehe, wheee!"
    # 		s "Oh dear…"
    # 		r "That kid felt kind of… hot."
    # 		s "Hot? Could they be running a fever…?"
    # 	> Give the Medicine
    # 		s "Little Whitney? I heard someone's not feeling good and needs to take her medicine."
    # 		"No…! NO! I don’t want to take my medicine!"
    # 		s "Now now… You have to be strong so you can be healthy and play outside."
    # 		s "Open up~"
    # 		"It… It doesn’t taste all that bad."
    # 		s "See? What a good girl! I hope you feel better soon."
    # 		"Thanks, lady!"
    # 		r "...Let me guess, you added some sugar."
    # 		s "Hmmm hm~ ♫"
    #
    # Bunny3(second page, right below the giant clock near the client)
    # 	> Talk to Bunny
    # 		"Our little sis hasn’t been feeling well lately, but she’s weak to the taste of medicine so she tries to lie her way out of it. How spoiled!"
    # 	> Give the Medicine
    # 		"Medicine? Me? I’m not the sick one! Give it to Little Whitney!"
    # 	> Ask for help
    # 		s "Hello,
    # 		"Hmph… If it helps big sis Marchie out…"
    # 		[Debris pile pic changes to something smaller]
    #
    # Bunny4:(second page, top right corner, the image has two bunnies but change it to just one)
    # 	> Talk to Bunny
    # 		"Our parents are really busy so Marchie took up the job to take care of all of us in their stead. I’m the second oldest but recently I’ve been away for school."
    # 		"I hope Marchie is doing alright…"
    # 	> Give the Medicine
    # 		"Oh are you looking for Little Whitney? She’s an outgoing kid so you’d probably find her somewhere more open."
    # 	> Ask for help
    # 		"Why yes, I’d love to help if that would be okay!"
    # 		[Debris pile pic changes to something smaller]
    #
    # Bunny5:(second page, bottom near the stacks of paper)
    # 	> Talk to Bunny
    # 		"[something about marchie]
    # 	> Give the Medicine
    # 		"C-cherry medicine…?! Oh no thank you, I’m glad I’m not the sick one this time."
    # 	> Ask for help (1)
    # 		"Oh before that, can I ask for a favor as well?"
    # 		Somnia "Sure sweetie, what is it?"
    # 		"You see, I wanted to give big sis Marchie a gift for all that she’s done for us."
    # "Big sis Marchie’s favorite color is red! But all the flowers here are white…!"
    # "I brought some paint earlier, could you help me color 7 flowers?"
    # s "What a lovely idea! We’ll be sure to do that."
    # Remerie "Painting… the flowers?"
    # Remerie "Well I guess it’s the thought that counts."
    # 	> Ask for help (2)
    # 		"Have you found all the flowers? There should be [number of flowers] left."
    # > Ask for help (3)
    # 	"Wah, it’s so pretty!"
    # 	Somnia "I’m sure your big sis Marchie would love the present."
    # 	"Thank you! I’ll help clean up now."
    # [Debris pile pic changes to something smaller]
    # [also player gets Fine Herbs]
    #
    # Scattered Flowers (found all around the first and second page. Flowers are littered around the first (3) and second (4) page. Used for bunny sidequest)
    # 	> Paint the Rose
    # 		[flower just fades from white to red, and the interactable gets removed from the list, there’s no dialogue needed.]
    #
    # (if player clicks on marchie anytime before completing all three tasks)
    # Marcella: "And I have to do this… and don’t forget that… Oh and I need to…"
    # r "Looks like Marcella’s frozen in their thoughts."
    #
    # (when all three tasks are complete and the player is on the second page)
    # -- pause investigation --
    # s "We did it…! The place looks so much nicer now."
    # r "How is Marcella feeling?"
    # Marchie: "Urgh and I still have to remember to go there… and pick up that… and call the…"
    # r "There’s more tasks to do?!"
    # s "Remi, look!"
    # To the dismay of the investigative duo, the oppressive atmosphere of debris returned.
    # Undoing all the progress made, the two dream eaters paused to gather their bearings as they became overwhelmed, once more, in the clutter.
    # r "All our hard work…!"
    # r "What could we be doing wrong?"
    # s "Even in the planner, the pages are just getting filled up with more and more scribbles."
    # s "Maybe it’s not the tasks themselves that are the problem…"
    # r "What- So they don’t want our help?"
    # Client "Help…? Why would I need help? These are my responsibilities!"
    # # [Client fades away again]
    # r "Ack! There they go again…!"
    # s "Let’s go Remi, we mustn’t leave them!"
    #
    # [Right arrow gets unlocked for the third page]
    #
    # (sand r sees the client stuck on top of the tower in confusion, what does this all mean?!)
    # [narrator text..?]
    #
    # [Finally close enough, the client's thoughts can be heard more clearly]
    # Client "I-- I can't keep up with this anymore…"
    # Client "My list keeps growing and growing… but the little ones! They're all depending on me!"
    # Bunnies: "Big sis! Big sis! We’re hungry…! Hungry!"
    # r "The bunnies here… They’re not acting like the ones from earlier..."
    # [Bunnies that are surrounding Marchie]
    # 	"Big sis… Do you know where my shirt is? It has to be my favorite shirt!"
    # Clien "The kids are growing up… and that means their needs are growing too…"
    # Client "I can't let them down but there simply isn't enough time in the world to get all these things done!"
    # Client "I can’t afford to fall asleep, there’s too work much to be done!"
    # 	"Big sis, can we go to the park? No, I want to go to the movies!"
    # Client "Resting now means I'll be wasting my time!"
    # 	"Big sis Marchie is the oldest, so they can do everything!"
    # Client "I HAVE to keep going!!!"
    # [Client collapses in dream?!]
    # s "Oh dearie. So an issue with cleaning wasn't the problem after all."
    # r "Yes, it seems much deeper than that."
    # r "The root of the issue lies in the sibling bunnies."
    # s "Remerie, how could you! Don't you dare blame these sweet children!"
    # r "I'm not blaming them, I'm just thinking out loud!"
    # r "We have to consider why the bunnies are in the client's worried dreams to begin with."
    # r "Marchie obviously cares a lot about their siblings, but their perception has been warped."
    # r "Our client has been so focused on meeting everyone’s demands that they haven’t had the time to sleep."
    # r "Time…!"
    # r "Somnia, the clocks! Let’s go check on all the clocks!"
    # s "You’re right, there certainly were a lot of clocks in this dream."
    #
    # (if you talk to any of the bunnies in the previous pages, variations of the following)
    # 	"Eh? What time is it? It’s exactly 9 o’ clock! An hour before bedtime!" (and so and so variations)
    # 	"What time is it? Um… the longer needle is the minute hand so it’s… 9 o’ clock!"
    # 	"It’s 9 o’clock, my younger siblings should be going to bed around now."
    #
    # Clockface3 (page 3… just somewhere on page 3):
    # 	> Inspect the Clock(first time)
    # 		r "The position of this clock is different from the other one in the room."
    # 		s "The numbers and ticks seems to be missing, I wonder how we can tell the time?"
    # 		r "Hm… the minute hand’s not moving… I think it’s stuck. Oh! But it looks like I can move the hour hand."
    # 		r "Nothing seems to happen when I do, though."
    # 		s "Let’s check the other clocks too."
    # 	> Inspect the Clock
    # 		"A large clock something something flavor text after seeing the clock drawn"
    # 		"The hour hand is facing up, while the minute hand is stuck to the right."
    # 	> Move the Hour Up (correct answer)
    # 		"Remerie adjusts the clock."
    # 		"The hour hand is facing up, while the minute hand also faces up.."
    # 	> Move the Hour Left
    # "Remerie adjusts the clock."
    # 		"The hour hand is facing up, while the minute hand faces left."
    # 	> Move the Hour Right
    # "Remerie adjusts the clock."
    # 		"The hour hand is facing up, while the minute hand faces right."
    # 	> Move the Hour Down
    # "Remerie adjusts the clock."
    # 		"The hour hand is facing up, while the minute hand faces down."
    #
    # Clockface4 (page 3… just somewhere on page 3):
    # 	> Inspect the Clock (first time)
    # 		r "There’s also no numbers on this clock. And the minute hand is stuck."
    # 		s "Maybe we need to get all the clock’s time to match up..."
    # 		r "How can we do that if we can’t move the minute hand?"
    # 		s "We’ll figure it out, Remi! There has to be a way!"
    # 	> all other actions are similar to the one for clockface3
    # 		The answer would be move hour down, since minute hand is facing left.
    #
    # Clockface1 (page 2, the large one):
    # 	> all other actions are similar to the other for clockface3
    # 		The answer would be move hour right, since minute hand is facing down.
    #
    # Clockface2 (page 1, the small one on the column, we should erase the clock that’s on the second column since the player wouldn’t be able to click on it):
    # 	> all other actions are similar to the one for clockface3
    # 		The answer would be to move hour left, since minute hand is facing up.
    #
    # As the final clock struck nine, the sound of gears whirring filled the air.
    # The various clock faces occupying the dream space seemed to react at once, winding their hands with incredible speed.
    # Finally settling at one time, the clock hands began to move in sync, once more. The gentle click of each second echoing through the air was harmonious.
    # s "Remi, take a look! All the clocks are moving again."
    # r "That’s a relief. My hunch was right after all."
    # [Obtain the Clockwork Egg]
    # r "So Marcella had a warped perception of time, which fueled their pressure to keep working at the cost of their sleep."
    # s "Time flies when you’re having fun~"
    # r "I wouldn’t describe our client’s experience as "fun".”
    # s "Well, it sounds like dear Marchie needs a good break...fast."
    # r ""Hah Hah", but you’re right. And I have just the recipe we need to cook for this dream."
    # s "Ooh, I’m so excited! Then let’s go to the Wishing Kitchen."
    # [kitchen icon gets unlocked in the top left or right corner]
    #
    # [BEGIN dream cooking]
    #
    # (cooking minigame)
    # Tutorial about how to cooking the essences from the dream into a dish
    # s "What are you planning to make Remi?"
    # r "What better way to start the morning than with a tasty omelette plate?"
    # r "The Clockwork Egg will be our centerpiece."
    # r "We’ll need to use other ingredients extracted from the dream as well. So I would say…"
    # [Cooking meter/goal appears]
    # r "We’ll need to reach this amount to succeed. Cooking is a delicate balance after all."
    # r "Soms, you’ll help won’t you?"
    # 	[Not sure if we wanna add the scripted mess up BUT-]
    # s "Certainly! How about adding this?"
    # r "D-did you take one of the client's siblings from the dream?!"
    # s "They were soooo cute! Oh, I just couldn't help myself..."
    # s "Look-! Hm? Wait, it's just a dust bunny from all the cleaning we did..."
    # r "I'm not sure whether to be relieved or concerned."
    # [Obtained Cinnamon Spice]
    # s "How about we make some Cinnamon Scrambled Eggs!"
    # [Poofs the attribute meters into bonkers positions]
    # s "Of course! Let’s take a look through our ingredients~"
    #
    # -- start cooking game, player can also go back to the dream and yea--
    #
    # If player gets the combo, Somnia gets sparkly and (!) appears, if the player clicks on it, there’s a short cutout of Somnia doing a cooking smash skill.
    # 	SOMNIA’S [special attack name]
    # s "There we go~"
    # r "Hey! Somnia, you need to be sticking to the recipe! That’s not how cooking works!"
    # s "Whoops, I got too excited- this Creamy Strawberry was just begging to be a part of the dish!"
    # s "But Remi look~ Doesn’t the omelette look so much cuter now?"
    # r "...It does. But warn me next time when you go about one of your whims…"
    # s "Remi’s so nice."
    # r "C-come on, let’s finish up if the dish is done."
    #
    # [DREAM DISH]:
    # Regular dish: egg, fine herbs, bunny cut apples
    # Fluffy Omelette with Fruit
    # Special dish: egg, fine herbs, bunny cut apples, strawberries??
    # Creamy Omelette with Smooth Fruit Yoghurt (food words??? hard??)
    #
    # Good
    # s "Pretty good! Could use some more pep and zing though."
    # r "This looks serviceable."
    # Great
    # s "Such a dreamy looking dish! I almost don't want to eat it…"
    # r "Not bad at all. Next time I'll be expecting more."

    scene black

    window hide
    centered "Investigation happens"
    centered "Cooking happens"
    window auto

    with Pause (1.0)
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
    # if cooking is perfect:
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
