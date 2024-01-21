from finance_database import FinanceDatabase

if __name__ == "__main__":
    finance_db = FinanceDatabase()

    finance_db.insert_product('Personal Loan', 'Low-interest personal loan for any purpose.')

    finance_db.close_connection()
