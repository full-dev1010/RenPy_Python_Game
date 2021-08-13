label damien_demo:
    call showCenterText(__("The Stalker"), "100")
    pause

    $ play_audio("bustling_cafe", channel="sound")
    scene bg diner first day
    with dissolve
    $ play_audio("cheerful_music", channel="music")

    "It's a normal busy day at the diner where I work."

    "I'm a waitress here at Normann's Diner. I only work part-time so that I can make ends meet while I go to school."

    "It's not the best-paying job, but it was already hard enough to find employment that would work with my hours."

    "Normann's is a 24-hour diner near downtown where all the clubs and bars are, so we typically get a pretty good flow of
    customers."

    "It also means that we sometimes get very... interesting... characters, like the man who's just been seated in my area. Again."

    "I see him every week on Sunday mornings like clockwork. He comes in at eleven o'clock sharp, sits at the same table every time -
    although I don't know how he manages that - and orders the same thing."

    "I know his order by heart now: the Breakfast Special, with eggs over easy, four pieces of crispy bacon, two sausage links, hashbrowns,
    and two slices of Texas toast."

    "The man himself isn't necessarily weird. He's polite enough, doesn't make much small-talk, and isn't interested in friendly conversation.
    Though he does tip well."

    "He dresses nicely, has an air of superiority about him, and always looks out of place with his appearance of wealth when he sits on the
    green vinyl benches we provide. But he is a {i}little{/i} strange."

    "It's the staring. Despite a relaxed demeanor, his eyes are always moving, following, appraising..."

    "Me."

    "Like he's attuned to my presence, I can feel him watching me for the entire time that I'm within his line of sight. He's never said anything
    to me, never asked for my phone number or been inappropriate, but..."

    "Well, it makes me a little uncomfortable, even though he's handsome. How could it not?"

    "However, no matter how uncomfortable I am with his staring, it's not like I feel threatened or anything. Maybe he's shy. Maybe he's
    super socially awkward. All I really know is that he stares, doesn't really talk, and always looks like a model in the clothes he wears."

    coS "Hey, [playerName]! You better hurry before those plates get cold!"

    "I'm startled out of my thoughts on my strange customer and hurry to go grab the order for another table. It's always busy here and I should
    know better than to space out like that."

    pn "Sorry!"

    "I get my table settled with their food and finally, it's time: I have to go take my 'stalker's' order, even though I already know it."

    "Shelly says that he's harmless and I agree. After all, it's been months since he first started coming in and nothing bad has happened to me."

    "He's just a normal regular who likes to stare, and a customer is a customer. I need this job more than I'm worried about a guy who
    can't keep his eyes to himself."

    "I approach him, putting on my best customer service smile."

    show dam neutral crossed norm
    with dissolve

    pn "Hi, welcome back! Will it be your usual today?"

    s "Not today."

    "I can't help but raise my eyebrows. In all the time that he's come here, he's never ordered anything different."

    "Still, other than that, I don't show my surprise."

    pn "Really? Ready to try something new?"

    "I can't help that it sounds like I'm teasing him. It comes naturally to be friendly and inquisitive."

    "Customer service requires a certain amount of extroversion that I've adapted to well. I'm a naturally friendly person anyways, and
    I do enjoy my job, especially when dealing with friendly customers."

    s "I am."

    "There's an odd pause as I wait for him to continue, but he doesn't, so I break the silence first."

    pn "So, what can I get you?"

    show dam smile loose norm
    with dissolve

    "The man's expression softens suddenly. I've never seen him look anything but serious and cold, so it startles me."

    s "What would you recommend?"

    "That takes me by surprise. I'm caught on my back foot. Already this conversation is longer than any I've ever had with him before."

    pn "Um... well... We have a lot of good food. What are you in the mood for?"

    "To my bafflement, he doesn't make my job any easier."

    s "Whatever you think is best."

    "I quickly review my limited knowledge of him to figure out something he might like. It's my job to make sure he enjoys his meal and
    I feel oddly determined to make the right choice."

    "What would he like the most?"

    menu:
        "Something savory. It's what he always gets, so he must like it.":
            $con += 1
            $dubcon += 1
            jump savory

        "Something sweet. It's good to have variety, right?":
            $noncon += 1
            jump sweet

    label foodChoiceBridge: #No matter the choice, this will be said
            pn "I'll be right back with that."

            hide dam smile loose norm

            "It doesn't take too long for his food to come out, and I hurry to serve him before bustling off to my other tables."

            "When I come back, he's waiting for me with an empty plate."
            return

#==================Savoury======================
    label savory:
            show dam smile soft loose norm
            with dissolve

            pn "How about an omelette? The special is one of my favorites."

            "The man nods, looking like he approves."

            s "I'll have that, then."

            "I feel like I've passed a test and come out on the other side victorious. I can't help but grin happily."

            call foodChoiceBridge

            show dam neutral crossed norm
            with dissolve

            s "You have delightful taste. Thank you."

            "I'm surprised by how sincere and warm he sounds despite his cold expression. It makes my cheeks heat and I can only shake my head in
            embarrassment."

            pn "Thank you, but it wasn't all that much..."

            s "No. Don't deny it. You are a hard worker and do your best to cater to the..."

            "The man looks around the loud, messy diner with a very telling expression."

            show dam sneer crossed norm
            with dissolve

            s "...various {i}clientele{/i} of this establishment."

            "I can't help but frown at his elitist statement and want to speak up in the defense of my family-friendly diner, but he doesn't let me."

            show dam neutral crossed norm
            with dissolve

            d "My name is Damien, by the way."

            "He stands and holds out his hand to shake."

            "It's just one surprise after another today, isn't it? I give him my hand."

            pn "Um, nice to meet you. My name is [playerName]."

            "Then, instead of shaking it, he brings my hand up to his mouth and brushes his lips over my knuckles."

            d "A lovely name for a lovely young woman."

            "Now I'm really blushing. He's a charmer, that's for sure."

            "I can't help but remember how he's been essentially stalking me at my place of work for the past several months. Why speak up now?
            He never has before."

            pn "Th-thank you."

            "I fiddle with my hands and recall that I have his check with me."

            pn "W-well, here you are. I hope you have a great rest of your day."

            hide dam neutral crossed norm

            "I nervously hand him the bill and then walk away, cheeks ablaze. I'm glad that checkout happens at the counter now; I can escape his...
            Damien's... presence without having to talk to him anymore."

            "Fortunately, the rest of my shift goes well, and time seems to fly by. I'm excited to get home, get off my feet, and relax with some TV."

            jump chapter2

