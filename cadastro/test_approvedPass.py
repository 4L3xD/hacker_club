#https://docs.python.org/pt-br/3/library/unittest.html#test-discovery

import unittest
from approvedPass import Approved

class ApprovedPassTests(unittest.TestCase):
    def test_YouShouldNotPass(self):
        """Testando validade da senha digitada!"""
        self.assertIsNone(
            Approved().test_password("1234"),
        )

    def test_YouShouldPass(self):
        """Testando validade da senha digitada!"""
        self.assertEqual(
            Approved().test_password("1234ABCdef!@#$%"),
            '1234ABCdef!@#$%'
        )

if __name__ == '__main__':
    unittest.main()