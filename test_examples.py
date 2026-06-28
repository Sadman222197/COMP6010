import unittest, sys, json
import Stage_1_Basics as S1
from Stage_2_IngredientData import IngredientData
from Stage_3_Inventory import Inventory
from Stage_4_Kitchen import Kitchen

marks = 0
passed = []
skipped_big = 0
hidden = True
big_tests = True

unittest.util._MAX_LENGTH=256 # (optional) make it easier to see long errors

def main():
    error = False
    try:
        unittest.main(exit=False)
    except Exception as e:
        error = str(e)
    finally:
        data = {
            'marks' : marks,
            'passed' : passed,
            'error' : error,
            'skipped' : skipped_big,
        }
        with open('result.json', 'w') as f:
            json.dump(data, f)

        if error:
            sys.exit(1)
        else:
            sys.exit(0)

class Tester(unittest.TestCase):

    @classmethod
    def tearDownClass(self):
        global marks, passed, final_output
        passed = sorted(passed, key=lambda x: int(x['test'].split('.')[0]))

        print('\n'*3)
        print('<><><><><><><><><><>')
        print('--------------------')
        print('====================')
        print('--------------------')
        print(f'Final Mark: {marks}')
        print(f"Passed: {passed}")
        print('--------------------')
        print('====================')
        print('--------------------')
        print('<><><><><><><><><><>')
        final_output = f'Final Mark: {marks}\nPassed: {passed}'


    # ===============================
    # Tests for Stage 1: Basics
    # ===============================

    def test_analysis(self):
        # Input is 0 or 0.0...
        self.assertEqual(":)", S1.analysis(0.0))
        self.assertEqual(":)", S1.analysis(0.000))
        self.assertEqual(":)", S1.analysis(1 + 1 - 2))

        # Input is a nonzero int or float...
        self.assertEqual(0.1, S1.analysis(10))
        self.assertEqual(0.1, S1.analysis(10.0))
        self.assertEqual(2.5, S1.analysis(0.4))
        self.assertEqual(-2/3, S1.analysis(-3/2))

        # The output is allowed to be an int or a float
        self.assertEqual(10, S1.analysis(0.1))
        self.assertEqual(10.00, S1.analysis(0.1))
        self.assertEqual(1, S1.analysis(1))
        self.assertEqual(1.0, S1.analysis(1))
        self.assertEqual(1, S1.analysis(1.0))
        self.assertEqual(1.0, S1.analysis(1.0))

        # Mystery is a Boolean
        loud = True
        big = False
        self.assertEqual(loud and not big, S1.analysis(big or not loud))
        self.assertEqual(loud or big, S1.analysis(not loud and not big))
        self.assertEqual(loud and not loud, S1.analysis(loud or not loud))

        # Mystery is a string that is at least 5 characters long
        self.assertEqual("ae", S1.analysis("abcde"))
        self.assertEqual("aB", S1.analysis("abcABC"))
        self.assertEqual("Ae", S1.analysis("Abcdefgh"))
        self.assertEqual("W?", S1.analysis("What?"))
        self.assertEqual("h!", S1.analysis("hELP!"))
        self.assertEqual("tt", S1.analysis("tractor"))
        self.assertEqual("T ", S1.analysis("This is a test"))
        self.assertEqual(":3", S1.analysis(":) <3"))

        # Other cases
        self.assertEqual(42, S1.analysis(None))
        self.assertEqual(42, S1.analysis(["This", "is", "a", "list"]))
        self.assertEqual(42, S1.analysis([1, 2, 3, 4, 5, 6, 7]))
        self.assertEqual(42, S1.analysis("Help"))
        self.assertEqual(42, S1.analysis("!"))
        self.assertEqual(42, S1.analysis(""))

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "1.1. test_analysis (examples)", "marks" : 2.5})
        marks += 2.5

    def test_number_time(self):
        # two even ints
        self.assertEqual(None, S1.number_time(2, 4))
        self.assertEqual(None, S1.number_time(-12, 0))
        self.assertEqual(None, S1.number_time(0, 0))

        # two odd ints
        self.assertEqual(6, S1.number_time(17, 11))
        self.assertEqual(122, S1.number_time(123, 1))
        self.assertEqual(-2, S1.number_time(5, 7))
        self.assertEqual(0, S1.number_time(-1, -1))
        self.assertEqual(2, S1.number_time(-1, -3))

        # one odd int and one even int
        self.assertEqual(5, S1.number_time(2, 3))
        self.assertEqual(-1, S1.number_time(0, -1))
        self.assertEqual(125, S1.number_time(123, 2))
        self.assertEqual(1, S1.number_time(-1, 2))

        # no numbers
        self.assertEqual("No numbers", S1.number_time(True, False))
        self.assertEqual("No numbers", S1.number_time(None, "12"))

        # floats are not ints
        self.assertEqual("One number", S1.number_time(-3.141, -3))
        self.assertEqual("One number", S1.number_time(5.0, 5))

        # lists are not ints
        self.assertEqual("No numbers", S1.number_time(None, [1, "list"]))
        self.assertEqual("No numbers", S1.number_time([1, 2, 3], [4, 5, 6]))
        self.assertEqual("One number", S1.number_time(-3, [4, 5, 6]))
        self.assertEqual("One number", S1.number_time([4, 5, 6], 10))

        self.assertEqual("One number", S1.number_time([4, 5, 6], 10))
        self.assertEqual("No numbers", S1.number_time([12], 4.5))
        self.assertEqual("No numbers", S1.number_time(4.5, [12]))

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "1.2. test_number_time (examples)", "marks" : 2.5})
        marks += 2.5

    def test_is_more_than_double(self):

        self.assertEqual(True, S1.is_more_than_double(5, 1.1))
        self.assertEqual(True, S1.is_more_than_double(100, 49.999))

        self.assertEqual(False, S1.is_more_than_double(100, 50.001))
        self.assertEqual(False, S1.is_more_than_double(5, 3))

        # (-3) is greater than (-4)
        self.assertEqual(True, S1.is_more_than_double(-3, -2))

        # 0 is greater than (-2)
        self.assertEqual(True, S1.is_more_than_double(0, -1))

        self.assertEqual(True, S1.is_more_than_double(1, 0))
        self.assertEqual(True, S1.is_more_than_double(1, -1))

        # 2 is not greater than 2
        self.assertEqual(False,S1.is_more_than_double(2, 1))
        self.assertEqual(False,S1.is_more_than_double(2.0, 1.0))
        self.assertEqual(False,S1.is_more_than_double(2.0, 1))
        self.assertEqual(False,S1.is_more_than_double(2, 1.0))

        # (-1) is not greater than (-1)
        self.assertEqual(False,S1.is_more_than_double(-1, -0.5))
        self.assertEqual(False,S1.is_more_than_double(-1.0, -0.5))
        self.assertEqual(False,S1.is_more_than_double(-2, -1))
        self.assertEqual(False,S1.is_more_than_double(-2, -1.0))

        # 100 is not greater than 100
        self.assertEqual(False,S1.is_more_than_double(100, 50))
        self.assertEqual(False,S1.is_more_than_double(100, 50.0))
        self.assertEqual(False,S1.is_more_than_double(100.0, 50))
        self.assertEqual(False,S1.is_more_than_double(100.0, 50.0))

        self.assertEqual("Oh no", S1.is_more_than_double("0", 1))
        self.assertEqual("Oh no", S1.is_more_than_double(0, "1"))
        self.assertEqual("Oh no", S1.is_more_than_double("0", "1"))
        self.assertEqual("Oh no", S1.is_more_than_double(None, None))
        self.assertEqual("Oh no", S1.is_more_than_double(1, [2]))
        self.assertEqual("Oh no", S1.is_more_than_double([1], 2))
        self.assertEqual("Oh no", S1.is_more_than_double(4.0, True))
        self.assertEqual("Oh no", S1.is_more_than_double(False, 1.0))

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "1.3. test_is_more_than_double (examples)", "marks" : 2.5})
        marks += 2.5

    def test_redact(self):
        the_plaintext = "Hello, shopkeeper. I have 3 apples."
        result = S1.redact(the_plaintext)
        # result is a string
        self.assertIsInstance(result, str)
        # len(redact(the_plaintext)) equals len(the_plaintext)
        self.assertEqual(len(the_plaintext), len(result))
        # The result might contain '0', but can't contain '1' to '9'
        self.assertNotIn("1", result)
        self.assertNotIn("2", result)
        self.assertNotIn("3", result)
        self.assertNotIn("4", result)
        self.assertNotIn("5", result)
        self.assertNotIn("6", result)
        self.assertNotIn("7", result)
        self.assertNotIn("8", result)
        self.assertNotIn("9", result)
        # The result might contain 'X' or 'x', but can't contain other letters
        for letter in "ABCDEFGHIJKLMNOPQRSTUVW" + "YZ":
            self.assertNotIn(letter, result)
        for letter in "abcdefghijklmnopqrstuvw" + "yz":
            self.assertNotIn(letter, result)

        for i in range(len(the_plaintext)):
            extra_debug_output = f"index is {i}, the_plaintext = {the_plaintext}, result = {result}"
            if the_plaintext[i] in "., ":
                # The special characters should not be affected!
                self.assertEqual(the_plaintext[i], result[i], extra_debug_output)
            else:
                # The letters and digits should change.
                self.assertNotEqual(the_plaintext[i], result[i], extra_debug_output)

        the_plaintext = "Sale! Xylophones: $39.90 minus tax!"
        result = S1.redact(the_plaintext)
        self.assertIsInstance(result, str)
        self.assertEqual(len(the_plaintext), len(result))
        self.assertNotIn("1", result)
        self.assertNotIn("2", result)
        self.assertNotIn("3", result)
        self.assertNotIn("4", result)
        self.assertNotIn("5", result)
        self.assertNotIn("6", result)
        self.assertNotIn("7", result)
        self.assertNotIn("8", result)
        self.assertNotIn("9", result)
        for letter in "ABCDEFGHIJKLMNOPQRSTUVW" + "YZ":
            self.assertNotIn(letter, result)
        for letter in "abcdefghijklmnopqrstuvw" + "yz":
            self.assertNotIn(letter, result)

        for i in range(len(the_plaintext)):
            if the_plaintext[i] == "3" or the_plaintext[i] == "9" or the_plaintext[i] == "0":
                # digits
                self.assertEqual("X", result[i], f"i={i}, result = {result}")
            elif the_plaintext[i] == "S" or the_plaintext[i] == "X":
                # uppercase letters change
                self.assertEqual("x", result[i], f"i={i}, result = {result}")
            elif the_plaintext[i] in "!: $.":
                # symbols don't change
                self.assertEqual(the_plaintext[i], result[i], f"i={i}, result = {result}")
            else:
                # lowercase letters change
                self.assertEqual("0", result[i], f"i={i}, result = {result}")

        # more tests
        the_plaintext = "Hello, shopkeeper. I have 3 apples."
        result = S1.redact(the_plaintext)
        expected = "x0000, 0000000000. x 0000 X 000000."
        self.assertEqual(expected, result)

        the_plaintext = "Sale! Xylophones: $39.90 minus tax!"
        result = S1.redact(the_plaintext)
        expected = "x000! x000000000: $XX.XX 00000 000!"
        self.assertEqual(expected, result)

        self.assertEqual("xxx", S1.redact("ABC"))
        self.assertEqual("x", S1.redact("Q"))
        self.assertEqual("x", S1.redact("X"))
        self.assertEqual("-> xxxx xxxxx", S1.redact("-> FREE STUFF"))

        self.assertEqual("000", S1.redact("abc"))
        self.assertEqual("00, 000 00000!", S1.redact("hi, plz reply!"))

        self.assertEqual("XXXXXXXXXX", S1.redact("1234509876"))
        self.assertEqual("XX.X", S1.redact("16.2"))

        self.assertEqual(":x :) <X", S1.redact(":P :) <3"))
        self.assertEqual("  : 0_x ", S1.redact("  : o_O "))
        self.assertEqual("xxxxXXXX: x0000000000 00 x0000000 x0000000000",
                         S1.redact("COMP6010: Foundations of Computer Programming"))

        jay_pig_fox = "The jay, pig, fox, zebra, and my 90 wolves quack!"
        self.assertEqual(
            "x00 000, 000, 000, 00000, 000 00 XX 000000 00000!",
            S1.redact(jay_pig_fox))
        self.assertEqual(
            "xxx xxx, xxx, xxx, xxxxx, xxx xx XX xxxxxx xxxxx!",
            S1.redact(jay_pig_fox.upper()))
        self.assertEqual(
            "000 000, 000, 000, 00000, 000 00 XX 000000 00000!",
            S1.redact(jay_pig_fox.lower()))

        # If input is not a string, returns none
        self.assertIsNone(S1.redact(None))
        self.assertIsNone(S1.redact(1))
        self.assertIsNone(S1.redact(0))
        self.assertIsNone(S1.redact(0.1))
        self.assertIsNone(S1.redact(["l", "i", "s", "t"]))

        # examples end here
        # OPTIONAL: add your own examples!
        global marks, passed

        passed.append({"test" : "1.4. redact (examples)", "marks" : 2.5})
        marks += 2.5

    def test_is_better_wine_than(self):
        new_very_expensive_french_wine = {"vintage": 2026, "country": "France", "price": 9999.9}
        new_expensive_french_wine = {"vintage": 2026, "country": "fraNcland", "price": 500.0}
        new_cheap_french_wine = {"vintage": 2026, "country": "frAnz", "price": 450.0}
        new_expensive_wine = {"vintage": 2026, "country": "Australia", "price": 1234.5}
        new_cheap_wine = {"vintage": 2026, "country": "Frappe Shop", "price": 499.9 }
        old_very_expensive_french_wine = {"vintage": 1400, "country": "France", "price": 9999.9}
        old_expensive_french_wine = {"vintage": 1400, "country": "France", "price": 500.0}
        old_cheap_french_wine = {"vintage": 1991, "country": "fRAn", "price": 450.0}
        old_expensive_wine = {"vintage": 1666, "country": "fr", "price": 1234.5}
        old_cheap_wine = {"vintage": 1398, "country": "Flance", "price": 499.9 }

        # A wine is never better than itself.
        self.assertFalse(S1.is_better_wine_than(new_very_expensive_french_wine, new_very_expensive_french_wine))
        self.assertFalse(S1.is_better_wine_than(new_expensive_french_wine, new_expensive_french_wine))
        self.assertFalse(S1.is_better_wine_than(new_cheap_french_wine, new_cheap_french_wine))
        self.assertFalse(S1.is_better_wine_than(new_expensive_wine, new_expensive_wine))
        self.assertFalse(S1.is_better_wine_than(new_cheap_wine, new_cheap_wine))
        self.assertFalse(S1.is_better_wine_than(old_very_expensive_french_wine, old_very_expensive_french_wine))
        self.assertFalse(S1.is_better_wine_than(old_expensive_french_wine, old_expensive_french_wine))
        self.assertFalse(S1.is_better_wine_than(old_cheap_french_wine, old_cheap_french_wine))
        self.assertFalse(S1.is_better_wine_than(old_expensive_wine, old_expensive_wine))
        self.assertFalse(S1.is_better_wine_than(old_cheap_wine, old_cheap_wine))

        # Expensive is better than not...
        self.assertTrue(S1.is_better_wine_than(new_expensive_french_wine, new_cheap_french_wine))
        self.assertTrue(S1.is_better_wine_than(new_expensive_wine, new_cheap_wine))
        self.assertFalse(S1.is_better_wine_than(new_cheap_french_wine, new_expensive_french_wine))
        self.assertFalse(S1.is_better_wine_than(new_cheap_wine, new_expensive_wine))

        self.assertTrue(S1.is_better_wine_than(old_expensive_french_wine, old_cheap_french_wine))
        self.assertTrue(S1.is_better_wine_than(old_expensive_wine, old_cheap_wine))
        self.assertFalse(S1.is_better_wine_than(old_cheap_french_wine, old_expensive_french_wine))
        self.assertFalse(S1.is_better_wine_than(old_cheap_wine, old_expensive_wine))

        self.assertTrue(S1.is_better_wine_than(new_expensive_french_wine, old_cheap_french_wine))
        self.assertTrue(S1.is_better_wine_than(new_expensive_wine, old_cheap_wine))
        self.assertFalse(S1.is_better_wine_than(old_cheap_french_wine, new_expensive_french_wine))
        self.assertFalse(S1.is_better_wine_than(old_cheap_wine, new_expensive_wine))

        self.assertTrue(S1.is_better_wine_than(old_expensive_french_wine, new_cheap_french_wine))
        self.assertTrue(S1.is_better_wine_than(old_expensive_wine, new_cheap_wine))
        self.assertFalse(S1.is_better_wine_than(new_cheap_french_wine, old_expensive_french_wine))
        self.assertFalse(S1.is_better_wine_than(new_cheap_wine, old_expensive_wine))

        # ...but country takes precedence.
        self.assertTrue(S1.is_better_wine_than(new_cheap_french_wine, old_expensive_wine))
        self.assertFalse(S1.is_better_wine_than(old_expensive_wine, new_cheap_french_wine))

        wine_1 = {"vintage": 2026, "country": "France", "price": 0.0}
        wine_2 = {"vintage": 2026, "country": "Australia", "price": 500.0}
        self.assertTrue(S1.is_better_wine_than(wine_1, wine_2))
        self.assertFalse(S1.is_better_wine_than(wine_2, wine_1))

        wine_1 = {"vintage": 2026, "country": "France", "price": 0.0}
        wine_2 = {"vintage": 2026, "country": "iFrance", "price": 500.0}
        self.assertTrue(S1.is_better_wine_than(wine_1, wine_2))
        self.assertFalse(S1.is_better_wine_than(wine_2, wine_1))

        wine_1 = {"vintage": 2026, "country": "frAnz", "price": 0.0}
        wine_2 = {"vintage": 2026, "country": "Fra", "price": 500.0}
        self.assertTrue(S1.is_better_wine_than(wine_1, wine_2))
        self.assertFalse(S1.is_better_wine_than(wine_2, wine_1))

        wine_1 = {"vintage": 2026, "country": "FRANKFURT", "price": -5000.0}
        wine_2 = {"vintage": 2026, "country": "fra nce", "price": 5000.0}
        self.assertTrue(S1.is_better_wine_than(wine_1, wine_2))
        self.assertFalse(S1.is_better_wine_than(wine_2, wine_1))

        wine_1 = {"vintage": 2026, "country": "FRANKFURT", "price": -5000.0}
        wine_2 = {"vintage": 2026, "country": "fra nce", "price": 0.0}
        self.assertTrue(S1.is_better_wine_than(wine_1, wine_2))
        self.assertFalse(S1.is_better_wine_than(wine_2, wine_1))

        wine_1 = {"vintage": 2026, "country": "FRANKFURT", "price": -5000.0}
        wine_2 = {"vintage": 2026, "country": "fra nce", "price": 0.0}
        self.assertTrue(S1.is_better_wine_than(wine_1, wine_2))
        self.assertFalse(S1.is_better_wine_than(wine_2, wine_1))

        wine_1 = {"vintage": 2026, "country": "FRANKFURT", "price": -5000.0}
        wine_2 = {"vintage": 1884, "country": "fra nce", "price": 0.0}
        self.assertTrue(S1.is_better_wine_than(wine_1, wine_2))
        self.assertFalse(S1.is_better_wine_than(wine_2, wine_1))

        wine_1 = {"vintage": 2026, "country": "FRANKFURT", "price": -5000.0}
        wine_2 = {"vintage": 1884, "country": "fra nce", "price": 0.0}
        self.assertTrue(S1.is_better_wine_than(wine_1, wine_2))
        self.assertFalse(S1.is_better_wine_than(wine_2, wine_1))

        # Two expensive French wines from the same year are just as good as each other.
        self.assertFalse(S1.is_better_wine_than(new_expensive_french_wine, new_very_expensive_french_wine))
        self.assertFalse(S1.is_better_wine_than(new_very_expensive_french_wine, new_very_expensive_french_wine))

        # Tiebreak using age.
        self.assertTrue(S1.is_better_wine_than(old_very_expensive_french_wine, new_expensive_french_wine))
        self.assertTrue(S1.is_better_wine_than(old_expensive_french_wine, new_very_expensive_french_wine))
        self.assertTrue(S1.is_better_wine_than(old_expensive_french_wine, new_expensive_french_wine))
        self.assertFalse(S1.is_better_wine_than(new_expensive_french_wine, old_very_expensive_french_wine))
        self.assertFalse(S1.is_better_wine_than(new_very_expensive_french_wine, old_expensive_french_wine))
        self.assertFalse(S1.is_better_wine_than(new_expensive_french_wine, old_expensive_french_wine))

        self.assertTrue(S1.is_better_wine_than(old_cheap_wine, new_cheap_wine))
        self.assertTrue(S1.is_better_wine_than(old_expensive_wine, new_expensive_wine))

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "1.5. test_is_better_wine_than (examples)", "marks" : 2.5})
        marks += 2.5

    def test_best_wine(self):
        # examples end here
        # OPTIONAL: add your own examples!

        new_very_expensive_french_wine = {"vintage": 2026, "country": "France", "price": 9999.9}
        new_expensive_french_wine = {"vintage": 2026, "country": "fraNcland", "price": 500.0}
        new_cheap_french_wine = {"vintage": 2026, "country": "frAnz", "price": 450.0}
        new_expensive_wine = {"vintage": 2026, "country": "Australia", "price": 1234.5}
        new_cheap_wine = {"vintage": 2026, "country": "Frappe Shop", "price": 499.9 }
        old_very_expensive_french_wine = {"vintage": 1400, "country": "France", "price": 9999.9}
        old_expensive_french_wine = {"vintage": 1400, "country": "France", "price": 500.0}
        old_cheap_french_wine = {"vintage": 1991, "country": "fRAn", "price": 450.0}
        old_expensive_wine = {"vintage": 1666, "country": "fr", "price": 1234.5}
        old_cheap_wine = {"vintage": 1398, "country": "Flance", "price": 499.9 }

        # Pick a wine that is better than the others
        self.assertEqual(
            3,
            S1.best_wine([
                new_expensive_wine,     #0
                new_cheap_wine,         #1
                old_expensive_wine,     #2
                new_cheap_french_wine,  #3
                new_expensive_wine,     #4
                old_expensive_wine,     #5
                ]))

        self.assertEqual(
            0,
            S1.best_wine([
                new_cheap_french_wine,
                new_expensive_wine,
                new_cheap_wine,
                old_expensive_wine,
                new_expensive_wine,
                old_expensive_wine,
                ]))

        self.assertEqual(
            5,
            S1.best_wine([
                new_expensive_wine,
                new_cheap_wine,
                old_expensive_wine,
                new_expensive_wine,
                old_expensive_wine,
                new_cheap_french_wine,
                ]))

        self.assertEqual(
            4,
            S1.best_wine([
                new_expensive_wine,
                new_cheap_wine,
                old_expensive_wine,
                new_expensive_wine,
                new_expensive_french_wine,
                old_expensive_wine,
                new_cheap_french_wine,
                ]))

        self.assertEqual(
            4,
            S1.best_wine([
                new_expensive_wine,
                new_cheap_wine,
                old_expensive_wine,
                new_expensive_wine,
                new_expensive_french_wine,
                old_expensive_wine,
                old_expensive_wine,
                new_cheap_french_wine,
                old_cheap_french_wine,
                ]))

        self.assertEqual(
            5,
            S1.best_wine([
                new_expensive_wine,
                new_cheap_wine,
                old_expensive_wine,
                new_expensive_wine,
                old_expensive_wine,
                new_cheap_french_wine,
                ]))

        self.assertIsNone(S1.best_wine([]))

        # the chosen wine must be better than all the wines before it
        better_than_itself = S1.is_better_wine_than(old_expensive_wine, old_expensive_wine)
        self.assertEqual(
            0,
            S1.best_wine([
                old_expensive_wine,
                old_expensive_wine,
                old_expensive_wine,
                old_expensive_wine,
                old_expensive_wine,
                old_expensive_wine,
                ]),
            f"is_better_wine_than(old_expensive_wine,old_expensive_wine={better_than_itself})")

        self.assertEqual(
            5,
            S1.best_wine([
                new_very_expensive_french_wine,
                new_expensive_french_wine,
                new_cheap_french_wine,
                new_expensive_wine,
                new_cheap_wine,
                old_very_expensive_french_wine,
                old_expensive_french_wine,
                old_cheap_french_wine,
                old_expensive_wine,
                old_cheap_wine])
            )

        self.assertEqual(
            2,
            S1.best_wine([
                new_cheap_wine,
                new_expensive_french_wine,
                old_very_expensive_french_wine,
                new_cheap_french_wine,
                old_expensive_wine,
                old_expensive_french_wine,
                new_very_expensive_french_wine,
                old_cheap_wine,
                old_cheap_french_wine,
                new_expensive_wine,
                ])
            )

        self.assertEqual(
            5,
            S1.best_wine([
                new_expensive_wine,
                new_cheap_french_wine,
                old_expensive_wine,
                old_cheap_wine,
                new_expensive_french_wine,
                old_expensive_french_wine,
                new_very_expensive_french_wine,
                new_cheap_wine,
                old_cheap_french_wine,
                old_very_expensive_french_wine,
                ])
            )

        self.assertEqual(
            1,
            S1.best_wine([
                new_cheap_wine,
                old_cheap_wine,
                new_cheap_wine,
                old_cheap_wine,
                new_cheap_wine,
                new_cheap_wine,
                new_cheap_wine,
                old_cheap_wine,
                old_cheap_wine,
                ])
            )

        self.assertEqual(
            0,
            S1.best_wine([
                old_cheap_wine,
                ])
            )

        global marks, passed
        passed.append({"test" : "1.6. test_best_wine (examples)", "marks" : 2.5})
        marks += 2.5

    def test_country_game(self):
        the_countries = [
                "America",
                "algeria",
                "asia",
                "Africa"]
        # country 0 ends with 'a', country 1 starts with 'a': same
        # country 1 ends with 'a', country 2 starts with 'a': same
        # country 1 ends with 'a', country 2 starts with 'A': different
        self.assertEqual(2, S1.country_game(the_countries))

        the_countries = ["there is no next string"]
        self.assertEqual(0, S1.country_game(the_countries))

        the_countries = ["FRANCE", "Germany", "England"]
        # 'E' is not 'G'. 'y' is not 'E'.
        self.assertEqual(0, S1.country_game(the_countries))

        the_countries = ["Australia", "Australia", "Australia", "Australia", "and", "Australia"]
        self.assertEqual(1, S1.country_game(the_countries))

        the_countries = ["the next string is empty", "", "yes", "sorry"]
        self.assertEqual(1, S1.country_game(the_countries))
        the_countries = ["the next string is empty", "", "yes"]
        self.assertEqual(0, S1.country_game(the_countries))
        the_countries = ["the next string not empty", "yes"]
        self.assertEqual(1, S1.country_game(the_countries))

        the_countries = ["", "", "", "", "hello?"]
        self.assertEqual(0, S1.country_game(the_countries))

        the_countries = ["canada", "russia", "rome", "rome"]
        self.assertEqual(0, S1.country_game(the_countries))
        the_countries = ["canada", "russia", "rome", "estonia", "afghanistan"]
        self.assertEqual(2, S1.country_game(the_countries))


        the_countries = ["Denmark", "and", "denmark", "denmark", "king of england"]
        # one 'd' and one 'k'
        self.assertEqual(2, S1.country_game(the_countries))

        the_countries = ["XY", "YZ", "ZA", "XY", "AB", "BC"]
        # 'Y', 'Z', and 'B'
        self.assertEqual(3, S1.country_game(the_countries))

        the_countries = ["X", "X", "XY", "Y", "Y", "y"]
        self.assertEqual(4, S1.country_game(the_countries))
        the_countries = ["X", "X", "XY", "Y", "Y", "Y"]
        self.assertEqual(5, S1.country_game(the_countries))
        the_countries = ["X", "X", "Y", "Y", "X"]
        self.assertEqual(2, S1.country_game(the_countries))
        the_countries = ["X", "Y", "Y", "X", "X"]
        self.assertEqual(2, S1.country_game(the_countries))

        the_countries = []
        self.assertEqual(0, S1.country_game(the_countries))

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "1.7. test_country_game (examples)", "marks" : 2.5})
        marks += 2.5

    def test_board_plane(self):
        # Both inputs must be strings
        self.assertIsNone(S1.board_plane(None, "ABC"))
        self.assertIsNone(S1.board_plane("ABC", None))
        self.assertIsNone(S1.board_plane(["h", "i"], "ABC"))
        self.assertIsNone(S1.board_plane("ABC", ["h", "i"]))

        # The new queue should have the same number of first and second class passengers
        the_first = "AAAAAAAAAAAAAAA"
        the_economy = "BBBBBBBBBBBBBBB"
        result = S1.board_plane(the_first, the_economy)
        self.assertIs(type(result), str)
        self.assertEqual(len(the_first) + len(the_economy), len(result), f"result = {result}")
        number_of_As = len([c for c in result if c == "A"]) # count the "A"s
        number_of_Bs = len([c for c in result if c == "B"]) # count the "B"s
        self.assertEqual(len(the_first), number_of_As, f"result = {result}")
        self.assertEqual(len(the_economy), number_of_Bs, f"result = {result}")

        the_first = "AA"
        the_economy = "BBBBBBBBBBBBBBB"
        result = S1.board_plane(the_first, the_economy)
        self.assertIs(type(result), str)
        self.assertEqual(len(the_first) + len(the_economy), len(result), f"result = {result}")
        number_of_As = len([c for c in result if c == "A"]) # count the "A"s
        number_of_Bs = len([c for c in result if c == "B"]) # count the "B"s
        self.assertEqual(len(the_first), number_of_As, f"result = {result}")
        self.assertEqual(len(the_economy), number_of_Bs, f"result = {result}")

        the_first = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        the_economy = "BBBB"
        result = S1.board_plane(the_first, the_economy)
        self.assertIs(type(result), str)
        self.assertEqual(len(the_first) + len(the_economy), len(result), f"result = {result}")
        number_of_As = len([c for c in result if c == "A"]) # count the "A"s
        number_of_Bs = len([c for c in result if c == "B"]) # count the "B"s
        self.assertEqual(len(the_first), number_of_As, f"result = {result}")
        self.assertEqual(len(the_economy), number_of_Bs, f"result = {result}")

        the_first = "AAAAAAAAAAAAA"
        the_economy = ""
        result = S1.board_plane(the_first, the_economy)
        self.assertIs(type(result), str)
        self.assertEqual(len(the_first) + len(the_economy), len(result), f"result = {result}")
        number_of_As = len([c for c in result if c == "A"]) # count the "A"s
        number_of_Bs = len([c for c in result if c == "B"]) # count the "B"s
        self.assertEqual(len(the_first), number_of_As, f"result = {result}")
        self.assertEqual(len(the_economy), number_of_Bs, f"result = {result}")

        the_first = ""
        the_economy = "BBBBBBBBBBB"
        result = S1.board_plane(the_first, the_economy)
        self.assertIs(type(result), str)
        self.assertEqual(len(the_first) + len(the_economy), len(result), f"result = {result}")
        number_of_As = len([c for c in result if c == "A"]) # count the "A"s
        number_of_Bs = len([c for c in result if c == "B"]) # count the "B"s
        self.assertEqual(len(the_first), number_of_As, f"result = {result}")
        self.assertEqual(len(the_economy), number_of_Bs, f"result = {result}")

        # Same passenger names in the same order
        the_first = "first ClaS5"
        the_economy = "Econ0my"
        result = S1.board_plane(the_first, the_economy)
        for c in the_first:
            self.assertIn(c, result)
        for c in the_economy:
            self.assertIn(c, result)
        self.assertLess(result.index("f"), result.index("i"))
        self.assertLess(result.index("i"), result.index("r"))
        self.assertLess(result.index("r"), result.index("s"))
        self.assertLess(result.index("s"), result.index("t"))
        self.assertLess(result.index("t"), result.index(" "))
        self.assertLess(result.index(" "), result.index("C"))
        self.assertLess(result.index("C"), result.index("l"))
        self.assertLess(result.index("l"), result.index("a"))
        self.assertLess(result.index("a"), result.index("S"))
        self.assertLess(result.index("S"), result.index("5"))

        # If one queue is empty, board the other queue
        self.assertEqual("55555", S1.board_plane("55555", ""))
        self.assertEqual("55555", S1.board_plane("", "55555"))
        self.assertEqual("", S1.board_plane("", ""))
        self.assertEqual("abcABCabc", S1.board_plane("", "abcABCabc"))
        self.assertEqual("abcABCabc", S1.board_plane("abcABCabc", ""))

        # Board the first class passenger first
        self.assertEqual("AB", S1.board_plane("A", "B"))
        self.assertEqual("BA", S1.board_plane("B", "A"))
        self.assertEqual("30", S1.board_plane("3", "0"))
        self.assertEqual("03", S1.board_plane("0", "3"))

        # Board 3 first class passengers before boarding economy
        self.assertEqual("f?", S1.board_plane("f", "?"))
        self.assertEqual("fff", S1.board_plane("fff?", "?")[:3])
        self.assertEqual("fff", S1.board_plane("fffffff", "??????")[:3])
        self.assertEqual("fff", S1.board_plane("fffffff", "")[:3])
        self.assertEqual("fff", S1.board_plane("fff", "??????")[:3])
        self.assertEqual("fff", S1.board_plane("fff", "")[:3])

        # If passenger ratio is exactly 3:1, alternate 3 first and 1 economy
        self.assertEqual("AAAB" * 7, S1.board_plane("A" * 21, "B" * 7))
        self.assertEqual("AAAB" * 1, S1.board_plane("A" * 3, "B" * 1))
        self.assertEqual("AAAB" * 12, S1.board_plane("A" * 36, "B" * 12))

        # If not enough first class, board the rest of economy class
        self.assertEqual("AAABABBBB", S1.board_plane("A" * 4, "B" * 5))
        self.assertEqual("AAABAABBBB", S1.board_plane("A" * 5, "B" * 5))
        self.assertEqual("AAABAAABBBB", S1.board_plane("A" * 6, "B" * 5))
        self.assertEqual("AAABAAABAAABABB", S1.board_plane("A" * 10, "B" * 5))
        self.assertEqual("AAABAAABAAABAAABAAB", S1.board_plane("A" * 14, "B" * 5))
        self.assertEqual("AAABAAABB", S1.board_plane("A" * 6, "B" * 3))
        self.assertEqual("AAABAAABBBBBBB", S1.board_plane("A" * 6, "B" * 8))
        self.assertEqual("ABBBBBBBB", S1.board_plane("A" * 1, "B" * 8))
        self.assertEqual("AAABABBBBBBB", S1.board_plane("A" * 4, "B" * 8))

        # If not enough economy class, board the rest of first class
        self.assertEqual("AAABAAABA", S1.board_plane("A" * 7, "B" * 2))
        self.assertEqual("AAABAAABAAAA", S1.board_plane("A" * 10, "B" * 2))
        self.assertEqual("AAABAAABAAABAAABAAAAAA", S1.board_plane("A" * 18, "B" * 4))

        # The boarding works the same for different passenger names
        self.assertEqual("AAABAAABAAABABB", S1.board_plane("AAAAAAAAAA", "BBBBB"))
        self.assertEqual("ABCaDEFbGHIcJde", S1.board_plane("ABCDEFGHIJ", "abcde"))
        self.assertEqual("AAABAABBBB", S1.board_plane("AAAAA", "BBBBB"))
        self.assertEqual("helwloorld", S1.board_plane("hello", "world"))
        self.assertEqual("i ahm appy", S1.board_plane("i am ", "happy"))
        self.assertEqual("AAABAAABAAABAAAA", S1.board_plane("AAAAAAAAAAAAA", "BBB"))
        self.assertEqual("unifverusitny is", S1.board_plane("university is", "fun"))

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "1.8. test_board_plane (examples)", "marks" : 2.5})
        marks += 2.5

    # ===============================
    # Tests for Stage 2: IngredientData
    # ===============================

    def test_init_ingredientdata(self):
        # In this example, we give a bad id and name.
        ingredient_data = IngredientData("1", ["lentil"], 4)
        self.assertIs(type(ingredient_data.id), int)
        self.assertIs(type(ingredient_data.name), str)
        self.assertIs(type(ingredient_data.quantity), int)
        self.assertEqual(0, ingredient_data.id)
        self.assertEqual("", ingredient_data.name)
        self.assertEqual(4, ingredient_data.quantity)

        # In this example, we give a bad name and quantity.
        ingredient_data = IngredientData(-1, 2, "bread")
        self.assertIs(type(ingredient_data.id), int)
        self.assertIs(type(ingredient_data.name), str)
        self.assertIs(type(ingredient_data.quantity), int)
        self.assertEqual(-1, ingredient_data.id)
        self.assertEqual("", ingredient_data.name)
        self.assertEqual(0, ingredient_data.quantity)

        # In this example, we give a bad id and quantity.
        ingredient_data = IngredientData(1.000, "cabbage", 4.000)
        self.assertIs(type(ingredient_data.id), int)
        self.assertIs(type(ingredient_data.name), str)
        self.assertIs(type(ingredient_data.quantity), int)
        self.assertEqual(0, ingredient_data.id)
        self.assertEqual("cabbage", ingredient_data.name)
        self.assertEqual(0, ingredient_data.quantity)

        # In this example, we give a bad id and name.
        ingredient_data = IngredientData(1.000, ["cabbage"], 4)
        self.assertIs(type(ingredient_data.id), int)
        self.assertIs(type(ingredient_data.name), str)
        self.assertIs(type(ingredient_data.quantity), int)
        self.assertEqual(0, ingredient_data.id)
        self.assertEqual("", ingredient_data.name)
        self.assertEqual(4, ingredient_data.quantity)

        # Use a for loop to do many tests at once:

        for x in [123, 5, -66]:
            ingredient_data = IngredientData(x, "soap", 12)
            self.assertEqual(x, ingredient_data.id, f"x = {x}")
            self.assertEqual(12, ingredient_data.quantity, f"x = {x}")

        for x in [123, 5, -66]:
            ingredient_data = IngredientData(2, "soap", x)
            self.assertEqual(2, ingredient_data.id, f"x = {x}")
            self.assertEqual(x, ingredient_data.quantity, f"x = {x}")

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "2.1. test_init_ingredientdata (examples)", "marks" : 2.5})
        marks += 2.5

    def test_ingredientdata_str(self):
        ingredient_data = IngredientData(123, "tomato", 2)
        self.assertEqual("IngredientData(123,name=tomato,quantity=2)", str(ingredient_data))

        ingredient_data = IngredientData(124, "lentil", 999000)
        self.assertEqual("IngredientData(124,name=lentil,quantity=999000)", str(ingredient_data))

        # Some strange names
        ingredient_data = IngredientData(-1, ":)", -1)
        self.assertEqual("IngredientData(-1,name=:),quantity=-1)", str(ingredient_data))
        ingredient_data = IngredientData(0, "=)", -345)
        self.assertEqual("IngredientData(0,name==),quantity=-345)", str(ingredient_data))
        ingredient_data = IngredientData(1, "tasty, tasty carrots", 0)
        self.assertEqual("IngredientData(1,name=tasty, tasty carrots,quantity=0)", str(ingredient_data))
        ingredient_data = IngredientData(888, "", 2)
        self.assertEqual("IngredientData(888,name=,quantity=2)", str(ingredient_data))
        ingredient_data = IngredientData(0, ",'_',", 0)
        self.assertEqual("IngredientData(0,name=,'_',,quantity=0)", str(ingredient_data))
        ingredient_data = IngredientData(124, "chef's secret sauce", 999000)
        self.assertEqual("IngredientData(124,name=chef's secret sauce,quantity=999000)", str(ingredient_data))

        # In this example, we give a bad name and quantity.
        ingredient_data = IngredientData(-1, 2, "bread")
        self.assertEqual("IngredientData(-1,name=,quantity=0)", str(ingredient_data))

        # In this example, we give a bad id and quantity.
        ingredient_data = IngredientData(1.000, "cabbage", 4.000)
        self.assertEqual("IngredientData(0,name=cabbage,quantity=0)", str(ingredient_data))

        # In this example, we give a bad id and name.
        ingredient_data = IngredientData(1.000, ["cabbage"], 4)
        self.assertEqual("IngredientData(0,name=,quantity=4)", str(ingredient_data))

        # Use a for loop to do many tests at once:

        for x in [123, 5, -66]:
            ingredient_data = IngredientData(x, "soap", 12)
            self.assertTrue(
                    str(ingredient_data).startswith(f"IngredientData({x}"),
                    f"{str(ingredient_data)} should start with IngredientData({x}")

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "2.2. test_ingredientdata_str (examples)", "marks" : 2.5})
        marks += 2.5

    # ===============================
    # Tests for Stage 3: Inventory
    # ===============================

    def test_init_inventory(self):
        # The attribute `num_ingr` must equal the number of *different* names.
        the_names = ["cherry", "apple", "banana", "cherry"]
        number_of_different_names = 3 # apple, banana, and cherry
        inventory = Inventory(the_names)
        self.assertEqual(inventory.num_ingr, number_of_different_names)

        the_names = ["name 1", "name 2", "name 3", "", "name 5"]
        number_of_different_names = 5
        inventory = Inventory(the_names)
        self.assertEqual(inventory.num_ingr, number_of_different_names)

        the_names = ["123", "321", ""]
        number_of_different_names = 3 # 123, 321, and [blank]
        inventory = Inventory(the_names)
        self.assertEqual(inventory.num_ingr, number_of_different_names)

        the_names = ["", "", "123", "321", "123", "321", "", "123"]
        number_of_different_names = 3 # apple, banana, and cherry
        inventory = Inventory(the_names)
        self.assertEqual(inventory.num_ingr, number_of_different_names)

        inventory = Inventory(["sun-dried single origin Fancy bananas"])
        self.assertEqual(inventory.num_ingr, 1)

        the_names = ["apple", "apple", "apple", "apple", "apple"]
        number_of_different_names = 1 # apple
        inventory = Inventory(the_names)
        self.assertEqual(inventory.num_ingr, number_of_different_names)

        inventory = Inventory(["apple", "apple", "apple", "SURPRISE!", "apple", "apple"])
        self.assertEqual(inventory.num_ingr, 2)

        inventory = Inventory(["SURPRISE!", "apple", "apple", "apple", "apple", "apple"])
        self.assertEqual(inventory.num_ingr, 2)

        inventory = Inventory(["apple", "apple", "apple", "apple", "apple", "SURPRISE!"])
        self.assertEqual(inventory.num_ingr, 2)

        inventory = Inventory([])
        self.assertEqual(inventory.num_ingr, 0)

        inventory = Inventory([""])
        self.assertEqual(inventory.num_ingr, 1)

        inventory = Inventory(["!", "#"])
        self.assertEqual(inventory.num_ingr, 2)

        # different strings are different names
        inventory = Inventory(["banana", "Banana"])
        self.assertEqual(inventory.num_ingr, 2)

        inventory = Inventory(["banana!", "banana?"])
        self.assertEqual(inventory.num_ingr, 2)

        inventory = Inventory(["banAna?", "banAna?"])
        self.assertEqual(inventory.num_ingr, 1)

        the_names = []
        number_of_different_names = 0 # apple
        inventory = Inventory(the_names)
        self.assertEqual(inventory.num_ingr, number_of_different_names)

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "3.1. test_init_inventory (examples)", "marks" : 2.5})
        marks += 2.5

    def test_inventory_get_ingredient_by_id(self):
        # If ingredient_id is not an int, returns `None`.
        inventory = Inventory(["cherry", "apple", "banana", "cherry"])
        self.assertIsNone(inventory.get_ingredient_by_id("apple"))
        self.assertIsNone(inventory.get_ingredient_by_id("banana"))
        self.assertIsNone(inventory.get_ingredient_by_id(True))
        self.assertIsNone(inventory.get_ingredient_by_id(False))
        self.assertIsNone(inventory.get_ingredient_by_id(None))
        self.assertIsNone(inventory.get_ingredient_by_id(0.0))
        self.assertIsNone(inventory.get_ingredient_by_id(1.0))
        self.assertIsNone(inventory.get_ingredient_by_id(-1.0))
        self.assertIsNone(inventory.get_ingredient_by_id([]))
        self.assertIsNone(inventory.get_ingredient_by_id([0]))

        inventory = Inventory([])
        self.assertIsNone(inventory.get_ingredient_by_id("apple"))
        self.assertIsNone(inventory.get_ingredient_by_id("banana"))
        self.assertIsNone(inventory.get_ingredient_by_id(True))
        self.assertIsNone(inventory.get_ingredient_by_id(False))
        self.assertIsNone(inventory.get_ingredient_by_id(None))
        self.assertIsNone(inventory.get_ingredient_by_id(0.0))
        self.assertIsNone(inventory.get_ingredient_by_id(1.0))
        self.assertIsNone(inventory.get_ingredient_by_id(-1.0))
        self.assertIsNone(inventory.get_ingredient_by_id([]))
        self.assertIsNone(inventory.get_ingredient_by_id([0]))

        # Rule 2: Every ingredient has an id between 0 and inventory.num_ingr-1.
        # If there isn't an ingredient with the requested id, returns None.
        inventory = Inventory(["cherry", "apple", "banana", "cherry"])
        for i in range(0, 10):
            # ingredient ID that is too big
            the_id = 3 + i
            self.assertIsNone(inventory.get_ingredient_by_id(the_id), f"Test case: the_id = {the_id}")
            # ingredient ID that is too small
            the_id = -1 - i
            self.assertIsNone(inventory.get_ingredient_by_id(the_id), f"Test case: the_id = {the_id}")

        inventory = Inventory(["pie", "", "meat"])
        for i in range(0, 10):
            # ingredient ID that is too big
            the_id = 3 + i
            self.assertIsNone(inventory.get_ingredient_by_id(the_id), f"Test case: the_id = {the_id}")
            # ingredient ID that is too small
            the_id = -1 - i
            self.assertIsNone(inventory.get_ingredient_by_id(the_id), f"Test case: the_id = {the_id}")

        # Rule 2: Every ingredient has an id between 0 and inventory.num_ingr-1.
        # Rule 1+3: There are inventory.num_ingr ingredients with different ids.
        inventory = Inventory(["cherry", "apple", "banana", "cherry"])
        for the_id in range(0, inventory.num_ingr):
            result = inventory.get_ingredient_by_id(the_id)
            # there is an ingredient with this id
            self.assertIsNotNone(result, f"Test case: the_id = {the_id}")
            # it is an IngredientData
            self.assertIsInstance(result, IngredientData)
            self.assertIs(type(result), IngredientData)
            # the returned ingredient's id must be ingredient_id
            self.assertEqual(the_id, result.id, f"the_id = {the_id}, result = {result}")
            # quantity should be 0
            self.assertEqual(0, result.quantity, f"the_id = {the_id}, result = {result}")
            # The name should be from the original list
            self.assertIn(result.name, ["cherry", "apple", "banana", "cherry"], f"Test case: the_id = {the_id}")

        # Every ingredient has a different name and different ID
        inventory = Inventory(["cherry", "apple", "banana", "cherry"])
        self.assertEqual(3, inventory.num_ingr)
        for i in range(3):
            for j in range(3):
                if i != j:
                    self.assertNotEqual(inventory.get_ingredient_by_id(i).name, inventory.get_ingredient_by_id(j).name)

        inventory = Inventory([])
        self.assertEqual(inventory.num_ingr, 0)
        self.assertIsNone(inventory.get_ingredient_by_id(0))
        self.assertIsNone(inventory.get_ingredient_by_id(1))

        inventory = Inventory([""])
        self.assertEqual(inventory.num_ingr, 1)
        self.assertIsNotNone(inventory.get_ingredient_by_id(0))
        self.assertIsNone(inventory.get_ingredient_by_id(1))
        self.assertEqual(0, inventory.get_ingredient_by_id(0).id)
        self.assertEqual("", inventory.get_ingredient_by_id(0).name)
        self.assertEqual(0, inventory.get_ingredient_by_id(0).quantity)

        inventory = Inventory(["cucumber", "CUCUMBER", "apple", "cucumber", "banana", "cucumber", "pear", "CUCUMBER"])
        self.assertEqual(inventory.num_ingr, 5)
        self.assertIsNone(inventory.get_ingredient_by_id(6))
        self.assertEqual(0, inventory.get_ingredient_by_id(0).id)
        self.assertEqual(1, inventory.get_ingredient_by_id(1).id)
        self.assertEqual(2, inventory.get_ingredient_by_id(2).id)
        self.assertEqual(3, inventory.get_ingredient_by_id(3).id)
        self.assertEqual(4, inventory.get_ingredient_by_id(4).id)
        self.assertEqual("cucumber", inventory.get_ingredient_by_id(0).name)
        self.assertEqual("CUCUMBER", inventory.get_ingredient_by_id(1).name)
        self.assertEqual("apple", inventory.get_ingredient_by_id(2).name)
        self.assertEqual("banana", inventory.get_ingredient_by_id(3).name)
        self.assertEqual("pear", inventory.get_ingredient_by_id(4).name)
        self.assertEqual(0, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(2).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(3).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(4).quantity)

        inventory = Inventory([""])
        self.assertEqual(inventory.num_ingr, 1)
        self.assertEqual("", inventory.get_ingredient_by_id(0).name)

        inventory = Inventory(["!", "#"])
        self.assertEqual(inventory.num_ingr, 2)
        self.assertEqual("!", inventory.get_ingredient_by_id(0).name)
        self.assertEqual("#", inventory.get_ingredient_by_id(1).name)

        # different strings are different names
        inventory = Inventory(["banana", "Banana"])
        self.assertEqual(inventory.num_ingr, 2)
        self.assertEqual("banana", inventory.get_ingredient_by_id(0).name)
        self.assertEqual("Banana", inventory.get_ingredient_by_id(1).name)

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "3.2. test_inventory_get_ingredient_by_id (examples)", "marks" : 2.5})
        marks += 2.5

    def test_inventory_get_ingredient_by_name(self):
        # If ingredient_id is not a string, returns `None`.
        inventory = Inventory(["cherry", "apple", "banana", "cherry"])
        self.assertIsNone(inventory.get_ingredient_by_name(0))
        self.assertIsNone(inventory.get_ingredient_by_name(1))
        self.assertIsNone(inventory.get_ingredient_by_name(True))
        self.assertIsNone(inventory.get_ingredient_by_name(False))
        self.assertIsNone(inventory.get_ingredient_by_name(None))
        self.assertIsNone(inventory.get_ingredient_by_name(0.0))
        self.assertIsNone(inventory.get_ingredient_by_name(1.0))
        self.assertIsNone(inventory.get_ingredient_by_name(-1.0))
        self.assertIsNone(inventory.get_ingredient_by_name([]))
        self.assertIsNone(inventory.get_ingredient_by_name([0]))

        inventory = Inventory([])
        self.assertIsNone(inventory.get_ingredient_by_name(0))
        self.assertIsNone(inventory.get_ingredient_by_name(1))
        self.assertIsNone(inventory.get_ingredient_by_name(True))
        self.assertIsNone(inventory.get_ingredient_by_name(False))
        self.assertIsNone(inventory.get_ingredient_by_name(None))
        self.assertIsNone(inventory.get_ingredient_by_name(0.0))
        self.assertIsNone(inventory.get_ingredient_by_name(1.0))
        self.assertIsNone(inventory.get_ingredient_by_name(-1.0))
        self.assertIsNone(inventory.get_ingredient_by_name([]))
        self.assertIsNone(inventory.get_ingredient_by_name([0]))

        # If the input `ingredient_names` contains the string "apple",
        # there must be an ingredient with name "apple".
        inventory = Inventory(["cherry", "apple", "banana", "cherry"])
        self.assertIsNotNone(inventory.get_ingredient_by_name("apple"))
        # the returned ingredient should have the name "apple"
        self.assertEqual(inventory.get_ingredient_by_name("apple").name, "apple")
        # Rule 2: ID is between range(0, num_ingr)
        self.assertLess(inventory.get_ingredient_by_name("apple").id, 3)
        self.assertGreaterEqual(inventory.get_ingredient_by_name("apple").id, 0)
        # Initial quantity should be 0
        self.assertEqual(0, inventory.get_ingredient_by_name("apple").quantity)

        for the_name in ["cherry", "apple", "banana", "cherry"]:
            self.assertIsNotNone(inventory.get_ingredient_by_name(the_name), f"Test case: the_name = {the_name}")
            self.assertLess(inventory.get_ingredient_by_name(the_name).id, 3, f"Test case: the_name = {the_name}")
            self.assertGreaterEqual(inventory.get_ingredient_by_name(the_name).id, 0, f"Test case: the_name = {the_name}")
            self.assertEqual(inventory.get_ingredient_by_name(the_name).name, the_name, f"Test case: the_name = {the_name}")
            self.assertEqual(0, inventory.get_ingredient_by_name(the_name).quantity, f"Test case: the_name = {the_name}")

        the_names = ["cucumber", "CUCUMBER", "apple", "cucumber", "banana", "cucumber", "pear", "CUCUMBER"]
        inventory = Inventory(the_names)
        for the_name in the_names:
            self.assertIsNotNone(inventory.get_ingredient_by_name(the_name), f"Test case: the_name = {the_name}")
            self.assertLess(inventory.get_ingredient_by_name(the_name).id, 5, f"Test case: the_name = {the_name}")
            self.assertGreaterEqual(inventory.get_ingredient_by_name(the_name).id, 0, f"Test case: the_name = {the_name}")
            self.assertEqual(inventory.get_ingredient_by_name(the_name).name, the_name, f"Test case: the_name = {the_name}")
            self.assertEqual(0, inventory.get_ingredient_by_name(the_name).quantity, f"Test case: the_name = {the_name}")

        the_names = [""]
        inventory = Inventory(the_names)
        for the_name in the_names:
            self.assertIsNotNone(inventory.get_ingredient_by_name(the_name), f"Test case: the_name = {the_name}")
            self.assertLess(inventory.get_ingredient_by_name(the_name).id, 1, f"Test case: the_name = {the_name}")
            self.assertGreaterEqual(inventory.get_ingredient_by_name(the_name).id, 0, f"Test case: the_name = {the_name}")
            self.assertEqual(inventory.get_ingredient_by_name(the_name).name, the_name, f"Test case: the_name = {the_name}")
            self.assertEqual(0, inventory.get_ingredient_by_name(the_name).quantity, f"Test case: the_name = {the_name}")

        the_names = ["!", "#"]
        inventory = Inventory(the_names)
        for the_name in the_names:
            self.assertIsNotNone(inventory.get_ingredient_by_name(the_name), f"Test case: the_name = {the_name}")
            self.assertLess(inventory.get_ingredient_by_name(the_name).id, 2, f"Test case: the_name = {the_name}")
            self.assertGreaterEqual(inventory.get_ingredient_by_name(the_name).id, 0, f"Test case: the_name = {the_name}")
            self.assertEqual(inventory.get_ingredient_by_name(the_name).name, the_name, f"Test case: the_name = {the_name}")
            self.assertEqual(0, inventory.get_ingredient_by_name(the_name).quantity, f"Test case: the_name = {the_name}")

        the_names = ["banana", "Banana"]
        inventory = Inventory(the_names)
        for the_name in the_names:
            self.assertIsNotNone(inventory.get_ingredient_by_name(the_name), f"Test case: the_name = {the_name}")
            self.assertLess(inventory.get_ingredient_by_name(the_name).id, 2, f"Test case: the_name = {the_name}")
            self.assertGreaterEqual(inventory.get_ingredient_by_name(the_name).id, 0, f"Test case: the_name = {the_name}")
            self.assertEqual(inventory.get_ingredient_by_name(the_name).name, the_name, f"Test case: the_name = {the_name}")
            self.assertEqual(0, inventory.get_ingredient_by_name(the_name).quantity, f"Test case: the_name = {the_name}")

        # Return None if an ingredient name isn't in the database
        inventory = Inventory(["cherry", "apple", "banana", "cherry"])
        self.assertIsNone(inventory.get_ingredient_by_name(""))
        self.assertIsNone(inventory.get_ingredient_by_name("#"))
        self.assertIsNone(inventory.get_ingredient_by_name("!"))
        self.assertIsNone(inventory.get_ingredient_by_name("Banana"))
        self.assertIsNone(inventory.get_ingredient_by_name("appl"))
        self.assertIsNone(inventory.get_ingredient_by_name("apples"))
        self.assertIsNone(inventory.get_ingredient_by_name("cherr"))
        self.assertIsNone(inventory.get_ingredient_by_name("cherry "))

        # Every ingredient has a different name and different ID
        the_names = ["cherry", "apple", "banana", "cherry"]
        inventory = Inventory(the_names)
        for first_name in the_names:
            for second_name in the_names:
                if first_name != second_name:
                    self.assertNotEqual(
                            inventory.get_ingredient_by_name(first_name).id,
                            inventory.get_ingredient_by_name(second_name).id)

        the_names = ["cucumber", "CUCUMBER", "apple", "cucumber", "banana", "cucumber", "pear", "CUCUMBER"]
        inventory = Inventory(the_names)
        for first_name in the_names:
            for second_name in the_names:
                if first_name != second_name:
                    self.assertNotEqual(
                            inventory.get_ingredient_by_name(first_name).id,
                            inventory.get_ingredient_by_name(second_name).id)

        the_names = [""]
        inventory = Inventory(the_names)
        for first_name in the_names:
            for second_name in the_names:
                if first_name != second_name:
                    self.assertNotEqual(
                            inventory.get_ingredient_by_name(first_name).id,
                            inventory.get_ingredient_by_name(second_name).id)

        the_names = ["!", "#"]
        inventory = Inventory(the_names)
        for first_name in the_names:
            for second_name in the_names:
                if first_name != second_name:
                    self.assertNotEqual(
                            inventory.get_ingredient_by_name(first_name).id,
                            inventory.get_ingredient_by_name(second_name).id)

        the_names = ["banana", "Banana"]
        inventory = Inventory(the_names)
        for first_name in the_names:
            for second_name in the_names:
                if first_name != second_name:
                    self.assertNotEqual(
                            inventory.get_ingredient_by_name(first_name).id,
                            inventory.get_ingredient_by_name(second_name).id)

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "3.3. test_inventory_get_ingredient_by_name (examples)", "marks" : 2.5})
        marks += 2.5

    def test_inventory_add_amount_of_ingredient(self):
        inventory = Inventory(["cherry", "apple", "banana", "cherry"])
        self.assertEqual("cherry", inventory.get_ingredient_by_id(0).name)
        self.assertEqual("apple", inventory.get_ingredient_by_id(1).name)
        self.assertEqual("banana", inventory.get_ingredient_by_id(2).name)
        self.assertEqual(0, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(2).quantity)

        # There are 0 apples beforehand.
        # After we add 7 apples...
        result = inventory.add_amount_of_ingredient(1, 7)
        self.assertIsInstance(result, IngredientData)
        # there should be 0 + 7 apples.
        self.assertEqual(1, result.id)
        self.assertEqual("apple", result.name)
        self.assertEqual(0 + 7, result.quantity)

        self.assertEqual(0, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(7, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(2).quantity)
        # There are 7 apples and 0 cherries beforehand.
        # After we add 10 cherries...
        result = inventory.add_amount_of_ingredient(0, 10)
        # there should be 0 + 10 cherries.
        self.assertEqual(0, result.id)
        self.assertEqual("cherry", result.name)
        self.assertEqual(0 + 10, result.quantity)

        self.assertEqual(10, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(7, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(2).quantity)
        # and add -1 apples...
        result = inventory.add_amount_of_ingredient(1, -1)
        # there should be 7 + (-1) apples.
        self.assertEqual(1, result.id)
        self.assertEqual("apple", result.name)
        self.assertEqual(7 - 1, result.quantity)

        self.assertEqual(10, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(6, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(2).quantity)

        # If ingredient id is not an int, returns None and does nothing
        result = inventory.add_amount_of_ingredient("cherry", 3)
        self.assertIsNone(result)

        self.assertEqual("cherry", inventory.get_ingredient_by_id(0).name)
        self.assertEqual("apple", inventory.get_ingredient_by_id(1).name)
        self.assertEqual("banana", inventory.get_ingredient_by_id(2).name)
        self.assertEqual(10, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(6, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(2).quantity)

        result = inventory.add_amount_of_ingredient(1.0, 3)
        self.assertIsNone(result)

        result = inventory.add_amount_of_ingredient("", 2)
        self.assertIsNone(result)

        self.assertEqual("cherry", inventory.get_ingredient_by_id(0).name)
        self.assertEqual("apple", inventory.get_ingredient_by_id(1).name)
        self.assertEqual("banana", inventory.get_ingredient_by_id(2).name)
        self.assertEqual(10, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(6, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(2).quantity)

        # If amount to add is not an int, returns None and does nothing
        result = inventory.add_amount_of_ingredient(1, 3.0)
        self.assertIsNone(result)
        result = inventory.add_amount_of_ingredient(1, "three apples")
        self.assertIsNone(result)
        result = inventory.add_amount_of_ingredient(1, "")
        self.assertIsNone(result)
        result = inventory.add_amount_of_ingredient("", "")
        self.assertIsNone(result)

        self.assertEqual(10, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(6, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(2).quantity)
        result = inventory.add_amount_of_ingredient(2, -99)
        self.assertEqual(2, result.id)
        self.assertEqual("banana", result.name)
        self.assertEqual(-99, result.quantity)

        self.assertEqual(10, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(6, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(-99, inventory.get_ingredient_by_id(2).quantity)

        self.assertEqual(10, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(6, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(-99, inventory.get_ingredient_by_id(2).quantity)
        result = inventory.add_amount_of_ingredient(2, 200)
        self.assertEqual(2, result.id)
        self.assertEqual("banana", result.name)
        self.assertEqual(101, result.quantity)

        self.assertEqual(10, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(6, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(101, inventory.get_ingredient_by_id(2).quantity)

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "3.4. test_inventory_add_amount_of_ingredient (examples)", "marks" : 2.5})
        marks += 2.5

    def test_inventory_new_ingredient(self):
        inventory = Inventory(["cherry", "apple", "banana", "cherry"])
        result = inventory.add_amount_of_ingredient(2, 17)
        result = inventory.add_amount_of_ingredient(1, -1)
        result = inventory.add_amount_of_ingredient(0, 3)

        self.assertEqual(3, inventory.num_ingr)
        self.assertEqual("cherry", inventory.get_ingredient_by_id(0).name)
        self.assertEqual("apple", inventory.get_ingredient_by_id(1).name)
        self.assertEqual("banana", inventory.get_ingredient_by_id(2).name)
        self.assertEqual(3, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(-1, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(17, inventory.get_ingredient_by_id(2).quantity)

        # if the input is not a string, return None and do nothing
        result = inventory.new_ingredient(True)
        self.assertIsNone(result)
        self.assertEqual(3, inventory.num_ingr)

        result = inventory.new_ingredient(False)
        self.assertIsNone(result)
        self.assertEqual(3, inventory.num_ingr)

        result = inventory.new_ingredient(0)
        self.assertIsNone(result)
        result = inventory.new_ingredient(1)
        self.assertIsNone(result)
        result = inventory.new_ingredient(1)
        self.assertIsNone(result)
        result = inventory.new_ingredient(True)
        self.assertIsNone(result)
        result = inventory.new_ingredient(False)
        self.assertIsNone(result)
        result = inventory.new_ingredient(None)
        self.assertIsNone(result)
        result = inventory.new_ingredient(0.0)
        self.assertIsNone(result)
        result = inventory.new_ingredient(1.0)
        self.assertIsNone(result)
        result = inventory.new_ingredient(-1.0)
        self.assertIsNone(result)
        result = inventory.new_ingredient([])
        self.assertIsNone(result)
        result = inventory.new_ingredient([0])
        self.assertIsNone(result)
        result = inventory.new_ingredient(0)
        self.assertIsNone(result)

        self.assertEqual(3, inventory.num_ingr)
        self.assertEqual("cherry", inventory.get_ingredient_by_id(0).name)
        self.assertEqual("apple", inventory.get_ingredient_by_id(1).name)
        self.assertEqual("banana", inventory.get_ingredient_by_id(2).name)
        self.assertEqual(3, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(-1, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(17, inventory.get_ingredient_by_id(2).quantity)

        old_num_ingr = inventory.num_ingr
        result = inventory.new_ingredient("durian")
        # returns an IngredientData
        self.assertIsInstance(result, IngredientData)
        # The returned ingredient's name should be equal to the input
        self.assertEqual("durian", result.name)
        # matches up with get_ingredient_by_id
        ingredient_from_database = inventory.get_ingredient_by_id(result.id)
        self.assertEqual(result.id, ingredient_from_database.id)
        self.assertEqual(result.name, ingredient_from_database.name)
        self.assertEqual(result.quantity, ingredient_from_database.quantity)
        # Rule 2: the returned ingredient's ID should be in range
        self.assertLess(result.id, inventory.num_ingr)
        self.assertGreaterEqual(result.id, 0)

        # no ingredients lost
        self.assertGreaterEqual(inventory.num_ingr, old_num_ingr)
        # Is num_ingr still correct?
        self.assertIsNotNone(inventory.get_ingredient_by_id(inventory.num_ingr - 1))
        # no surprising new ingredients
        for i in range(inventory.num_ingr):
            self.assertIn(inventory.get_ingredient_by_id(i).name,
                          ["apple", "banana", "cherry", "durian"])
        self.assertLessEqual(inventory.num_ingr, old_num_ingr+1)

        old_num_ingr = inventory.num_ingr
        result = inventory.new_ingredient("banana")
        # returns an IngredientData
        self.assertIsInstance(result, IngredientData)
        # The returned ingredient's name should be equal to the input
        self.assertEqual("banana", result.name)
        # matches up with get_ingredient_by_id
        ingredient_from_database = inventory.get_ingredient_by_id(result.id)
        self.assertEqual(result.id, ingredient_from_database.id)
        self.assertEqual(result.name, ingredient_from_database.name)
        self.assertEqual(result.quantity, ingredient_from_database.quantity)
        # Rule 2: the returned ingredient's ID should be in range
        self.assertLess(result.id, inventory.num_ingr)
        self.assertGreaterEqual(result.id, 0)

        # no ingredients lost
        self.assertGreaterEqual(inventory.num_ingr, old_num_ingr)
        # Is num_ingr still correct?
        self.assertIsNotNone(inventory.get_ingredient_by_id(inventory.num_ingr - 1))
        # no surprising new ingredients
        for i in range(inventory.num_ingr):
            self.assertIn(inventory.get_ingredient_by_id(i).name,
                          ["apple", "banana", "cherry", "durian"])
        self.assertLessEqual(inventory.num_ingr, old_num_ingr+1)

        old_num_ingr = inventory.num_ingr
        result = inventory.new_ingredient("cherry")
        # returns an IngredientData
        self.assertIsInstance(result, IngredientData)
        # The returned ingredient's name should be equal to the input
        self.assertEqual("cherry", result.name)
        # matches up with get_ingredient_by_id
        ingredient_from_database = inventory.get_ingredient_by_id(result.id)
        self.assertEqual(result.id, ingredient_from_database.id)
        self.assertEqual(result.name, ingredient_from_database.name)
        self.assertEqual(result.quantity, ingredient_from_database.quantity)
        # Rule 2: the returned ingredient's ID should be in range
        self.assertLess(result.id, inventory.num_ingr)
        self.assertGreaterEqual(result.id, 0)

        # no ingredients lost
        self.assertGreaterEqual(inventory.num_ingr, old_num_ingr)
        # Is num_ingr still correct?
        self.assertIsNotNone(inventory.get_ingredient_by_id(inventory.num_ingr - 1))
        # no surprising new ingredients
        for i in range(inventory.num_ingr):
            self.assertIn(inventory.get_ingredient_by_id(i).name,
                          ["apple", "banana", "cherry", "durian"])
        self.assertLessEqual(inventory.num_ingr, old_num_ingr+1)

        old_num_ingr = inventory.num_ingr
        result = inventory.new_ingredient("eggplant")
        # returns an IngredientData
        self.assertIsInstance(result, IngredientData)
        # The returned ingredient's name should be equal to the input
        self.assertEqual("eggplant", result.name)
        # matches up with get_ingredient_by_id
        ingredient_from_database = inventory.get_ingredient_by_id(result.id)
        self.assertEqual(result.id, ingredient_from_database.id)
        self.assertEqual(result.name, ingredient_from_database.name)
        self.assertEqual(result.quantity, ingredient_from_database.quantity)
        # Rule 2: the returned ingredient's ID should be in range
        self.assertLess(result.id, inventory.num_ingr)
        self.assertGreaterEqual(result.id, 0)

        # no ingredients lost
        self.assertGreaterEqual(inventory.num_ingr, old_num_ingr)
        # Is num_ingr still correct?
        self.assertIsNotNone(inventory.get_ingredient_by_id(inventory.num_ingr - 1))
        # no surprising new ingredients
        for i in range(inventory.num_ingr):
            self.assertIn(inventory.get_ingredient_by_id(i).name,
                          ["apple", "banana", "cherry", "durian", "eggplant"])
        self.assertLessEqual(inventory.num_ingr, old_num_ingr+1)

        self.assertEqual(5, inventory.num_ingr)
        self.assertEqual("cherry", inventory.get_ingredient_by_id(0).name)
        self.assertEqual("apple", inventory.get_ingredient_by_id(1).name)
        self.assertEqual("banana", inventory.get_ingredient_by_id(2).name)
        self.assertEqual("durian", inventory.get_ingredient_by_id(3).name)
        self.assertEqual("eggplant", inventory.get_ingredient_by_id(4).name)
        self.assertEqual(3, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(-1, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(17, inventory.get_ingredient_by_id(2).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(3).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(4).quantity)

        result = inventory.add_amount_of_ingredient(4, 2)
        result = inventory.add_amount_of_ingredient(2, 2)

        # adding imaginary ingredients still doesn't work
        self.assertIsNone(inventory.add_amount_of_ingredient(5,10))
        self.assertIsNone(inventory.add_amount_of_ingredient(-1,10))

        self.assertEqual(3, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(-1, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(19, inventory.get_ingredient_by_id(2).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(3).quantity)
        self.assertEqual(2, inventory.get_ingredient_by_id(4).quantity)

        old_num_ingr = inventory.num_ingr
        result = inventory.new_ingredient("fig")
        # returns an IngredientData
        self.assertIsInstance(result, IngredientData)
        # The returned ingredient's name should be equal to the input
        self.assertEqual("fig", result.name)
        # matches up with get_ingredient_by_id
        ingredient_from_database = inventory.get_ingredient_by_id(result.id)
        self.assertEqual(result.id, ingredient_from_database.id)
        self.assertEqual(result.name, ingredient_from_database.name)
        self.assertEqual(result.quantity, ingredient_from_database.quantity)
        # Rule 2: the returned ingredient's ID should be in range
        self.assertLess(result.id, inventory.num_ingr)
        self.assertGreaterEqual(result.id, 0)

        self.assertIsNotNone(inventory.add_amount_of_ingredient(5,-1))

        self.assertEqual(6, inventory.num_ingr)
        self.assertEqual("cherry", inventory.get_ingredient_by_id(0).name)
        self.assertEqual("apple", inventory.get_ingredient_by_id(1).name)
        self.assertEqual("banana", inventory.get_ingredient_by_id(2).name)
        self.assertEqual("durian", inventory.get_ingredient_by_id(3).name)
        self.assertEqual("eggplant", inventory.get_ingredient_by_id(4).name)
        self.assertEqual("fig", inventory.get_ingredient_by_id(5).name)
        self.assertEqual(3, inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(-1, inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(19, inventory.get_ingredient_by_id(2).quantity)
        self.assertEqual(0, inventory.get_ingredient_by_id(3).quantity)
        self.assertEqual(2, inventory.get_ingredient_by_id(4).quantity)
        self.assertEqual(-1, inventory.get_ingredient_by_id(5).quantity)

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "3.5. test_inventory_new_ingredient (examples)", "marks" : 2.5})
        marks += 2.5

    # ===============================
    # Tests for Stage 4: Kitchen
    # ===============================

    def test_init_kitchen(self):

        the_names = ["cherry", "apple", "banana", "cherry"]
        kitchen = Kitchen(the_names, [])
        self.assertEqual(kitchen.inventory.num_ingr, 3)
        self.assertListEqual([], kitchen.recipes)

        two_apples_and_one_cherry = [1, 1, 0]
        apple_cherry_apple = [1, 0, 1]
        single_banana = [2]
        one_of_each = [0, 1, 2]

        the_names = ["cherry", "apple", "banana", "cherry"]
        kitchen = Kitchen(the_names, [two_apples_and_one_cherry])
        self.assertListEqual([two_apples_and_one_cherry], kitchen.recipes)

        kitchen = Kitchen(the_names, [two_apples_and_one_cherry, two_apples_and_one_cherry,
                                      apple_cherry_apple])
        self.assertListEqual([two_apples_and_one_cherry, two_apples_and_one_cherry,
                              apple_cherry_apple], kitchen.recipes)

        the_names = ["name 1", "name 2", "name 3", "", "name 5"]
        kitchen = Kitchen(the_names, [[1, 2, 0], [1, 2, 3]])
        self.assertEqual(kitchen.inventory.num_ingr, 5)
        self.assertListEqual([[1, 2, 0], [1, 2, 3]], kitchen.recipes)

        the_names = ["123", "321", ""]
        kitchen = Kitchen(the_names, [[-1, 0, 2, 18], [1, 2, 3]])
        self.assertEqual(kitchen.inventory.num_ingr, 3)
        self.assertListEqual([[-1, 0, 2, 18], [1, 2, 3]], kitchen.recipes)

        kitchen = Kitchen(["sun-dried single origin Fancy bananas"], [[0], [0], [0]])
        self.assertEqual(kitchen.inventory.num_ingr, 1)
        self.assertListEqual([[0], [0], [0]], kitchen.recipes)

        empty_recipe = []

        kitchen = Kitchen(["sun-dried single origin Fancy bananas"], [empty_recipe])
        self.assertListEqual([empty_recipe], kitchen.recipes)

        kitchen = Kitchen([], [empty_recipe])
        self.assertListEqual([empty_recipe], kitchen.recipes)

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "4.1. test_init_kitchen (examples)", "marks" : 2.5})
        marks += 2.5

    def test_kitchen_is_recipe_ready(self):
        the_names = ["apple", "custard", "egg"]
        recipe0 = [0, 0, 0, 0, 0, 1, 1, 1, 2]
        recipe1 = [2, 1, 1, 0, 0, 2, 1]
        recipe2 = [1, 1, 0, 1, 1]
        empty_recipe = []
        impossible_recipe = [3]
        kitchen = Kitchen(the_names, [recipe0, recipe1, recipe2, empty_recipe, impossible_recipe])

        self.assertEqual(5,len(kitchen.recipes))
        # valid recipes
        self.assertIsNotNone(kitchen.is_recipe_ready(0))
        self.assertIsNotNone(kitchen.is_recipe_ready(1))
        self.assertIsNotNone(kitchen.is_recipe_ready(2))
        self.assertIsNotNone(kitchen.is_recipe_ready(3))
        # ingredient ID out of range
        self.assertIsNone(kitchen.is_recipe_ready(4))

        # not enough ingredients for the recipes yet
        self.assertFalse(kitchen.is_recipe_ready(0))
        self.assertFalse(kitchen.is_recipe_ready(1))
        self.assertFalse(kitchen.is_recipe_ready(2))
        self.assertIsNotNone(kitchen.is_recipe_ready(0))
        self.assertIsNotNone(kitchen.is_recipe_ready(1))
        self.assertIsNotNone(kitchen.is_recipe_ready(2))

        kitchen.inventory.add_amount_of_ingredient(0, 3)
        kitchen.inventory.add_amount_of_ingredient(1, 4)
        kitchen.inventory.add_amount_of_ingredient(2, 1)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 0 needs 5*apple, 3*bread, 1*egg. Not enough apple.
        self.assertFalse(kitchen.is_recipe_ready(0))
        # recipe 1 needs 2*apple, 3*bread, 2*egg. Not enough eggs.
        self.assertFalse(kitchen.is_recipe_ready(1))
        # recipe 2 needs 1*apple, 4*bread.
        self.assertTrue(kitchen.is_recipe_ready(2))
        # recipe 3 needs nothing.
        self.assertTrue(kitchen.is_recipe_ready(3))

        kitchen.inventory.add_amount_of_ingredient(0, 1)
        kitchen.inventory.add_amount_of_ingredient(1, -1)
        kitchen.inventory.add_amount_of_ingredient(2, 1)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(2, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 0 needs 5*apple, 3*bread, 1*egg. Not enough apple.
        self.assertFalse(kitchen.is_recipe_ready(0))
        # recipe 1 needs 2*apple, 3*bread, 2*egg.
        self.assertTrue(kitchen.is_recipe_ready(1))
        # recipe 2 needs 1*apple, 4*bread. Not enough bread.
        self.assertFalse(kitchen.is_recipe_ready(2))
        # recipe 3 needs nothing.
        self.assertTrue(kitchen.is_recipe_ready(3))

        kitchen.inventory.add_amount_of_ingredient(0, 1)
        self.assertEqual(5, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(2, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 0 needs 5*apple, 3*bread, 1*egg.
        self.assertTrue(kitchen.is_recipe_ready(0))
        # recipe 1 needs 2*apple, 3*bread, 2*egg.
        self.assertTrue(kitchen.is_recipe_ready(1))
        # recipe 2 needs 1*apple, 4*bread. Not enough bread.
        self.assertFalse(kitchen.is_recipe_ready(2))
        # recipe 3 needs nothing.
        self.assertTrue(kitchen.is_recipe_ready(3))

        kitchen.inventory.add_amount_of_ingredient(0, -10)
        self.assertEqual(-5, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(2, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 0 needs 5*apple, 3*bread, 1*egg. Not enough apple.
        self.assertFalse(kitchen.is_recipe_ready(0))
        # recipe 1 needs 2*apple, 3*bread, 2*egg. Not enough apple.
        self.assertFalse(kitchen.is_recipe_ready(1))
        # recipe 2 needs 1*apple, 4*bread. Not enough apple or bread.
        self.assertFalse(kitchen.is_recipe_ready(2))
        # recipe 3 needs nothing.
        self.assertTrue(kitchen.is_recipe_ready(3))

        # ingredient ID out of range
        self.assertIsNone(kitchen.is_recipe_ready(-1))
        self.assertIsNone(kitchen.is_recipe_ready(5))
        self.assertIsNone(kitchen.is_recipe_ready([1]))
        self.assertIsNone(kitchen.is_recipe_ready(0.0))
        self.assertIsNone(kitchen.is_recipe_ready("0"))
        self.assertIsNone(kitchen.is_recipe_ready(True))

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "4.2. test_kitchen_is_recipe_ready (examples)", "marks" : 2.5})
        marks += 2.5

    def test_kitchen_buy_ingredient(self):
        the_names = ["apple", "custard", "egg"]
        recipe0 = [0, 0, 0, 0, 0, 1, 1, 1, 2]
        recipe1 = [2, 1, 1, 0, 0, 2, 1]
        recipe2 = [1, 1, 0, 1, 1]
        empty_recipe = []
        impossible_recipe = [3]
        kitchen = Kitchen(the_names, [recipe0, recipe1, recipe2, empty_recipe, impossible_recipe])

        result = kitchen.buy_ingredient(0, 3)
        self.assertEqual(3, result)
        result = kitchen.buy_ingredient(1, 4)
        self.assertEqual(4, result)
        result = kitchen.buy_ingredient(2, 1)
        self.assertEqual(1, result)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(2).quantity)

        kitchen.buy_ingredient(0, 1)
        kitchen.buy_ingredient(2, 1)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(2, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # if amount is negative, returns None and does nothing
        result = kitchen.buy_ingredient(1, -1)
        self.assertIsNone(result)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(2, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # if amount is not an int, returns None and does nothing
        result = kitchen.buy_ingredient(0, 1.0)
        self.assertIsNone(result)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(2, kitchen.inventory.get_ingredient_by_id(2).quantity)

        kitchen.inventory.add_amount_of_ingredient(1, -1)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(2, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 0 needs 5*apple, 3*bread, 1*egg. Not enough apple.
        self.assertFalse(kitchen.is_recipe_ready(0))
        # recipe 1 needs 2*apple, 3*bread, 2*egg.
        self.assertTrue(kitchen.is_recipe_ready(1))
        # recipe 2 needs 1*apple, 4*bread. Not enough bread.
        self.assertFalse(kitchen.is_recipe_ready(2))
        # recipe 3 needs nothing.
        self.assertTrue(kitchen.is_recipe_ready(3))

        result = kitchen.buy_ingredient(0, 1)
        self.assertEqual(5, result)
        self.assertEqual(5, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(2, kitchen.inventory.get_ingredient_by_id(2).quantity)

        result = kitchen.buy_ingredient(2, 0)
        self.assertEqual(2, result)
        self.assertEqual(5, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(2, kitchen.inventory.get_ingredient_by_id(2).quantity)

        self.assertTrue(kitchen.is_recipe_ready(0))
        self.assertTrue(kitchen.is_recipe_ready(1))
        self.assertFalse(kitchen.is_recipe_ready(2))
        self.assertTrue(kitchen.is_recipe_ready(3))

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "4.3. test_kitchen_buy_ingredient (examples)", "marks" : 2.5})
        marks += 2.5

    def test_kitchen_cook(self):
        the_names = ["apple", "custard", "egg"]
        recipe0 = [0, 0, 0, 0, 0, 1, 1, 1, 2]
        recipe1 = [2, 1, 1, 0, 0, 2, 1]
        recipe2 = [1, 1, 0, 1, 1]
        empty_recipe = []
        impossible_recipe = [3]
        kitchen = Kitchen(the_names, [recipe0, recipe1, recipe2, empty_recipe, impossible_recipe])

        kitchen.buy_ingredient(0, 3)
        kitchen.buy_ingredient(1, 4)
        kitchen.buy_ingredient(2, 1)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # if recipe ID is nonsense, returns None and does nothing
        result = kitchen.cook(-1)
        self.assertIsNone(result)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(2).quantity)

        result = kitchen.cook(0.0)
        self.assertIsNone(result)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(2).quantity)

        result = kitchen.cook(["1"])
        self.assertIsNone(result)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(2).quantity)

        result = kitchen.cook(5)
        self.assertIsNone(result)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # if recipe is impossible, returns None and does nothing
        result = kitchen.cook(4)
        self.assertIsNone(result)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # cooking the empty recipe does nothing
        result = kitchen.cook(3)
        self.assertTrue(result)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 0 needs 5*apple, 3*bread, 1*egg. Not enough apple.
        # returns False and does nothing
        result = kitchen.cook(0)
        self.assertIsNotNone(result)
        self.assertFalse(result)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 1 needs 2*apple, 3*bread, 2*egg. Not enough eggs.
        result = kitchen.cook(1)
        self.assertIsNotNone(result)
        self.assertFalse(result)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 3 needs nothing.
        self.assertTrue(kitchen.is_recipe_ready(3))

        # buy 10 eggs
        kitchen.buy_ingredient(2,10)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(11, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 1 needs 2*apple, 3*bread, 2*egg.
        # Consumes the ingredients and returns True.
        result = kitchen.cook(1)
        self.assertTrue(result)
        self.assertEqual(3 - 2, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(4 - 3, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(11 - 2, kitchen.inventory.get_ingredient_by_id(2).quantity)

        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(9, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 1 needs 2*apple, 3*bread, 2*egg. Not enough apple or bread.
        result = kitchen.cook(1)
        self.assertIsNotNone(result)
        self.assertFalse(result)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(9, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 2 needs 1*apple, 4*bread. Not enough bread.
        # returns False and does nothing
        result = kitchen.cook(2)
        self.assertIsNotNone(result)
        self.assertFalse(result)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(9, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # cooking the empty recipe does nothing
        result = kitchen.cook(3)
        self.assertTrue(result)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(9, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # buy 6 bread
        kitchen.buy_ingredient(1,6)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(7, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(9, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 1 needs 2*apple, 3*bread, 2*egg. Not enough apples.
        result = kitchen.cook(1)
        self.assertIsNotNone(result)
        self.assertFalse(result)
        self.assertEqual(1, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(7, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(9, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 2 needs 1*apple, 4*bread.
        # Consumes the ingredients and returns True.
        result = kitchen.cook(2)
        self.assertTrue(result)
        self.assertEqual(0, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(9, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 2 needs 1*apple, 4*bread. Not enough apples or bread.
        result = kitchen.cook(2)
        self.assertIsNotNone(result)
        self.assertFalse(result)
        self.assertEqual(0, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(9, kitchen.inventory.get_ingredient_by_id(2).quantity)

        # recipe 2 needs 1*apple, 4*bread. Not enough apples or bread.
        result = kitchen.cook(2)
        self.assertIsNotNone(result)
        self.assertFalse(result)
        self.assertEqual(0, kitchen.inventory.get_ingredient_by_id(0).quantity)
        self.assertEqual(3, kitchen.inventory.get_ingredient_by_id(1).quantity)
        self.assertEqual(9, kitchen.inventory.get_ingredient_by_id(2).quantity)

        ###
        # New kitchen!
        ###
        the_names = ["harissa", "jalapeno", "koji"]
        kitchen = Kitchen(the_names, [[0, 1], [1, 2], [2, 0], [1, 3]])
        # name the recipes
        HJ, JK, KH, oops = 0, 1, 2, 3
        self.assertListEqual([0, 1], kitchen.recipes[HJ])
        self.assertListEqual([1, 2], kitchen.recipes[JK])
        self.assertListEqual([2, 0], kitchen.recipes[KH])
        self.assertListEqual([1, 3], kitchen.recipes[oops])

        for i in [HJ, JK, KH]:
            result = kitchen.cook(i)
            self.assertIsNotNone(result, f"i = {i}")
            self.assertFalse(result, f"i = {i}")
        self.assertIsNone(kitchen.cook(oops))

        # 0x harissa, 0x jalapeno, 0x koji

        kitchen.buy_ingredient(1, 12)

        # 0x harissa, 12x jalapeno, 0x koji

        for i in [HJ, JK, KH]:
            result = kitchen.cook(i)
            self.assertIsNotNone(result, f"i = {i}")
            self.assertFalse(result, f"i = {i}")
        self.assertIsNone(kitchen.cook(oops))

        for i in [HJ, JK, KH]:
            result = kitchen.cook(i)
            self.assertIsNotNone(result, f"i = {i}")
            self.assertFalse(result, f"i = {i}")
        self.assertIsNone(kitchen.cook(oops))

        # 0x harissa, 12x jalapeno, 0x koji

        kitchen.buy_ingredient(2, 3)

        # 0x harissa, 12x jalapeno, 3x koji

        result = kitchen.cook(HJ)
        self.assertFalse(result)
        result = kitchen.cook(KH)
        self.assertFalse(result)

        result = kitchen.cook(HJ)
        self.assertFalse(result)
        result = kitchen.cook(KH)
        self.assertFalse(result)

        # 0x harissa, 12x jalapeno, 3x koji

        result = kitchen.cook(JK)
        self.assertTrue(result)

        # 0x harissa, 11x jalapeno, 2x koji

        result = kitchen.cook(JK)
        self.assertTrue(result)

        # 0x harissa, 10x jalapeno, 1x koji

        result = kitchen.cook(JK)
        self.assertTrue(result)

        # 0x harissa, 9x jalapeno, 0x koji

        result = kitchen.cook(JK)
        self.assertIsNotNone(result)
        self.assertFalse(result)

        # 0x harissa, 9x jalapeno, 0x koji

        result = kitchen.cook(JK)
        self.assertIsNotNone(result)
        self.assertFalse(result)

        # 0x harissa, 9x jalapeno, 0x koji

        # let's try some invalid recipes
        self.assertIsNone(kitchen.cook(oops))
        self.assertIsNone(kitchen.cook(-1))
        self.assertIsNone(kitchen.cook(4))
        self.assertIsNone(kitchen.cook(1.0))
        self.assertIsNone(kitchen.cook(17.9))
        self.assertIsNone(kitchen.cook([0]))
        self.assertIsNone(kitchen.cook([]))
        self.assertIsNone(kitchen.cook(True))

        # 0x harissa, 9x jalapeno, 0x koji

        self.assertFalse(kitchen.is_recipe_ready(HJ))
        self.assertFalse(kitchen.is_recipe_ready(JK))

        kitchen.buy_ingredient(0,6)
        kitchen.buy_ingredient(2,6)

        # 6x harissa, 9x jalapeno, 6x koji

        self.assertTrue(kitchen.is_recipe_ready(HJ))
        self.assertTrue(kitchen.is_recipe_ready(JK))
        self.assertTrue(kitchen.is_recipe_ready(KH))

        # 6x harissa, 9x jalapeno, 6x koji

        self.assertTrue(kitchen.cook(HJ))
        self.assertTrue(kitchen.cook(JK))
        self.assertTrue(kitchen.cook(JK))
        self.assertTrue(kitchen.cook(HJ))

        # 4x harissa, 5x jalapeno, 4x koji

        self.assertTrue(kitchen.cook(HJ))
        self.assertTrue(kitchen.cook(JK))
        self.assertTrue(kitchen.cook(JK))
        self.assertTrue(kitchen.cook(HJ))

        # 2x harissa, 1x jalapeno, 2x koji

        self.assertTrue(kitchen.cook(HJ))

        # 1x harissa, 0x jalapeno, 2x koji

        result = kitchen.cook(JK)
        self.assertIsNotNone(result)
        self.assertFalse(result)

        # 1x harissa, 0x jalapeno, 2x koji

        self.assertTrue(kitchen.cook(KH))

        result = kitchen.cook(KH)
        self.assertIsNotNone(result)
        self.assertFalse(result)

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "4.4. test_kitchen_cook (examples)", "marks" : 2.5})
        marks += 2.5

    def test_kitchen_get_ingredient_table(self):

        the_names = ["berry", "Berry", "bread"]
        recipe0 = [0, 0, 0, 0, 0, 1, 1, 1, 2]
        recipe1 = [2, 1, 1, 0, 0, 2, 1]
        recipe2 = [1, 1, 0, 1, 1]
        kitchen = Kitchen(the_names, [recipe0, recipe1, recipe2])
        self.assertDictEqual(
                kitchen.get_ingredient_table(0),
                {"berry": 5, "Berry": 3, "bread": 1})
        self.assertDictEqual(
                kitchen.get_ingredient_table(1),
                {"berry": 2, "Berry": 3, "bread": 2})
        self.assertDictEqual(
                kitchen.get_ingredient_table(2),
                {"berry": 1, "Berry": 4})

        the_names = ["cherry", "apple", "banana", "cherry", "eggplant", "fig", "banana",
            "grapefruit", "durian", "?"]
        recipe0 = [0, 0, 1, 3, 1]
        recipe1 = [0, 8, 7, 0]
        recipe2 = [3, 7, 7, 3, 2, 3, 4, 5, 6]
        kitchen = Kitchen(the_names, [recipe0, recipe1, recipe2])

        self.assertIsNone(kitchen.get_ingredient_table(3))
        self.assertIsNone(kitchen.get_ingredient_table(-1))
        self.assertDictEqual(
                kitchen.get_ingredient_table(0),
                {"cherry": 2, "apple": 2, "eggplant": 1})
        self.assertIsNone(kitchen.get_ingredient_table(1))
        self.assertDictEqual(
                kitchen.get_ingredient_table(2),
                {"?": 2, "banana": 1, "eggplant": 3, "durian": 1, "fig": 1, "grapefruit": 1})

        the_names = ["cherry", "apple", "banana", "cherry"]
        empty_recipe = []
        kitchen = Kitchen(the_names, [empty_recipe])
        self.assertDictEqual(
                kitchen.get_ingredient_table(0),
                {})
        self.assertIsNone(kitchen.get_ingredient_table(1))

        # examples end here
        # OPTIONAL: add your own examples!

        global marks, passed
        passed.append({"test" : "4.5. test_kitchen_get_ingredient_table (examples)", "marks" : 2.5})
        marks += 2.5

if __name__ == "__main__":
    main()