#=========================Sweet=======================
    label sweet:
            pn "What do you think of crepes? Our strawberry-cheesecake crepes are the best in town."

            show dam sneer crossed norm
            with dissolve
            "The man clearly doesn't like my answer at all."

            s "I've changed my mind. Get me my usual."

            show dam serious crossed norm
            with dissolve

            "I feel like I've just failed an important test but don't understand what it was or what the stakes were. Instead, I quickly jot
            down the order."

            call foodChoiceBridge

            show dam neutral crossed norm
            with dissolve

            s "The food was excellent, as always."

            "Thinking of my blunder - why on earth had I thought he'd like something sweet? - I nod gratefully."

            pn "I'm glad you enjoyed it."

            "I blush and fiddle with the bill in my hands."

            pn "Well, here's the check..."

            "The man suddenly holds out his hand."

            d "My name is Damien."

            "I can't help but remember how he's been essentially stalking me at my place of work for the past several months. Why speak up now?
            He never has before."

            "Still, it's only polite."

            pn "My name is [playerName]. It's nice to meet you."

            "I take his hand, but instead of shaking it, he brings my hand up and brushes his lips against my knuckles."

            d "A pleasure, [playerName]."

            pn "U-Uhh..."

            "What on earth? He's got me tongue-tied."

            "He then takes the check from me and nods."

            pn "H-Have a good day!"

            hide dam neutral crossed norm

            "I'm still blushing like a tomato as he walks toward the checkout counter."

            "I'm glad I can escape his... Damien's... presence without having to talk to him anymore. He really flustered me."

            "Fortunately, the rest of my shift goes well, and time seems to fly by. I'm excited to get home, get off my feet, and relax with some TV."

            $ stop_audio("music", 2)
            $ stop_audio("sound")

            jump chapter2



label chapter2:

    call clearScene
    call showCenterText(__("The Gift"), "100")

    pause

    scene bg hallway item
    with dissolve
    $ play_audio("relaxed_music", channel="music")

    "It's such a relief to finally be getting home. Today was a long day."

    "After Damien left, I was really off-kilter for a little while. I got back to normal quickly enough, but not before my boss told me off
    for being scatter-brained."

    "I can't help but feel a little uncomfortable with him now, and the thought of seeing him again next Sunday makes me uneasy."

    "It's probably not a big deal, I know. He just asked for my opinion, like many customers often do, and introduced himself. There's no
    reason for me to feel wary, and yet I do."

    "But I just can't shake this feeling of foreboding that's settled on my shoulders from the moment he kissed my hand."

    "It was such an awkward thing to do, but he acted so naturally that no one even batted an eye! My face gets warm again just thinking about
    what people must have thought."

    "I'm distracted as I walk up to my front door, so I don't notice what's there right away."

    pn "Huh?"

    "Lying up against my door are a bouquet of flowers and a package."

    "I haven't ordered anything and today isn't a special occasion, so I have no idea what's in the box or who the flowers are from."

    "Even though it looks like someone just got me something really nice for no reason, I can't help but hesitate to bring it inside."

    "Not thinking too much about it, I pick up the flowers and package and take them inside with me."

    $ play_audio("front_door_open.mp3", channel="sound")

    scene bg bedroom night
    with dissolve

    "I put the flowers - they're my favorite kind, which is a bit odd for someone to know - in a vase on my dining room table,
    adding some water to it to keep them alive longer, before going to my bedroom."

    "After opening the package, I find that the interior is covered in protective plastic."

    "I look inside, pulling out the bubble wrap hiding the gift. I gasp as I see a jewelry box - and the brand name on it."

    "Whatever this is, it's from one of the most expensive jewelry stores in the city!"

    "I stare at it in shock."

    "Who could have gotten this for me? Nobody I know has this kind of money, ruling out any family or friends. And it was left
    at my doorstep, which means that someone I {i}don't know{/i} knows where I live."

    "Further inspection of the box shows that it wasn't posted through the mail but rather hand delivered. That's... unsettling."

    "I hesitate to open the gold box. Maybe the person got the wrong address? That certainly makes more sense than a stranger getting me
    something like this out of nowhere."

    "Still, curiosity wins out. They'll never know if I open it first, just to check, right?"

    "I ignore the warning bells going off in my head, perhaps foolishly, but I can't help myself."

    "It's been a weird kind of day. First, my stoic, silent customer finally talking to me, then these strange gifts... It's enough to make any girl
    tired."

    "Putting my good sense aside, I open the box carefully and inside is one of the most expensive chokers I've ever seen."

    "It's beautiful; exquisite. It's understated, but that's real gold and those are real diamonds. It looks like it'll fit perfectly if I put
    it on."

    "Part of me really wants to put it on right now, this instant. It's such a fine piece of work. But it could easily get stolen, and seems like
    the casual kind of display of wealth that might get me mugged."

    "Another part of me wants to keep it - but keep it in my house, safe, and only take it out for special occasions... Not that I have many of those,
    and especially not any that would require something this nice."

    "And then there's the part that is suspicious of this seemingly innocuous, if lavish, gift. It might make more sense to get rid of it. I
    don't think I could bring myself to put it in the trash, though. It's too nice for that."

    "Instead, I'll have to go to the front desk and see if anyone is missing their delivery."

    "Standing there, looking at the choker and watching it glimmer in the yellow lighting, I try to decide what to do."

    menu:
        "Tampering with mail is a felony and this is {i}probably{/i} not meant for me. I'd better get it returned to the right person.":
            $noncon += 1
            $s_choker = "no"
            jump noChoker

        "I'm going to keep it, but I don't want to flaunt wealth I don't have, so I'll keep it tucked away in my bedroom where it'll be safe.":
            $dubcon += 1
            $s_choker="some"
            jump someChoker

        "I doubt a delivery person would mess up this badly. I'm going to put it on right now - I don't want to seem ungrateful to whoever gave it to
        me.":
            $con += 1
            $s_choker="yes"
            jump withChoker

    label noChoker:
        "I put the choker back into its box and wistfully push it aside. It's late, I have studying to do still, and an essay to write. It's
        best to not think too hard about the weirdness of today."

        "I make some food for myself and then settle in for a long night, thoughts of Damien and the choker out of my mind."

        jump chapter3

    label someChoker:
        "I carefully put the choker back into its box and bring it to my bedroom, where I make sure it goes into one of the false bottoms
        of my jewelry box."

        pn "There, now you'll be safe and sound."

        "Once that's sorted, my stomach grumbles and I remember how hungry I am. I go to make dinner quickly - I still have to study for a test
        and write an essay for school."

        "I put my best effort forth to concentrate, but my mind keeps going back to Damien and the gifts I'd been given. I keep thinking about it
        all night."

        jump chapter3

    label withChoker:
        "I carefully remove the choker all the way and then put it around my neck. I struggle for a moment to get the clasps right, but once it clicks
        together, it stays on firmly."

        "I go to the bathroom to survey myself in my mirror - and wow, I look good with this on. It goes really well with my complexion, but is
        understated enough to not look as ostentatious as I'd imagined."

        "But it's not something to wear around the house, so I go to take it off -"

        "-and can't."

        "It won't come off."

        "Whatever device I had used to put it on before almost seems to have... disappeared. Pulling the choker around to see what exactly is
        going on, I realize that where the two ends joined, there's a {i}lock{/i} that covers it."

        "Essentially, it'll take someone with a key to open it, and I don't have that. I check the box it came in and there was nothing else."

        "I take a deep breath in, then out, and repeat. It's almost impossible not to start panicking. I definitely shouldn't have ignored
        my instincts."

        "Did the person who sent this know what they were sending me? Is this somehow malicious?"

        "I can't help but want to think that maybe it was an innocent mistake. It'll be terrible if I end up having to cut it off, but I finally calm down
        when I realize that even if the locking device is weird, it's not like there's anything actually wrong with the choker itself."

        "I'm still uneasy about the whole thing, but I feel a bit better and am able to make dinner and settle in to do my homework."

        jump chapter3

        $ stop_audio("music", 2)


