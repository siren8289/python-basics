"""unittest로 validator.py의 동작을 검증한다. 실행: python3 -m unittest -v"""
import unittest

from validator import (
    MISSING_MESSAGE,
    validate_age,
    validate_all,
    validate_email,
    validate_password,
)


class TestValidateAge(unittest.TestCase):
    def test_valid_ages(self):                       # 1
        for age in (0, 20, 150):
            with self.subTest(age=age):
                self.assertEqual(validate_age(age), (True, "OK"))

    def test_bool_is_rejected(self):                 # 2
        self.assertFalse(validate_age(True)[0])

    def test_out_of_range(self):                     # 3
        self.assertFalse(validate_age(-1)[0])
        self.assertFalse(validate_age(151)[0])

    def test_string_is_rejected(self):               # 4
        self.assertFalse(validate_age("20")[0])


class TestValidateEmail(unittest.TestCase):
    def test_valid_email(self):                      # 5
        self.assertTrue(validate_email("siren@example.com")[0])
        self.assertTrue(validate_email("  siren@example.com  ")[0])

    def test_missing_or_multiple_at(self):           # 6
        self.assertFalse(validate_email("siren.example.com")[0])
        self.assertFalse(validate_email("a@b@c.com")[0])

    def test_empty_local_part(self):                 # 7
        self.assertFalse(validate_email("@example.com")[0])

    def test_bad_domain(self):                       # 8
        for email in ("a@com", "a@.com", "a@b."):
            with self.subTest(email=email):
                self.assertFalse(validate_email(email)[0])

    def test_non_string(self):                       # 9
        self.assertFalse(validate_email(123)[0])


class TestValidatePassword(unittest.TestCase):
    def test_valid_password(self):                   # 10
        self.assertTrue(validate_password("abcdef12")[0])

    def test_too_short(self):                        # 11
        self.assertFalse(validate_password("abc1")[0])

    def test_custom_min_length(self):                # 12
        self.assertFalse(validate_password("abcdef12", 12)[0])
        self.assertTrue(validate_password("abcdef123456", 12)[0])

    def test_no_digit(self):                         # 13
        self.assertFalse(validate_password("abcdefgh")[0])

    def test_no_alpha(self):                         # 14
        self.assertFalse(validate_password("12345678")[0])

    def test_optional_rules_off(self):               # 15
        self.assertTrue(validate_password("abcdefgh", require_digit=False)[0])

    def test_keyword_only_argument(self):            # 16
        # '*' 뒤 인자를 위치 인자로 넘기면 TypeError
        with self.assertRaises(TypeError):
            validate_password("abcdef12", 8, False)


class TestValidateAll(unittest.TestCase):
    def test_all_valid(self):                        # 17
        data = {"age": 30, "email": "a@b.com", "password": "abcdef12"}
        self.assertEqual(validate_all(data), (True, {}))

    def test_collects_multiple_errors(self):         # 18
        data = {"age": -1, "email": "nope", "password": "short"}
        ok, errors = validate_all(data)
        self.assertFalse(ok)
        self.assertEqual(set(errors), {"age", "email", "password"})

    def test_missing_field(self):                    # 19
        ok, errors = validate_all({"age": 30, "email": "a@b.com"})
        self.assertFalse(ok)
        self.assertEqual(errors, {"password": MISSING_MESSAGE})


if __name__ == "__main__":
    unittest.main()
