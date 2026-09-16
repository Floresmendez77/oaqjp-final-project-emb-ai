"""Pruebas unitarias para la función emotion_detector."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Verifica que emotion_detector identifique correctamente
    la emoción dominante para distintos textos de ejemplo."""

    def test_emotion_detector(self):
        """Prueba las 5 emociones: joy, anger, disgust, sadness y fear."""
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        result_2 = emotion_detector("I am so angry")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        result_3 = emotion_detector("I am so disgusted")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        result_4 = emotion_detector("I am so sad")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        result_5 = emotion_detector("I am so afraid")
        self.assertEqual(result_5['dominant_emotion'], 'fear')


unittest.main()