# -*- coding: utf-8 -*-

# Imports
import json
import numpy as np

# Class code


class Person:
    """

    """
    emotions = "unknown";

    def getHumor(self):
        dominantEmotion = "unknown"
        for x,y in self.emotions:
            if y >= 0.7 :
                dominantEmotion = x

        return dominantEmotion



    def __init__(self, personParms):

        faceRectangle = {}
        faceRectangle['left'] = personParms["faceRectangle"]

        emotions = personParms["scores"]