from naoqi import ALProxy
from naoqi import ALModule
global memory


class NaoTextEventModule(ALModule):
    """
    NaoTextEventModule module qui fait la reconnaissance vocal.
    """
    def __init__(self, name):
        ALModule.__init__(self, name)
        self.tts = ALProxy("ALTextToSpeech")
        try:
            sr = ALProxy("ALSpeechRecognition")
            sr.setLanguage("French")
            sr.setVocabulary(["oui", "non"], False)  # si true : mot au milieu d'une phrase, si false : que le mot
        except Exception as e:
            sr = None
        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("WordRecognized",
                                "NaoTextEvent",
                                "onSpeechDetected")
        self.motion = ALProxy("ALMotion")
        self.tracker = ALProxy("ALTracker")

        # First, wake up.
        self.motion.wakeUp()

        # Add target to track.
        targetName = "Face"
        faceWidth = 1
        self.tracker.registerTarget(targetName, faceWidth)

    def onSpeechDetected(self, eventName, value, subIdent):

        # Unsubscribe to the event when talking,
        # to avoid repetitions
        memory.unsubscribeToEvent("WordRecognized", "NaoTextEvent")
        memory.subscribeToEvent("WordRecognized",
                                "NaoTextEvent",
                                "onSpeechDetected")



