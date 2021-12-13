import unittest


import ezcli
import ezcli._error
import ezcli._prebuilt
import ezcli.conf


class TestConfig(unittest.TestCase):
    def setUp(self):
        ezcli.conf.CONFIG.ISDONE = False

    def test_default_config(self):
        ezcli.config()

        self.assertTrue(ezcli.conf.CONFIG.ISDONE)
        self.assertEqual(ezcli.conf.CONFIG.LANGUAGE, 'en')
        self.assertEqual(ezcli.conf.CONFIG.NAME, ezcli._prebuilt.NO_NAME)
        self.assertEqual(ezcli.conf.CONFIG.VERSION, ezcli._prebuilt.NO_VERSION)

    def test_reconfig(self):
        ezcli.config()

        with self.assertRaises(ezcli._error.EzCLIError):
            ezcli.config()

    def test_normal_config(self):
        ezcli.config(appname='Unit tests', appversion='1.2.3', language='en')

        self.assertTrue(ezcli.conf.CONFIG.ISDONE)
        self.assertEqual(ezcli.conf.CONFIG.LANGUAGE, 'en')
        self.assertEqual(ezcli.conf.CONFIG.NAME, 'Unit tests')
        self.assertEqual(ezcli.conf.CONFIG.VERSION, '1.2.3')


if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(TestConfig('test_default_config'))
    suite.addTest(TestConfig('test_reconfig'))
    suite.addTest(TestConfig('test_normal_config'))

    unittest.TextTestRunner().run(suite)