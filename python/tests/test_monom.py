import unittest


from monom import Monom


class TestBoolMonom(unittest.TestCase):

    def setUp(self):
        Monom.variables = "abcd"

    def test_init(self):
        m1 = Monom([1,1,1,0])
        m2 = Monom([1,1,0,0])
        m3 = Monom([0,0,1,0])
        m4 = Monom([0,0,0,1])

        self.assertEqual(m1, (1,1,1,0))
        self.assertEqual(m2, (1,1,0,0))
        self.assertEqual(m3, (0,0,1,0))
        self.assertEqual(m4, (0,0,0,1))

    def test_mul(self):
        a = Monom((1,0,0,0))
        b = Monom((0,1,0,0))

        self.assertEqual(a*a, a)
        self.assertEqual(b*a, a*b)

    def test_truediv(self):
        a = Monom([1,0,0,0])
        b = Monom([0,1,0,0])
        c = Monom([0,0,1,0])

        ab = a*b
        bc = b*c
        abc = a*b*c

        _0, _1 = Monom.zero, Monom.one

        # 1/a == 0
        self.assertEqual(_0, _1/a)
        # a == a/1
        self.assertEqual(a, a/_1)
        # a/b == 0
        self.assertEqual(_0, a/b)
        # ab/b == a
        self.assertEqual(a, ab/b)
        # ab/a == b
        self.assertEqual(b, ab/a)
        # abc/ab == c
        self.assertEqual(c, abc/ab)
        # ab/bc == 0
        self.assertEqual(_0, ab/bc)

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

        self.assertEqual([1,3], m1.vars)
