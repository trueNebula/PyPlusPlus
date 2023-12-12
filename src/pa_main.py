import unittest

from structures.parser import Parser
from structures.grammar import Grammar

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.g = Grammar()
        self.g.read('./examples/grammars/g1.in')
        self.w = "aacbc"
        self.p = Parser(self.g, self.w)

    def test(self):
        self.p.success()
        self.assertEqual(self.p.get_config().get_current_state(), 'final')
        self.p.momentary_insuccess()
        self.assertEqual(self.p.get_config().get_current_state(), 'back')
        self.p.advance()
        self.assertEqual(self.p.get_config().get_current_state(), 'back')
        self.assertEqual(self.p.get_config().get_current_position(), 2)
        self.assertEqual(self.p.get_config().get_stack(), ['S'])


if __name__ == "__main__":
    t = Test()
    t.setUp()
    t.test()
        
