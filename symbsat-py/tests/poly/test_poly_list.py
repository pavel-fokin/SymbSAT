import unittest

from symbsat.monom import Monom4 as Monom
from symbsat.poly_new import PolyList, PolyZDD


class BaseTest(unittest.TestCase):

    def setUp(self):
        # Added this because of the pylint warning
        self.poly_cls = object

    def test_init_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.poly_cls()

    def test_init_from_var(self):
        self.poly_cls(var=0)

    def test_init_from_monom(self):

        monom_zero = Monom.zero()
        self.poly_cls(monom=monom_zero)

        monom_one = Monom.one()
        self.poly_cls(monom=monom_one)

        monom_a = Monom(vars=[1])
        self.poly_cls(monom=monom_a)

        monom_ab = Monom(vars=[1, 2])
        self.poly_cls(monom=monom_ab)

    def test_init_from_monoms(self):
        monom_a = Monom(vars=[1])
        monom_b = Monom(vars=[2])
        self.poly_cls(monoms=[monom_a, monom_b])


class TestPolyList(BaseTest):

    def setUp(self):
        self.poly_cls = PolyList

    @unittest.skip('Not implemented')
    def test_init_from_var(self):
        pass


class TestPolyZDD(BaseTest):

    def setUp(self):
        self.poly_cls = PolyZDD

    #  @unittest.skip('Not implemented')
    #  def test_init_from_monom(self):
    #      pass

    @unittest.skip('Not implemented')
    def test_init_from_monoms(self):
        pass


def load_tests(loader, tests, pattern):
    test_cases = (TestPolyList, TestPolyZDD)

    suite = unittest.TestSuite()
    for test_case in test_cases:
        tests = loader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)

    return suite
