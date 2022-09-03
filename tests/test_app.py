from unittest import TestCase
from app import app
from forex_python.converter import CurrencyRates, Decimal


class FlaskTests(TestCase):

    def setUp(self):
        app.config["TESTING"] = True

    def test_home_page(self):

        conversion = round(CurrencyRates(force_decimal=True).convert(
            "USD", "USD", Decimal(1)), 2)

        self.assertEqual(conversion, 1.00)
        self.assertNotEqual(conversion, 2)

        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("<h1>Forex Converter!</h1>", html)
