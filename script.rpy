# This is the main script called upon when a new game is selected

# Define characters
define mae = Character("Mae", color="#ff3f54")
define bea = Character("Bea", color="#4f7175")
define gregg = Character("Gregg", color="#e8971a")
define angus = Character("Angus", color="#6fbc92")
define lori = Character("Lori", color="#c1e0fc")
define germ = Character("Germ", color="#a384e5")
define selma = Character("Selmers", color="#d15384")
define narrator = Character("")
define player = Character("Wayfarer")
define candy = Character("Candy")
define stan = Character("Stan")
define name = Character("Avery")
define cafebird = Character("Trish")
define loriunknown = Character("???", color="#c1e0fc")
define maeunknown = Character("???", color="#ff3f54")
define selmaunknown = Character("???", color="#d15384")
define trishunknown = Character("???")
define trish = Character("Trish")
define greggunknown = Character("???", color="#e8971a")
define beaunknown = Character("???", color="#4f7175")
define angusunknown = Character("???", color="#6fbc92")
define harleyunknown = Character("???")
define harley = Character("Harley")
define receptionist = Character("???")
define marcie = Character("Marcie")
define kid = Character("Kid")
define cashier = Character("Cashier")
define pa = Character("PA")
define raccoon = Character("Raccoon")
define danny = Character("Danny")
define citycouncil1 = Character("City Council 1")
define citycouncil2 = Character("City Council 2")
define citycouncil3 = Character("City Council 3")
define citycouncil4 = Character("City Council 4")
define saleem = Character("Saleem")
define sadie = Character("Sadie")
define man = Character("Man")
define madamespectre = Character("Madame Spectre")


