import pandas as pd

def load_data():
    # Зареждане на данни от CSV файловете
    try:
        credit_products = pd.read_csv('credit_products.csv')
        user_profiles = pd.read_csv('user_profiles.csv')

        print("Данните са успешно заредени от CSV файловете.")
        return credit_products, user_profiles

    except FileNotFoundError:
        print("Грешка: CSV файловете не са намерени. Моля, създайте ги първо.")
        return None, None

if __name__ == "__main__":
    credit_products, user_profiles = load_data()

    if credit_products is not None and user_profiles is not None:
        # Извеждане на заредените данни
        print("Кредитни Продукти:")
        print(credit_products)
        print("\nПотребителски Профили:")
        print(user_profiles)
