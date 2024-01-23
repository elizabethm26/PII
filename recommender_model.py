from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.preprocessing import MinMaxScaler
def train_recommendation_model(credit_products, user_profiles):
    # матрица на профилите
    user_matrix = user_profiles.drop('user_id', axis=1).to_numpy()

    # матрица на продуктите
    product_matrix = credit_products.drop(['product_id', 'product_name', 'product_description'], axis=1).to_numpy()

    # Нормализация на данните
    scaler = MinMaxScaler()
    user_matrix_normalized = scaler.fit_transform(user_matrix)
    product_matrix_normalized = scaler.fit_transform(product_matrix)

    # Изчисляване на сходство на косинус между потребителите и продуктите
    recommendation_model = cosine_similarity(user_matrix_normalized, product_matrix_normalized)

    return recommendation_model

def generate_recommendations(recommendation_model, user_profiles, user_id):
    # Намиране на индекса на потребителя в матрицата
    user_index = user_profiles[user_profiles['user_id'] == user_id].index.values[0]

    # Извличане на сходствата за конкретния потребител
    user_similarities = recommendation_model[user_index]

    # Намиране на индексите на продуктите с най-голямо сходство
    top_product_indexes = np.argsort(user_similarities)[::-1]

    # Извличане на информацията за топ продуктите
    top_products = user_profiles.iloc[top_product_indexes][['product_id', 'product_name', 'product_description']]

    return top_products