label chapter3:

    call clearScene
    call showCenterText(__("The Necklace"), "100")

    pause

    scene bg diner the necklace
    with fade
    $ play_audio("cheerful_music", channel="music")
    $ play_audio("bustling_cafe", channel="sound")

    "The next week goes well without any further gifts or weirdness. Still, I'm a little hesitant to see Damien again, as I assume I will, on Sunday
    morning."

    "I show up to work bright and early. Shelly, one of my coworkers, is already clocked in, and she greets me warmly."

    if s_choker == "yes":

        coS "Wow, look at you! That's a gorgeous necklace!"

        "I blush and finger it. I still haven't been able to get it off, despite my best efforts. Still, it looks so nice that I've gotten over
        my alarm and have decided that at least this way, no one can steal it from me."

        pn "Thanks! It looks really good, doesn't it?"

        coS "It sure does."

        "She winks."

        coS "But it looks expensive - I bet it cost more than a year's worth of rent for me! Are you holding out one me, or do you have some secret
        rich boyfriend?"

        "I know she's teasing, but her words bring to mind the fact that I do have a secret admirer who certainly does appear to be wealthy."

        pn "It was a gift... I have no idea who from, though."

        "Shelly gasps and then grins widely."

        coS "Oh, man, I'm so jealous! A rich guy secretly pining after you... it's so romantic!"

        "I shrug uncomfortably. It doesn't feel as romantic as Shelly's making it out to be. Even though I'm enjoying my gift, it makes me a little
        uneasy that I don't know who it's from."

    else:
        coS "Hey, [playerName]! Bright-eyed and bushy-tailed this morning, huh?"

        "I nod."

        coS "As usual. You're always working really hard, aren't you?"

        pn "I try to do my best, at least... Hey, you want to know something really weird that happened last Sunday?"

        "Shelly looks intrigued."

        coS "Yeah! Come on, spill!"

        "I tell her about the gift that I received."

        if s_choker == "no":

            pn "So I figured it was meant for someone else, but the office said that no one was missing any packages they were expecting, so I ended up
            keeping it. It's really nice, but I just can't imagine it was meant for me."

            coS "Why not? You're a pretty girl, kind, dedicated, smart - what's not to like?"

            "Shelly seems surprised by my self-deprecation and I shrug uneasily."

            pn "I don't know... it was {i}really{/i} nice."

            "I lower my voice."

            pn "Like, diamonds and gold nice."

            "Her eyes widen and then she squeals excitedly."

            coS "Oh, I'm so jealous! That's so romantic!"

            "I frown."

            pn "I don't even know who it's from, so... I'm not sure how romantic that is."

            coS "He'll reveal himself eventually, don't you worry. And then you can have a nice, rich boyfriend who can lavish you with gifts and love."

        elif s_choker == "some":

            pn "So I have it tucked away safely where no one can get to it."

            coS "Really? Why? Something that nice should be worn, loud and proud!"

            pn "I'm worried it could get stolen, or make me a target for mugging, even though I'm poor as hell."

            "We both share a laugh. Waitressing isn't the best paying job, especially at a cheap, if popular, diner like Normann's."

            coS "Well, you obviously have someone who thinks you're special, and you must see him around, even if you don't know who he is. Not wearing
            it might tell him you're uninterested, and who wants to pass up a kind, rich boyfriend?"

            "I laugh ruefully, but Shelly's serious and so am I."

            pn "I don't know, I don't even know who he is. I might not be interested, and wearing it could give the wrong signal."

            coS "I think you should just wear it for a week and see what happens. Can't hurt, right?"

            pn "I don't know..."

    coR "Hey, ladies! Those tables aren't going to serve themselves!"

    "Our manager, Rick, calls out from the kitchen, apparently seeing us chatting away and not working. We grin sheepishly and hurry to
    get back to work."

    "Sunday mornings are always pretty busy. I forget about Damien and the choker with all the hubbub and it's only when he shows up
    at nine, impeccably dressed and looking handsome as usual, that I remember."

    show dam neutral crossed norm
    with dissolve

    "It's with a wary sort of warmth that I approach him. It only feels right to be a bit friendlier after our introduction last week. My
    discomfort isn't a priority, it's maintaining good customer service."

    pn "Damien, good to see you back! How's your week been?"

    "He looks at me with an expression of skeptical surprise."

    show dam skept crossed norm
    with dissolve

    d "It's been..."

    "His gaze isn't meeting mine. Instead, he's looking lower... at my neck."

    if s_choker == "yes":

        "He's looking at the choker, I realize."

        $ stop_audio("music", 1)
        $ stop_audio("sound")
        $ play_audio("creepy", channel="music")

        show dam smile soft loose norm
        with dissolve

        d "Very satisfying."

        "His eyes lift to meet mine again."

        d "And how was your week, [playerName]?"

        pn "Oh, it was fine. You know, school, work, the usual."

        "I feel kind of flattered that he's taking such an interest in me. Stalker or not, I can't deny that he's an attractive man."

        "Between his normal reticent silence and my wariness of his repeat visits, I've never really given it any thought, though now it's
        sticking like a burr."

        show dam amused crossed norm
        with dissolve

        d "{i}Just{/i} the usual?"

        "The way he says it makes it a leading statement and I wonder for a moment if he knows something I don't."

        "The way he was looking at me neck, I realize. He must have noticed the choker. Oh..."

        "If he really is 'stalking' me, wouldn't he be a bit jealous of someone else's gift? Especially since I'm wearing it."

        pn "Well..."

        "I reach up and toy with the choker absentmindedly."

        pn "I did get a surprise gift last weekend. It looks nice, doesn't it?"

        "I motion to the choker around my neck."

        d "It truly does."

        show dam smile crossed norm
        with dissolve

        "He looks so smug, so satisfied, that for a moment, I wonder..."

        "Is Damien behind the gift? Is he the one who gave it to me?"

        "And suddenly, the question is on the tip of my tongue."

        menu:
            "Ask him teasingly if he knows something I don't.":
                $dubcon += 1
                $s_ch3_asked = True
                jump asktease

            "This is really bold of me, but I have to know. Ask him if he's the sender.":
                $con += 1
                $s_ch3_asked = True
                jump askserious

            "I'm too nervous. I can't bring myself to ask it, despite my curiosity.":
                $noncon +=1
                $s_ch3_asked = False
                jump noask

        label asktease:
            "There's a moment where our eyes meet and it feels like he's looking into my soul."

            show dam soft smile loose norm
            with dissolve

            "But he just keeps looking at me, saying nothing, with only a mysterious smile on his face."

            "Finally, I give up. He's obviously not going to give me an answer."

            pn "Sorry! That was awkward of me..."

            "I quickly change the subject. I've been lingering at his table for too long, anyway."

            pn "So, the usual?"

            "Damien nods, still smiling mysteriously... and softly."

            d "That's fine."

            "I grin enthusiastically, but feel that my cheeks are hot. I'm so embarrassed...! How could I harass a customer like that?
            Rick would have my head."

            pn "I'll have that right now for you."

            hide dam soft smile loose norm

            "I quickly make my way to the kitchen to turn in his order."

            jump chapter4

        label askserious:
            show dam skept crossed norm
            with dissolve

            "Damien was clearly not expecting me to ask that, if his expression is anything to go by."

            d "Why would you think that?"

            "His question is mild and unoffended, but I realize pretty quickly that I've overstepped."

            pn "Oh - uh - no reason! Just... thought I'd ask... You know, since the giver didn't leave their name."

            "I'm fit to burst with humiliation. What could have possessed me to ask that? So bluntly, and to a stranger at that!"

            "So what if he shows up every Sunday and sits in my section and stares at me? There are so many other explanations that
            are plausible besides him being a stalker."

            "Sure, stalker is the first thing that comes to mind, but you're not supposed to judge a book by it's cover, or something like that..."

            pn "I'm sorry, that was really out of line."

            "I don't even expect a tip at this point. I'll be happy if he doesn't complain to Rick."

            show dam neutral crossed norm
            with dissolve

            d "I'll have my usual."

            "I'm a little taken aback by his sudden change of subject."

            pn "O-of course. I'll be right back with it."

            "I turn to leave, needing to wallow in my shame out of the public eye, when I feel a warm hand gently grab my wrist."

            "I turn back and see Damien smiling at me."

            show dam smile soft loose norm
            with dissolve

            d "I wouldn't worry about getting gifts from strangers. I'm sure your gift-giver has no ill intentions towards you."

            pn "U-uh?"

            d "Just be grateful that someone cares enough to spend that time to put a smile on your face."

            "I can only nod dumbly. He releases my hand, and I stiffly make my way to the kitchen to give the order, baffled by
            his words."

            hide dam smile soft loose norm
            with dissolve

            jump chapter4

        label noask:
            "I hold my tongue and the moment to ask my question passes."

            pn "So, your usual?"

            "I ask it cheerfully, wanting to move away from any awkwardness on my part."

            d "Yes."

            pn "I'll have that right out for you."

            "Feeling like a coward, I turn tail to go put in his order and move on to my next table."

            jump chapter4


    else:
        $ stop_audio("music", 1)
        $ stop_audio("sound", 1)
        $ play_audio("creepy", channel="music")
        show dam furrow
        with dissolve

        pause 2.0

        show dam sneer crossed norm
        with dissolve

        "His eyes flash, one moment with anger and then back to his normal blank expression."

        d "A disappointment."

        show dam neutral crossed norm

        "What could have made him look like that? I would glance down to see what made him angry, but it's not like
        I can see my own neck without a mirror."

        d "You look nice today."

        "I look up in utter surprise at the sudden change. What could have prompted that? I haven't done anything different from the norm."

        d "Your outfit is lacking, however... Perhaps something around your neck would complete your look and bring out
        your true beauty."

        "For a moment, I can only gape at him. Talk about a back-handed compliment if there ever was one!"

        pn "W-well..."

        "I deal with difficult customers all the time, so I should be immune, but something about Damien's words digs under my skin
        and so I'm left blindsided."

        "I grasp for some kind of response and think of the choker."

        menu:
            "Mention the choker.":
                $con += 1
                jump mentionchoker

            "Don't say anything. Just nod politely.":
                $dubcon += 1
                $noncon += 1
                jump nomentionchoker

        label mentionchoker:
            pn "Oh... Well, I did receive this really nice gift the other day. Maybe I could wear that?"

            "The words come out senselessly and I'm more talking to myself than him, but Damien speaks up anyways."

            d "You should wear it, then. I can guarantee you'll look beautiful."

            pn "...Right."

            "It's all I can do to keep my composure. Quick, change the subject!"

            jump chokerChoiceBridge

        label nomentionchoker:
            show dam furrow crossed norm
            # with dissolve

            "The silence is awkward. I stare at him while he stares back, and it almost feels like a battle of wills. Like he's
            trying to get me to reveal something, but I don't know what he could possibly want."

            "For a moment I entertain the idea that Damien was the one who sent the choker, then immediately discard it.
            He barely knows me."

            "Finally, he speaks."

            d "I'm sure you must have in your possession something to wear around your neck? I thought women were interested
            in jewelry."

            "He's right; I'm happy to wear some cute earrings or bracelets. In fact, I'm wearing some silver studs in the shape
            of roses this very moment. I can't very well say I don't like accessories."

            pn "Well... I guess I do."

            "It comes out reluctantly. This is so awkward! I don't know what to do, but I can't bring myself to just walk away.
            Not only is that rude, but I'm on the job."

            "It's time to get his order and get out of here!"

        label chokerChoiceBridge:
            pn "So, would you like your usual?"

            d "Yes."

            "He's looking at me like I'm some kind of rare specimen, something he doesn't understand but wants to and will do anything
            to possess."

            "My mouth runs, like it always does when I'm nervous."

            pn "Then I'll get that right out to you! It'll only be a moment."

            hide dam neutral crossed norm

            "I quickly turn to leave and move on from Damien's soul-penetrating gaze, only breathing a sigh of relief when I'm
            well out of sight."

            jump chapter4

