import unittest

import ezcli
import ezcli._config
import ezcli._prebuilt

class TestConfig(unittest.TestCase):
    def setUp(self):
        ezcli._config.DONE = False

    def test_default_config(self):
        ezcli.config()
        self.assertTrue(ezcli._config.DONE)
        self.assertEqual(ezcli._config.NAME, ezcli._prebuilt.NO_NAME['en'])
        self.assertEqual(ezcli._config.VER, ezcli._prebuilt.NO_VERSION['en'])
        self.assertEqual(ezcli._config.LANG, 'en')

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestConfig('test_default_config'))
    unittest.TextTestRunner().run(suite)