label start:

    # variables and definitions

    $ currentDate = "December 1"
    $ currentDay = 1
    $ gender = ""

    # keeps track of how much the characters like the player (AP = affinity points)
    $ maeAP = 0
    $ beaAP = 0
    $ greggAP = 0
    $ angusAP = 0
    $ loriAP = 0
    $ selmaAP = 0
    $ germAP = 0

    # personality values. they correspond to defining traits of each character and act as a secondary way to appeal to them. unlocks some dialogue options.
    #lori
    $ timid = 0

    #gregg
    $ bold = 0
    
    #germ
    $ sympathetic = 0
    
    #bea
    $ cynical = 0
    
    #mae
    $ rebellious = 0
    
    #angus
    $ gentle = 0
    
    #selma
    $ mature = 0

    # scene specific variables
    $ beenToChurch = False
    $ chosendrink = ""
    $ wentWithGregg = ""
    $ confectionChoice = "treat"
    $ loriInteractionRude = False
    $ loriInteractionNull = False
    $ loriInteractionBold = False
    $ loriInteractionNotBold = False
    $ loriInteractionNeutral = False
    $ firstWander = True
    $ audiencepoet = ""
    $ selmaNeutral = False
    $ selmaGood = False
    $ selmaBad = False

    # Scene completion status (as in, has the player experienced this scene on their playthrough)
    $ beaSelmaPoetryCompleted = False
    $ maeLoriSleepoverCompleted = False
    $ maeChurch1Completed = False
    $ maeLoriSleepoverCompleted = False
    $ beaAntiqueCompleted = False
    $ workingWithBeaCompleted = False
    $ angusTownCompleted = False
    $ greggTownCompleted = False
    $ selmaLibraryReadingCompleted = False
    $ loriFilmCompleted = False
    $ dragonsDungeons1Completed = False
    $ artsCouncilCompleted = False

    # note: if you want to quickly test a scene, put "jump [sceneName]" right below this line



    ####################
    
    # Start day 1 (technically 2nd day in possum springs, you arrived the night of nov 29)
    #november 30 2022 (2017 nitw release date + 5 years) (wednesday)

    scene bg black with fade

    play music "music/americano_loop.mp3" fadein 1.0

    scene bg cafe with dissolve

    play sound "sound/storebell.mp3"

    "Finally, you made it."
    "A bell on the door chimes as you walk into a cozy little cafe."
    "The sign on the door read:\nPosspresso\nEST. 2020"
    "The smell of roasted coffee beans guided you from a block away."
    "You brush the snow off your jacket and take a moment to bask in the warmth."
    "While fairly clean and new looking, the place has a rustic country charm to it."
    #finally a modern cafe in possum springs!
    #"It's the only one in Possum Springs if that map you got from the bus station is to be believed."
    #running joke about how every door in possum springs has a bell, even people's residences surprisingly ("it's just for the holidays. it's festive!")
    "Hardwood flooring, homely wallpaper, a chalkboard menu, the works."
    "Crude paintings adorn the walls, no doubt bought on the cheap from local artists."
    "There's even a large picnic table occupies the center of the room."
    "How did they even fit that through the door, you wonder?"
    "Behind the counter, a young bird lady with brick red feathers smiles and waves at you."

    show trish neutral at center with dissolve

    trishunknown "Hi there! I'll be with you in just a minute!"
    
    hide trish with dissolve

    "She's busy helping another customer at the moment, giving you time to look over the menu."
    "There's a variety of breakfast-y food and drinks to choose from as well as some sweets."

    show trish neutral at right
    show selma neutral flip at left:
        yalign selmaheight
    with dissolve

    selmaunknown "Hmm, I'm feelin' a salted caramel mocha today."

    trishunknown "Ya want whipped cream on top?"

    selmaunknown "Hell yeah."

    trishunknown "Hahaha will that be all for you, Selmers?"

    selma "Throw in a cinnamon roll too please."
    
    trishunknown "Alright, that'll be... seven dollars and eighty five cents!"

    #trishunknown "Alright, that'll be... six dollars and sixy six cents!"
    
    #selma "What a lucky number..."
    
    #trishunknown "Hahaha I know, right? Hopefully it's not like a bad omen or something!"

    "The bear pulls a crumpled $10 bill out of her pocket and slides it over."

    selma "Keep the change."

    trishunknown "Thank you very much!"

    hide selma with dissolve
    
    show trish at center with move

    "The bear steps aside and the barista looks over to you."

    trishunknown "Ain't seen you around before!"
    trish "Welcome to Posspresso! You can call me Trish!"
    trish "Have you decided what you'd like?"

    menu:
        "{cps=0}I'll have uh...{/cps}"
        "What she had":
            $ selmaAP = selmaAP + 1
            $ chosendrink = "mocha"
            "You order the same thing Selmers got, with the addition of a strawberry waffle to fill your belly."
        
        "Posspresso Special":
        #surprise me
            $ bold = bold + 1
            $ chosendrink = "posspressospecial"
            "You order the Posspresso Special. There's no description for it, but you wanted to try something new and local."
            "You also get an everything bagel with cream cheese to go along with it."

        "Americano":
            $ cynical = cynical + 1
            $ chosendrink = "americano"
            "You order an americano and a blueberry bagel with honey butter spread to go along with it."
            "Gotta have something sweet to balance out the bitterness."

        "You're not sure...":
            $ timid = timid + 1
            $ chosendrink = "cappuccino"
            "You can't really decide. The barista suggests a cappuccino. You can't really argue but you order a chocolate chip waffle to go along with it."

    trish "Oki doki!"

    "The barista taps the tablet a few times and reads out your total."
    "Seeing that you've got your debit card ready, she turns the machine around over to you. You swipe your card and hit confirm."
    "It asks if you would like to give a tip."
    
    menu:
        "15%":
            $ sympathetic = sympathetic + 1
            "A standard tip for standard service. Gotta pay the \"Please don't spit in my coffee" tax."
        "30%":
            $ gentle = gentle + 1
            "Eff it, you're feeling generous today. She'd probably enjoy the extra cash more than you."
        
        "No tip":
            $ rebellious = rebellious + 1
            "The barista is just doing what's expected of her job, right? It's her employer's responsibility to pay her, not you."
            "Right?"

    trish "And can I get a name for you?"

    $ povnameValid = False
    $ player = Character("[name]")
    jump namescript1
    label namescript1:

        python:
            povname = renpy.input("Oh shoot, what's your name again?", length = 14)
            povname = povname.strip()
            povnameValid = True
            # prevents the player from naming themselves certain names and names them Avery if nothing is input
            if povname.upper() == "MAE":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "MARGARET":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "BEA":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "BEATRICE":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "GREGG":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "GREG":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "ANGUS":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "GERM":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "JEREMY":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "LORI":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "SELMA":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "SELMERS":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "STAN":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "CANDY":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "TRISH":
                "Choose another name."
                povnameValid = False
            if povname.upper() == "MARCIE":
                "Choose another name."
                povnameValid = False
            if not povname:
                #default name in case you don't type anything
                povname = "Avery"
                povnameValid = True

        if povnameValid == True:
            "Your name is [name]?"
        else:
            "Choose another name."
            jump namescript1
            "Your name is [name]?"

    menu:
        "{cps=0}Your name is [name]?{/cps}"
        "That's right":
            player "That's right!"
        "That's wrong":
            jump namescript1

    trish "Alright, I'll have that ready for y'all in just a minute!"

    hide trish with dissolve

    "That bear girl already found a table and was busy plugging a laptop into a nearby power socket."
    "You quietly find a place to sit by a window, looking out at the blinding white landscape."
    "The past few days have been really chaotic. It's nice to slow down for a moment and relax. How did you wind up here again?"
    #"Come on, there was something really important you were gonna do today, what was it?"
    #"You decide to retrace your steps leading up to you coming to the cafe. Maybe that will jog your memory."
    
    #make this trip just about getting wifi but you decide to get groceries while you're out after checking your map app and seeing what's nearby

    "Let's see... You woke up this morning freezing."
    "Winter decided to come early this year. You heard there was a blizzard on its way and true enough it's been snowing nonstop since you arrived in Possum Springs last night."
    "You thought you turned on the heater before bed but your new home was colder than the innermost circle of hell when you got up."
    "The first thing you did was take a hot shower."

    scene bg bathroomfoggymirror with fade
    play music "music/Distant.mp3" fadein 1.0

    "Steam cascades throughout the room after a lengthy shower, fogging up the mirror. You wipe some of it off and admire your glistening..."

    # scene bg bathroomclearmirror with dissolve

    #"After getting dressed you wipe the mirror clean, only getting a brief glance at yourself before it fogs up again."
    
    menu:
        "{cps=0}Steam cascades throughout the room after a lengthy shower, fogging up the mirror. You wipe some of it off and admire your glistening...{/cps}"
        "Scales":
            $ animaltype = "reptile"
            "...scales. Because you're a reptile, of course."
        "Fur":
            $ animaltype = "mammal"
            "...fur. Because you're a mammal, of course."
        "Feathers":
            $ animaltype = "bird"
            "...feathers. Because you're a bird, of course."
            
    "You wipe away the moisture with a towel and take a closer look in the mirror."
    "How would you describe yourself?"

    menu:
        "{cps=0}How would you describe yourself?{/cps}"
        "A masculine wreck":
            $ gender = "masculine"
            $ heshethey = "he"
            $ guygirlperson = "guy"
            $ hishertheir = "his"
            $ hisherstheirs = "his"
            $ himherthem = "him"
            "Yeah, you lean on the masculine side."
        "A feminine wreck":
            $ gender = "feminine"
            $ guygirlperson = "girl"
            $ heshethey = "she"
            $ hishertheir = "her"
            $ hisherstheirs = "hers"
            $ himherthem = "her"
            "Naturally , you lean on the feminine side."
        "A gender neutral wreck":
            $ gender = "neutral"
            $ guygirlperson = "person"
            $ heshethey = "they"
            $ hishertheir = "their"
            $ hisherstheirs = "theirs"
            $ himherthem = "them"
            "It's hard to tell where you lie on the gender scale. Just the way you like it."

    "Whew, glad you got that identity crisis out of the way."

    play music "music/Breeze.mp3" fadein 1.0

    "You check your phone out of habit, despite not getting any signal in this god forsaken town."
    "You called an internet company ahead of time to get things set up for you before you moved in but the wifi is locked."
    #"You can't live like this, you need wifi ASAP."
    #"You paid the internet company before you moved in but the access point requires a password."
    "The router should have the password should be written on it, wherever it is."
    #"This unfamiliar house is like a labrynth to you."
    #"Using the wifi strength indicator on your phone like a radar, you eventually stumble upon the room containing the source of the signal."

    scene bg home_interior_day with dissolve
    
    "After some searching, you find it in a dark corner in the living room."
    "You blow the dust off and try to read the code to no avail. It's too faded to make out."
    "Damn, now what?"
    "Your stomach rumbles, reminding you that you haven't eaten in nearly 24 hours."
    "Screw this, you need to find a good meal before you wither away."
    "Even a small town like Possum Springs must have a place to get breakfast, right? Hopefully some decent coffee too."
    "That, and a restaurant is bound to have public wifi."
    "The map of Possum Springs you snagged from the bus station yesterday should point you in the right direction."
    "You put on a jacket and shoes and venture out into the unknown."
    #"That's all the motivation you need to put on some shoes and head out the door and begin the hunt for food and internet."
    
    
    
    
    

    #"That's odd, the lamp is already on."
    #"The soft glow illuminates the tidy room and all its furnishings."
    #"You had called the utilities companies ahead of time to get things ready for your arrival, but apparently nobody took the time to turn off this one light."
    #"A thick layer of dust cakes the various books and binders on the shelf but the desk area remains relatively clean."
    #hint that there's a mark where a book used to lie on the table
    #"Surprisingly this house hasn't been ransacked and vandalized in all the years it was sitting unoccupied, at least not from what you can tell."
    #"You're lucky this house you've inherited hasn't been broken into and vandalized in all the time it was sitting empty."
    #"At the very least the safe appears to be... safe. "
    #"No sign that anybody tried to break into that safe, so whatever it contains is probably... safe."
    #"Interestingly there's a safe built into one of the walls. You wonder what that's all about but there's no way you're getting it open without the combination."
    #maybe gregg can crack it
    #"You'll have to try and crack it later, right now you're more interested in cracking the wifi password."
    #gregg can crack the safe?
    #"You follow the wires coming out of the computer under the desk, which leads you straight to the router."
    #"Jackpot!"
    #"You look all over the box but the default password has faded from the label."
    #"Damn cheap piece of shit ink."
    #"You desperately look around the room for any sticky notes with passwords scrawled on them to no avail."
    #"Even the computer is locked behind a password when you try turning it on."
    #"Why can't phones just come with ethernet ports? You could plug yours in directly and satisfy your internet addiction if people weren't so obsessed with having thin phones."
    #"If only your phone had an ethernet port."
    #"You step away and sigh."
    #"Now what are you gonna do?"
    #"Your inheritance hasn't hit your bank account yet so buying a new computer or router is out of the question."
    #"Especially when you haven't even bought groceries."
    #"Your stomach rumbles."
    #"You better find something to eat soon. Even a small town like Possum Springs must have a place to get breakfast, right? Hopefully some decent coffee too."
    #"That, and a restaurant is bound to have public wifi."
    #"That map of Possum Springs you snagged from the bus station yesterday should point you in the right direction."
    #"You put on a jacket and shoes and ventured out in search of food and internet."
    #"That's all the motivation you need to put on some shoes and head out the door and begin the hunt for food and internet."
    
    #scene bg black with fade
    
    #"...And that's how you ended up here."
    
    trish "Selmers!"

    scene bg cafe with fade

    play music "music/americano_loop.mp3" fadein 1.0
    
    "The barista's voice pulls you out of your flashback, conveniently right as it was about to end anyway."
    #"Now you remember! You were on your way to buy groceries and you stopped by this cafe on the way for breakfast!"
    "The bear finishes typing something on her laptop before going up to the counter to collect her drink."

    #show selma neutral flip at left with dissolve:
    #    yalign selmaheight

    #selma "Thanks!"

    "You can't resist taking a glance at what she ordered. It looks as good as it smells."
    "It's in a glass mug so you can see the thick chocolaty treat with a layer of froth topped by a generous helping of whipped cream with caramel sauce drizzled upon it."
    "You eagerly wait for your own drink to be ready."

    #hide selma with dissolve

    "..."
    trish "[name]!"

    if chosendrink == "posspressospecial":
        "You fetch your bagel and steaming hot coffee from the counter and head back to your seat by the wall."
        "The mug contains a dark concoction with a layer of light foam, topped with dark chocolate shavings."
        "You blow on it then take a sip."
        "..."
        #"This is the most bitter thing you've ever tasted."
        "It's a mixture of overwhelming bitterness and sweetness."
        "The flavor is earthy and potent with a burnt chocolate aftertaste."
        "It's an exceptionally strong drink that leaves you wanting more of it."
        "You can't resist taking another satisfying sip before moving on to your bagel."
        "Nothing special here, just an ordinary bagel topped with seeds and herbs and ample cream cheese stuffed between its halves."
    
    elif chosendrink == "americano":
        "You fetch your bagel and steaming hot coffee from the counter and head back to your seat by the wall."
        "The mug contains a dark-as-your-soul brew with a few bubbles on the surface."
        "You blow on it then take a sip."
        "..."
        "So bitter. So good."
        "Nothing says \"I hate myself\" more than drinking straight espresso with nothing but a little extra water to make it tolerable."
        #"It's incredibly smooth and gently massages your taste buds with a light, warming flavor."
        "You can't resist taking another satisfying sip before moving on to your bagel."
        "It's full of juicy blueberries and the honey butter spread oozes pure sweetness."

    elif chosendrink == "cappuccino":
        "You fetch your waffle and steaming hot coffee from the counter and head back to your seat by the wall."
        "The mug contains a gradient of different flavors. A creamy espresso mixture on the bottom that turns into a milky white the further up you go, topped with a layer of foam."
        "You blow on it then take a sip."
        "..."
        "It gives you two distinct flavors of steamed milk and espresso. One is light and the other is strong, neither overpowering the other."
        "Can't go wrong with a classic drink like this, even if it is kinda plain."
        "You can't resist taking another satisfying sip before moving on to your waffle."
        #"You cut a slice and pop it into your mouth."
        "The sweet chocolate chips combined with the melted butter send your taste buds to heaven with a first class ticket."
    
    elif chosendrink == "mocha":
        "You fetch your waffle and steaming hot coffee from the counter and head back to your seat by the wall."
        "The glass mug shows a light brown mixture with a layer of chocolate on the bottom. Up top is a layer of whipped cream, with a drizzle of caramel and sea salt"
        "You lick away some of the cream then take a sip of the actual drink."
        "..."
        "The salt contrasts with the sugary taste of chocolate and caramel, which balance the bitterness of espresso."
        "All the flavors combine into an exquisite beverage that gives you everything you could want in a drink."
        "You can't resist taking another satisfying sip before moving on to your waffle."
        #"You slice off a chunk and pop it into your mouth."
        "Juicy strawberries are baked right into it, and much like your drink, the combination with butter serves to give your taste buds the ultimate experience."

    "Meanwhile, the bear on the other side of the room taps away on her keyboard, her claws making quite a racket."
    "You can hear a lot of frustrated backspacing after she types a long block of text."
    "You know that feel all too well."
    "You pull out your phone and get up to date on all your internet needs between bites and sips."
    "It may be a while before you get internet again, so you should download something to keep yourself busy later on."
    
    menu:
        "Download movies":
            $ loriAP = loriAP + 1 #because she's known for liking movies
            $ greggAP = greggAP + 1 #because choosing movies over books is something gregg would relate to
            "This will give you something to relax to. You just wish you didn't have to watch them on a 5 inch screen."
            "You spend some time curating which movies you're interested in and finding working links."
            
        
        "Download books":
            $ mature = mature + 1
            $ selmaAP = selmaAP + 1
            "Books will last longer than movies and give you something to think about, though it is more work to read."
            "You spend some time curating which books you're interested in and finding working links."
            
        "Download music":
            $ beaAP = beaAP + 1
            $ maeAP = maeAP + 1
            "You'd rather not suffer in silence. Even if you've got nothing else to do you can always rock out to something."
            "You spend some time curating which albums you're interested in and finding working links."
    
    "Before you know it, it's already afternoon. You better hit the road soon."
    "You look up a route to the nearest grocery store and memorize it before you're cut off from the internet."
    "It seems the bear is still furiously typing away, concentrated on whatever she's writing."
    "You wonder how long she'll stay here."
    
    #"Code? A blog post? A school project?"
    #"As curious as you are, you don't want to bother a stranger who's focused on their work."
    #"You consider asking her, but she seems focused on whatever she's working on and you don't want to intrude."
    #"Instead you quietly finish your breakfast then prepare to hit the road."
    #"You download a few e-books and videos to watch later, then look up a route to the nearest grocery store."
    #"You've got a long walk ahead of you..."
    "As you're heading out the door, the barista chirps."
    
    show trish at center with dissolve

    trish "Thanks for coming in! Have a nice day!"

    player "Thanks, you too!"
    
    hide trish with dissolve
    
    "Feeling energized from the coffee, you set out on the next leg of your journey."

    stop music fadeout 2.0

    scene bg woods_day

    #"Now that you've had your morning coffee, you're in a position to get things done."
    #"Now that your belly is filled and your veins are pulsating with caffeine, you're in a position to get things done."
    "Next stop: Ham Panther. It's on the other side of the highway to the east of town."
    #"It's almost noon already judging by the position of the sun. Best hurry if you want to make it home before dark."
    "Best hurry if you want to make it home before dark. Longest Night is coming up soon, which means you don't have a lot of daylight to work with."
    #Longest Night is in just a few weeks so you don't have much daylight to burn."
    
    
    scene bg ham_panther with fade

    play music "music/itsadrag_loop.mp3" fadein 1.0

    "Now here's a familiar place. The soulless, sterile, yet gross corporate chain grocery store."
    "Ham Panthers are basically the same everywhere. And man are they everywhere."
    "Except a couple miles closer to your house apparently."
    "You're just shopping for the basics so you grab a basket and get to work."
    "Oatmeal, bread, rice..."
    "Should you pick up milk as well?"
    "Eh, why not? You don't have to worry about it spoiling on the walk back home since it's more likely to freeze."
    "Now for the million dollar question, almond milk or normal milk?"
    
    #almond milk or cow milk, determines your preference for vegetarianism and affects your interaction with stan. if vegetarian he's a bit pushy about getting you to buy something but you just end up getting the vegetable sushi.
    
    menu:
        "Almost milk":
            $ sympathetic = sympathetic + 1
            "You'd think packaging the runoff water from washing almonds would be cheaper than raising a cow but somehow it's always the more expensive option."
            "Oh well, at least you've grown accustomed to the taste and it doesn't upset your tummy."
            "You pass by the deli counter, not really planning on getting anything from it but the jolly old man behind the counter calls out to you."
            
            show stan neutral at right:
                yalign .5
            with dissolve
            
            stan "Ahoy! I don't see any meats in that basket of yours. Why don't you take a gander at my wares to see if anything interests you!"
            
            "You give him the courtesy of at least pretending to be interested, even though you don't see anything you want."
            
            stan "Ahahaha, sorry, an old man's gotta entertain himself somehow standing back here all day. Anything catch your eye?"
            
            player "Not really... I'm not super into meat I guess."
            
            stan "Not into meat? Well I reckon you're in the wrong aisle, the garden section is on the other side of the store har har har!"
            stan "Really though, we do have a selection of tofu and vegetable sushi if that's more your style."
            
            player "Sushi huh? Who would have thought there'd be sushi in a small town like this."
            
            stan "Well... don't tell my supervisor I said this but you're better off being a vegetarian if you're eyeing the sushi here."
            stan "I wouldn't trust the definition of \"fresh\" they use for the fish here."
            stan "But the ones that are just veggies and avacado wrapped in rice should still be edible!"
            
            player "Good to know..."
            
            "You pick up one of the packages, not entirely convinced."
            "You shrug and place it in your basket. Can't be that bad. At least it's cheap."
            
            stan "Hope you enjoy it! Let me know how it is!"

            player "Sure thing. Have a nice day."
            
            stan "You do the same!"

            hide stan with dissolve
            
        "Moo cow milk":
            "Where else are you supposed to get your calcium? You need strong bones for... well you just need them, okay?"
            "Ok, what's next?"
            "You grab a few more things then swing by the deli where an old cat in an apron and paper hat stands behind the counter."
            "He catches you looking at the meats on display and bellows out a jolly greeting that startles you."

            #supposed to be in deli uniform, no sprite available for now :(
            show stan neutral at right:
                yalign .5
            with dissolve

            stan "Howdy! Let me know if you need anything and I'd be happy to assist you."

            "You give him a nod of acknowledgement then go back to deliberating which meat to get."

            player "Hi there..."

            "You glance at his nametag."

            player "...Stan. Can I get some..."
            
            "You pick out a few meats to stock your freezer with so you won't have to make frequent trips back here."

            stan "Sure thing! I'll have that ready for you in a jiffy!"

            "You shift your weight from one foot to the other while the clerk prepares the meats."
            "Once he's finished, he slides the packaged product toward you and you cross it off your shopping list."

            stan "Have a nice day!"

            player "Thanks, you too!"

            hide stan with dissolve

    "You go down a few more aisles, tossing some extras into your basket until it's filled to the brim, then proceed to the check out."

    show gregg apron at center with dissolve:
        yalign greggheight

    greggunknown "Heya!"

    "A chipper fox greets you when you wander up to a register."
    #"A fox with amber orange fur mans the register you wandered up to."
    #"He sports a dark grey turtleneck sweater underneath his apron, along with a chipper attitude."
    "The name tag pinned to the apron reads \"Gregg\", with a tiny, crude portrait of himself drawn next to it."

    player "Hey."

    "You start unloading the contents of your basket onto the conveyor belt. The cashier rings them up with ease, not even looking at what he's scanning."

    gregg "You find everything alright?"

    player "Mhm."

    "You mutter a response as you try to get your debit card out."

    gregg "So where ya headed?"

    "You look up from your wallet and blink a couple times."

    player "Huh?"

    gregg "Lots of people passing through from Bright Harbor lately, goin' to visit family for the holidays."

    player "Oh uh, I just moved into Possum Springs actually."

    "The cashier stops scanning your groceries and freezes in place."

    gregg "What, really?!"
    gregg "Nobody ever just like, comes here to live."
    gregg "Have you tried the pierogies at the diner yet? They're *amazing!~*"

    player "I just arrived yesterday. I'm trying to get my pantry filled up first."

    gregg "Gotchya. Takin' it one day at a time. I respect that."

    player "Heh, thanks. I just hope I make it back before dark. I don't have a car so I had to walk all the way out here."

    "Gregg takes a glance outside through the automatic sliding doors with a contemplative expression."

    gregg "Hey, if you want I can drive you home. My shift's about to end anyway."

    menu:
        "{cps=0}Should you let Gregg drive you home?{/cps}"
        "Sure, what could go wrong?":
            $ greggAP = greggAP + 1
            $ bold = bold + 1
            $ wentWithGregg = True

            player "You'd do that?"

            gregg "Sure! It beats standing around scanning food."

            player "Well... ok. I guess I can get in a stranger's car just this once."

            gregg "Oh I don't have a car or anything, I ride a motor bike."

            player "Cool, so I can jump off if you try to kidnap me or something."

            gregg "That's the spirit!"

            "He quickly finishes scanning and bagging your groceries, practically bouncing off the walls with excitement. Must have been a slow day for him."

            gregg "Alright, meet me out front in a minute. I have to go clock out."

            "The fox runs off without a care in the world before your receipt is even done printing."

            hide gregg with dissolve

            "You give him a delayed thumbs up he doesn't even see then head outside with your bags."

            stop music fadeout 2.0

            "Gregg pops out shortly afterward, zipping up a black leather jacket suitable for a biker."

            show gregg neutral at center with dissolve:
                yalign greggheight

            gregg "Sorry I took so long. Boss caught me leaving early and I had to make up an excuse."

            player "It's fine, still faster than me walking home."

            gregg "I don't think I caught your name earlier. I'm Gregg!"

            player "Nice to meet you Gregg! I'm [name]."

            gregg "You ready to roll, [name]? Come on, my bike's over here."
            
            show gregg neutral at offscreenleft with move

            # have gregg slide off screen then reappear

            "He shows you to a bike rack. You're guessing his is the one with a motor installed in front of the back wheel."
            #"It also has a seat sticking out on the back and pegs to rest your feet."
            
            show gregg neutral at center with dissolve

            gregg "Ta-da! Pretty sweet, huh?"
            
            player "It's..."
            
            gregg "I know, not exactly what you think when you hear motorbike."
            gregg "I don't even know if it's street legal but that never stopped me before!"
            gregg "Here, lemme take your bags."

            "Gregg picks up your bags and slips them onto the handlebars, giving them a few turns left and right to test the stability with the added weight."

            gregg "Yeah, that should work. Go ahead and hop on!"

            "Gregg jumps into his seat and pats the one behind him. You carefully climb on, holding onto his shoulders."
            "Before you've gotten comfortable in this unusual setup, he revs up the motor and the bike lurches forward toward town."

            gregg "WOOOOOOOOOOOOOO!!!!"

            #play music "music/revvedup_v2loop.mp3" fadein 1.0
            

            #"He swivels the bike around sharply and goes down a small ramp into the parking lot where he builds up speed before making a wide turn onto the grass next to the highway."

            #stop music fadeout 2.0

            scene bg playerhouseexterior with fade
            
            "The sun sank below the horizon quicker than you expected, making it difficult for you to recall how to get home in the darkness but you did eventually make it."

            show gregg neutral flip at left with dissolve:
                yalign greggheight

            gregg "Nice place. Reminds me of the Shreigeist House."

            player "I dunno what that is but it sounds spooky."

            gregg "It is. When they decorate it for Harfest it becomes less spooky."
            gregg "Not gonna lie though, this house looks kinda abandoned."

            player "It was until recently."

            gregg "Anybody else living here with you?"

            player "Nope, just me."

            gregg "How can you afford a place like this? Are you a drug dealer?"

            player "It's an inheritance."
            
            gregg "From a drug dealer?"
            
            player "I don't think so."
            player "I'm not really sure what my father did for a living."

            #gregg "Oh."
            #gregg "That's uh, not what I was expecting."
            gregg "Oh."
            gregg "Sorry..."

            "You both stand around uncomfortably for a few seconds, then you change the topic."

            player "Anyway, thanks for driving me down here!"

            gregg "No problem dude! I would say \"anytime\" but I'm not a taxi service. Not unless it pays well enough for me to quit Ham Panther."

            "You laugh but his expression indicates he was serious."

            player "Don't worry, I'll figure something out. Just wish there was a closer store."

            gregg "The Snack Falcon in town isn't far but yeah, if you can't survive off chips and slushies there's kind of a monopoly on grocery stores around here."

            player "Mh-hm. Well, I guess I'll see you next time I go out shopping then."

            gregg "Probably! I'm at Ham Panther pretty much all day almost every day."
            gregg "In fact, I'm gonna take off now cause I gotta get up early tomorrow for work."

            player "Oh, sure. Drive safe!"

            gregg "Where's the fun in that?"

            "He helps you remove your bags from the bike's handlebars. He grins at you as he hops onto the bike and revs the engine."

            gregg "Take care!"

            hide gregg with dissolve

            "With a casual salute, he circles around back to the road and you swear you can hear him hollering like he's on a rollercoaster as he rides down the hills."

            #scene bg home_interior_night with dissolve

            "Now, time to go inside, put your groceries away, make something to eat, and go to bed."

            #play sound "sound/changing clothes.mp3"

            ###if you got sushi, just eat that. else snack on something

            #"You can't be bothered to cook tonight, despite your stomach's protests, but you do stop by the pantry on your way to the living room to grab a snack."
            #"Now you can curl up on the living room couch and watch the videos you downloaded on your phone in peace, occasionally munching on your favorite treat."
            #"You kinda wish you had bothered to pay for cable now that internet is in such limited supply so you could at least put some background noise on the television."
            #"You didn't bother spending money on cable now that the internet has replaced any need or general desire for it."
            #"Oh well. First world problems you guess."
            #"Before long the sun finishes setting, plunging you into a darkness broken only by the glow of your phone."
            #"Your phone is about out of juice so you begrudgingly retire to your bedroom, put it on the charger, and settle into bed."
            #"But just before sleep overtakes you, low rumblings make their approach and an abrupt train horn drags you back to consciousness."
            #"Ugh, it just keeps getting louder and louder for what seems like eternity."
            #"Finally it passes."
            #"Not long afterward, *another* train screeches past your house."
            #"Frustrated, you shove your face into your pillow and begin counting sheep."

            #"1...2...3..."

            #"..."

            #"...156...157...158..."

            #"..."

            #"..."

            #"..."

            scene bg black with fade

        "No, don't want to be a bother.":
            $ timid = timid + 1
            $ wentWithGregg = False

            player "Nah, I can make it on my own."

            gregg "Are you sure? I can take you, it's no big deal. Really."

            player "It's fine. Appreciate it though."

            "He shrugs."

            gregg "Your choice, man. Just be careful you don't like, wander into a wild bear's den on the way back."

            player "Haha I won't."

            "He quietly finishes scanning and bagging your groceries while you get your debit card ready."
            "With a swipe and a press of a button, you pay for your groceries and Gregg hands you your receipt."

            gregg "Have a nice day!"

            player "Thanks, you too."

            hide gregg with dissolve

            scene bg home_interior_night with fade

            "Of course it's night and bitterly cold by the time you reach your house."
            "You drag yourself inside then unload your groceries in the kitchen, using the empty plastic bags to discard the wrappers from things you snacked on along the way."
            "You promptly retire to your bedroom, put your phone on the charger, and settle into bed."
            #"But just before sleep overtakes you, low rumblings make their approach and an abrupt train horn drags you back to consciousness."
            #"Ugh, it just keeps getting louder and louder for what seems like eternity."
            #"Finally it passes."
            #"But not long afterward, *another* train screeches past your house."
            #"Frustrated, you shove your face into your pillow and begin counting sheep."

            #"1...2...3..."

            #"..."

            #"...156...157...158..."

            #"..."

            #"..."

            #"..."

            scene bg black with fade
    
        # Day 2, thursday
        $ currentDay = 2
        $ currentDate = "December 2"

        play sound "sound/birds.mp3"
        "After a restless sleep, you awaken to the sound of birds chirping outside."
        #"Even underneath this thick blanket, you feel frostbitten."
        #"What the hell, is the heater working properly?"
        #"Ugh, guess you have to get up and check."
        "Drawing in a deep breath, you stretch your limbs and loosen up a few stiff muscles."
        "Your bones crackle and you let out a contented sigh when your spine finally pops into place."
        "Ahh... that felt good."
        "You crawl out from under the covers and pull back the curtains draping the window to let some light in."

        play sound "sound/curtains.mp3"
        #transition to background of view from window
        play music "music/whenskiesclear_loop.mp3" fadein .5

        #"To your surprise, snow has appeared in full force overnight!"
        #"Snowflakes plummet to the earth, covering the landscape in fluffy whiteness. Your eyes sting from how white it is but you can't look away."
        #"Everything's so different, your backyard is hardly even recognizable."
        #"The ground that had been littered with autumn leaves is now a clean blank slate, broken only by the dark tree trunks growing out of it."
        #"Even the treetops are frosted white, matching the bright cloudy sky."
        #"It's not like you've never seen snow before, but something about it makes you feel nice."
        #play sound "sound/stomach growl.mp3"
        #"As much as you'd like to spend the morning admiring the scenery, your stomach's growling is getting to be too much to ignore."
        #"You need to get something to eat after skipping dinner again last night."
        #"After turning up the thermostat, you make your way to the kitchen and see what you've got."

        #scene bg home_interior_day with fade

        #"...Not much, but you can at least make a bowl of oatmeal."
        "You watch the snow fall through the window as you eat your boring breakfast, wishing you had bought ingredients to make hot cocoa at the store yesterday."
        "Leaving the dishes in the sink to wash later, you take a trip to the bathroom to get ready for the day."

        scene bg bathroom with fade

        

        "You dry yourself off and put on some clothes, deliberating what to do today."
        #"Do you want to stay in or go out?"
        #"You've done a lot of walking lately so you're inclined to stay here and relax."
        "You haven't really explored your new home yet. You should at least familiarize yourself with the general layout before you start wandering around town."
        "You grab your phone and head into the halls."

        scene bg home_office_day with fade

        #"Your tour of the house concludes when you find yourself back in the office."
        "Your tour of the building took you through different rooms filled with art, furniture, and books."
        "Nothing out of the ordinary for a well-off boomer. You noted your father had a taste for antiques."
        "But what stood out to you the most was what must have been your father's bedroom."
        "Just thinking about it sends a chill up your spine and you're not sure why."
        "The room smelled like old stale clothes, and neither of the two windows provided much light. There was nothing in there except a king sized bed, a nightstand, and a wardrobe."
        "It didn't feel right to mess with anything so you shut the door and made a note to leave it be, like a tomb."
        "Wandering over to the desk, you take a gander at the shelves stuffed with binders and books. They seem to be work related."
        "You sit down in the leather chair and slowly spin around."
        "It's actually really comfortable. You guess you'd splurge on a nice chair too if you were gonna sit in it for long periods of time."
        "In your idle spinning, you must have accidentally bumped the mouse, because you hear the computer suddenly turn on."
        "You try a few common passwords but have no luck getting in."
        "You'll need to figure out a way to get past the login screen sometime."
        "You wander what could possibly be on the hard drive."
        "It's probably just going to be full of vacation photos and spreadsheets. A cryptocurrency wallet or two if you're lucky."
        "But you don't wanna wipe the drive until you've taken a look."

        # pause

        "As you shut the computer down, you notice a photo frame next to the monitor."
        "Inside there's a faded picture of you as a kid. You're holding up a fish you caught and your father is kneeling beside you with a proud look on his face."
        "You vaguely remember when that photo was taken. It was in early spring, when all the leaves were bright green."
        "You got up early and spent the whole day fishing, just you and your dad. Then when the sun started going down you sat on the bank and fed the fish with the remainder of your bait."
        "Simpler times, those were. Your parents were still together back then."
        "You feel a lump in your throat, but you push it down because adults aren't supposed to cry."
        #"With a heavy sigh, you look back at the monitor."
        #"You half-heartedly try a few random passwords until it locks you out."
        #might change back to the corrupt hard drive in recovery mode thing, but have to go back and rewrite the first time the player boots it up
        #"Dang, the disk is saying it's corrupt. It's starting a recovery procedure now."
        #"The estimated finish time is given in... days?!"
        #"Just how big is the hard drive?"
        #"Ugh, you'll deal with this later. You leave the machine running and prepare to head out."
        "There's just one more room left to check out."

        stop music fadeout 1.0

        scene bg basement1 with fade

        play music "music/woulditmatter_loop.mp3" fadein 1.0

        "You'd noticed a shed in the backyard when you looked outside this morning so you put on your jacket and ventured out to it."
        "It's pretty large for a shed. It's more like a garage, really."
        "It's cold and echoey and smells like gasoline in here."
        "Judging by the debris and tools strewn about, it hasn't been cleaned in a while. Nobody even bothered to sweep the leaves from the floor."
        "A tarp covers something in the corner of the room. Probably a lawnmower"
        #"A pile of skeletons, used for a demon-summoning ritual perhaps?"
        #"Or maybe it's a stockpile of cocaine. Never know when you might need a couple hundred pounds of that stuff."
        "Nothing makes an old man happier than mowing the lawn at the crack of dawn on weekends."
        "Bracing yourself for disappointment, you grab a corner of the tarp and take a peek."
        "No way."
        "Your hand reaches out to touch it. The cold metal stings your fingertips."
        "You pull aside the rest of the tarp, revealing an impressive motorcycle."
        "Its design harkens back to the motorcycles of the 70s and 80s."
        "Shiny chrome contrasts with the leathery black upholstery. You just need a pair of aviators and you can become a biker."
        "You take back what you thought about your dad being a lame boomer, he was in fact a cool boomer."
        "Now you can ride around town instead of having to walk everywhere *and* you can do so stylishly!"
        "You can't wait to feel the wind on your face when you take her for a spin."
        "A quick search yields a key hidden in a nearby toolbox. The original is probably long gone, wherever your dad went."
        "You try not to think about that while you insert the key and turn it."
        "The engine makes a weird noise for a second and then nothing."
        "You try again."
        "Fuck."
        "You spend a few hours tinkering with it trying anything and everything but you're hindered by a lack of tools."
        #you break the tool you needed?
        
        
        "Still nothing. Out of fuel maybe?"
        "You pop off the cap and look inside the gas tank, using the light on your phone to see into the darkness."
        "Empty."
        "A nearby gas can remedies this issue, but the engine still refuses to start."
        "Hmm."
        "You look around for the repair manual, remembering you saw something like it on the workbench."
        "You skim through it and get the gist on how to check the engine and oil and troubleshoot common problems."
        "Oil seems ok, but you're not sure if sitting around for so long has done it any favors."
        "You grab a few tools, get on the floor, and get to work opening her up."
        "Ugh, it's grimy as Hell down here."
        "It just gets worse the more you work on it."
        "As you pry off a covering, a gear comes loose and falls to the ground, shattering into pieces."
        "That's not good."
        "Was that what was wrong with it? You look around for any spare gears but fail to find any."
        "Well damn, there's no way you can fix it now."
        "With a frustrated sigh, you wipe your hands on a towel before checking your phone to look up any nearby auto shops."
        "As fate would have it, the nearest one is even further out than Ham Panther."
        "One of the related results however is a local hardware store in town, not that much further away than the cafe. Maybe they have what you need?"
        "You return to the house to grab your wallet before setting out toward town."

        stop music fadeout 2.0

        scene bg park with fade

        "Old brick buildings line the streets as you approach your destination."
        "Some of them look lived in, others look like they're about to crumble."
        "Some look like both."
        "A short walk later, you come up to the Ol' Pickaxe."
        "You ascend the couple of steps leading to the front door and head inside."

        scene bg pickaxe with dissolve

        play music "music/picknaxe_loop.mp3" fadein 1.0

        "It's your typical hardware store, nothing too fancy. Mostly basic tools you won't find at a dollar store along with a small collection of less common parts."
        "Snow shovels seem to be selling quick these days."
        "Behind the counter stands a bluish green crocodile giving off gothic vibes."
        "Her eyes sluggishly drift to look in your direction."

        show bea apron at right with dissolve:
            yalign beaheight

        beaunknown "Welcome to the Ol' Pickaxe. Let me know if I can help you find any- *yawn* -...thing."

        player "I don't suppose you have any spare motorcycle parts here, would you?"

        beaunknown "Uhh, you'd really wanna go out to the auto shop outside of town for that... What exactly are you looking for?"

        "You pull the shattered pieces of the gear out of your pocket and show it to the clerk."

        player "I'm not really sure what this is called... It fell out when I was trying to fix the engine."

        "You can feel her silently judging you as she looks over the part."

        beaunknown "How did you manage to break a metal gear like this?"

        player "I think it was the cold that did it."

        beaunknown "Well I'm pretty sure we don't have any gears this size in stock. I'd have to special order one but you're better off ordering one online."

        player "Oh..."

        "The croc sighs and pulls out an electronic cigarette. It lights up as she takes a puff from it."

        beaunknown "Tell ya what. I'll check the backroom and see if there's anything that *might* help."

        player "Thanks!"

        "You give her a bright smile."

        beaunknown "Mh-hm."

        "She yawns and shuffles over to the back of the store."

        hide bea with dissolve

        "While she's away, you pass the time by taking a look around the shop."
        "Lots of boxes and miscellaneous items are strewn about like they're in the middle of reorganizing their inventory."
        "You're studying the oddly large keys behind the counter when the front door opens and a short cat bursts in."

        show mae neutral flip at left with dissolve

        #"Wait a minute, you recognize her as the same cat who picked up the mouse girl at the bus station the other day!"
        #"You didn't notice it at the time, but one of her ears is torn and she has subtle red highlights in her fur."
        "She frantically looks around the store before coming up to you."

        mae "Hey, do you know if Bea here right now?"

        player "Is that the cashier?"

        mae "More like owner but yes."

        player "She went to check the back room real quick."

        mae "Ok cool thanks."

        show mae skeptical flip at left

        "She narrows her eyes at you."

        mae "Do I know you from somewhere?"

        player "I don't think so?"
        
        mae "I thought I saw you at the bus station the other day."
        
        n "The memory comes flooding back to you."
        
        #(flashback to day 0, nov 30 tuesday)
        #lori is back from school early due to weather
        
        scene bg bus_interior with fade
        play sound "sound/bus_onboard.mp3" fadein 1.0
        play music "music/deathterrors_v2loop.mp3" fadein 1.0

        "You wake up to the sound of some unusual music coming from nearby."
        "It takes you a while to realize where you are and recall why you're here."
        "You're on a bus to Possum Springs, a small town your father lived in after your parents split up."
        "That was ages ago and you'd rarely seen him since."
        "In fact, nobody's seen him in the past four years. He just vanished one day without a trace."
        "Normally it takes seven years for a missing person to be legally declared dead but apparently your father was not the most patient man."
        "He had written in his will that if he disappeared for just four to go ahead and hand all his belongings down to you."
        "His cash assets would be distributed to you over time though. Guess he didn't want you spending his fortune all in one place."
        "He did however leave behind a house for you to move into immediately."
        "Your previous living conditions were not ideal to say the least, so you jumped at the chance to move anywhere else, even if it was in some nowhere town."
        "You check the time on your phone. It's only 6:15. You'd never know that by looking outside though. It's pitch black out already."
        "Well, Longest Night is drawing near after all."
        "Thankfully you hadn't missed your stop."
        "There's quite a few more people on board now. They must have come on while you were asleep."
        "Apparently one of them likes loud music."
        "You can see a pair of ears sticking up over a seat with wires trailing down from them. That must be whoever's earphones making that noise."
        "At least they have the decency not to blast it through their phone speakers."

        menu:
            "{cps=0}What will you do?{/cps}"
            "Ask her what she's listening to.":
                $ inquisitive = inquisitive + 1
                $ loriAP = loriAP + 1
                $ loriInteractionBold == True

                "It actually sounds like something you'd listen to so she must be pretty cool. You decide to strike up a conversation before she slips away, never to be seen again."
                "Moving up to the empty seat beside her, you can't help but take a peak at what she's writing in her notebook."
                "It's hard to read from this angle but it looks to be a story, with horrific doodles in the margins."
                "Jagged-toothed monsters, devilish demons, intestines spilling out of the innocent..."
                "Strange, she doesn't look the type to draw stuff like that."

                show lori neutral at right with dissolve:
                    yalign loriheight

                "She doesn't seem to have noticed you yet so you clear your throat, a bit louder than you need to."

                player "*Ahem*"

                show lori breath

                "The mouse glances up from her journal and nearly jumps out of her seat."
                "In a flash, she clutches her notebook and scrambles away from you until her back is pressed against the window."
                "The poor thing's rapidly breathing in and out as she watches you with fear in her eyes."
                "You hold your hands up to show you meant no harm."

                player "Whoa, didn't mean to startle you."

                "Easing back into her seat, she takes her earphones out and makes a concentrated effort to slow her breathing."

                loriunknown "Oh goodness, you scared me! Hah hah... hah..."

                "You chuckle lightheartedly."

                player "I guess that makes us even. Pretty cool music by the way."

                show lori neutral

                "The girl looks confused for a moment then realizes her earphones still playing and are audible from a distance."

                loriunknown "Oh gosh, you could hear that? I'm so sorry!"

                stop music fadeout 2.0

                "She mashes the volume down button on her phone in a panicked, embarrassed fashion."

                loriunknown "*Huff huff*"

                player "No, it's fine. Actually I wanted to get the name of it before one of us got off the bus."

                "You confidently smile as you reassure her. She looks at you like you're crazy for a second then smiles back, scooting closer to you."

                loriunknown "Well uh, it's called Deathterrors. The album, that is. It's by Kerosinners."

                player "Nice. I'll check it out once I get to my place."

                "She seems excited to talk more about it, but the bus driver cuts your conversation short as he announces you'll be arriving in Possum Springs momentarily."

                loriunknown "Oop, that's my stop!"

                player "Really? It's mine too!"

                loriunknown "No way! No one else ever gets off at Possum Springs!"

                player "Yeah, I'm moving in today."

                loriunknown "Cool! Maybe I'll see you around town later... Whoops!"

                "She reaches down to grab her pen that had just rolled off her notebook, but you get to it first and hand it back."

                loriunknown "Hah, thanks! Guess I better pack up before our stop, huh?"

                player "Yeah, that might be a good idea haha."

                hide lori with dissolve

                "While she gathers her things and stuffs them in her backpack, you take a look outside."
                "The forest has opened up into a hilly countryside. Aside from the train track and an old factory, there's hardly anything noteworthy out there. Just miles and miles of emptiness."
                "A short time later, the bus pulls up to an abandoned-looking station and stops by an empty bench."
                "The whole area has fallen into disrepair. Plants sprout from the multitude of cracks in the walls and sidewalk, and graffiti marks nearly every vertical surface."
                "It looks like a ghost town."
                "At least some of the lights are on, even if most of them are flickering or have cracked face plates."
                "You let the mouse girl stand up and start walking toward the exit first, then check your pockets to make sure you got everything and head out yourself."

                stop sound fadeout 1.0

                #this is supposed to be an exterior background but we didn't have one available :/
                scene bg busstation with dissolve

                $ renpy.sound.set_volume(.3, 0, channel='sound')
                play sound "sound/crickets.mp3" fadein 1.0

                "The air outside is chillier than expected, in contrast to the surprisingly warm interior of the bus."
                "You can see your breath forming thick clouds that rapidly rise into the overcast sky as you shuffle over to the storage compartment, shivering."
                "It's just you and her waiting out here under a streetlight, both with your hands in your pockets and hunched over to cope with the cold."
                "Your eyes meet at one point and you exchange friendly smiles and subtle nods."

                # brief pause

                "Jeez, how long is the driver gonna make you wait?"
                "He takes his sweet time before finally waddling out and unlocking the storage door."
                "Gesturing for her to go first, you patiently wait for the girl to retrieve her bags, then reach in to dig out your own stuff."

                show lori neutral at right with dissolve:
                    yalign loriheight

                loriunknown "See you around!"

                "You look up to see the mouse waving goodbye to you with her free hand as she totes her suitcase to a car that had just pulled up to the curb."
                "You take a break from pulling your bags out to wave back."

                player "See ya!"

                "You're rewarded with a wide grin before she runs into the arms of the black-furred cat who had just stepped out of the vehicle, giggling and embracing her fondly."

                # hug scene
                show mae neutral flip at left with dissolve:
                    yalign maeheight

                maeunknown "Lori!"

                lori "Mae!"

                mae "Welcome back to Possum Springs!"

                lori "Haha it's good to be back!"

                mae "Glad to see you again! Here, lemme get those for you."

                "The cat takes Lori's luggage and hoists it into the trunk of her car, but the mouse chooses to hold onto her backpack."

                lori "Hang on, I wanna keep my notebook close by."

                mae "Gotchya. Ready to go?"

                lori "Yeah!"

                hide lori
                hide mae
                with dissolve

                "Lori hops into the passenger seat while her friend closes the trunk and goes back around to the driver side."
                "The car revs to life and begins to drive away as you drag your things from the bus."
                "One heavy backpack and two suitcases filled to the brim. All of your belongings in one place."
                "The bus driver wordlessly closes the compartment and locks it, then returns to his helm of his vessel. With a final roar, the engine hauls its passengers to their next destination."


            "Ask her to turn it down.":
                $ loriAP = loriAP - 1
                $ bold = bold + 1
                $ loriInteractionRude == True

                "You don't wanna hear any more of that creepy music, and you're sure everyone else on the bus would appreciate some peace and quiet."
                "Moving up to the empty seat beside her, you can't help but take a peak at what she's writing in her notebook."
                "It's hard to read from this angle but it looks to be a story, with horrific doodles in the margins."
                "Jagged-toothed monsters, devilish demons, intestines spilling out of the innocent..."
                "What kind of person draws stuff like this?"

                show lori neutral at right with dissolve:
                    yalign loriheight

                player "Excuse me."

                $ cynical = cynical + 1

                show lori anxious3:
                    yalign loriheight

                "She jumps a little when she notices you, knocking her pen to the floor."
                "She hastily picks it back up then takes out her earphones. Her movement is kinda jittery and she's breathing heavily."

                show lori breath

                loriunknown "Um, hey? Huff huff... Did you need something?"

                "You point to her earphones lying on her journal."

                player "Would you mind turning that down?"

                "She glances down at her earphones then back up to you with a panicked, embarrassed expression."

                loriunknown "Oh gosh, you could hear that? I'm so sorry, hang on!"

                stop music fadeout 2.0

                "She mashes the volume down button on her phone."

                loriunknown "Huff huff... Huff huff..."

                player "Appreciate it."

                hide lori with dissolve

                "With that out of the way, you decide to look out the window and admire the countryside."
                "Hills, a train track, a factory, and more hills. So this is it, huh? It's quite... plain."
                "The driver announces you'll be arriving in Possum Springs shortly, and a few minutes later you pull up to an empty bench near an abandoned-looking station."
                "The whole place has fallen into disrepair. Plants sprout from the multitude of cracks in the walls and sidewalk, and graffiti marks most vertical surfaces."
                "It looks like a ghost town."
                "At least some of the lights are on, even if most of them are flickering or have cracked face plates."
                "The mouse girl hurriedly stands up and starts walking toward the exit, looking a bit distressed."
                "Is she angry because you asked her to turn down her music?"
                "Regardless, you check your pockets to make sure you got everything and head out yourself."

                stop sound fadeout 1.0

                scene bg busstation with dissolve

                $ renpy.sound.set_volume(.3, 0, channel='sound')
                play sound "sound/crickets.mp3" fadein 1.0

                "The air outside is chillier than expected, in contrast to the surprisingly warm interior of the bus."
                "You can see your breath forming thick clouds that rapidly rise into the overcast sky as you shuffle over to the storage compartment, shivering."
                "It's just you and that girl waiting out here under a streetlight, both with your hands in your pockets and hunched over to cope with the cold."
                "She avoids eye contact with you."

                # brief pause

                "Jeez, how long is the driver gonna make you wait?"
                "He takes his sweet time before finally waddling out and unlocking the storage door."
                "Gesturing for the mouse to go first, you patiently wait for her to retrieve her bags, then reach in to dig out your own stuff."
                "Out of the corner of your eye, you can see her walk up to a car as it pulls up to the curb."
                "A black-furred cat steps out to happily greet her with a nice big hug."

                show lori neutral at right:
                    yalign loriheight
                show mae neutral flip at left
                with dissolve

                maeunknown "Lori!"

                lori "Mae!"

                mae "Welcome back to Possum Springs!"

                lori "Haha it's good to be back!"

                mae "Glad to see you again! Here, lemme get those for you."

                "The cat takes hold of Lori's luggage and hoists it into the trunk of her car, but the mouse opts to keep her backpack with her."

                lori "Hang on, wanna keep my notebook close."

                mae "Gotchya. Ready to go?"

                lori "Yeah!"

                hide lori
                hide mae
                with dissolve

                "Lori hops into the passenger seat while her friend closes the trunk and goes back around to the driver side."
                "The car revs to life and begins to drive away as you drag your things from the bus."
                "One heavy backpack and two suitcases filled to the brim. All of your belongings in one place."
                "The bus driver comes and locks the compartment, then wordlessly returns to his helm of his vessel. With a final roar, the engine hauls its passengers to their next destination."


            "Move away from her.":
                $ loriInteractionNull = True
                $ cynical = cynical + 1

                "You don't wanna bother her. You'll be off this bus soon anyway."
                "You move over to a seat further away from her and take a look out the window, losing yourself in thought."
                "The forest has opened up into a hilly countryside."
                "Aside from the train track and an old factory, there's hardly anything noteworthy out there. Just miles and miles of emptiness. So this is it huh? It seem so... plain."
                "The driver announces you'll be arriving in Possum Springs shortly, and a few minutes later you pull up to an empty bench near an abandoned-looking station."
                "The whole place has fallen into disrepair. Plants sprout from the multitude of cracks in the walls and sidewalk, and graffiti marks most vertical surfaces."
                "It looks like a ghost town."
                "At least some of the lights are on, even if most of them are flickering or have cracked face plates."
                "The mouse girl stands up and walks toward the exit before you do. You wonder if she lives here."
                "Seems she's the only one besides yourself getting off at this stop. You check your pockets to make sure you got everything and head out yourself."

                stop music fadeout 2.0
                stop sound fadeout 1.0

                scene bg busstation with dissolve

                $ renpy.sound.set_volume(.3, 0, channel='sound')
                play sound "sound/crickets.mp3" fadein 1.0

                "The air outside is chillier than expected, in contrast to the surprisingly warm interior of the bus."
                "You can see your breath forming thick clouds that rapidly rise into the overcast sky as you shuffle over to the storage compartment, shivering."
                "It's just you and her waiting out here under a streetlight, both with your hands in your pockets and hunched over to cope with the cold."
                "Your eyes meet at one point and you exchange friendly smiles and subtle nods."
                "She still has her earphones in, and you can overhear all the cries and moans and screams that she doesn't seem to mind at all."

                # brief pause

                "Jeez, how long is the driver gonna make you wait?"
                "He takes his sweet time before finally waddling out and unlocking the storage door."
                "Gesturing for her to go first, you patiently wait for the girl to retrieve her bags, then reach in to dig out your own stuff."
                "Out of the corner of your eye, you can see her remove her earphones then excitedly run up to a car as it pulls up to the curb."
                "A black-furred cat steps out to happily greet the mouse and give her a nice big hug."

                show lori neutral at right:
                    yalign loriheight
                show mae neutral flip at left:
                    yalign maeheight
                with dissolve

                maeunknown "Lori!"

                lori "Mae!"

                "Welcome back to Possum Springs!"

                lori "Haha it's good to be back!"

                mae "Glad to see you again! Here, lemme get those for you."

                "The cat takes hold of Lori's luggage and hoists it into the trunk of her car, but the mouse opts to keep her backpack with her."

                lori "Hang on, wanna keep my notebook close."

                mae "Gotchya. Ready to go?"

                lori "Yeah!"

                "Lori hops into the passenger seat while her friend closes the trunk and goes back around to the driver side."

                hide mae
                hide lori
                with dissolve

                "The car revs to life and begins to drive away as you drag your things from the bus."
                "One heavy backpack and two suitcases filled to the brim. All of your belongings in one place."
                "The bus driver comes and wordlessly locks the compartment, then returns to his helm of his vessel. With a final roar, the engine hauls its passengers to their next destination."

        # restore default music volume
        $ renpy.music.set_volume(0.7, 0, channel='music')

        scene bg black with fade

        "From there you remember walking through the woods to get to your new home."

        show mae neutral flip at left

        "A look of realization dawns on her."

        mae "Oh yeah! I remember seeing you! It's not every day someone new arrives in Possum Springs!"

        player "I just moved here. My name's [name]."

        mae "Mae. Mae Borowski. Nice to meet you!"

        player "Same!"

        mae "So what made you decide to come all the way out to Possum Springs?"

        player "Ah you know, the relaxing countryside, the fresh air... oh and inheriting a house up past the train tracks."
        player "The old man was nice enough to put it in my name before he died four years back."

        show mae sad1 flip at left

        "Mae looks away and mumbles to herself."

        mae "Died... four years back...?"

        show mae panic flip at left

        "She suddenly looks like she's seen a ghost."

        mae "Uhh, look at the time Ihavetogobye!"

        #have mae run off the screen instead
        hide mae with dissolve

        "She runs out of the store just as the crocodile comes back."

        show bea apron at right with dissolve:
            yalign beaheight

        bea "Was that Mae just now?"

        "You're still processing what just happened. You snap out of it and turn to the shop owner."

        player "Uh, yeah. You know her?"

        bea "You could say that. What did she want?"

        player "I dunno. She just came in, asked if you were here, then left."

        bea "Huh. Weird. Anyway, I didn't find anything that could help you. Sorry."

        player "Oh. That's ok, it was kind of a long shot. Thanks for checking though."

        bea "No problem. Let me know if there's anything else you need."

        player "Just these."

        "You grab a pack of batteries and set them down on the counter. Never know when you might need some."
        "She rings you up and you decline a bag in lieu of stuffing your purchase into your coat pocket."

        bea "Alrighty. Have a good one."

        player "You too!"

        hide bea with dissolve

        stop music fadeout 2.0

        scene bg park with fade

        "You walk out the door and take a few aimless steps down the street, mulling over everything."
        "Well that sure was disappointing."
        "Not getting any of the parts you need, that is."
        "But that chat with Mae sure was odd too."
        "Maybe you should stop parading the fact that your dad died. It's probably freaking people out."
        "..."
        "No, it's definitely freaking people out."
        "You're internally cringing at yourself when a delightfully sweet smell reaches your nose through the bitterly cold air."
        "It draws you to the source, a shop called Bear Essentials Bakery."
        "After the long walk here, you might as well grab a snack for the road."

        scene bg bakery_interior with fade

        play sound "sound/storebell.mp3"
        play music "music/Indecisive_Redux.mp3" fadein 1.0

        "As soon as you walk in, the scent of peppermint hits you like a truck."
        "You feel bad for the baker behind the counter who has to put up with this for hours every day."
        "At least he probably comes home smelling nice."
        "He pulls a tray full of holiday themed cookies out from the oven then turns to you with a warm smile."

        show angus neutral flip at left with dissolve:
            yalign angusheight

        angusunknown "Welcome! I'll be with you in just a second!"

        "You nod to him as he sets the tray on a cooling rack and moves a fresh batch into the oven."

        hide angus with dissolve

        "You take the time to look over the confections in the glass case, and after deciding what you want, you have a quick glance around the room."
        "The thing that sticks out the most is the stage taking up nearly a third of the room."
        "It seems odd for a simple bakery to have a stage but it's probably left over from this building's previous business, much like the cracking paint on the walls."

        show angus neutral flip at left with dissolve:
            yalign angusheight

        angusunknown "Sorry for the wait. What can I get you?"

        menu:
            "Poppy seed muffin":
                $ confectionChoice = "muffin"
                player "I'll have one poppy seed muffin, please!"
                $ cinnamonRoll = False
            "Cinnamon roll":
                $ confectionChoice = "cinnamon roll"
                $ cinnamonRoll = True
                player "I'll have a cinnamon roll, please!"
            "Glazed lemon cake":
                $ confectionChoice = "cake"
                $ cinnamonRoll = False
                player "I'll have a slice of lemon cake, please!"
            "Raspberry scones":
                $ confectionChoice = "scones"
                $ cinnamonRoll = False
                player "I'll have a few raspberry scones, please!"

        angusunknown "Sure! Would you like me to heat it up?"

        "You look over your shoulder at the snowy environment, remembering how cold it is."

        player "Please do."

        "The baker catches you looking outside and chuckles as he grabs the [confectionChoice] with a pair of tongs."

        angusunknown "Haha that snow came out of nowhere, didn't it? My winter coat isn't even fully grown in yet!"

        menu:
            "I like the cold.":
                player "I like the cold."

                angusunknown "I do too, but I'd say I'm better equipped to handle it than most. Thick fur and a stocky build designed for winter weather hehehe."
            "I hate the cold.":
                player "I hate the cold."

                angusunknown "I can see that. It makes me sleepy. I think it makes everyone sleepy."
            "The cold doesn't bother me.":
                player "The cold doesn't bother me."

                angusunknown "Well that's good, cause I have a feeling we're in for a loooong winter."

        play sound "sound/storebell.mp3"
        "The bell on the door chimes as the baker sets your snack inside a small toaster oven."
        "You take a look over your shoulder and to your surprise it's the fox from the grocery store!"

        show gregg neutral at right with dissolve:
            yalign greggheight

        gregg "Hey Angus! And look who we have here!"

        "He swaggers up to the counter and makes a grandiose gesture toward you, grinning from ear to ear."

        gregg "This is who I was telling you about earlier!"

        if wentWithGregg == True:
            gregg "The one I drove home yesterday and has that big house in the woods!"

            angus "Just how many strangers did you drive home yesterday, Gregg?"

            player "Thanks for that again. I never would have expected people out here to be so... kind."

            angus "Oh don't worry, you'll meet some jerks sooner or later."

            gregg "Not us though! We're super chill and nice!"
            gregg "By the way this is Angus. All you need to know about him is that he is the best."

            angus "Oh you."

            player "Nice to meet you, Angus. I'm [name]."

            angus "It's a pleasure to meet you as well."

            "It seems everyone knows each other in this town. Like everyone's in one big family."
            "It's kinda heartwarming."

            play sound "sound/storebell.mp3"

            "Everyone's attention shifts to the toaster oven when the timer dings."
            "Gregg leans over the counter and sniffs at your treat as Angus removes it."

            gregg "[confectionChoice], yum."

            player "Can I get that to go please?"

            angus "Of course!"

            player "Thanks."

            "He drops the [confectionChoice] into a small bag, then places that inside a bigger bag and sets it on the counter."
            "As he does so, you pull out your wallet and dig out your debit card."

            angus "Paying with card? Here you go. The machine takes a minute to process though."

            "He slides a tablet with a card reader plugged in toward you."
            "You insert your card and sure enough it gets stuck on the processing screen."
            "..."
            "After a while, Angus clears his throat and breaks up the lull in the conversation."

            angus "So is Gregg gonna be chauffeuring you every time you need groceries or do you have another way of getting around?"
            angus "Sorry if that sounded rude, I'm just wondering what your living situation is like."

        elif wentWithGregg == False:
            gregg "The one who's new in town! Fancy meeting you here!"
            gregg "By the way, I don't think I properly introduced myself yesterday. I'm Gregg!"

            "He holds out his paw and you take hold of it. He's got a firm, eager handshake."

            player "[name]."

            if newname.upper() == "SCOTT":
                gregg "[name], huh? When we lived in Bright Harbor our neighbor was a Scott. I think he was an animator or something."
            if newname.upper() == "ALEC":
                gregg "[name], huh? We knew an Alec when we lived in Bright Harbor. I think he was a musician or something."
            if newname.upper() == "BETH":
                gregg "[name], huh? There was a Beth we ran into a few times when we lived in Bright Harbor. I think she was making an indie game or something."
            if newname.upper() == "BETHANY":
                gregg "[name], huh? There was a Bethany we ran into a few times when we lived in Bright Harbor. I think she was making an indie game or something."

            angus "I'm Angus. It's a pleasure to meet you."

            player "Nice to meet you as well!"

            "It seems everyone knows each other in this town. Like everyone is one big family."
            "It's kinda cute."

            "Everyone's attention shifts to the toaster oven when the timer dings."
            "Gregg leans over the counter and sniffs at your treat as Angus removes it."

            gregg "[confectionChoice], yum."

            player "Can I get that to go please?"

            angus "Of course!"

            player "Thanks."

            "He drops the [confectionChoice] into a small bag, then places that inside a bigger bag and sets it on the counter."
            "As he does so, you pull out your wallet and dig out your debit card."

            angus "Paying with card? Here you go. The machine takes a minute to process though."

            "He slides a tablet with a card reader plugged in toward you."
            "You insert your card and sure enough it gets stuck on the processing screen."
            "..."
            "After a while, Angus clears his throat and breaks up the lull in the conversation."

            angus "So are you planning on walking every time you need groceries or do you have some means of transportation?"
            angus "Sorry if that sounded rude, I'm just wondering what your living situation is like."

        "The machine beeps and you take back your card. Angus passes you your receipt as you're talking."

        player "Actually I've got a motorcycle I'm trying to fix. I've never worked on this sort of thing though so it might take a while."

        "Gregg's ears perk up."

        gregg "Did I hear \"motorcycle?\""

        angus "That is what [heshethey] said."

        gregg "I can help you fix it!"
        gregg "I learned a bunch of stuff from working on my own bike! I bet I can get yours running smoothly in a jiffy!"

        player "That would be great! It doesn't run at all at the moment."

        angus "Don't worry, Gregg is great at getting broken things to work. He built that robot thing this one time..."

        gregg "Yeah, I can come to your place tomorrow morning and check it out!"

        player "That would help me out a lot, thanks so much!"

        if wentWithGregg == True:

            player "You remember how to get to my place?"

            gregg "Yup!"

            player "Cool. See you later!"

            gregg "See ya!"

        elif wentWithGregg == False:

            player "Oh, I guess you'd need to know where I live."

            gregg "That would be useful to know, yes."

            "You hastily jot down your address on the back of the receipt with a pen that was lying on the counter and hand it to Gregg."

            gregg "Sweet! I'll see you there!"

            player "See ya!"

        angus "Have a nice day!"

        player "You too!"

        stop music fadeout 2.0

        hide gregg
        hide angus
        with dissolve

        scene bg park with dissolve

        "Taking your bag, you leave the store and decide to rest at the park lodged in between the bakery and hardware store."
        "You brush aside the snow that has accumulated on one of the stone benches next to some sort of monument."
        "Names are carved into a pillar, which houses a statue depicting a soldier carrying a rifle with a bayonet."
        "They must have been locals who served in some war a century or so ago."
        "You read a few names as you mindlessly open up your bag and pull out your [confectionChoice], but you don't recognize anyone on there."
        "You munch on your snack in peace until a particularly curious squirrel hops onto the far edge of the bench, staring at you."
        "The animals in this town seem to have no fear of people and walk right past you, close enough you could touch one."
        "You watched them on your walk here as they scrambled to get last minute errands done before the real cold hits."
        "Burying food, fetching nesting materials, that sort of thing."
        "This one here comes closer and sniffs at the treat in your hand."
        "Squirrels like [confectionChoice], right? You break off a piece and set it on the bench."
        "He hesitantly comes over and picks it up with its little hands then shoves it into its mouth before skittering off."
        "You're welcome."

        scene bg home_interior_night with fade

        "The sun had gone down by the time you made it home."
        "You lazed around and watched a few videos on your phone for a while until you were hungry enough to start dinner, then you continued to laze around until it was time for bed."
        #try tinkering with the bike, go to bed early since gregg is showing up in the morning


        scene bg bedroom with fade

        "You crawl under the covers and think about your future here."
        "You need to get a job at some point. Sooner or later you'll need the income."
        "You wouldn't mind making some friends too while you're here."
        "It's been so long since you've hung out with anyone, you can hardly remember what it's like."
        "At least Gregg is coming over tomorrow. He seems like a nice guy."
        "You yawn and turn over, clutching your pillow as sleep overtakes you."

        scene bg black with fade
        
        
        stop music fadeout 1.0
    
    

    # Day 3, friday
    $ currentDay = 3
    $ currentDate = "December 3"
    

    play sound "sound/motorbike arriving.mp3"
    #scene fading in

    "You had managed to get used to the train and its blaring horn passing by several times each night but now your slumber is disturbed by a new sound."
    "It's the rumbling of a motor approaching, followed by tires digging into the ground just outside the front door."
    "You quickly become alert once you realize that must be Gregg coming over to fix your bike."
    "You scramble out of bed but before you can change out of your pajamas he's already knocking on the front door. You have no choice but to answer it like this."

    scene bg home_interior_night with fade

    "It's not even daylight out yet."
    "You flip on the lights and open the door to find Gregg standing there proudly with an overstuffed backpack in his hand."
    "He seems oblivious to the fact that you've just woken up."

    play music "music/cozycidersipping_loop.mp3" fadein 1.0

    show gregg neutral flip at left with dissolve:
        yalign greggheight

    gregg "Morning, [name]! I brought all my tools and a bunch of parts."

    player "Uh, morning Gregg. I didn't expect you so early."

    gregg "I only have an hour before I have to be at work."
    gregg "Well? Where's the bike?"

    player "Oh uh, right this way."

    scene bg basement1 with fade

    "You put on some slippers and lead him to the shed."
    "Gregg's eyes go wide at the sight of the motorcycle as you open the door."

    show gregg neutral flip at left with dissolve:
        yalign greggheight

    gregg "She's beautiful. I love her."

    player "I'd love her more if she didn't leak fuel."

    "You point at the puddle of gas soaking into the concrete floor."

    gregg "Ooh, yeah that's a big problem."

    show gregg sad3 flip

    gregg "Hmm."

    "He drops to the ground and gets an up close look at the engine."

    show gregg neutral flip

    gregg "You got a towel?"

    "You grab a towel from the workbench and hand it to him."

    gregg "Thanks."

    "He wipes off some of the grime, then pulls his backpack close and rummages around until he finds a flashlight."
    "Lighting up the area underneath the bike, he pokes and prods at a few parts then furrows his brow."

    gregg "Hrmmm..."

    player "What is it?"

    gregg "Not sure yet."

    player "Can I get you anything? A drink?"

    gregg "Nah, I'm good."

    "He pulls a wrench from his bag and starts unscrewing nuts and bolts while you stand by, just observing."
    "You wish you could help, but you're really at a loss at what to do and you don't want to get in his way."
    "He takes off quite a few bits and pieces, and at times looks like he's confused by what he's working with, but he continues working with confidence."

    gregg "Hey how much fuel is in the tank, do you know?"

    player "Um."

    "Suddenly a valve clanks against the floor and the entire gas tank empties itself onto Gregg's sleeve."
    "He recoils in surprise and falls back on his rear."

    gregg "AAAAAAAH!"

    player "Oh shit!"

    gregg "Haha don't worry, it's fine! Didn't get much on me."

    "Gregg flicks his arm to get the remaining droplets off."
    "Thankfully most of it had slid off his leather jacket and splattered onto the floor instead of soaking into his fur."

    player "Still..."

    menu:
        "Wipe down his jacket":
            #+1 greggAP
            #+1 understanding

            "You grab a spare cloth and wipe the excess liquid off his jacket, noticing he got a smudge of oil on his face too."

            player "Hold still."

            gregg "Wha-?"

            "You scrub the oil spot off as gently as you can. He freezes in place as you clean his fluff."

            player "There. You had something on your face."

            gregg "O-oh!"
            gregg "Haha thanks! I wouldn't wanna show up to work with a big splotch on my face! Hahaha!"

            "His lighthearted laughter is contagious, at least enough to put a smile on your face."

        "Hand him a clean towel":
            #+1 cynical

            player "Sorry, I should have warned you ahead of time..."

            "You hand him a spare cloth."

            gregg "Nah, it's alright."

            "He wipes the excess liquid off his jacket."

            gregg "See? No harm done."

            player "You got a bit of oil on your face too. Right there."

            "You point in the general area where the splotch is on his face. He roughly scrubs at the area."

            gregg "Did I get it?"

            "Not really..."

            player "Yeah."

    gregg "Alright, let me finish working on this. I think I can get her running soon."

    "Gregg goes back to operating on your bike, wiping down gunked up parts, reseating pieces, and duct taping components."
    "Time flies by as you watch him. He really seems like he's having a good time fixing your bike and making idle chit chat."
    "Before you know it he stands and claps his paws together."

    gregg "That should do it!"
    gregg "Hopefully!"
    gregg "Let's roll her out of here and see if she starts!"

    menu:
        "I'm so excited!":
            $ greggAP = greggAP + 1

            player "I'm so excited!"

            gregg "Come on come on come on let's push her out onto the yard!"

            "You flip up the kickstand and the both of you wheel the bike through the garage door and out into the snow."
            "Gregg looks at you eagerly as you put the key into the ignition and give it a turn."

            play sound "sound/motorcycle fail.mp3"

            "..."

            "Another turn."

            play sound "sound/motorcycle fail.mp3"

            "..."

            play sound "sound/motorcycle start.mp3"

            "Just as you're losing hope, the engine comes to life."

            player "Hahaha yeah!!!"

            "Gregg looks so relieved. He's flailing his arms and howling."

            gregg "AWOOOOOOOOOOOOOOO!"

            "And then the engine dies."

            gregg "Huh?"
            gregg "Oh yeah, we never replaced the gas!"

            "You glance at the near-empty gas canister in the garage."

            player "I have a little bit left inside still. It's kinda old though."

            gregg "That's fine, just make sure you put some fresh fuel in there soon."
            gregg "And you'll probably wanna take it to a real mechanic sometime."

            player "At least now I can drive it to one."

            gregg "Yup!"
            gregg "Well, I better get going before I'm late for work."

            player "Ok! Thanks so much for fixing my bike!"

            gregg "No problem! It beats bagging groceries at the Ham Panther all day!"
            gregg "Oh that reminds me, we're having a little get together this evening if you wanna come. Me, Angus, and a friend of ours."

            player "Sure, that sounds fun! I'm not doing anything tonight anyway."

            gregg "Cool, we're meeting at six. We live on the floor above the bakery."

            player "Sounds good. See ya then!"

            gregg "Hey do you have Chattrbox? You should add me!"

            "You haven't used Chattrbox in quite a while."
            "Regardless, you get his account name and make a note to reinstall the app later."

            gregg "Alright, see ya later!"

            "He jogs over to his own bike and rides off as the sun begins to rise."

        "I'll be surprised if this works.":
            #(-1 Gregg AP, +1 cynicism)

            player "I'll be surprised if this works."

            "Gregg's ears droop."

            show gregg sad2 flip

            gregg "Hey man, don't doubt my abilities. At least it can't run *worse* now after all that work I put into it."

            "You flip up the kickstand and the both of you wheel the bike through the garage door and out into the snow."
            "Gregg looks at you with anticipation in his eyes as you put the key into the ignition and give it a turn."

            play sound "sound/motorcycle fail.mp3"

            "..."

            "Another turn."

            play sound "sound/motorcycle fail.mp3"

            "..."

            "Just as you thought, he couldn't fix-"

            play sound "sound/motorcycle start.mp3"

            "*VROOOOOM*"

            "The engine comes to life, much to Gregg's relief."

            show gregg neutral flip

            gregg "Yes!"

            player "Well this is a pleasant surprise."

            "And then the engine dies."

            gregg "Huh?"
            gregg "Oh yeah, we never replaced the gas!"

            "You glance at the near-empty gas canister in the garage."

            player "I have a little bit left inside still. It's kinda old though."

            gregg "That's fine, just make sure you put some fresh fuel in there soon."
            gregg "And you'll probably wanna take it to a real mechanic sometime."

            player "At least now I can drive it to one."

            gregg "Yup!"
            gregg "Well, I better get going before I'm late for work."

            player "Ok! Thanks for fixing my bike!"

            gregg "No problem! It beats bagging groceries at the Ham Panther all day!"
            gregg "Oh that reminds me, we're having a little get together this evening if you wanna come. Me, Angus, and a friend of ours."

            player "Sure, I'm not doing anything tonight anyway."

            gregg "Cool, we're meeting at six. We live on the floor above the bakery."

            player "Sounds good. See ya then!"

            gregg "Hey do you have Chattrbox? You should add me!"

            "You haven't used Chattrbox in quite a while."
            "Regardless, you get his account name and make a note to reinstall the app later."

            gregg "Alright, see ya later!"

            "He jogs over to his own bike and rides off as the sun begins to rise."

        "What was wrong with it?":
            #+1 Gregg AP, +1 inquisitive)

            player "What was wrong with it?"

            gregg "Not enough duct tape. It's the most important part in making things work."

            player "Riiiight..."
            player "Well, what did you do about the missing gear?"

            gregg "Huh? There was a missing gear?"
            gregg "Eh, don't worry about it. Now come on, let's see if it works now!"

            "You flip up the kickstand and the both of you wheel the bike through the garage door and out into the snow."
            "Gregg looks at you eagerly as you put the key into the ignition and give it a turn."

            play sound "sound/motorcycle fail.mp3"

            "..."

            "Another turn."

            play sound "sound/motorcycle fail.mp3"

            "..."

            play sound "sound/motorcycle start.mp3"

            "Just as you're losing hope, the engine comes to life."

            player "It works!"

            "Gregg looks so relieved. He's flailing his arms and howling."

            gregg "AWOOOOOOOOOOOOOOO!"

            "And then the engine dies."

            gregg "Huh?"
            gregg "Oh yeah, we never replaced the gas!"

            "You glance at the near-empty gas canister in the garage."

            player "I have a little bit left inside still. It's kinda old though."

            gregg "That's fine, just make sure you put some fresh fuel in there soon."
            gregg "And you'll probably wanna take it to a real mechanic sometime."

            player "At least now I can drive it to one."

            gregg "Yup!"
            gregg "Well, I better get going before I'm late for work."

            player "Ok! Thanks so much for fixing my bike!"

            gregg "No problem! It beats bagging groceries at the Ham Panther all day!"
            gregg "Oh that reminds me, we're having a little get together this evening if you wanna come. Me, Angus, and a friend of ours."

            player "Sure, that sounds fun! I'm not doing anything tonight anyway."

            gregg "Cool, we're meeting at six. We live on the floor above the bakery."

            player "Sounds good. See ya then!"

            gregg "Hey do you have Chattrbox? You should add me!"

            "You haven't used Chattrbox in quite a while."
            "Regardless, you get his account name and make a note to reinstall the app later."

            gregg "Alright, see ya later!"

            "He jogs over to his own bike and rides off as the sun begins to rise."

    hide gregg with dissolve
    stop music fadeout 2.0

    "Now then, time to go back inside and take a hot shower."

    scene bg bathroom with fade

    "You somehow managed to put off taking a shower until late afternoon."
    "It's about time to head to Gregg's place."
    "You drove the bike around the yard a bit to make sure it works and you're fairly confident it can make it to town."
    "You grab your daily carry stuff then head down to the shed."

    scene bg basement1 with dissolve

    "Gregg had messaged you on Chattrbox a few hours ago asking you to bring over the tools he left behind."
    "You gather his things into the bag then zip it up and sling it over your shoulder."
    "Oof, this thing's heavy!"
    "You manage to bear with it and roll your bike outside, stepping into the night."
    "It's cold and breezy out with soft moonlight coming through the clouds."
    "Nice night for a ride."
    "You close the shed door behind you and hop on your bike, revving it a few times before venturing into the darkness."

    scene bg parkdark with fade

    "You pull up to the curb next to the Bear Essentials Bakery and check the time on your phone."
    "You're a little earlier than you expected, thanks to the lack of cops in Possum Springs to deter you from riding fast."
    "But... the building looks abandoned?"
    "Lights are off, the sign says closed, and the only apparent entrances are locked."
    "No response when you bang on the door either."
    "Does Gregg really live here on the second floor or was he messing with you?"
    "You can't even text him because the only wifi spots available are password protected."
    "You have no choice other than to wait and see if Gregg or Angus show up."
    "Crossing your arms, you lean against the building and sigh."
    "Your breath is easily visible in this weather, the contrails spiraling upward and being whisked away by the wind."
    "You remember pretending to be a dragon when you were a child, blowing out \"smoke\" when it was cold out."
    "You reminisce over moments like those and try spewing fire like you always wanted to."
    "Nope, still just smoke."
    "Which is really just hot air."
    play sound "sound/footsteps.mp3"
    "Your thoughts are interrupted by the sound of snow crunching behind you."
    "Footsteps."
    "They're coming closer."
    "More than one person."
    "You risk a glance over your shoulder, more worried that someone saw you acting out your dragon fantasies rather than someone coming to mug you."
    "You're pleasantly surprised to find Angus walking toward you with a pizza box in his arms."
    "And he's got a friend in tow."
    "That must be the guy Gregg was talking about. He's a short birdy fellow with a rucksack on his back."

    show angus neutral flip at left:
        yalign angusheight
    show germ neutral at right
    with dissolve

    angus "Hello, [name]! Gregg hasn't let you inside yet?"

    player "Hey Angus. Nah, I haven't seen him. The place looks empty."

    angus "Hmm. He's probably watching TV in the dark and couldn't hear you."
    angus "This is Germ by the way. Germ, this is [name]."

    germ "Hi [name]! I hope you like video games! I brought some with me."

    "He adjusts his bag to emphasize his point."

    menu:
        "I love video games!":
            player "Nice to meet you uh... Germ? And yeah, I love video games!"
        "They're alright.":
            player "Nice to meet you uh... Germ? And yeah, video games are alright."

    "You're not sure if you heard his name right but just smiles and doesn't correct you."
    "Kind of an odd name but who are you to judge?"

    angus "And I bought pizza! I didn't know what kind you liked so I just got cheese."

    player "Cheese is fine."
    player "So are we gonna go in or...?"

    angus "Oh right. Forgot you guys are probably freezing."
    angus "Come with me."

    hide angus
    hide germ
    with dissolve

    "You and Germ follow Angus to the back of the building."
    "It feels a bit sketchy, but you doubt a guy carrying a pizza is going to mug you."
    "He starts up the metal stairway of the emergency exit."

    show angus neutral flip at left with dissolve:
        yalign angusheight

    angus "Sooo, fun fact. The stairs inside are broken."
    angus "They caved in before we bought the place. That's why we have to take the fire escape to get to the second floor."

    player "Caved in? How does something like that even happen?"

    "Angus shrugs."

    angus "This building isn't exactly up to code."
    angus "I don't think it's even legal for us to live here but it's the cheapest option and nobody's stopped us yet."

    hide angus with dissolve

    "You climb up the staircase after Angus with Germ taking up the rear."
    "When you reach the second floor, you have to crawl through a window to get inside."

    scene bg greggapartment with fade

    play music "music/dissonance_to_chill_to.mp3" fadein 1.5

    "Gregg is passed out on a stained couch in front of a TV."
    "Beer bottles litter the floor around him."

    show angus neutral flip at left with dissolve:
        yalign angusheight

    angus "Honey, I'm home! And I picked up two hitchhikers!"

    "The startled fox rolls off the couch and hits the floor with a thud."

    show gregg neutral at right with dissolve

    gregg "AAAAAAAAAAHH!"

    "He quickly regains his composure, acting like nothing had just happened."

    gregg "[name]! Germ! What's up?"

    angus "I found Germ wandering around on the way back from the pizza joint, and [name] was just sitting out front."

    gregg "Oops, that's my fault. I shoulda been waiting out there for ya, [name]."
    gregg "Please accept Angus's pizza as an apology on my behalf."

    player "Apology accepted."

    angus "I'm happy I could be of service."

    "Angus slides the pizza onto a table and opens a cabinet to grab some paper plates and plastic cups while Gregg pulls a 2-liter bottle of soda out from a mini fridge in the corner."
    "Meanwhile Germ sneaks away to the television and unzips his bag."

    germ "I'm gonna set up the games."

    angus "I'll get you a plate, Germ."

    germ "Thanks."

    angus "[name], you can just set your backpack down wherever, you know."

    player "Oh right, Gregg left his tools at my place so I brought 'em over."

    "You take off the backpack and hand it to Gregg."

    gregg "Aww, thanks for not stealing them!"

    "He carelessly tosses it against the wall beside the couch."

    player "Anytime."

    "Angus opens up the pizza box and hands you a plate."

    angus "Guests first."

    player "You don't have to tell me twice!"

    "You grin and take a couple slices then move over so Gregg can get some while you pour yourself a drink."

    gregg "So you rode your motorcycle here right? How's she run?"

    player "Pretty good once I got some fuel in her."

    angus "I'm glad Gregg could help you fix her up."

    gregg "And that she didn't explode."

    "Angus fills up a plate for Germ, then takes the remainder of the pizza for himself."

    angus "Gregg, could you get drinks for me and Germ?"

    gregg "Sure thing!"

    hide angus
    hide gregg
    with dissolve

    "Gregg pours extra drinks as you and Angus make your way to the couch."
    "Germ is crouched by the TV hooking up the connectors to the very outdated cube shaped console sitting on the floor."
    "Angus gives Germ his plate and grabs a controller for you, Gregg, and himself."

    show angus neutral at right:
        yalign angusheight
        xalign 1.1
    show germ neutral flip at left:
        yalign germheight
        xalign -.02
    with dissolve

    angus "Thanks for bringing your console, Germ. I'll take the busted controller this time."

    germ "If you insist."

    "Gregg comes by shortly after and sets the drinks on a small table then sits on the couch with his plate in his lap."

    show gregg neutral:
        yalign greggheight - .5
        xalign .7
    with dissolve

    gregg "Angus and I had to sell our consoles when we moved, [name]. We were very sad."

    angus "I mostly play on PC."

    gregg "*I* was very sad."

    player "Where'd you move from?"

    angus "Bright Harbor."

    if newname.upper() == "SCOTT":
        player "Ah right, you mentioned living in Bright Harbor before."
    if newname.upper() == "ALEC":
        player "Ah right, you mentioned living in Bright Harbor before."
    if newname.upper() == "BETH":
        player "Ah right, you mentioned living in Bright Harbor before."
    if newname.upper() == "BETHANY":
        player "Ah right, you mentioned living in Bright Harbor before."

    gregg "We used to live here in Possum Springs, then moved to Bright Harbor, then back here."

    "Sounds like the two of them have some history going pretty far back."
    "It just now occurs to you that they might be more than just friends."

    player "Sorry if this is a dumb question but are you two... together?"

    "Gregg snuggles up to Angus, who leans his head on him."

    gregg "Yup! "

    angus "I can barely remember a time when I wasn't with Gregg."

    germ "*Ahem*"

    "Germ turns to you with two game cases in his hands."

    germ "What game should we play?"

    gregg "You decide, [name]."

    menu:
        "The platformer fighting game.":
            $ gameChoice = "fighting"
            "You point at the fighting game."
        "The board-based party game.":
            $ gameChoice = "party"
            "You point at the party game."
    player "That one."

    germ "K."

    "He takes the undersized disc and pops it into the console."
    "Germ opts to stay sitting on the floor, while you, Gregg, and Angus fill up the couch. You all enjoy a few bites of pizza while the intro video plays."

    germ "This is the like, newest game I have."

    gregg "Isn't this game 20 years old?"

    germ "Yup!"

    "Germ hits start and sets up the game."

    angus "Ugh, I hate getting grease on the controller."

    gregg "That's what pants are for."

    "Gregg wipes his paws on his pants."

    angus "Be right back, I'm gonna grab some napkins."

    "Angus gets up and steps over the wires on the way to the table."
    "He comes back with a stack of napkins and hands them out to everyone before sitting back down."

    gregg "Ready?"

    angus "Yeah."

    "You all pick a character and begin a round."

    if gameChoice == "fighting":

        "Germ is surprisingly good at this game. His inputs are efficient and he punishes with grace."
        "Despite that, he gives you and the others a fair chance by leaving his defenses open."
        "Gregg's aggressive plays allow him to take a couple of lives, at the cost of his character getting killed as well more often than not."
        "Angus seems to be trying to get used to the controls, which only adds to the hilarity when he accidentally knocks someone off the stage."
        "You just try to survive as long as you can and land a few hits whenever you can."
        "Unsurprisingly Germ wins the round."

        gregg "Angus. You press X to jump."

        "Gregg points to the button on Angus's controller."

        angus "Well I wish you would have told me before I died a million times!"

        "Germ unassumingly eats his pizza while waiting for the next round to start. Everyone chooses a new character and you go to a random stage."
        "As soon as it loads, Gregg immediately jumps off and dies."

        gregg "Wait I thought I was the other guy! Restart!"

        germ "No redoes."

        "Against your better judgement, you decide to taunt Gregg, both in real life and in the game."

        player "Yeah, no redoes."

        "You blow a raspberry at the fox as your character dances on screen."
        "Your in-game taunt ends up getting you killed but thankfully Gregg restrains himself from doing the same to you in reality."
        "Angus fares a little better this time."
        "You all go easy on him and avoid targeting him unless he engages first. Gregg however is out for blood, doing whatever it takes to get you off the stage."
        "Usually Germ ends up finishing both of you off."
        "Eventually it's just Germ and Angus left standing. You eat your pizza and watch while Gregg coaches Angus."
        "It all comes to an anticlimactic conclusion when Angus misses an easy punish and slowly falls off the bottom of the stage."

        gregg "Angus! You have to press B and up at the same time to recover!"

        angus "I was doing that!"

        gregg "No like, you have to slam the stick like this."

        "Gregg demonstrates."

        angus "Hrm."

        "You start up another round. This time you all have the same idea to gang up on Germ."
        "He doesn't seem to mind, and he methodically takes you all on simultaneously."
        "You and Gregg manage to get a few combos off on him but once again the match ends with a showdown between Angus and Germ."
        "Germ shields against Angus's special then completely whiffs his own attack, giving Angus a chance to launch him off stage."

        gregg "OOOOOOOOOOOOOOH! GOT HIM!"

        "You all have a laugh at the outcome, especially after Gregg's reaction to it."


    elif gameChoice == "party":

        "You decide on a board then your characters all roll a die and move forward however many spaces."
        "Each space you land on has a different effect, whether it's gaining or losing money, acquiring an item, teleporting to a different spot on the board, or a variety of other events."
        "And at the end of each turn, you have to play a minigame. Sometimes it's a free-for-all, sometimes it's 2 vs. 2 or 1 vs. 3 with randomly selected teams."
        "The game is designed to be impossible to play seriously no matter how hard you try, with all its randomness and janky controls."
        "As frustrating as it can be to lose everything because the game felt like it, it's difficult to stay mad when you get your points swapped with the guy in first place on the next turn."
        "There's a lot of downtime between minigames since you just have to press a button to roll the die and watch the game play out, giving you ample time to munch on your pizza."
        "Germ is such a pro at this game he eats his while playing the minigames."
        "Gregg's aggressive plays are counterbalanced by his incredibly bad luck throughout the round, landing him in last place."
        "Angus on the other hand plays safely. Perhaps a bit too safely, since he usually ends up missing chances to get points."
        "It all culminates in a last minute exchange where Germ risks everything on a duel between you and him. Of course the minigame you have to play for the championship is entirely based on chance."
        "Basically you have to jump onto one of the colored quadrants of a carousel and hope it's not the wrong one."
        "It spins around for a while and when it stops a monster chained to the wall eats whoever is on the space closest to it."
        "If no one is on that spot, you choose another one and it takes another spin. This goes on indefinitely until one of you dies."
        "Germ goes first, picking red. You jump on yellow and you both go for a spin."
        "When it starts to slow down it looks like Germ is about to lose but he ends up just out of the monster's range when it stops. Death narrowly avoids you as well."
        "Now you both hop off and choose a quadrant again."
        "You both last a shockingly large number of turns. A statistically improbable amount. But sooner or later one of you has to die."
        "The tension is rising. Will you outlast your opponent? Or does he have lady luck on his side tonight? Who will be the one to get eaten?"

        gregg "Oh my god, I can't watch."

        "Gregg covers his eyes. Germ jumps on the yellow spot. You're up next."

        player "Aaah I can't decide!"

        "Gregg takes a quick peek to offer his coaching."

        gregg "Red!"

        angus "Green."

        germ "Anything but blue."

        "It's all random anyway so you just press A and jump onto whatever space. You end up on blue."
        "The merry-go-round spins up and the monster approaches with a hungry look in its eyes."
        "As you come to a crawl, Germ coasts right past the kill area. Green and red go by and then finally it stops on blue."
        "Your character gets gobbled up and all your points are taken away, just like that."

        angus "Ooh!"

        "Gregg uncovers his eyes while the next scene loads."

        gregg "What happened? Who lost?"

        angus "[name] got eaten!"

        gregg "OOOOOH! GERM IS THE MASTER OF LUCK!"
        gregg "AWOOOOOOOOOO!"

        "Gregg sure seems happier about this outcome than Germ does. The final results screen pops up, showing Germ on top and you on bottom."
        "Angus got second place and Gregg got third."

        player "How did you know it was gonna be blue?"

        "Germ shrugs."

        germ "I had a feelin.'"


    #fade to black and back

    hide gregg
    hide germ
    hide angus
    with dissolve

    stop music fadeout 1.5

    "The night goes on with the four of you having a good time playing games until Germ says he has to go back home."
    "At that point you were tired and getting ready to call it quits anyway. You coil up your controller's wire and help Germ pack away his system."
    "Zipping up his bag, he stands up and waves to you."

    show germ neutral flip at left:
        yalign germheight
    with dissolve

    germ "See ya!"

    hide germ with dissolve

    "That's all he says before going to leave through the window."
    "He's certainly an odd guy, but he's very friendly."
    "Gregg and Angus finish cleaning up the plates and napkins and come up to you."

    show gregg neutral flip at left:
        yalign greggheight
    show angus neutral at right:
        yalign angusheight
    with dissolve

    gregg "Whew, that was fun."

    angus "It sure was."

    player "Yeah."

    "There's an uncomfortable silence as nobody is sure what to say and everyone just wants to hurry this up and go to bed."

    gregg "So Angus, what do you think? Dragons and Dungeons next week?"

    angus "Sure, that sounds good. Perhaps our new friend would like to join us?"

    player "I'd be down for that. Just have to check my schedule first."

    angus "Ah, the persistent problem of finding a time where everyone is available."

    gregg "No problem dude, just let us know when you're free and we'll work something out."

    angus "Do you use Chattrbox by any chance? We could coordinate a date on there."

    player "Yeah, hold on."

    "You pull out your phone and exchange contact info with Angus."
    "From there, you thank him and Gregg for the pizza and say your goodbyes before climbing out the window and going down the fire escape."

    hide gregg
    hide angus
    with dissolve

    scene bg parkdark with dissolve

    "It was refreshing to hang out with a group again."
    "Gregg's upbeat personality is fun to be around, and Angus is a really sweet guy."
    "It's hard to pin down how you really feel about Germ since he was so quiet, but he seems cool."
    "You hop onto your bike and ride back home, reflecting on how much your life has changed in just a few short days."
    "You're enjoying a fresh independent lifestyle but you're also making new friends and coming out of your shell. It feels good."

    scene bg home_interior_night with fade

    "When you arrive at home, you notice both Gregg and Angus sent you a message on Chattrbox."

    gregg "Awesome night dude, can't wait to hang again!"
    gregg "I usually get off work at ham panther in the afternoon if you wanna swing by and ride bikes and stuff."

    angus "Just making sure you made it home safely."
    angus "Had a fun night with you all. Come by the bakery anytime if you're ever in the area and just wanna chat or something."
    angus "You won't be a bother, I don't get that many customers."

    "You send them both a short thank you message and let them know you had fun too before turning in for the night."

    scene bg black with fade

    # Day 4, saturday
    $ currentDay = 4
    $ currentDate = "December 4"

    play music "music/home_again.mp3" fadein 1.0
    scene bg home_interior_day with fade

    "It's been a few days since you moved in and you've just about settled into your new life."
    "Most of the anxiety has melted away, and you're now comfortable living as you see fit and taking things at your own pace."
    "This morning you help yourself to a large breakfast, a long hot shower, and plenty of free time to browse the web."
    "Sitting around all day can get kinda boring though."
    "Maybe you should see if Gregg or Angus are free?"
    "Nah, don't want to seem too clingy."
    "You could explore town a bit. There's still a lot you've yet to see."
    "But where exactly would you go?"
    "You pace around the house pondering this question and wind up in what must have been the smoking room, judging by the stench of cigarette smoke permeating the air even after all these years."
    "You thought these things went out of style a century ago but here we are."
    "Not like a little smoke bothers you at this point though."
    "You recline in one of the big fancy chairs in the room and close your eyes."
    "Maybe you'll just nap away the boredom."
    "..."
    "No, this is too boring."
    "Your hand wanders over to the side table and picks up the book that was resting on it."
    "You lazily turn your head to the side and read the title."
    "\"Cryptids of the Western Hemisphere.\""
    "Opening it up to the bookmarked page, you find an article on the Jersey Devil, a weird skinny goat thing with wings."
    "The paranormal sure loves its goats, doesn't it?"
    "Upon reading further, it appears the Jersey Devil is nothing more than a fabrication by hysterical religious country bumpkins."
    "There's not even anything unique about him, he's just a winged goat with devil connotations who sometimes steals chickens."
    "As you close the book, your fingers brush against a bump on its spine."
    "Turning it over reveals a sticker, not unlike the kind you'd find on a library book."
    "Hold on a second, this *is* a library book!"
    "This thing must have been sitting here overdue for ages!"
    "You should return this to the library soon. You're certain they're just dying to get this book back."
    "They might even be so glad to see it again that they'll waive the late fee."
    "It's not like they could charge you a fee if even they wanted to, right?"
    "It's not your book, you just happened to find it."
    "Regardless of the consequences, you've been given a quest and you intend to see it through to the end."

    stop music fadeout 1.5

    "This is the most excited you've ever been to go to the library."

    scene bg library_floor1 with fade

    play music "music/deweydecimal_loop.mp3" fadein 1.0

    "Possum Springs sure has an impressive library."
    "It's a three story building with lavish old-timey architecture and has been very well maintained."
    "Gargoyles adorn the outside while giant pillars and arches frame the murals on the inside."
    "The interior has been modernized with new carpet and a fresh coat of paint that accentuate the comfortingly dim lighting."
    "You stare at the multitude of books organized neatly on shelves as you walk up to the reception desk. Sitting there is the same bear you met at the cafe the other day."
    "What did the barista call her?"
    "\"Selmers?\""
    "She looks up from writing something in a notepad."

    show selma neutral flip at right with dissolve:
        yalign selmaheight

    selma "Oh hey, it's you."

    player "Hey."
    player "You're... Selmers, right?"

    "Her carefree demeanor wavers slightly and there's a hint of disdain in her voice."

    selma "That's what most folk call me."
    selma "I remember you from Posspresso but I didn't get your name."

    player "[name]."

    selma "Nice to officially meet you, [name]."
    selma "Welcome to the Possum Springs Public Library. Is there anything I can do for you?"

    "You take one last look at the book in your hand then slide it over the counter."

    player "I found a book that belongs here and wanted to return it."

    "Selmers picks up the book and gives it a look over with an intrigued expression before scanning it into the system."
    "She rotates her chair to face the computer monitor and clicks the mouse a few times."

    selma "Wow, this was checked out way before I even started working here."
    selma "Where'd you find this?"

    player "It was uhh..."

    menu:
        "Lying at the bottom of a well":
            player "...lying at the bottom of a well."
        "Left in an abandoned house":
            player "...left in an abandoned house."
        "Sitting on a bench":
            player "...sitting on a bench."

    #suspicious selma sprite goes here
    selma "Hmm."

    #back to normal sprite
    selma "That explains why it never found its way back here until now. Glad you returned it, it's the only copy we had."

    player "I don't have to pay the late fee, do I?"

    "That gets a chuckle out of her as she sets the book aside."

    selma "Naw, consider it on the house. It was probably written off as lost forever, so thanks for bringing it back."

    player "No problem."

    selma "Will that be all? Or would you like to get a library card while you're here?"

    "You raise a brow."

    player "How'd you know I didn't have one?"

    selma "I know everyone who has one."
    selma "Possum Springs is a small town and the number of people here who have a library card in 2021 is even smaller."

    player "Oh."
    player "Well since I'm here, I might as well."

    selma "Aight. Just need you to fill out this form and show me a valid ID."

    "She pulls a sheet of paper out from a filing cabinet and pushes it toward you."
    "You grab a pen from the holder and quickly fill it out."
    "Once you're done, you pull out your driver's license and pass both it and the sheet back to Selmers."

    selma "K, just have to type this in real quick..."

    "She looks over your license and makes a few keystrokes before handing it back."

    selma "...and now all of this..."

    "She waves the application form in the air."

    selma "...then scan it in and print your card from the office."
    selma "You're welcome to explore and find some books to check out while I do that. I'll have your card ready by the time you're done."

    player "Ok! Be back in a bit."

    hide selma with dissolve

    "You leave her to her work and go over to the bookshelves across the room, skimming over book titles without really reading them."
    "You're not looking for anything in particular but maybe something will grab your attention."
    "Nope, nothing here stands out."
    "That elevator in the corner of your eye however is a different story."
    "This floor seems to be dedicated to boring nonfiction, so the fiction section must be up above."
    "That's probably where that book you just returned will get shelved. You wonder if there are any others like it your father might have checked out as well."
    "It's kinda weird. Like you're retracing the footsteps your father took at some point."
    "You feel like you're following a treasure map and slowly piecing together his interests along the way."
    "It's neat seeing what he was like, but it also fills you with remorse for not getting to know him better while he was alive."
    "He'll always be some vague idea of a man in your mind and not someone you had a real bond with."
    "You shake off the feelings bubbling inside you and go call down the elevator."

    stop music fadeout 1.0

    "You've kind of lost interest in the books around you but you still want to finish exploring the library at least."
    "The doors open with a mechanical grinding sound and you ride up to the second floor."

    play music "music/Stagnant_Tone-down.mp3" fadein 2.0

    "Here the walls are painted a salmon pink and minty green and the lights are brighter. It no longer has that regal feeling of the first floor, but it's still warm and comforting here."
    "Desks with computers line the nearest wall and lead into the children's book section, as evidenced by the Charity Bearity mural thing in the corner."
    "You turn away from it and head down an aisle more suited to your age, where you spend some time reading titles and a few back cover descriptions to get your mind off things."
    "Your browsing leads you down each aisle until you reach the last one, where you discover a young mouse sitting on the floor among a pile of books."
    "She seems to be so engrossed in the book in her hands, she doesn't notice of your presence."
    "You consider leaving so as to not disturb her, but then you spot the poorly lit sign indicating that this is the horror section."
    "This would be where where the cryptids book and any others similar to it would be found, right?"
    "You curiously enter the aisle and make your way through it, scouring the titles."
    "You keep an eye out for anything related to cryptids, trying not to make any noise."
    "As you're perusing a shelf, you feel your leg bump into something and hear a startled squeak from beside you."

    show lori anxious3 flip at left with dissolve:
        yalign loriheight

    "You look down and see the mouse girl pressed up against the bookshelf, frozen in place with the look of a deer caught in the headlights."
    "You step back and clear your throat, about to say \"Excuse me\" when suddenly she lets out the breath she'd been holding in."

    show lori breath flip

    lori "*Huff huff huff* Sorry, sorry!"

    show lori sad2 flip

    "She hastily shovels her books aside so you can get past."

    player "No, I'm the one who should be apologizing..."

    show lori anxious3 flip

    "She glances back up to you."

    lori "Wait a minute... Haven't I seen you before?"

    "Your memory finally catches up and you recognize her as the girl who was listening to that weird music on the ride into town."

    lori "You were on the bus the other day, weren't you?"

    # if player asked her to turn down music and was rude:
    if loriInteractionRude == True:

        player "Oh yeah, I remember you!"
        player "I think your music is what's been giving me nightmares lately."

        show lori sad flip

        lori "I just keep getting in your way I guess..."

        "She mumbles, looking away."
        "You shrink down, realizing how rude you're being."
        "You should try being more amicable."
        "And if that doesn't work, you could always just leave her alone."
        "The girl clears her throat and looks back up to you."

        show lori anxious2 flip

        lori "So are you visiting Possum Springs or something?"

        player "I just moved in actually."
        player "My name's [name]."

        lori "Lori."

        "You squat down and crane your neck to read the titles of the books in her little pile."

        player "Whatcha reading?"

        show lori neutral flip

        "She seems to lighten up in response to your interest in her reading material."

        lori "Oh these? Just some spooky stories to read in the dark."

        player "You a big horror fan?"

        lori "Well, I *am* going to film school to make horror movies."

        player "Really? What kind of movies do you watch?"

        show lori nervous2 flip

        lori "Uh, scary ones? Ones about existential dread and incomprehensible terrors mostly but I also watch a ton of monster movies."

        player "Nice! That reminds me, I just returned a book on monsters. \"Cryptids of the Western Hemisphere\" is what it was called I think."

        show lori neutral flip

        "Lori's eyes go wide in excitement."

        lori "I've been looking for that book for forever! I used to check it out all the time when I was a kid!"
        lori "It's kind of a cliché but my favorite cryptid is the skinwalker. The stories about them always felt the most realistic, even if they did get samey."

        player "Yeah? Mine's uh, the Jersey Devil. It's supposed to live around this area haha."

        lori "That's true!"
        lori "I tried hunting for it when I was younger. I'm still not convinced it won't show up out of nowhere one day."

        "You can tell she's really into this kind of stuff. Her ears are perked up and her voice is eager to go on and on about it."
        "You listen to her ramble about scary things, just smiling and nodding your head until she asks a question."

        lori "Hey, have you seen the movie The Nightmare Before Longest Night?"
        lori "Some friends of mine are throwing a little party this evening at the bakery and we're gonna watch it."
        lori "And I figured since you're new in town and like spooky things you might wanna come?"

        player "Sure, that'll be fun!"

        lori "Awesome! See you there!"

        player "You bet!"
        player "I guess I'll let you get back to your books now. See you later!"



    # if player changed seats without talking to her
    if loriInteractionNull == True:

        player "Oh yeah, I remember you!"
        player "Do you live here? I just moved in the other day."

        show lori neutral flip

        lori "Yup! Been here my whole life til I started going to film school a few months ago. I'm here on break now."

        player "Nice! What kind of films do you like?"

        lori "Most kinds, but horror in particular. Like, existential dread and incomprehensible terrors but regular monster movies are cool too!"

        player "Yeah I noticed you have a knack for horror. Funny enough, I just got finished returning a book on cryptids."

        "You squat down and pick up a book from the pile scattered on the floor, reading the title. \"Picnic by the Roadside.\""

        lori "It wouldn't happen to have been \"Cryptids of the Western Hemisphere\" would it?"

        player "How'd you know?"

        lori "I've been looking for that book forever! I used to check it out all the time as a kid but I haven't seen it in a while. It's one of the best encyclopedias on cryptids!"

        player "Hopefully they'll put it on the shelf soon and you can snag it before anyone else does."

        lori "That would make my day."
        lori "What's your favorite cryptid?"
        lori "I know it's kind of cliché but mine's the skinwalker. The stories about them always felt the most realistic, even if they did get samey."

        player "Yeah? Mine's uh, the Jersey Devil. It's supposed to live around this area haha."

        lori "That's true!"
        lori "I tried hunting for it when I was younger. I'm still not convinced it won't show up out of nowhere one day."

        "You can tell she's really into this kind of stuff. Her ears are perked up and her voice is eager to go on and on about it."
        "You listen to her ramble about scary things, just smiling and nodding your head until she asks a question."

        lori "Hey, have you seen the movie The Nightmare Before Longest Night?"
        lori "Some friends of mine are throwing a little party this evening at the bakery and we're gonna watch it."
        lori "And I figured since you're new in town and like spooky things you might wanna come?"

        player "Sure, that'll be fun!"

        lori "Awesome!"
        lori "Before I forget, what's your name?"

        player "[name]."

        lori "Lori."

        player "Nice to meet you Lori!"

        lori "Likewise!"

        player "I guess I'll let you get back to your books now. See you later!"


    # if player asked about the music and was bold
    if loriInteractionBold == True:

        player "Hey! What a coincidence seeing you here!"

        lori "Not really. Possum Springs is like, really small. We would have run into each other sooner or later."

        player "Seems like it! I don't believe I caught your name earlier. I'm [name]."

        lori "Nice to meet you again, [name]! I'm Lori!"

        player "I still haven't gotten around to listening to that album yet but it's on my to do list. Been adjusting after moving in."

        show lori neutral flip

        lori "I get that, resettling and stuff. I've been away from home for a while and I'm getting used to living next to train tracks again."

        player "Oof. I live a little bit away from them and have a bunch of trees to block out most of the noise but the trains are still pretty loud."

        lori "To think I used to play and take naps and read books right between the tracks."

        player "That sounds... dangerous."

        lori "It is."

        player "Huh."

        "You squat down and take a look at some of the books strewn about. Most of them are from this aisle apparently."

        player "So are you reading here?"

        lori "Just some spooky stories to read in the dark. It's technically studying material."

        player "Studying for what?"

        lori "Film school assignments!"

        "She holds up a book, \"Monster Design in Cinema.\""

        player "Cool! That reminds me, I just returned an encyclopedia on weird creatures. \"Cryptids of the Western Hemisphere\" is what it was called I think."

        "Lori's eyes go wide in excitement."

        lori "I've been looking for that book for forever! I used to check it out all the time when I was a kid!"
        lori "It's kind of a cliché but my favorite cryptid is the skinwalker. The stories about them always felt the most realistic, even if they did get samey."

        player "Yeah? Mine's uh, the Jersey Devil. It's supposed to live around this area haha."

        lori "That's true!"
        lori "I tried hunting for it when I was younger. I'm still not convinced it won't show up out of nowhere one day."

        "You can tell she's really into this kind of stuff. Her ears are perked up and her voice is eager to go on and on about it."
        "You listen to her ramble about scary things, just smiling and nodding your head until she asks a question."

        lori "Hey, have you seen the movie The Nightmare Before Longest Night?"
        lori "Some friends of mine are throwing a little party this evening at the bakery and we're gonna watch it."
        lori "And I figured since you're new in town and like spooky things you might wanna come?"

        player "Sure, that'll be fun!"

        lori "Awesome!"

        player "I guess I'll let you get back to your books now. See you later!"



    "You give her a friendly smile and stand back up."

    lori "Bye!"

    "She waves a tiny paw at you then resumes reading while you scoot around her and out of the aisle."

    hide lori with dissolve

    "Where to now?"
    "There's still another floor to explore. You've just about exhausted your options on this floor so it's time to head up."
    "The elevator rattles louder this time as its doors open and close, making you question just how safe this thing really is."

    stop music fadeout 2.0

    "Safe enough to get you to the third floor unharmed is the answer you get soon enough."
    "Dust floats through the air, tickling your nostrils as soon as the elevator doors open."
    "The lighting on this floor is much more subdued and the walls are painted a dark blue. "
    "You creep forward, wondering if there's anybody up here."
    "It's dead silent save for the sounds of the heating unit. You pass by each aisle and confirm you're alone."
    "Come to think of it, this whole building is pretty empty. It's just you, Selmers, and Lori, each on different floors."
    "Selmers was right about not many people using the library these days."
    "Getting back to the matter at hand, you wonder what the purpose of this floor in particular is."
    "A quick look around reveals it's for really old media and records apparently."
    "Things like last century's yearbooks, outdated almanacs, newspaper clippings, and even some tomes that remind you of the ones back home."
    "As you're scouting the area, something catches your eye: a big glowing box on one of the desks."
    "It looks like one of those old tube computer monitors, but even bulkier."
    "And warmer."
    "You can feel the heat coming off it from a few feet away."
    "This must be one of those microfilm projector things."
    "A microfiche, you think it's called."
    "There's no film loaded into it though so there's nothing on the screen."
    "Someone must have forgotten to turn it off when they used it last."
    "You flip the power switch off, plunging the room into near total darkness."
    "Welp, that about concludes your tour of the library today."
    "You make your way back to the elevator and return to the ground floor. Selmers should have your card ready by now."
    "As you walk up to the counter empty handed, the bear looks up with a casual grin."

    show selma neutral at right with dissolve:
        yalign selmaheight

    selma "Find what you were looking for?"

    player "Not quite, but that's more my fault than the library's."

    selma "If you're looking for a book in particular, I can help you find it if we have it."

    player "Thanks, I'll keep that in mind."

    selma "I also got your card printed. Here ya go."

    "She slides the card over the counter."

    selma "It expires three years from today, or one year after your last check out. Whichever comes first."

    player "Thank you!"

    selma "Wish I got paid commission for these. But I don't. Haha."

    player "How often do you convince someone to sign up for a card?"

    selma "Almost as often as someone new comes in."
    selma "I have experience in sales."

    player "Wow."

    selma "And if you don't mind me trying to sell you on something else, the library's hosting an event this coming Tuesday at 4:00PM where we read books aloud to small children."
    selma "We're short on staff so we're asking for volunteers."
    selma "It'd be nice if you could, y'know, come and read for the kids. We'll have juice and cookies too."

    menu:
        "I'll think about it.":
            $ selmaNeutral = True

            player "I'll think about it."

            selma "That's better than a flat out no I guess."

            "You can't help but feel a twinge of guilt. You look away momentarily, mulling over whether you should go or not."

            selma "Anyway is that all I can do for you?"

            "You refocus your attention back to her."

            player "Oh, yeah. Thanks, have a nice day."

            selma "You too."

        "Sorry, don't think I can make it.":
            $ selmaBad = True

            player "Sorry, don't think I can make it."

            selma "I expected as much. Don't worry, we'll find someone else."
            selma "Or I'll just pull double duty like last time."

            player "That understaffed, huh?"

            selma "Yup."

            "You can't help but feel some sympathy toward her. Maybe you could come out and help for an hour or two."

            selma "Well if you change your mind, let me know."

            player "Will do."

            selma "Anyway, do you need assistance with anything else?"

            player "Nope. I'm good, thanks."

            selma "K. Have a nice day."

            player "You too."

        "I'd be happy to!":
            player "I'd be happy to!"
            $ selmaGood = True

            selma "That- was not the response I was expecting. You sure? Those kids can be real punks sometimes."

            player "It's no trouble, I can handle them."

            selma "If you say so. Let me know if you change your mind later."

            player "Sure."

            selma "Thanks though. It means a lot and it would be cool seeing you here."

            "She has a genuinely appreciative smile on her face, but there's something else behind it you can't quite grasp."
            "Does she just want you to come help out or is there more to it?"

            selma "Anyway is there anything else I can do for you?"

            "You refocus your attention back to the conversation at hand."

            player "Oh yeah, no I'm good."

            selma "Ok. Hope you have a nice day!"

            player "Thanks, you too!"

    hide selma with dissolve

    scene bg bakery with dissolve

    "On your way home, you think about how surprisingly lively Possum Springs is."
    "Already you've been invited to several events and met some pretty cool people."
    "You never imagined how much happier you'd be living out here."
    "When you get to your house, you decide to make some lunch and chill out until evening."
    "Nightfall creeps up on you quickly and you suddenly realize you don't have a specific time to be at the bakery."
    "Wait a minute, bakery? Like the one Gregg and Angus live above?"
    "Surely they'd know something about a party underneath their apartment."
    "You shoot them both a text and wait a while."
    "No response."
    "Screw it, you should just head out now. Better to be early than to arrive after the party's over."
    "You hastily freshen up, then hop on your bike and ride into town."
    "As you pull up to the store, you hear the final notes of a song blasting from inside, rattling the windows."
    "Bright light leaking through inhibits your view of the interior until you step inside and your eyes adjust."

    play music "music/whenskiesclear_loop.mp3" fadein .5

    "Standing on the stage are some familiar faces who are just as shocked to see you as you are to find them here."
    "Gregg with a guitar, Angus at the mic, Mae on bass, and Bea from the hardware store next to a keyboard and laptop."

    show bea at right:
        xalign 2.0

    show angus at left:
        xalign -1.0

    "On the wall behind them is a DVD player screensaver being displayed from a projector mounted on the ceiling."

    show lori neutral at right:
        yalign loriheight
        xalign 1.02
    with dissolve

    lori "[name]! You made it!"

    "You look to the source of the voice. You didn't even notice the mouse girl sitting at one of the tables. She stands up and runs toward you."

    lori "Sorry I forgot to give you a time to come. To be honest I wasn't sure when we were meeting!"

    player "Uh, it's fine."

    "You're still confused from discovering Gregg and Angus are in a band with Mae and the hardware store girl."

    lori "Guys, this is [name]! [name], that's Gregg, Angus, Mae, and Bea!"

    "She points to each of them as she lists their names."

    player "I've already met everyone, actually."

    "Gregg hops down from the stage with his guitar still strapped over his body."

    show gregg neutral flip at left:
        yalign greggheight
        xalign -.12
    with dissolve

    gregg "Yeah, we played video games and ate pizza the other day."

    show lori breath

    lori "Whaaaaaat? Really??"

    show bea neutral at right:
        yalign beaheight
        xalign .9
    with moveinright

    bea "Mae and I saw them at the Ol' Pickaxe too."

    lori "Oh gosh, I-I thought..."

    "Lori trails off and shrinks down in shame."

    show angus neutral flip at left:
        yalign angusheight
        xalign .12
    with moveinleft

    angus "It's cool. [name] is cool."

    lori "Sorry for inviting [name] without knowing if it was ok... I thought it was going to be a bigger party..."

    gregg "No, it's fine. Tell ya what, we'll go out to eat after putting things away here. You hungry, [name]?"

    player "I could eat."

    bea "I can make time for something quick at the diner. And I can get dinner to-go for my dad while we're there."

    gregg "Cool! Let's pack up and get the heck outta here!"

    "Gregg hops back on stage and kicks open his worn guitar case. Angus, Bea and Mae go ahead and start putting their things away while Lori waits at a table."

    hide lori
    hide gregg
    hide angus
    hide bea
    with dissolve

    show mae neutral at right:
        xalign 1.5

    menu:
        "Offer to help clean":
            #+1 trust

            player "Let me help you with that!"

            show gregg neutral flip at left:
                yalign greggheight
            with dissolve

            gregg "Hm? Oh sure. Can you unplug those amps and put 'em in the storage closet over there?"

            player "'Course!"

            "You readily do as he requested while the others put away their instruments."
            "Angus coils up the mic wire and collapses the tripod while Bea folds up the table her keyboard was on and stuffs the laptop in her bag."
            "Mae strummed on her bass a few times, adjusting the tuning before putting it away in a case and helping out with general cleaning."
            "She was awfully quiet and seemed to keep her distance from you, only occasionally making weird glances in your direction. She whispers something to Bea."
            "You brush it off and finish helping, bumping into Gregg as he stowed the last speaker."

            player "I didn't know you guys were in a band. I thought this was just gonna be a movie party."

            gregg "Is that what Lori told you? We ended up watching the movie early on, then Bea wanted to test a song she's been writing."

            player "Bea writes music?"

            gregg "Yeah, she just finished going to school for that sort of thing."
            gregg "Honestly, I haven't picked up my guitar in ages and kinda suck at playing now."
            gregg "But it was fun getting together and playing again!"

            player "I never would have imagined all you guys were in a band."

            gregg "Believe me, this is the least crazy thing about us."
            gregg "Hey be right back, I need to hit the bathroom."

            hide gregg with dissolve
            show bea neutral at right:
                xalign 2.0

            "The fox locks away all the gear with a key then heads to the back of the building and out the exit door."
            "Rather than question where exactly he's going, you decide to approach Lori who had been seated at a table looking stressed as she scrolls through her phone."

            show lori sad at right:
                yalign loriheight
                xalign 1.06
            with dissolve

            player "You ok?"

            show lori neutral

            lori "Huh? Oh, yeah I'm fine! You guys done?"

            player "I think so. Just waiting on Gregg to get back."

            "You chat with Lori while Mae, Bea and Angus converse amongst themselves."
            "After a minute or so Gregg walks back in and approaches you. The others hop down from the stage and gather around."
            "The crocodile has her bag slung over one shoulder and her keyboard pinned between her arm and her side."

            show bea neutral at right:
                yalign beaheight
                xalign .96
            with moveinright

            bea "Ready to go?"

        "Hang back with Lori":
            $ loriAP = loriAP + 1

            show bea neutral at right:
                xalign 2.0

            "You pull up a seat across from Lori, who looks stressed as she scrolls through her phone."

            show lori sad at right:
                yalign loriheight
                xalign 1.06
            with dissolve

            player "You ok?"

            show lori neutral

            lori "Huh? Oh, yeah I'm fine!"
            lori "...Sorry I made things awkward earlier."

            "You shrug nonchalantly."

            player "Don't worry about it. It all worked out in the end."

            if loriAP > 1:
                lori "Shame you missed out on the movie though... maybe we can watch it together another time?"

                player "I'd love that! It's been ages since I've last seen it!"

                lori "I watch it every year hahaha!"

            else:
                lori "Yeah..."

            "Out of the corner of your eye you see Gregg rush out the exit toward the back of the building while the others finish putting everything away."

            player "Hey so, dumb question, but are they like, in a band?"

            "You gesture toward the group on the stage."

            lori "Oh! Yeah, well, they used to be. But Bea just finished her degree in music studies and wanted to test a song she's been writing so they brought out all their old instruments."

            player "Wow. Did it turn out well?"

            lori "Nnnnot really. Gregg's pretty rusty with his guitar."
            lori "Don't let him know I said that though!"

            "Just then, Gregg returns from whatever it was he was doing and everyone gathers around the table you and Lori are seated at."
            "Bea has her bag slung over one shoulder and her keyboard pinned between her arm and her side."

            show bea neutral at right:
                yalign beaheight
                xalign .96
            with moveinright

            bea "Everything's packed up. You ready to go?"


    show angus neutral at left:
        yalign angusheight
        xalign -1.0

    show gregg neutral flip at left:
        yalign greggheight
        xalign -.2
    with moveinleft

    gregg "Yup!"

    show angus neutral flip at left:
        yalign angusheight
        xalign .12
    with moveinleft

    angus "Indeed!"

    lori "Mh-hm!"

    player "Yeah!"

    show mae sad1 at right:
        yalign maeheight
        xalign .67
    with moveinright

    mae "Sure."

    "Bea adjusts her grip on the keyboard and turns toward the door."

    bea "Let's roll."

    hide mae
    hide gregg
    hide bea
    hide angus
    hide lori
    with dissolve

    "You all file out through the doorway and into the cold dark street."

    stop music fadeout 1.5

    show bea neutral at right:
        yalign beaheight
        xalign 1.08
    with dissolve

    "Bea turns toward the group and does a headcount."

    bea "There's too many of us to fit in my car so I guess we're walking."

    show angus neutral flip at left:
        yalign angusheight
        xalign .08
    show gregg neutral flip at left:
        yalign greggheight
        xalign -.1
    with dissolve

    gregg "I volunteer to sit in Angus's lap to make space."

    bea "That would work if I didn't have a big box of records in the passenger seat, and a keyboard soon to be occupying the back."

    gregg "Aww."

    hide gregg
    hide angus
    with dissolve

    bea "Be right back."

    hide bea with dissolve

    "Bea starts toward the Ol' Pickaxe where her car is parked."

    show mae panic flip at left:
        yalign maeheight
    with dissolve

    mae "I'll go with you!"

    "Mae hastily runs off to catch up to Bea."

    show mae at right:
        yalign maeheight
        xalign 2.0
    with move
    show bea at right:
        yalign beaheight
        xalign 2.0

    "You consider going with them just so your body can warm up by walking but the moment of opportunity has already passed."
    "You're all just standing here with nothing else to do so why not break the ice?"

    show angus neutral flip at left:
        yalign angusheight
        xalign .0
    show gregg neutral flip at left:
        yalign greggheight
        xalign -.12
    show lori neutral at right:
        yalign loriheight
        xalign 1.06
    with dissolve

    player "So why is there a stage in the middle of the bakery?"

    angus "It's a holdover from the previous business. We used to break in and play music on it way back in the day."
    angus "No need for breaking in now."

    gregg "Lame."

    angus "Nowadays it usually gets used for banquets and whatever other local events need a stage."

    lori "Like the Harfest play!"

    gregg "Yeah, like that thing literally nobody cares about but we still do for some reason."

    "You stand around idly chatting waiting for Mae and Bea to come back."
    "How long does it take to put away a keyboard??"

    show bea neutral at right:
        yalign beaheight
        xalign 1.0
    with moveinright
    show mae sad1 at right:
        yalign maeheight
        xalign .7
    with moveinright

    "Seems Lori was thinking the same thing. When the pair finally return, she makes a quip."

    lori "Did ya get lost along the way?"

    bea "Har har. Come on, we doing this or not?"

    mae "Yeah. Let's go."

    hide gregg
    hide angus
    hide lori
    with dissolve

    "Bea stands between you and Mae as your party advances, footsteps crunching against the snow."
    "While the others joke and converse, you sneak a glance at Mae. You can feel that there's something conflicting her and that she doesn't want to be here."
    "Unfortunately you don't know what you can do about it other than feel bad for her."

    hide bea
    hide mae
    with dissolve

    show mae neutral at right:
        xalign 2.0

    "The diner turns out to only be a few blocks away. It's a repurposed train car with an orange neon sign reading CLIK CLAK DINER."

    show angus neutral left:
        yalign angusheight
        xalign -2.0
    show lori neutral right:
        yalign loriheight
        xalign 2.0

    show gregg neutral flip at left:
        yalign greggheight
        xalign -.15
    with dissolve

    gregg "Here we are!"

    "Gregg holds the door open for everyone. Inside, you're met with a cramped, cluttered space, vaguely reminiscent of Art Deco design, covered with photos, paintings, and other artwork on the walls."
    "You're seated at a booth and given a menu that has the typical diner offerings."
    "Pizza, burgers, bacon and eggs, club sandwiches, and even pierogies. You all make your selections and chat while the food is cooked."

    show bea neutral at right with dissolve:
        yalign beaheight
        xalign 1.18

    bea "So [name], I heard you moved here recently? What are you doing in Possum Springs?"

    player "Eh, just wanted to get away from home, ya know? Move out and be independent and all that stuff."
    player "I have to say, I'm enjoying Possum Springs a lot more than I thought I would."

    bea "Really? Almost everyone I know can't wait to escape from here."

    "A subtle hush falls over the group. Bea quickly changes the topic."

    bea "Anyway, you got a job here yet?"

    player "Nope. Living off of savings at the moment. Why, you know anybody who's hiring?"

    show lori neutral at right:
        yalign loriheight
        xalign .85
    with dissolve

    lori "I could scrounge together something and pay you a little if you help me work on my movie."

    player "You're making a movie?"

    lori "Yup! It's partly a school project but it's also something I just wanna do."
    lori "I'm out in the woods or by the tracks nearly every day if you wanna come and watch or set up equipment or maybe even act in it?"

    player "Sounds spooky. I'll definitely consider it."

    "Lori giggles at your choice of words."

    bea "*Ahem*"
    bea "I could use a hand at the shop if you're interested. Backbreaking work but decent untaxed, under the table pay."

    player "What do I have to do?"

    bea "Lift heavy stuff, maybe direct a customer toward said heavy stuff, and on rare occasion move the heavy stuff to their car."

    player "Noted. I'll consider that as well."

    show angus neutral flip at left:
        yalign angusheight
        xalign .0
    with dissolve

    gregg "I could try putting in a good word for you at Ham Panther. I don't think they're hiring right now though."

    angus "I've got my paws full just trying to pay myself at the bakery so..."

    gregg "Maybe Mae could get you something at the arts council if you're into that."

    "All eyes turn toward an unsuspecting Mae. She looks like she wasn't paying much attention to the conversation and was caught off guard."

    show mae panic at right:
        yalign maeheight
        xalign .7
    with dissolve

    mae "Oh uh, yeah. I teach art stuff at the Deep Hollow County Arts Council on Fridays and Saturdays. Painting, clay sculpting, photography..."

    lori "Mae's the one who taught me how to use a camera!"

    show mae sad1

    "Mae shrugs."

    mae "At this point, Lori's more comfortable with cameras than I am. I just know enough to teach the basics."

    player "Gotchya. I'll check it out if I'm feeling artsy."

    show mae neutral

    "Mae flashes you a forced smile. Luckily the awkward moment is interrupted by the waitress coming by with your food."
    "Food has a way of lightening the mood. Mae relaxes and even becomes more talkative as the evening goes on."
    "Even though your meal isn't very good, you still have a pleasant time with your new friends."
    "Towards the end of the night, Bea gets a box for her leftovers and the waitress drops off the meal she ordered for her father."
    "When it comes time to pay the bill, Gregg insists that he cover for you but you politely decline, knowing you can spare the cash more comfortably."
    "Ironically, Angus is the one to put down his debit card for both himself and Gregg."
    "Bea pays for her own, and Mae asks the waitress to put hers and Lori's meals on one bill."

    show mae blush

    "Lori wordlessly expresses her gratitude by resting her head on Mae's shoulder and wrapping her arm around Mae's. For the first time this night you see Mae smile in earnest."

    #scene transition

    show mae neutral

    "Once you're outside, you all crowd around under a streetlight and discuss your plans for the rest of the night."

    gregg "This was great. We should do this again."

    lori "Yeah, it was awesome seeing you guys playing as a band again!"

    "Bea lights a cigarette."

    bea "Always a joy. But I think I'm gonna go home, relax and watch some TV with my dad now."

    lori "Hmm, yeah I should get home too before my dad starts worrying where I am so late."

    mae "I'll drive you home so you don't have to walk back in the dark Lori."

    lori "Thanks!"

    gregg "Me and Angus will probably watch some streams then go to sleep."

    player "Yeah, sleep sounds good right about now. It was fun hanging out with you all though."

    bea "Before I forget, you have Chattrbox right? Add me and we can talk more about having you work at the Pickaxe."

    lori "Oh and add me too in case you decide to help me out on my film!"

    "You pull out your phone and get their Chattrbox names."
    "You'll have to wait until you have wifi again before it registers but it's no big deal. You pocket your phone and give them a smile."

    player "Sweet. I'm open to just chatting too if you want."

    bea "Sure."

    lori "Of course!"

    hide lori
    hide gregg
    hide angus
    hide bea
    hide mae
    with dissolve

    "You walk as a group back to the bakery before parting ways. Gregg and Angus go around to the back of the building, while Mae, Bea and Lori go to the parking lot by the Ol' Pickaxe."
    "You hop on your motorcycle and rev her up for the trip home, where you promptly get ready for bed."
    "You add Bea and Lori to your Chattrbox then set your phone to 'Do not disturb' mode and fall asleep with your face buried in your pillow."

    scene bg black with fade