label chapter4:

    call clearScene
    call showCenterText(__("The Encounter"), "100")
    pause

    $ play_audio("relaxed_music", channel="music")
    scene bg bedroom night
    with dissolve

    "What happened with Damien hangs like some kind of rain cloud over the rest of the week."

    if s_ch3_asked:
        #optional thread: except if noask
        "Embarrassment clings to me from seeing Damien and that awful conversation."
        if s_choker == "yes":
            #optional thread: if yes choker, except noask
            "Even though he wouldn't say he was the one who gave it to me, after a lot of thought I've decided he must have something to do
            with it."

    # '!=' means does not equal
    if s_choker != "yes":
    #optional thread: if no or some choker
        "He was so forward about me wearing it, it makes me a little nervous. You'd think he was the one who sent me the choker, the
        way he went on about it!"

    #normal thread
    "I don't have any proof, though, and I've humiliated myself enough."

     #optional thread: if no or some choker
    if s_choker != "yes":
        "At Shelly's insistence and Kaley's reassurance, I decided to put the choker on in the end, if only to see how it looked."

        "I was immediately alarmed when I couldn't take it back off. Kaley was the one who kept me calm and told me not to worry about it;
        at least it can't be stolen, right?"

        "I don't want to make a big deal out of it. It's probably nothing, and it looks good, so I'm trying not to make a fuss out of it."

    #normal thread
    "Thoughts about Damien and the choker cycle through my mind unbidden like they have been all week."

    "I think about how he's been staring at me for months now. At first, when Shelly called him my stalker, I thought that she was
    overreacting and took it as more like a joke, even though after a while, I started thinking the same thing myself."

    "But nothing ever came of it and so I was never worried."

    "Then he started talking to me, and then the flowers and choker."

    "The choker I can't take off."

    "The thing is, any evidence I have about Damien being a real threat is circumstantial, and I'm hesitant to call him anything of the kind
    even now. It's never seemed like it, but he could be shy or something. He could just be that socially awkward, like I considered at first."

    "It seems like he has a lot of money from the way he dresses, so even if the choker {i}is{/i} from him, it could be a weird
    way of showing affection... He might not be able to express it very well."

    if s_ch3_asked:
        #optional thread: except if noask
        "Then again, he wouldn't admit to it when I asked. That's odd if he's using it to make a move of some kind."

    #normal thread
    "There's also the chance that he really is a stalker the way Shelly had said. I wonder if I should be worried."

    "But... and it may sound stupid... I still don't really feel threatened by him regardless of what he is."

    "Uncomfortable, yes. A little weirded out? Absolutely. But afraid of him? Not at all."

    "Still, part of me is dreading going to work on Sunday and seeing him. Something's changed between us, something I can't
    see or define but know it's there anyways."

    "My thoughts keep conflicting with each other, and I want to keep thinking about this until I can unravel the mess in my mind despite
    not making any progress over the last week. I'm so confused, I don't really know what to think..."

    "{i}But{/i} right now it's Saturday and I'm going to meet my friend for a night out on the town. It's been too long since I've really
    let loose."

    "The choker is a comforting weight against my neck and I've taken to fiddling with it when I'm bored or nervous. No matter who
    gave it to me, Damien or some stranger, and the circumstances surrounding it, I really appreciate the gift."

    "I do wonder what the catch is - there's always a catch to good things - but since there's nothing I can do, it's just one more
    thing to conflict my thoughts, so I'm trying not to think about it."

    "Either way, it's time to get going. I take one last look in my mirror to make sure I'm ready. Seeing my makeup look flawless and my clothes
    immaculate, I leave my apartment and head for the bus stop."

    $ play_audio("club_excited", channel="music")
    scene bg nightclub
    with dissolve

    k "Hey, look who's finally taken a break from life to hang out with her friend!"

    pn "I'm not {i}that{/i} much of a workaholic, Kaley..."

    "It's nice to see her. She's one of my best friends and it feels like we've been through everything together - childhood,
    her parents' divorce, high school, now college and adulthood."

    "I couldn't ask for a better friend."

    pn "So, where do you want to start?"

    "We're at one of the most popular night clubs in town. On a Saturday night like this one, it's packed with people and it
    takes a while to reach the counter and get our drinks. We order shots to get the night started, then go to the dance floor."

    "Getting into the mood, we drink, we dance, we flirt - well, Kaley does, anyway, I'm not in the mood for a one-night stand -
    and we have a great time. It's wonderful to let loose."

    "We both can hold our liquor pretty well, so we're not sloppy drunks, but Kaley's a bit ahead of me with all the drinks various
    cute guys have bought her."

    "I'm no ugly duckling myself, but Kaley has a sort of charisma that just draws people in. She's a real Queen Bee, so to speak,
    but she's never cruel or malicious. Her confidence out-matches mine by a lot."

    "I've known her since kindergarten and even though she's always had a lot of friends, she and I have always been closest. She's
    encouraged me over the years to grow confident and strong, but even so, there's still only so much I can manage."

    "I'm not necessarily a wallflower, but I can't just flit from person to person, making small talk and new friends as easily as
    breathing, like Kaley does."

    "Kaley nudges me, interrupting my thoughts."

    k "You wanna grab some more drinks?"

    "She has to speak loudly over the beat of the bass and the chattering crowd. I turn to her and nod, but I've got a pretty good buzz and don't want
    to ruin it by overindulging. A nice cold water would be good, though."

    "We step up to the bar and while we're waiting for the bartender to come our way, a guy starts chatting Kaley up almost
    immediately."

    "Kaley seems interested in him, distinctly more so than the others so far, so after we get our orders, I decide to go find somewhere
    to sit for a bit. My heels are starting to hurt and I could use some time off my feet."

    hide kaley test

    "I find a table for two and all but slump into the cushioned metal chair. I sigh and gulp my water down - I hadn't realized
    how thirsty I was until I put the glass to my lips."

    s "[playerName]?"

    "A somewhat familiar voice saying my name makes me look up, and then -"

    show dam smile loose casual
    with dissolve

    pn "{i}Damien?{/i}"

    "I'm shocked. I would never have expected to see someone like him in a place like this. He dresses too well, and he definitely
    doesn't give off the aura of a partier."

    "Still, he's holding a glass of what looks like whiskey straight and wearing much more casual clothing than I'm used to seeing
    on him."

    pn "What are you doing here?"

    "I blurt it out and realize how rude it sounds only a second after it's out of my mouth. However, Damien doesn't seem to be offended."

    d "The same as you are, I assume."

    "I nod dumbly."

    d "I see you decided to wear your gift."

    "My embarrassment from our last interaction comes roaring back and I blush."

    pn "Y-yeah... It seemed too nice to just leave alone, you know?"

    d "I'm glad. It looks good on you."

    "There's a brief, awkward pause, at least on my end, before I come back to the present."

    pn "Oh, um, would you like to sit?"

    show dam smile soft loose casual
    with dissolve

    d "That would be lovely."

    "As he takes a seat across from me, I wonder at the chances of us meeting up in such a big city. It seems unlikely to me.
    I'm not going to say my thoughts aloud, though. I'd sound paranoid."

    "I sip at my water, not really knowing what to say. I don't know Damien despite having seen him every Sunday for months.
    He'd never seemed open to conversation before two Sundays ago, so now that I'm faced with him alone and without a
    conversation starter, I'm lost."

    "Finally..."

    pn "Do you come here often?"

    "Damien's gaze turns to me and I feel like I'm a bug under a microscope."

    d "No. This was a bit of an... experiment."

    "I desperately want to know how going clubbing could in any way be an experiment."

    pn "What's your hypothesis, then?"

    "He looks at me, eyes intense, before smirking."

    d "That's a secret."

    "He seems so calm and unflappable while saying it, even as he shuts down my attempt to start a conversation, that I get a
    little flustered."

    pn "W-well..."

    d "Are you here with anyone or did you come out by yourself?"

    "I relax at his question. I don't really want to just sit here in relative awkward silence with a somewhat familiar acquaintance;
    I had come here for a break."

    pn "I'm with a friend. She's somewhere around here getting hit on by a cute guy."

    show dam furrow crossed casual
    with dissolve

    "Damien's expression darkens for the slighest second before relaxing."

    show dam serious crossed casual
    with dissolve

    d "It's dangerous to be alone in places like these. There are many who would take advantage of a single drunk young woman."

    "Well, that's kind of insulting, even if there is some truth to it."

    pn "I'm not drunk, just a bit tipsy. Trust me, I can rely on Kaley."

    "To make my point clear, I turn in my seat to point out my friend. I don't know why I feel compelled to give him proof. Maybe
    it's because a lot of what he said was true and I don't actually want to be left alone, either."

    "But..."

    "I don't see her anywhere."

    d "Is something wrong?"

    pn "I don't think so... I just can't find my friend."

    d "Would you like some help tracking her down?"

    pn "Maybe in a bit, if she doesn't show up soon. I don't want her wandering off by herself for too long..."

    d "A reasonable desire."

    pn "Did you come with anyone?"

    d "No. Fortunately, I am not considered an 'easy' target by unscrupulous men."

    "I laugh a little at that. That's an understatement."

    pn "No, I guess you're not. So... You just came to a nightclub to... dance?"

    show dam amused crossed casual
    with dissolve

    "Damien laughs like I said something funny."

    "Looking at him, I can see why. He's not dressed for dancing, but I can easily see him picking up any girl he'd like."

    "The thought makes me a little uncomfortable, especially with the way he's been watching me at the diner."

    "Scratch that... with the way he's looking at me {i}now{/i}."

    show dam smile soft loose casual
    with dissolve

    pn "So... if you're not here to dance, why are you here?"

    d "Truthfully, I wanted to socialize. My work means I spend most of my time giving orders and managing others. In an
    environment such as this, I can meet with... equals."

    "At his admission, I start to feel a little excited. I know nothing about this man other than that he likes savory food
    and has money, if the quality of his clothes are any indication."

    "I want to know more about him."

    pn "What exactly do you do?"

    "There's a brief pause before Damien continues."

    d "I trust you won't go spreading this around. I enjoy my anonymity."

    "I nod eagerly."

    d "I'm the CEO of AllMart."

    "I can't help the involuntary gasp that comes immediately after his statement."

    "AllMart is the #1 grocery chain in the world. It has cheap prices, a wide variety of stock, the freshest produce, and
    lots of name brands. You can get clothes, electronics, and furniture there, too. Like its name implies, it has 'all' of
    everything."

    pn "W-wow. That's... that's big."

    "I'm now unnerved. I've treated him like a normal person this whole time!"

    #combination of s_choker or nomentionchoker
    if s_choker == "yes" or s_choker == "no":
        "More than that, I made the absolutely ridiculous assumption that he could have given me the choker and flowers!"

    "I wonder what such an affluent, upper-class man is doing spending time at Normann's Diner in the first place. No wonder
    he'd look so out of place! With the quality of his clothes, he belongs at a gala or charity fundraiser, not a diner like
    mine or even at this nightclub!"

    "Why isn't he sitting in the VIP section?"

    "Damien seems to read my thoughts."

    d "Like I said, I appreciate anonymity. Telling the world who I am would result in paparazzi and special treatment. I
    do not particularly want that following me everywhere."

    pn "Oh... I guess that makes sense."

    "It does, to a certain degree. I can't imagine being followed around just for pictures, nor do I think I would like
    to always be treated differently from others. Still, it doesn't entirely sit right with me."

    "Like it's not the whole truth."

    "But I can't very well argue with him, so I don't voice my doubts."

    d "Think about how you would have treated me had you known who I was. It wouldn't be anything like our past interactions,
    would it?"

    "Well, he's definitely right about that. I still don't know how I feel about the way I've treated him, but I won't be
    forgetting this information any time soon. If I start acting differently toward him, will that drive him away from the
    diner after all?"

    pn "No, it wouldn't. Honestly, I don't really know what to think about this..."

    show dam furrow crossed casual
    with dissolve

    d "Please, don't let it bother you. I've enjoyed spending the little time I have with you."

    "There's no mistaking his words, I realize all of a sudden. The months of showing up every Sunday, always in my section,
    the way he would watch me, the kiss on my knuckles when he met me, the compliments he paid me about being pretty... It's
    clear now what he wants."

    "For some outrageous reason, Damien wants me."

    "ME! A normal girl, struggling to pay the bills between college and rent, with ever-growing student loans, working
    part-time at a diner that barely covers my costs."

    "He wants {i}ME?!{/i}"

    pn "U-um, thank you. I've enjoyed our interactions, too..."

    "It feels like the right thing to say, even though I spend so much time flustered and unsure around him that I'm not
    sure it's entirely true. Still, the last thing I want to do is offend him."

    d "I'm glad."

    d "I would like to get to know you better. You're an intelligent girl - I'm sure you know by now that I'm interested in
    you."

    "Oh, boy. He's right, he's made it fairly obvious, but... Between meeting him at my job and him being the CEO of AllMart,
    this... could get messy."

    "If I offend him, he could ruin my life. Easily."

    "Sure, I've noticed that he's handsome. He seems nice enough, although cold and stoic. He's only started to be more expressive
    recently. I wonder if that's him letting his guard down so I would somehow know I'm special."

    "I didn't realize before, but that seems to be the case."

    "I don't know what changed on that Sunday when he introduced himself, but it feels like this is happening really fast."

    "I have to ask myself: am I interested in him, too? Or is this too much?"

    menu:
        "I... I think I like him, too. I wouldn't mind getting to know him.":
            $con += 1
            jump chooselike

        "I don't {i}dislike{/i} him... But I don't want to move too fast, either.":
            $dubcon += 1
            jump chooseslow

        "I don't know what to think, but what I do know is that I'm not into him the way he's into me.":
            $noncon += 1
            jump choosenolike

    label chooselike:
        "I'm a little nervous being so bold, but I speak my truth."

        pn "I would like to get to know you better, too."

        show dam smile soft loose casual
        with dissolve

        d "I'm glad. Now that we're in agreement, would you like me to buy you a drink?"

        "He pauses."

        show dam amused crossed casual
        with dissolve

        d "I didn't want to be presumptuous by asking earlier. Of course, it seems it wouldn't have been too presumtuous
        after all."

        "It's been a bit since I last had a drink and my buzz is fading. I smile at him gratefully."

        pn "That sounds great. I could use a little extra booze now."

        "Damien seems amused and stands up."

        d "I'll be right back."

        hide dam amused crossed casual

        "As he heads toward the bar, I watch as the crowds seem to instictively shift around him, clearing a path. I'm not
        sure if it's his natural confidence or the cold look he generally has on his face, but he doesn't meet any
        resistance making it to the bar."

        "While he's there, I scan the crowds for Kaley, but don't find her anywhere. It's okay for now; I'm not planning on going
        home right now."

        "I'm excited. It's been a long time since I last had a boyfriend, or even time for a relationship. Part of me is worried
        I still don't have time, but I think - I {i}want{/i} to make it work."

        "Not five minutes later, Damien is back, holding my favorite drink."

        show dam neutral crossed casual
        with dissolve

        pn "Wow, how did you know this is my favorite?"

        d "It was a lucky guess. I'm glad you like it."

        "Not wanting to get buzzed too fast, I sip at my drink, savoring it as we continue to talk."

        "Conversation flows smoothly, and soon we're talking about more serious matters."

        d "My goal recently has been to fund solar technology via one of our subsidiaries to reduce the corporation's carbon footprint.
        I can't give any details, but I believe it's coming along nicely."

        "I laugh."

        pn "Like I could do anything with the details. Really."

        show dam smile loose casual
        with dissolve

        d "You could always report it to the press. I hear they pay nicely."

        pn "You shouldn't tell me that! Now you're giving me ideas!"

        "Damien laughs, catching the joke. Still, I wonder at even the meager trust he's given me. How does he know that I wouldn't
        go to the press with even the smallest bit of information?"

        "I laugh too, but as I do, my head starts spinning a little bit. I feel dizzy, and a bit more drunk than what I've had
        should be making me."
        # stop music fadeout 1.0
        $ play_audio("creepy", channel="music")

        "As the time passes, my words start to slur and I get dizzier and dizzier until I start swaying off the chair."

        "I don't feel well at all. This isn't a good buzz."

        show dam serious crossed casual
        with dissolve

        pn "I'm-I'm'not feelin' v'ry good... Gotta... gotta find Kay-ley... G' home."

        d "I haven't seen her. I'd go look for her, but I don't want to leave you alone like this."

        pn "'s fine... I'm... I'm 'kay..."

        show dam concern crossed casual
        with dissolve

        d "No you're not. Let me take you home."

        pn "Thasss okay... I'll g-"

        "I hiccup."

        pn "-get a caaab..."

        d "Don't be stubborn. You're in no state to wander around on your own. Here."

        "Damien comes and hoists me up. His hands are warm, even with the humidity and heat of the club. I sway in his
        firm grasp as he lifts me to standing and then wraps an arm around my shoulders."

        d "Come along. Everything will be fine."

        pn "I dun... dunno... Kaley..."

        d "She'll be fine. She's been... taken care of."

        pn "Wha?!"

        "I don't like the tone of his voice at all. What does he mean, she's been 'taken care of'?"

        hide dam concern crossed casual
        scene cg_1
        with fade

        "Out front, a limosuine is idling. Damien guides me into it, despite my growing protests, and I can't help but collapse
        into the cushy seats."

        pn "Dammm-Damien... this 's wrong... Wanna go home... Kaley..."

        d "Don't worry, [playerName]. I'm going to take good care of you. You won't want for anything, as long as you obey me."

        "That sends my thoughts into a tailspin, but I'm not sure what to do - or what I even can do."

        "Damien comes in after me and taps on the dividing screen."

        d "Take us home, Walter."

        "I can feel the car start to move, and it occurs to me that this isn't what I signed up for when I started talking to Damien.
        What happened to getting to know each other?"

        pn "Dam-Damien... pl'se... wha's goin' on?"

        d "I'm taking you to your new home. You'll like it there, I promise."

        pn "Wha'? Wha', no! Wanna... wanna go home!"

        d "We're going there. Calm down. If you make a fuss, I might have to punish you first thing, and I don't want our
        relationship to start off that way."

        "He adjusts me so that my head is on his lap. I've never felt weaker or more helpless in my life. Terror makes me shake
        even as Damien cards his warm fingers through my hair soothingly."

        d "Just let go, [playerName]. All is well."

        "And despite nothing being well, I can't help but give in to unconsciousness."

        call clearScene
        call showCenterText(__("Credits:"), "100")
        call screen credits with Dissolve(1.)

    return

    label chooseslow:
        pn "I think I could like you, too... But you have to know, I don't really have a lot of time. If it's okay with you,
        I'd like to move slowly."

        show dam serious crossed casual
        with dissolve

        d "That's fine. We have time."

        "Despite his words, he doesn't seem as 'fine' with it as he says. I try not to let it bother me; if he gets pushy, I'll
        know he's not right for me."

        "Despite that, I feel the urge to at least explain myself."

        pn "The thing is, I'm in college. I work at a diner part-time, four days a week. I have to study too. I'm close to the
        end of my degree and my homework is piling up. I just don't have a lot of time to dedicate to a relationship, you know?"

        d "I understand."

        "He still seems reticent, but I don't know what else to say to smooth things over."

        "But he doesn't let it get awkward, even as I'm thinking this might not be a good idea."

        d "We can take it slow if you wish, [playerName]. For now, let's just get to know each other."

        "I smile in relief."

        pn "Thank you."

        d "If I may ask, what are you majoring in?"

        "I tell him with a bit of pride in my voice. I can't help it; my degree is being hard-earned. I can't wait to get out of
        school and get a job, and tell him as much."

        "We talk for a while and the conversation flows naturally. After a while, my water runs out and my buzz is fading. Feeling
        a little parched, I pick up my cup."

        pn "I'm getting a little thirsty. Do you want anything from the bar?"

        show dam amused crossed casual
        with dissolve

        d "Let me get it for you. It's a man's job to take care of his lady."

        "I feel a little uncomfortable with his declaration, but I also don't particularly want to brave the thick crowds. Better
        him than me."

        "I smile cautiously."

        pn "Thanks, I appreciate it. I'll be here waiting."

        hide dam amused crossed casual
        with dissolve

        "As he heads toward the bar, I watch as the crowds seem to instictively shift around him, clearing a path. I'm not
        sure if it's his natural confidence or the cold look he generally has on his face, but he doesn't meet any
        resistance making it to the bar."

        "While he's there, I scan the crowds for Kaley, but don't find her anywhere. It's okay for now; I'm not planning on going
        home right now."

        "I'm excited but wary. It's been a long time since I last had a boyfriend, or even time for a relationship. Part of me is worried
        I still don't have time, but I think - I {i}want{/i} to make it work."

        "Not five minutes later, Damien is back, holding my favorite drink."

        show dam amused crossed casual
        with dissolve

        pn "How did you know this was my favorite?"

        "I can't help but think that it's a little weird. He knows my favorite drink, though I don't know how."

        d "A simple guess. I hope you enjoy it."

        pn "I definitely will."

        "Encouraged by his expression and the fact that he likes me and is willing to take things slow anyways,
        I eagerly take a long swallow of my drink."

        d "Slow down. You don't want to overdo it."

        pn "It's fine, my buzz has mostly faded. You don't have to worry about me."

        show dam concern crossed casual
        with dissolve

        "The look on his face says that he worries greatly, but that doesn't bother me. I know my limits."

        "As we talk, I feel the alcohol kicking in more and more - a little too strongly, actually. I start feeling woozy, swaying
        in my seat. The world spins but I haven't moved."

        d "[playerName], are you feeling alright?"

        pn "Y-yeaaaahhhh... Th' worl's... sp-spinning..."

        pn "I am {i}sooooooooooo{/i} drunk..."

        "I giggle, but that sends my head whirling. My hand slaps down on the table clumsily to balance myself, and then I feel myself
        falling."

        "I suddenly feel warm arms around me, catching me before I tumble out of my chair."

        show dam zoom

        d "You're much too drunk. I told you to take it slow."

        pn "Yeaaahhh, yeaaaaahhhh..."

        "Is's a little known s'cret, but sometimes... sometimes I'ma belligerent drunk... instead of a hap-happy o...one. It seems tha'
        b'lligerenccce is the name-name of the g-gaaaaame t'day..."

        "Why're m' thoughtsss sooo... blurrryyy?"

        d "You need to go home, [playerName]. Let me take care of you."

        "I just... g-giggle."

        pn "Oh-okayyyy..."

        "The... last thing I kno'... Damien's pickin' m' up... an' I'm go-goin' hoooome..."

        hide dam concern crossed casual
        scene cg 1
        with fade

        d "I cannot wait to take you to your new home, [playerName]. You'll like it there."

        d "If you don't... Well, you'll adjust."

        d "Since I'm never letting you go."

        d "Ever."

        "Th-tha'... sounds bad. Really, {i}really{/i} bad..."

        "Was... I s'posed ta hear it?"

        pn "Wh-whaaaa'?"

        "I turn m' head... look at his seriousss face... and... my world goes black."

    #insert ending credits and advertisement for full game
    #branch to new file
        call clearScene
        call showCenterText(__("Credits:"), "100")
        call screen credits with Dissolve(1.)


