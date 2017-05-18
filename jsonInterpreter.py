# -*- coding: utf-8 -*-

# Imports
import json
from PersonClass import Person
#
def addPeople(crosoftJson) :
    """
    :return:gens[Person]
    """
    elJson = json.loads(crosoftJson)
    gens = []

    for x in elJson:
        gens.append(Person(x))

    return gens