label church1:
    # day 5, sunday, dec 5
    scene bg home_interior_day with fade

    "Your first week in Possum Springs has come to a close."
    "Really this is only your sixth day here, but it's Sunday so you're counting it as having been a week."
    "Each new day further cements your routine. Wake up, shower, eat breakfast, play around on the internet for a bit, and so on."
    "The excitement of moving into an unfamiliar town has worn off, yet you still seek the thrills you've felt over the past few days."
    "You should get out of this dusty old house and go on an adventure today."

    #scene bg outsidePlayerHouseSnowClearSky
    play sound "sound/door open and close.mp3"
    scene bg home_exterior_night with fade

    "The snowstorm has finally subsided."
    "The skies are bright and clear once again, but the ground is going to be covered with a thick blanket of snow for a while."
    "That shouldn't hinder your ability to get around though. \nNow then, where shall you go today?"
    "Why not visit the top of that big hill in town? You bet you can see everything in Possum Springs from up there!"

    jump churchScene1

label jobs1:
    # day 6, monday
    $ currentDay = 6
    $ currentDate = "December 6"
    scene bg home_interior_day with fade

    "Another day, a new adventure awaits."
    "Or something like that."
    "Either way, you make yourself presentable and prepare to go out."

    menu:
        "{cps=0}Where do you want to go?{/cps}"
        "Ol' Pickaxe" if workingWithBeaCompleted == False:
            jump workingWithBea
        "Help Lori with film project" if loriHelpCompleted == False:
            jump loriFilm
        "Check out the arts council" if maeArtsCompleted == False:
            jump maeArts
            
      
