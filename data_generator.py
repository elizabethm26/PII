import pandas as pd

def create_sample_data():
    # Примерни данни за кредитни продукти
    credit_products_data = {
        'product_id': [1, 2],
        'product_name': ['Personal Loan', 'Credit Card'],
        'product_description': ['Quick personal loan...', 'Rewards credit card...'],
        'interest_rate': [8.5, 18.9],
        'loan_term': [24, None],  # None може да означава неопределен срок
        'max_credit_limit': [20000, 5000]
    }

    credit_products = pd.DataFrame(credit_products_data)

    # Записване на кредитните продукти в CSV файл с разделител запетая (comma)
    credit_products.to_csv('credit_products.csv', index=False, sep=',')

    # Примерни данни за потребители
    user_profiles_data = {
        'user_id': [101, 102],
        'user_name': ['John', 'Jane'],
        'income': [60000, 80000],
        'expenses': [40000, 50000],
        'credit_history': ['Good', 'Excellent'],
        'preferred_product': ['Personal Loan', 'Credit Card']
    }

    user_profiles = pd.DataFrame(user_profiles_data)

    # Записване на потребителските профили в CSV файл с разделител запетая (comma)
    user_profiles.to_csv('user_profiles.csv', index=False, sep=',')

    print("Примерни данни създадени и записани в CSV файлове.")


def main():
    create_sample_data()

if __name__ == "__main__":
    main()
