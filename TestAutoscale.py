# File name: TestAutoscale.py
# This file contains the unit tests for model_auto_config.py.
# python -m unittest -v TestAutoscale.py

import unittest
import autoscale_deployment

class TestAutoscale(unittest.TestCase):
       def setUp(self):
              self.trans = autoscale_deployment.Translator()
       def test_translation(self):
              self.assertEqual(self.trans.translate("hello"), 'bonjour')

if __name__ == '__main__':
      unittest.main()