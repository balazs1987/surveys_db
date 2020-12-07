"""
Define sqlite DB structure which represents survezs
:Author: Balazs Szigeti <microdose-studz.protonmail.com>
:Copyright: 2020, DrugNerdsLab
:License: MIT
"""

from pony.orm import *

db = Database()

class Scale(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    items = Set('Item')
    subscales = Set('Subscale')
    full_name = Optional(str)


class Item(db.Entity):
    id = PrimaryKey(int, auto=True)
    scale = Required(Scale)
    subscale = Optional('Subscale')
    text = Required(str)
    reverse_score = Required(bool, default=False)
    response_options = Set('ResponseOption')


class Subscale(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    scale = Required(Scale)
    items = Set(Item)


class ResponseOption(db.Entity):
    id = PrimaryKey(int, auto=True)
    value = Required(int)
    item = Required(Item)
    response = Required(str)