label day7:
    #day 7, tuesday, dec 7
    #

    #add a random event where you hang out with germ. maybe you see him hauling animal feed across town in a stolen shopping cart, making him look homeless
            
            
            
label jobs2:
    # day 8, wednesday, dec 8
    "Another day, a new adventure awaits."
    "Or something like that."
    "Either way, you make yourself presentable and prepare to go out."

    menu:
        "{cps=0}Where do you want to go?{/cps}"
        "Ol' Pickaxe" if workingWithBeaCompleted == False:
            jump workingWithBea
        "Help Lori with film project" if loriHelpCompleted == False:
            jump loriFilm
        "Check out the arts council" if maeArtsCompleted == False:
            jump maeArts
            
            
            
            
            

    

label day9:
    # day 9, thursday
    $ currentDay = 9
    $ currentDate = "December 9"

    scene bg home_interior_day with fade

    "As you're eating breakfast, a you suddenly feel like you're forgetting something."
    "Wasn't there something you were supposed to do today?"
    "Oh yeah, Selmers is hosting an event at the library this afternoon and asked if you could help out!"
    "Huh?"
    "Your phone just vibrated and a text message appeared on the screen. It's from Lori."
    "It says \"Hey just wanted to let you know me and Gregg are gonna be filming at the historical society this evening if you wanna come help!\""
    "Well shoot, you can't do both."

    menu:
        "{cps=0}Where do you want to go?{/cps}"
        "Library":
            jump selmaLibraryReading
        "Historical Society":
            jump loriGreggHistorical

    label day10:
    # day 10, friday
    $ currentDay = 10
    $ currentDate = "December 10"

    scene bg home_interior_day with fade

    "Another day, a new adventure awaits."
    "Or something like that."
    "Either way, you make yourself presentable and prepare to go out."

    menu:
        "{cps=0}Where do you want to go?{/cps}"
        "Ol' Pickaxe":
            jump beaAntiqueShop
        "Bakery":
            #visit bakery but are surprised by lack of coffee. learn that they have a deal with posspresso where they don't sell coffee and possprsso doesn't sell certain baked goods. angus mentions his favorite drink there and you offer to get him one in exchange for your confection. at the cafe you find selma, and you can give her your treat as apology for missing the library event
        "Explore town":
            jump maeLoriSleepover

