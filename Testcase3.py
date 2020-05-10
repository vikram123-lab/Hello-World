import unittest


class AppTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("open appp")

    @classmethod
    def setUp(self):
        print("This is setup method")

    def test_search(self):
        print("This is search test")

    def test_advancesearch(self):
        print("This is advance search test")

    def test_prepaidRecharge(self):
        print("This is prepaid recharge")

    def test_postpaidRecharge(self):
        print("This is postpaid recharge test")
    @classmethod
    def tearDown(self):
        print("This is tearDown method")
    @classmethod
    def tearDownClass(cls):
        print("close the app")

if __name__=="__main__":
    unittest.main()

