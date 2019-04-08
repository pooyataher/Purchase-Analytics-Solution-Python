import products
import unittest


class Test_products(unittest.TestCase):

    def setUp(self):
        # infname1 contains a header, but infname2 does not.
        # We expect the same output from both files.
        infname1 = '../insight_testsuite/tests/test_1/input/products.csv'
        infname2 = '../insight_testsuite/tests/test_2/input/products.csv'
        self.infname = [infname1, infname2]

    def test_load_csv(self):
        output = {'104': '13', '35': '12', '91': '16', '83': '4',
                  '112': '3', '86': '16', '19': '13', '93': '3'}
        for infname in self.infname:
            self.assertEqual(products.load_csv(infname, 2, 3), output)

    def test_load_prod_table(self):
        output = {'9327': '13', '17461': '12', '17668': '16', '28985': '4',
                  '32665': '3', '33120': '16', '45918': '13', '46667': '4',
                  '46842': '3'}
        for infname in self.infname:
            self.assertEqual(products.load_prod_table(infname), output)


if __name__ == '__main__':
    unittest.main()
