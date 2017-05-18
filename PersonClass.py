# -*- coding: utf-8 -*-

# Imports
import json
import numpy as np

# Class code


class Person:
    """

    """
    def getHumor(self):
        """
        :return:tuple(emotion dominante, score dominante)
        """
        dominantEmotion = "unknown"
        dominantScore = "0"
        for x,y in self.emotions:
            if y >= dominantScore :
                dominantEmotion = x
                dominantScore = y

        return dominantEmotion, dominantScore

    def getScore(self, emotion):
        score = self.emotions[emotion]

        return score

    def __init__(self, personParms):

        faceRectangle = {}
        faceRectangle['left'] = personParms["faceRectangle"]

        emotions = personParms["scores"]