# main.py
import pandas as pd
import numpy as np
from data_generator import create_sample_data
from data_loader import load_data
from recommender_model import train_recommendation_model, generate_recommendations
from sklearn.feature_extraction.text import TfidfVectorizer
from recommender_system import train_tfidf_model
from recommender_system import train_tfidf_model, calculate_cosine_similarity

def main():
    # Създаване на примерни данни 
    create_sample_data()

    # Зареждане на данни
    credit_products, user_profiles = load_data()

    if credit_products is not None and user_profiles is not None:
        # Обучение на модел за препоръки
        recommendation_model = train_recommendation_model(credit_products, user_profiles)

        # Генериране на препоръки за определен потребител
        user_id_to_recommend = 101  # Потребител, за който искаме да генерираме препоръки
        recommendations = generate_recommendations(recommendation_model, user_profiles, user_id_to_recommend)

        # Извеждане на препоръките
        print(f"Препоръки за потребител с ID {user_id_to_recommend}:")
        print(recommendations)
        
tfidf_vectorizer, tfidf_matrix = train_tfidf_model('credit_products.csv')
#tfidf_vectorizer = TfidfVectorizer()

def generate_personalized_recommendations(user_preferences, cosine_similarities):
    # Преобразуване на текстовата информация в TF-IDF представяне
    user_preferences_tfidf = tfidf_vectorizer.transform(user_preferences) 
    
    # обученият модел за Content-based препоръчване
    recommendation_model = train_recommendation_model(credit_products, user_profiles)
    
        # Използване на обучения модел за предсказване на предпочитанията на потребителя
    recommendations = recommendation_model.predict(user_preferences_tfidf)
    
      # Обучение на TF-IDF модел
    tfidf_vectorizer, tfidf_matrix = train_tfidf_model('credit_products.csv')
    
     # Избор на най-високите 5 препоръки
    N = 5
    top_n_recommendations = recommendations.argsort()[0][-N:][::-1]
    
    
    
     # Измерване на косинусово сходство
    cosine_similarities = calculate_cosine_similarity(tfidf_matrix)

    # Използване на обучения модел за предсказване на предпочитанията на потребителя
    recommendations = recommendation_model.predict(user_preferences_tfidf)

   

    # Визуализация или запис на резултатите
    print(f"\nТоп {N} препоръки за потребителя:")
    for product_id in top_n_recommendations:
        print(f"Продукт ID: {product_id + 1}, Вероятност за предпочитание: {recommendations[0][product_id]}")
  

   
def generate_recommendations(product_index, cosine_similarities):
    # Измерване на сходството на текущия продукт с останалите
    similarity_scores = list(enumerate(cosine_similarities[product_index]))

    # Сортиране на продуктите според степента на сходство
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Извличане на индексите на препоръчаните продукти (без самия продукт)
    recommended_indices = [i for i, _ in similarity_scores[1:]]

    return recommended_indices


if __name__ == "__main__":
    # Допълнителни стъпки, ако е необходимо
    create_sample_data()
    credit_products, user_profiles = load_data()

      # Обучение на модел за препоръки
    recommendation_model = train_recommendation_model(credit_products, user_profiles)
    # Обучение на TF-IDF модел
    tfidf_vectorizer, tfidf_matrix = train_tfidf_model('credit_products.csv')
    
    # Измерване на косинусово сходство
    cosine_similarities = calculate_cosine_similarity(tfidf_matrix)
    
    # Генериране на персонализирани препоръки за конкретен потребител
    user_preferences = ["Quick personal loan..."]
    generate_personalized_recommendations(user_preferences)
    
    
     
  

    

    


