from pymongo import MongoClient


client = MongoClient(
    "mongodb+srv://bitshiftlabs:t3Amb1tSH1ft@reasons-to-x.d80cu.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = client.get_database('Reason_to_x_db')

records = db.X

Reasons = [
    {
        "x": "cancel a party",
        "reasons": [
            "I'm not feeling well today",
            "Sorry,I can't come",
            "Sorry,I have to attend another party",
            "Sorry,I have planned a trip today",
            "Sorry, My grandma is ill",
            "Sorry,I am ill",
            "Sorry :( ,my dad is ill",
            "I am quarantined",
            "I am tired.",
            "I drank too much last night",
        ],
    },
    {
        "x": "cancel a trip",
        "reasons": [
            "Sorry,I am not feeling well today",
            "I don't have money.",
            "I don't have my own vehicle",
            "Sorry :(,I have planned a trip today!",
            "Sorry, My mother is ill",
            "Sorry :(,I am ill",
            "Sorry,my dad is ill",
        ],
    },
    {

        "x": "chill on a wednesday",
        "reasons": [
            "It's my choice",
            "As I have finished my work on tuesday",
            "I have scored full marks in my exam",
            "My exams are finished",
            "I have nothing to do",
        ],
    },
    {

        "x": "skip a family function",
        "reasons": [
            "I have my exams on this date",
            "I have my tests on this date",
            "I am not feeling well",
            "I am tired",
            "Sorry,I have planned a trip today!!",
            "Sorry, My mom is ill",
            "Sorry:(,I am ill",
            "Sorry,my dad is ill :(",
        ],
    },
    {

        "x": "buy a car",
        "reasons": [
            "Peace Of Mind",
            "Easier Finance Schemes",
            "Depreciation Is Taken Care Of",
            "You Can Upgrade In Life",
            "Buying A Used Car Saves Money",
        ],
    },
    {

        "x": "buy a cat",
        "reasons": [
            "Cats can bathe themselves",
            "Cats will keep your house and yard rodent-free",
            "Cats are low-maintenance and independent",
            "Cats are an eco-friendly pet choice",
            "Cats can help reduce stress",
        ],
    },
    {

        "x": "buy a dog",
        "reasons": [
            "Dogs make Us Laugh",
            "Dogs are loyal",
            "we're more social with a dog",
            "Dogs keep Us Healthy",
            "We are more active with dogs",
            "Dogs save lives",
            "Dogs give Us a sense of purpose",
            "Dogs give us confidence",
            "Dogs make Us Genuinely Happy",
            "Dogs are faithful and responsible",
        ],
    },
    {

        "x": "avoid a lecture",
        "reasons": [
            "Tell your professor you got food poisoning",
            "Let your professor know that you’re scheduled for jury duty. They can’t argue with the law. Tread lightly, however, if your prof is the type to ask for proof.",
            "Simply tell your professor that you’ve been in the bathroom all morning. No one wants to hear the details on your diarrhea, so they likely won’t pry any further.",
            "Claim that you accidentally ate some peanuts and you’re having an allergic reaction. No one’s going to make you come to class if you’re breaking out in hives. The best part—you don’t need a doctor’s note.",
            "Whether it was a fender bender or a four-car pile up, accidents are a great excuse to get an extension.",
            "Tell your teacher that you locked your keys in your car and by the time Triple-A comes to the rescue, class will be over.",
            "Tell your professor your car got stolen,you have no way of getting to school. Say that you have to file a police report, even though the only cars getting jacked are the pixelated ones on your TV.",
            "If you tell your teacher you contracted lice over the weekend, they’ll actually be thankful you didn’t come to class. The email is quick and easy: “That’s the last time I’m buying a beanie from a thrift store…”",
            "MY ALARM NEVER WENT OFF",
            "I am ill",
            "I am suffering from fever",
            "I have a family function",
        ],
    },
    {

        "x": "excuses for incomplete homework",
        "reasons": [
            "I was ill",
            "Tell your professor you got food poisoning",
            "I had a family function",
            "Had headache",
            "forgot copy at home",
            "I didn't get the topics you taught in last lecture",
        ],
    },
    {

        "x": "live life",
        "reasons": [
            "Life is an invitation to learn. We can learn something from every moment, good or bad. ",
            "Life is not static; it's in constant movement, much like the waves of the ocean. Each wave that comes brings with it experiences, and each one is different. Just as the bad waves can sometimes show no mercy, the good ones come along and refresh us. Nothing lasts forever.",
            "Life is a gift; some people depart too soon and don’t have the fortune to know life. Those who have it should enjoy it.",
            "Our lives are not only our own. They also belong to those who surround us. We should take care of ourselves because we are important to others—even though we sometimes forget it.",
            "Each new day is a new experience. If we don't live it, we won't know what we’re missing.",
            "We are the designers of our life. It is our challenge to find beauty, even—and especially—when the opposite occurs. Finding beauty in the world is possible and brings countless rewards.",
            "We all live through experiences that leave scars. However, there is always someone to give us a hand during those difficult times. The important thing is to accept that help.",
            "Making an effort to deal with problems can make us aware of how strong we really are. Life's challenges don't exist only to upset us—they exist so that we understand ourselves better and get to know who we really are. ",
            "To live is to discover something about ourselves of which we were not aware. ",
            "To live is to look at ourselves in the mirror and discover a message of love in our own eyes.",
            "To live is to allow ourselves to fall in love—with someone, with something, or with life itself. ",
        ],
    },
    {

        "x": "work on sunday",
        "reasons": [
            "to attain success",
            "Avoid messing up on Monday",
            "Meetings preparation",
            "Devoting Time for Networking",
            "Getting applause from boss",
            "Time management",
            "Getting financial Satisfaction",
            "Planning things for next week",
            "To devote time for responding to pending Emails",
            "to Work without disturbance",
        ],
    },
    {

        "x": "enjoy weekend",
        "reasons": [
            "'If you don’t have a start and an end to a week, then it’s just one long continuous work week, which can be problematic,'says Jonathan Alpert, a psychotherapist and performance coach in New York City and author of the book 'Be Fearless: Change Your Life In 28 Days'.",
            "Working excessive weekend hours can also damage your mental health",
            "Change your way of thinking",
            "Give yourself a break from work",
            "Manage your stress issues",
            "Maintain a work-life balance",
            "Change your routine",
            "Get your devices a break at least on weekends",
            "Don’t habituate to oversleeping",
        ],
    },
    {

        "x": "exercise daily",
        "reasons": [
            "Builds aerobic power.",
            "Reduces blood pressure. ",
            "Lowers Type 2 diabetes risk.",
            "Maintains immune functioning.",
            "Reduces body fat.",
            "Keeps bones strong.",
            "Builds muscle mass.",
            "Improves breathing.",
            "Reduces the risk of arthritis.",
            "Brings about better sleep.",
            " Improves mood. ",
        ],
    },
    {

        "x": "eat healthy",
        "reasons": [
            " Good Nutrition Improves Well-Being",
            "It’s Expensive To Be Unhealthy",
            "Helps You Manage A Healthy Weight",
            "Maintains Your Immune System",
            "Delays the Effects Of Aging",
            "Gives You Energy",
            "Reduces The Risk of Chronic Disease",
            "Healthy Eating Positively Affects Your Mood",
            "Increases Focus",
            "Healthy Diets May Lengthen Your Life",
        ],
    },
    {

        "x": "avoid junkfood",
        "reasons": [
            "Junk food may be the reason behind your fatigue",
            "If you eat junk food every time you’re hungry, you may feel chronically fatigued.",
            "Junks food may lead to depression in teenagers",
            "It impairs digestion",
            "It causes fluctuations in blood sugar levels",
            "It affects the brain function",
            "It increases the risk of heart disease",
            "It can cause kidney disease",
            "It can damage your liver",
            "It can cause type 2 diabetes",
            "It increases your risk of cancer",
        ],
    },
    {

        "x": "love studies",
        "reasons": [
            "Studies show us there is little correlation between salary earned and job satisfaction. ",
            " But should we all follow our passions? Studies also show us that doing so can be a recipe for professional disaster, simply for the fact that many passions aren’t transferrable to skills that can be marketed. ",
            "Studying Gives You Purpose",
            "Studying Develops Your Character",
            "Studying Always Rewards",
            "Studying Broadens Your Horizons",
            "Studying Gives You Options",
            "Good grades will also allow you access to more courses, and your Matric 80% for a subject might just be the differentiating factor between you and another applicant for a job! ",
            "Studying now allows you to become a better version of yourself in your future.",
            "Achievement generates self-confidence! ",
        ],
    },
    {

        "x": "wear a mask",
        "reasons": [
            "To keep your friends and neighbors safe",
            "Wearing a mask sets a good example and encourages others to wear masks too. That means everyone is less likely to get ill.",
            "It is so easy. Wearing a mask, for most people, is as easy a thing as could possibly be accomplished. It is a small thing that makes a big difference.",
            "It’s a form of self-expression. For those artistic folks among us, a mask presents a whole new opportunity to introduce fun colors and patterns to their wardrobe.",
            "For healthcare workers and first responders. As someone who works in a hospital, I love this reason for wearing a mask. Even if you never come into direct contact with a hospital worker or first responder, your mask shows them you care. You are keeping them safe by limiting the spread of illness in your community. We appreciate it!",
            "To get back to business. Right on. The more people wear masks, the fewer cases there will be. ",
            "To get back to fun. Masks lessen cases. The more of us wear masks, the sooner we will be able to do things like visit friends, go to movies, travel where we want, and eat out safely.",
            "To embrace the new normal. Showing yourself in your mask helps normalize it for people who are still uncomfortable with wearing theirs.",
            "Many note that they wear their masks particularly to protect the most vulnerable people in our communities, including the elderly and those with conditions that put them at higher risk.",
            "They reduce viral transmission (if worn correctly).",
            "They prevent asymptomatic spread.",
        ],
    },
    {

        "x": "avoid ac",
        "reasons": [
            "While it is a relief to walk into a cool room after being out in the hot sun, prolonged use of air conditioners causes more harm than good. ",
            "ACs pull out moisture from the skin as well and leave it feeling dry and stretched",
            "If your skin is not sufficiently protected to combat it, constant dryness will affect the inner layer of the skin. When skin becomes dry and stretched, it feels itchy. ",
            "Those who have a dry skin will notice that their skin becomes flaky.",
            "Air conditioners aggravate skin disorders,” says cosmetologist and skin specialist, Dr Rajan T D.",
            "AC removes water i.e. humidity from indoor air and robs the outer layer of the epidermis of skin. ",
            "When ACs remove the water or humidity content from a room, skin starts shrivelling. Skin also becomes prone to developing creases and wrinkles.",
            "Sudden shift from one extreme climate to another extreme is very stressful for the body.",
        ],
    },
    {

        "x": "buy a bicycle",
        "reasons": [
            "It’s really, really good for your heart",
            "Boost your immune system",
            "Save money by commuting by bike",
            "Increase the lifespan of your car",
            "Sell your car, make some money, save a fortune",
            "Maximize the resale value of your car",
            "Increase Vitamin D",
            "Live forever",
            "Help out the government of your country",
            "See the global local",
            "Get to actually know the place you live",
        ],
    },
    {

        "x": "watch tv",
        "reasons": [
            "TV Can Improve Your Self-Control",
            "TV Can Make You Feel More Giving",
            "TV Relieves Stress",
            "TV Can Boost Your Creativity",
            "Educational. TV has many educational benefits for children",
            "Stay Current",
            "Get Cultured.",
            "Mental Health.",
        ],
    },
    {

        "x": "play outdoor games",
        "reasons": [
            "a reduced risk of myopia, or nearsightedness",
            "greater exposure to bright light, which enhances health and mental performance",
            "increased activity levels, and greater freedom to run, jump, and climb",
            "opportunities for hands-on learning about physical forces and concepts",
            "reduced stress levels, better moods, and improved concentration",
            "more naturally-attuned sleep rhythms",
            "enhanced opportunities to learn social skills, overcome fears, and develop a lifelong connection with nature.",
            " it's possible that outdoor play could help reduce the incidence of behavior problems, and help fight obesity.",
        ],
    },
    {

        "x": "make new friends",
        "reasons": [
            "Open yourself up to new possibilities.",
            "Offer different perspectives.",
            "Teach you new things.",
            "Get you out of your comfort zone.",
            "Fill your social calendar.",
            "Free entertainment.",
            "Learn things about yourself.",
            "Fresh start.",
            "Introduce you to more people.",
            "Bring more joy to your life.",
            "The research has been done and the findings are clear, friendships enhance our lives.",
        ],
    },
]

# records.insert(Reasons)
