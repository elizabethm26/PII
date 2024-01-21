from data_generator import create_sample_data
from data_loader import load_data

def main():
    create_sample_data()
    credit_products, user_profiles = load_data()

    # Извеждане на заредените данни
    print("Кредитни Продукти:")
    print(credit_products)
    print("\nПотребителски Профили:")
    print(user_profiles)

if __name__ == "__main__":
    main()
