class Exchange:
    """Class to handle different exchanges and their specific column names and types."""

    # CSV format specifics for each exchange
    nexo_columns = ["Transaction", "Type", "Input Currency", "Output Currency", "Input Amount", "Output Amount", "Date / Time (UTC)", "USD Equivalent", "Average Price"]
    binance_columns = ["User_ID","UTC_Time","Account","Operation","Coin","Change","Remark"]
    crypto_com_columns = ["Timestamp (UTC)","Transaction Description","Currency","Amount","To Currency","To Amount","Native Currency","Native Amount","Native Amount (in USD)","Transaction Kind","Transaction Hash"]

    name = {
        "Nexo": {
            "columns": nexo_columns,
            "Type" : "Type",
            "Currency" : ["Input Currency", "Output Currency"],
            "Internal Transfers": ["Transfer to Nexo Wallet", "Transfer from Nexo Wallet"]
        },
        "Binance": {
            "columns": binance_columns,
            "Type" : "Operation",
            "Currency" : ["Coin"]
        },
        "Crypto_com": {
            "columns": crypto_com_columns,
            "Type" : "Transaction Description",
            "Currency" : ["Currency", "To Currency"]
        }
    }
    def __init__(self, exchange_name: str):
        if exchange_name not in self.name:
            raise ValueError(f"\033[91mExchange \033[34m'{exchange_name}'\033[91m not recognized. Available exchanges:\033[34m {list(self.name.keys())}\033[0m")
        self.exchange_name = exchange_name
        self.columns = self.name[exchange_name]["columns"]
        self.type = self.name[exchange_name]["Type"]
        self.currency_columns = self.name[exchange_name]["Currency"]


def test():
    binance = Exchange("Binance")
    nexo = Exchange("Nexo")
    crypto_com = Exchange("Crypto_com")
    coinbase = Exchange("Coinbase")  # This will raise a ValueError

    print(binance.type)
    print(nexo.type)
    print(crypto_com.type)

if __name__ == "__main__":
    test()
