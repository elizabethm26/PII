import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Зареждане на данните
credit_products = pd.read_csv('credit_products.csv')
user_profiles = pd.read_csv('user_profiles.csv')

# Визуализация с Matplotlib и Seaborn
plt.figure(figsize=(12, 6))

# Пример 1: Bar plot за средната лихва на кредитните продукти
plt.subplot(1, 2, 1)
sns.barplot(x='product_name', y='interest_rate', data=credit_products)
plt.title('Средна лихва на кредитните продукти')

# Пример 2: Box plot за доходите на потребителите
plt.subplot(1, 2, 2)
sns.boxplot(y='income', data=user_profiles)
plt.title('Box plot за доходите на потребителите')

# Показване на графиките
plt.tight_layout()
plt.show()