label anotherday:
#another germ scene, he slips on ice, you help him home, visit his animal shelter


    label day10:
        # day 10, thursday
        $ currentDay = 10
        $ currentDate = "December 16"
        
        "Another day, a new adventure awaits."
    "Or something like that."
    "Either way, you make yourself presentable and prepare to go out."

    menu:
        "{cps=0}Where do you want to go?{/cps}"
        "Ol' Pickaxe":
            jump beaAntiqueShop
        "bakery":
            #visit bakery but are surprised by lack of coffee. learn that they have a deal with posspresso where they don't sell coffee and possprsso doesn't sell certain baked goods. angus mentions his favorite drink there and you offer to get him one in exchange for your confection. at the cafe you find selma, and you can give her your treat as apology for missing the library event
        "Explore town":
            jump maeLoriSleepover
            


label day:
    #farmer's market?
    #group hangout at ??? with ???
    #germ is invited but couldn't make it
            
            
            
            
            
            
            
            
            
            
            
label nextday:

    menu:
        "Play video games with Gregg and Angus":
            jump dragonsDungeons1
        "Train Tracks" if loriFilmCompleted == False:
            jump loriFilm


    label day11:
        # day 11, friday
        $ currentDay = 11
        $ currentDate = "December 17"

        jump posspresso_group1

    label day12:
        # day 12, saturday
        $ currentDay = 12
        $ currentDate = "December 18"

        menu:
            "Arts Council":
                jump artsCouncilScene
            "Train Tracks" if loriFilmCompleted == False:
                jump loriFilm
            "DnD with Gregg and Angus" if dragonsDungeons1Completed == False:
                jump dragonsDungeons1


    label day13:
        # day 13, sunday
        $ currentDay = 13
        $ currentDate = "December 19"

        menu:
            "Church":
                jump churchWeek2
            "Ol' Pickaxe":
                scene bg pickaxe with fade

                play music "music/picknaxe_loop.mp3" fadein 1.0

                "You head down to the hardware store and find Bea manning the counter."

                show bea apron at right with dissolve:
                    yalign beaheight

                bea "Hey [name]. Me and Selma are going out to the Arts Council tonight for some poetry. You wanna come?"

                player "Sure!"

                bea "Meet us there at around 7:00, k?"

                player "Sounds good. See you then!"

                stop music fadeout 2.0

                bea "See ya."

                hide bea with dissolve

                jump beaSelmaPoetry
            #"Library":
                #jump beaSelmaPoetry
            #give option to go to library as well, selma tells invites player to poetry thing

    label day14:
        # day 14, monday
        $ currentDay = 14
        $ currentDate = "December 20"

        scene bg home_interior_day with fade

        "Welp, it's Longest Night Eve. Better write a scene for this."


    label day15:
        # day 15, tuesday
        $ currentDay = 15
        $ currentDate = "December 21"

        jump longestNightOpening

    label day16:
        # day 16, wednesday
        $ currentDay = 16
        $ currentDate = "December 22"

        jump endDemo


    label olPickaxeWeek1:
        # make beaSelmaPoetry available only after the cafe meetup

        scene bg pickaxe with fade

        play music "music/picknaxe_loop.mp3" fadein 1.0

        "You head down to the hardware store and find Bea manning the counter."

        show bea apron at right with dissolve:
            yalign beaheight

        bea "Hey [name]. Me and Selma are going out to the Arts Council tonight for some poetry. You wanna come?"

        player "Sure!"

        bea "Meet us there at around 7:00, k?"

        player "Sounds good. See you then!"

        stop music fadeout 2.0

        bea "See ya."

        hide bea with dissolve

        jump beaSelmaPoetry


        #menu:
            #"Sure!":

                #player "Sure!"

                #bea "Meet us there at around 7:00, k?"

                #player "Sounds good. See you then!"

                #stop music fadeout 2.0

                #bea "See ya."

                #hide bea with dissolve



                #jump beaSelmaPoetry
            #"Nope.":

                #player "Sorry, I think I'm busy around that time."

                #bea "No big deal. See ya around."

                #stop music fadeout 2.0

                #player "Bye!"

                #hide bea with dissolve

    label endDemo:
        scene bg black with fade
        "That concludes the demo! Thanks so much for playing! Stay tuned for more to come!"
        "Credits"
        "Project Management: Fishy"
        "Writing: Kodiak, Ferrin, MegaBirb, Tymime, Fishy, V-25 Sean"
        "Programming: Kodiak"
        "Music: Tymime, EightbyteOwl, Elias Lang, Ferrin, JunoDeer"
        "Character Sprites: Equestria Prevails, TRPCWings, Balderdash, LataviaBoy1999, Tymime, Starxeil, Lauri, EightbyteOwl"
        "Background Art: Eightbyteowl, Coldiru, Nukathefloof, TRPCWings, Balderdash, LataviaBoy1999, Careybou, WorkerQ, KDD, Lauri"
        "Licensing info: The contents of this game are licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License	https://creativecommons.org/licenses/by-nc-sa/3.0/us/"
        return

    return
