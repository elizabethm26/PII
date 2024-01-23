import pandas as pd

def create_sample_data():
    
    credit_products_data = {
        'product_id': [1, 2, 3, 4, 5, 6],
        'product_name': ['Personal Loan', 'Credit Card', 'Student Loan', 'Mortgage', 'Auto Loan', 'Business Loan'],
        'product_description': ['Quick personal loan...', 'Rewards credit card...', 'Cover cost of education…',
                                'Finance the purchase of real estate', 'Purchase vehicles', 'For business needs'],
        'interest_rate': [8.5, 18.9, 3.73, 3.45, 5.99, 7.62],
        'loan_term': [24, None, 120, None, 60, 36],  # None може да означава неопределен срок
        'max_credit_limit': [20000, 5000, 10000, 800000, 200000, 500000]
    }

    credit_products = pd.DataFrame(credit_products_data)

    # Записване на кредитните продукти в CSV файл с разделител запетая (comma)
    credit_products.to_csv('credit_products.csv', index=False, sep=',')

    
    user_profiles_data = {
        'user_id': [101, 102, 103, 104, 105, 106],
        'user_name': ['John', 'Jane', 'Misho', 'Mimi', 'Vanko', 'Preslava'],
        'income': [60000, 80000, 25000, 50000, 28000, 500000],
        'expenses': [40000, 50000, 18000, 30000, 20000, 300000],
        'credit_history': ['Good', 'Excellent', 'Average', 'Good', 'Average', 'Excellent'],
        'preferred_product': ['Personal Loan', 'Credit Card', 'Student Loan', 'Mortgage', 'Auto Loan', 'Business Loan']
    }

    user_profiles = pd.DataFrame(user_profiles_data)

    # Записване на потребителските профили в CSV файл с разделител запетая (comma)
    user_profiles.to_csv('user_profiles.csv', index=False, sep=',')

    print("Примерни данни създадени и записани в CSV файлове.")


def main():
    create_sample_data()

if __name__ == "__main__":
    main()
