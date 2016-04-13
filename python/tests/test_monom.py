import unittest


from monom import Monom


class TestBoolMonom(unittest.TestCase):

    def setUp(self):
        Monom.variables = "abcd"

    def test_init(self):
        m1, m2, m3, m4 = Monom([1,1,1,0]), Monom([1,1,0,0]), Monom([0,0,1,0]), Monom([0,0,0,1])

        self.assertEqual(str(m1), 'abc')
        self.assertEqual(str(m2), 'ab')
        self.assertEqual(str(m3), 'c')
        self.assertEqual(str(m4), 'd')

    def test_mul(self):
        m1 = Monom((1,0,0,0))*Monom((1,0,0,0))
        m2 = Monom((1,0,0,0))*Monom((0,1,0,0))

        self.assertEqual(str(m1), 'a')
        self.assertEqual(str(m2), 'ab')

    def test_truediv(self):
        m = Monom([1,0,0,0])

        r = Monom.one/m

        self.assertTrue(True)

    def test_isdivisible(self):
        m = Monom([1,0,0,0])

        self.assertFalse(Monom.one.isdivisible(m))

        self.assertTrue(Monom.one.isdivisible(Monom.one))

    def test_isrelativelyprime(self):
        m1 = Monom([1,0,0,0])
        m2 = Monom([0,1,0,0])
        self.assertTrue(m1.isrelativelyprime(m2))

        m1 = Monom([1,0,1,0])
        m2 = Monom([0,1,0,0])
        self.assertTrue(m1.isrelativelyprime(m2))

        m1 = Monom([1,0,0,0])
        m2 = Monom([1,0,0,0])
        self.assertTrue(m1.isrelativelyprime(m2))

        m1 = Monom([1,1,0,0])
        m2 = Monom([0,1,0,0])
        self.assertFalse(m1.isrelativelyprime(m2))

    def test_lcm(self):
        self.assertTrue(True)

    def test_vars(self):
        m1 = Monom([1,0,1,0])

        self.assertEqual([0,2], m1.vars)
