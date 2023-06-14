import sys
sys.path.append('..')
import unittest
from app.models.memory import Memory

class TestHand(unittest.TestCase):
    def setUp(self):
        print('hand')