return

label choosenolike:
    "Damien looks at me expectantly, waiting for an answer that I don't have."

    "I don't know what to say. He's a wealthy, influential man and I'm a mere waitress and college student. If he takes
    my rejection poorly, it could mean the end of me. As I noted earlier, he could easily ruin my life remorselessly if
    I offend him."

    "Finally, I figure out what to say. It's taken a moment, but he still waits patiently. That's encouraging."

    pn "I'm not really looking for a relationship right now, Damien. I have a lot going on and since I'm in my
    senior year of college, I need to focus on myself and my studies."

    pn "I'm sorry..."

    show dam concern crossed casual
    with dissolve

    d "It's alright, [playerName]. You have ambitions and don't want to fall short due to distractions. I understand."

    "I sigh, relieved, and relax back into my chair. I hadn't realized how stiff with tension I'd been."

    pn "I... I wouldn't mind being friends, though. You seem like a good guy, and I can always use new friends."

    "I put on a hopeful smile, but he doesn't seem to appreciate it."

    show dam skept crossed casual
    with dissolve

    d "It seems that our goals are in direct conflict. At the moment, I'm not interested in friends, even though I'm
    sure you're a wonderful one."

    "My face falls."

    pn "That's - that's too bad. Well..."

    show dam serious crossed casual
    with dissolve

    "Damien stands up, a look of finality on his face. He's returned to his icy cold, stoic expression that he's worn for
    the majority of the time I've known him, particular when I didn't know his name."

    "It makes me wonder if it's some kind of mask. A defense mechanism, maybe, to protect himself from being read by
    other people."

    "It suddenly occurs to me that I might never see him again after this. Even though I'm not attracted to him
    romantically, I realize that unbeknownst to me until now, I had appreciated his presence at the diner."

    "It was a routine that had grown familiar to me. And now, I highly doubt that he'll be back. As the CEO of AllMart,
    Normann's isn't special enough to warrant a visit when he, I assume, no longer has a reason to be there. Because I've
    rejected him."

    pn "I... I guess I'll see you around?"

    "I can't help the hopefulness in my tone and expression."

    d "...Perhaps."

    hide dam serious crossed casual

    "Without another word, he saunters away, and I wonder if he'll be taking home a one-night stand tonight since his
    pass at me failed. It feels kind of presumptuous to think, but I can't help it."

    "Disappointed, I lean back in my chair. I hadn't planned on going home soon, but my night has been ruined. So much
    for relaxation and letting loose; instead, I feel kind of like I've been broken up with, but on a much more minor scale."

    "After a moment, I sit up straight and start looking for Kaley. When she's not immediately visible, I pull out my phone
    and text her. I don't really feel like pushing my way through the crowds."

    "There's no telling where she's gotten to. Maybe she's caught up with the guy I last saw her flirting with."

    "My water cup is empty and it's hot and humid; I want another drink. While waiting for Kaley to text back, I go to
    the water cooler and refill my cup after standing in a short line."

    "By the time I've gotten a couple of cups of water and have texted her three times, Kaley still hasn't responded
    and I'm starting to get worried."

    "I have no choice. I start making my way through the crowds to see if I can spot her."

    "I don't have any luck, but finally my phone vibrates with a text. It must be from Kaley."

    "Instead... it's an unknown, private number. Expecting a spam text, I open it up to scoff at how dumb they must think
    people are."

    "Instead, it reads: Come back behind bar. Alone. Or she dies."

    "Attached... is a photo of Kaley."

    "I gag at the sight."

    "Her face is bruised and bloody, unrecognizable if not for the special necklace she always wears. Her shirt's been
    torn open and her breasts bared, bra laying in two pieces to her side."

    "There's more bruises on her chest, and peripherally it shows lacy red panties near the edge of the screen and her
    skirt pushed up to her hips."

    "I don't bother texting back. This isn't funny and some instinct is telling me this is no joke, no photoshop job."

    "Kaley has been attacked, and now I'm being told to come to a specific location by myself. I'm panicking, adrenaline spiking so
    hard that my hands start to shake."

    "I have to go save her. There's no other option."

    "Furious, scared, and desperate, I force the crowd to part for me until I reach the back exit of the club."

    "I shove the door open and dash outside."

    pn "Kaley!"

    "I see her lying there, barely conscious, and hear her sob weakly."

    k "[playerName]..."

    "Then I feel a strong arm wrap around my waist and pull me back into a hard body. A sweet-smelling rag is roughly pressed
    against my mouth and nose."

    "I gasp briefly but then try to hold my breath, struggling ferociously against my attacker."

    "But he's too strong. My arms are swiftly pinned against my body and the hand on my face presses harder."

    st "Dispose of the body."

    "I recognize that voice. What the holy hell?"

    "That's Damien's voice! What on earth is going on?!"

    d "Stop struggling, [playerName]. I gave you a chance to choose and you chose wrong. Now you have to face the
    consequences."

    pn "Mmph! Mmph!"

    d "{i}Be quiet.{/i}"

    "His voice is forceful and dangerous. I've never heard such a frightening tone in my life."

    "It's at this moment that I can't help but gasp for breath, my struggles draining the oxygen I'd managed to breathe in
    before the chloroformed rag was put up against my face."

    "The world starts to darken at the edges as my vision blurs, and with a few more desperate gasps of air, I start to
    lose consciousness."

    scene cg 1
    with fade

    "I feel Damien lift my limp form into his arms, cradling me carefully against his chest. I can only hang there
    helplessly as the world spins and darkens."

    "Before my world goes completely black, however, I hear..."

    d "Finally, you're mine. I'll never let you go, [playerName]."

    #insert credits scene

    call screen credits with Dissolve(1.)
