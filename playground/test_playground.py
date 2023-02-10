import unittest
from playground import PlayGround


class PlayGroundTest(unittest.TestCase):

    def setUp(self):
        self.playground = PlayGround()

    def test_get_google(self):
        response = self.playground.get_google()
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
