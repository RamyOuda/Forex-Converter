from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates, CurrencyCodes, Decimal

app = Flask(__name__)

# ----------

dict_file = open("CurrencyCodes.txt")
codes = [code.strip() for code in dict_file]
dict_file.close()

# ----------


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/get-data")
def get_data_from_form():
    input_from = request.args["from"].upper()
    input_to = request.args["to"].upper()
    input_amount = request.args["amount"].upper()

    if input_from not in codes:
        return render_template("home.html", error=f"{input_from} is an invalid currency code.")
    elif input_to not in codes:
        return render_template("home.html", error=f"{input_to} is an invalid currency code.")
    elif int(input_amount) <= 0:
        return render_template("home.html", error="Currency amount must be greater than 0.")

    symbol = CurrencyCodes().get_symbol(input_to)

    conversion = round(CurrencyRates(force_decimal=True).convert(
        input_from, input_to, Decimal(input_amount)), 2)

    return render_template("home.html", conversion=conversion, symbol=symbol)
