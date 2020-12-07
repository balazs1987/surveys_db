"""
:Author: Balazs Szigeti <szbazsu@gmail.com>
:Copyright: 2020, DrugNerdsLab
:License: MIT
"""

from pony.orm import db_session, commit
from .db_entities import *
import os

src_dir = os.path.dirname(os.path.abspath(__file__))
base_dir   = os.path.abspath(os.path.join(src_dir, os.pardir))

def hello():
    print('hello')

def open_db(filepath=os.path.join(base_dir, 'surveys.sqlite')):
    """ Open existing database """

    db.bind(provider='sqlite', filename=filepath, create_db=False)
    db.generate_mapping(create_tables=True)
    return db

#@db_session
def build_db(filepath=os.path.join(base_dir, 'surveys.sqlite')):
    """ Create databse form scratch """

    if os.path.isfile(filepath): # remove db if already exists
        os.remove(filepath)

    db.bind(provider='sqlite', filename=filepath, create_db=True)
    db.generate_mapping(create_tables=True)

    sss = Scale(name='SSS', full_name='Short suggestibility scale')
    Item(scale=sss, text="I am easily influenced by other people’s opinions.")
    Item(scale=sss, text="I get a lot of good practical advice from magazines or TV.")
    Item(scale=sss, text="When someone coughs or sneezes, I usually feel the urge to do the same.")
    Item(scale=sss, text="Imagining a refreshing drink can make me thirsty.")
    Item(scale=sss, text="A good salesperson can really make me want their product.")
    Item(scale=sss, text="I have picked-up many habits from my friends.")
    Item(scale=sss, text="It is important for me to fit in.")
    Item(scale=sss, text="When I see someone shiver, I often feel a chill myself.")
    Item(scale=sss, text="I get my style from certain celebrities.")
    Item(scale=sss, text="When people tell me how they feel, I often notice that I feel the same way.")
    Item(scale=sss, text="When making a decision, I often follow other people’s advice.")
    Item(scale=sss, text="Reading descriptions of tasty dishes can make my mouth water.")
    Item(scale=sss, text="I get many good ideas from others.")
    Item(scale=sss, text="I can be influenced by a good commercial.")
    Item(scale=sss, text="After I see a commercial for lotion, sometimes my skin feels dry.")
    Item(scale=sss, text="I discovered many of my favorite things through my friends.")
    Item(scale=sss, text="If a product is nicely displayed, I usually want to buy it.")
    Item(scale=sss, text="Thinking about something scary can make my heart pound.")
    Item(scale=sss, text="I frequently change my opinion after talking with others.")
    Item(scale=sss, text="If I am told I don’t look well, I start feeling ill.")
    Item(scale=sss, text="I follow current fashion trends.")

    stait = Scale(name='STAIT', full_name='state trait anxiety inventory')
    Item(scale=stait, text="I am happy.", reverse_score=True)
    Item(scale=stait, text="I am content.", reverse_score=True)
    Item(scale=stait, text="I feel satisfied with myself.", reverse_score=True)
    Item(scale=stait, text="I feel pleasant.", reverse_score=True)
    Item(scale=stait, text="I feel secure.", reverse_score=True)
    Item(scale=stait, text="I lack self-confidence.")
    Item(scale=stait, text="I feel inadequate.")
    Item(scale=stait, text="I feel like a failure.")
    Item(scale=stait, text="I am a steady person.", reverse_score=True)
    Item(scale=stait, text="I wish I could be as happy as others seem to be.")
    Item(scale=stait, text="I make decisions easily.", reverse_score=True)
    Item(scale=stait, text="I am 'calm, cool, and collected'.", reverse_score=True)
    Item(scale=stait, text="I feel rested.", reverse_score=True)
    Item(scale=stait, text="Some unimportant thought runs through my mind and bothers me.")
    Item(scale=stait, text="I worry too much over something that really doesn't matter.")
    Item(scale=stait, text="I get in a state of tension or turmoil as I think over my recent concerns and interests.")
    Item(scale=stait, text="I have disturbing thoughts.")
    Item(scale=stait, text="I feel nervous and restless.")
    Item(scale=stait, text="I take disappointments so keenly that I can't put them out of my mind.")
    Item(scale=stait, text="I feel that difficulties are piling up so that I can't overcome them.")

    panas = Scale(name='PANAS', full_name='positive and negative affection scale')
    panas_negative = Subscale(scale=panas, name='panas_negative')
    panas_positive = Subscale(scale=panas, name='panas_positive')
    Item(scale=panas, text="Interested", subscale=panas_positive)
    Item(scale=panas, text="Distressed", subscale=panas_negative)
    Item(scale=panas, text="Excited", subscale=panas_positive)
    Item(scale=panas, text="Upset", subscale=panas_negative)
    Item(scale=panas, text="Strong", subscale=panas_positive)
    Item(scale=panas, text="Guilty", subscale=panas_negative)
    Item(scale=panas, text="Scared", subscale=panas_negative)
    Item(scale=panas, text="Hostile", subscale=panas_negative)
    Item(scale=panas, text="Enthusiastic", subscale=panas_positive)
    Item(scale=panas, text="Proud", subscale=panas_positive)
    Item(scale=panas, text="Irritable", subscale=panas_negative)
    Item(scale=panas, text="Alert", subscale=panas_positive)
    Item(scale=panas, text="Ashamed", subscale=panas_negative)
    Item(scale=panas, text="Inspired", subscale=panas_positive)
    Item(scale=panas, text="Nervous", subscale=panas_negative)
    Item(scale=panas, text="Determined", subscale=panas_positive)
    Item(scale=panas, text="Attentive", subscale=panas_positive)
    Item(scale=panas, text="Jittery", subscale=panas_negative)
    Item(scale=panas, text="Active", subscale=panas_positive)
    Item(scale=panas, text="Afraid", subscale=panas_negative)

    qids = Scale(name='QIDS', full_name='quick inventory of depression symptology')
    Item(scale=qids, text="Falling asleep:")
    Item(scale=qids, text="Sleep during the night:")
    Item(scale=qids, text="Waking up too early:")
    Item(scale=qids, text="Sleeping too much:")
    Item(scale=qids, text="Feeling sad:")
    Item(scale=qids, text="Decreased appetite:")
    Item(scale=qids, text="Increased appetite:")
    Item(scale=qids, text="Decreased weight (within the last two weeks):")
    Item(scale=qids, text="Increased weight (within the last two weeks):")
    Item(scale=qids, text="Concentration/Decision making:")
    Item(scale=qids, text="View of myself:")
    Item(scale=qids, text="Thoughts of death or suicide:")
    Item(scale=qids, text="General interest:")
    Item(scale=qids, text="Energy level:")
    Item(scale=qids, text="Feeling slowed down:")
    Item(scale=qids, text="Feeling restless:")

    # Falling asleep
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Falling asleep:").first(),
        response="I never take longer than 30 minutes to fall asleep.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Falling asleep:").first(),
        response="I take at least 30 minutes to fall asleep, less than half the time.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Falling asleep:").first(),
        response="I take at least 30 minutes to fall asleep, more than half the time.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Falling asleep:").first(),
        response="I take more than 60 minutes to fall asleep, more than half the time.",
        value=3,)

    # Sleep during night
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Sleep during the night:").first(),
        response="I do not wake up at night.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Sleep during the night:").first(),
        response="I have a restless, light sleep with a few brief awakenings each night.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Sleep during the night:").first(),
        response="I wake up at least once a night, but I go back to sleep easily.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Sleep during the night:").first(),
        response="I awaken more than once a night and stay awake for 20 minutes or more, more than half the time.",
        value=3,)

    # Waking up too early
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Waking up too early:").first(),
        response="Most of the time, I awaken no more than 30 minutes before I need to get up.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Waking up too early:").first(),
        response="More than half the time, I awaken more than 30 minutes before I need to get up.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Waking up too early:").first(),
        response="I almost always awaken at least one hour or so before I need to, but I go back to sleep eventually.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Waking up too early:").first(),
        response="I awaken at least one hour before I need to, and can’t go back to sleep.",
        value=3,)

    # Sleeping too much
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Sleeping too much:").first(),
        response="I sleep no longer than 7–8 hours/night, without napping during the day.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Sleeping too much:").first(),
        response="I sleep no longer than 10 hours in a 24-hour period including naps.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Sleeping too much:").first(),
        response="I sleep no longer than 12 hours in a 24-hour period including naps.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Sleeping too much:").first(),
        response="I sleep longer than 12 hours in a 24-hour period including naps.",
        value=3,)

    # Feeling sad
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Feeling sad:").first(),
        response="I do not feel sad.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Feeling sad:").first(),
        response="I feel sad less than half the time.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Feeling sad:").first(),
        response="I feel sad more than half the time.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Feeling sad:").first(),
        response="I feel sad nearly all of the time.",
        value=3,)

    # Decreaed appetite
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Decreased appetite:").first(),
        response="There is no change in my usual appetite.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Decreased appetite:").first(),
        response="I eat somewhat less often or lesser amounts of food than usual.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Decreased appetite:").first(),
        response="I eat much less than usual and only with personal effort.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Decreased appetite:").first(),
        response="I rarely eat within a 24-hour period, and only with extreme personal effort or when others persuade me to eat.",
        value=3,)

    # Increased appetite
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Increased appetite:").first(),
        response="There is no change from my usual appetite.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Increased appetite:").first(),
        response="I feel a need to eat more frequently than usual.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Increased appetite:").first(),
        response="I regularly eat more often and/or greater amounts of food than usual.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Increased appetite:").first(),
        response="I feel driven to overeat both at mealtime and between meals.",
        value=3,)

    # "Decreased weight (within the last two weeks):"
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Decreased weight (within the last two weeks):").first(),
        response="I have not had a change in my weight.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Decreased weight (within the last two weeks):").first(),
        response="I feel as if I’ve had a slight weight loss.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Decreased weight (within the last two weeks):").first(),
        response="I have lost 2 pounds (about 1kg) or more.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Decreased weight (within the last two weeks):").first(),
        response="I have lost 5 pounds (about 2kg) or more.",
        value=3,)

    # "Increased weight (within the last two weeks):"
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Increased weight (within the last two weeks):").first(),
        response="I have not had a change in my weight.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Increased weight (within the last two weeks):").first(),
        response="I feel as if I’ve had a slight weight gain.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Increased weight (within the last two weeks):").first(),
        response="I have gained 2 pounds (about 1kg) or more.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Increased weight (within the last two weeks):").first(),
        response="I have gained 5 pounds(about 2kg) or more.",
        value=3,)

    # "Concentration/Decision making:"
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Concentration/Decision making:").first(),
        response="There is no change in my usual capacity to concentrate or make decisions.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Concentration/Decision making:").first(),
        response="I occasionally feel indecisive or find that my attention wanders.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Concentration/Decision making:").first(),
        response="Most of the time, I struggle to focus my attention or to make decisions.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Concentration/Decision making:").first(),
        response="I cannot concentrate well enough to read or cannot make even minor decisions.",
        value=3,)

    # "View of myself:"
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="View of myself:").first(),
        response="I see myself as equally worthwhile and deserving as other people.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="View of myself:").first(),
        response="I am more self-blaming than usual.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="View of myself:").first(),
        response="I largely believe that I cause problems for others.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="View of myself:").first(),
        response="I think almost constantly about major and minor defects in myself.",
        value=3,)

    # "Thoughts of death or suicide:"
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Thoughts of death or suicide:").first(),
        response="I do not think of suicide or death.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Thoughts of death or suicide:").first(),
        response="I feel that life is empty or wonder if it’s worth living.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Thoughts of death or suicide:").first(),
        response="I think of suicide or death several times a week for several minutes.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Thoughts of death or suicide:").first(),
        response="I think of suicide or death several times a day in some detail, or I have made specific plans for suicide or have actually tried to take my life.",
        value=3,)

    # "General interest:"
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="General interest:").first(),
        response="There is no change from usual in how interested I am in other people or activities.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="General interest:").first(),
        response="I notice that I am less interested in people or activities.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="General interest:").first(),
        response="I find I have interest in only one or two of my formerly pursued activities.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="General interest:").first(),
        response="I have virtually no interest in formerly pursued activities.",
        value=3,)

    # "Energy level:"
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Energy level:").first(),
        response="There is no change in my usual level of energy.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Energy level:").first(),
        response="I get tired more easily than usual.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Energy level:").first(),
        response="I have to make a big effort to start or finish my usual daily activities (for example, shopping, homework, cooking or going to work).",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Energy level:").first(),
        response="I really cannot carry out most of my usual daily activities because I just don’t have the energy.",
        value=3,)

    # "Feeling slowed down:"
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Feeling slowed down:").first(),
        response="I think, speak, and move at my usual rate of speed.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Feeling slowed down:").first(),
        response="I find that my thinking is slowed down or my voice sounds dull or flat.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Feeling slowed down:").first(),
        response="It takes me several seconds to respond to most questions and I’m sure my thinking is slowed.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Feeling slowed down:").first(),
        response="I am often unable to respond to questions without extreme effort.",
        value=3,)

    # "Feeling restless:"
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Feeling restless:").first(),
        response="I do not feel restless.",
        value=0,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Feeling restless:").first(),
        response="I’m often fidgety, wringing my hands, or need to shift how I am sitting.",
        value=1,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Feeling restless:").first(),
        response="I have impulses to move about and am quite restless.",
        value=2,)
    ResponseOption(
        item=db.Item.select(lambda item: item.text=="Feeling restless:").first(),
        response="At times, I am unable to stay seated and need to pace around.",
        value=3,)

    commit()
    return db
