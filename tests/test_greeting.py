import unittest

from src.greeting import create_greeting


class CreateGreetingTests(unittest.TestCase):
    def test_returns_greeting(self) -> None:
        self.assertEqual(create_greeting("Alex"), "Hello, Alex!")

    def test_trims_whitespace(self) -> None:
        self.assertEqual(create_greeting("  Sam  "), "Hello, Sam!")

    def test_rejects_empty_name(self) -> None:
        with self.assertRaisesRegex(ValueError, "name must not be empty"):
            create_greeting("   ")


if __name__ == "__main__":
    unittest.main()

