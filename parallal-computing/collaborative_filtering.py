"""
Question 6: Collaborative Filtering and Recommender Systems
"""

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

# =========================
# B. DATASET
# =========================

# Simple Movie Ratings Dataset
data = {
    'user': ['U1','U1','U1','U2','U2','U2','U3','U3','U3','U4','U4','U4'],
    'item': ['M1','M2','M3','M1','M2','M4','M1','M3','M4','M2','M3','M4'],
    'rating': [5,4,1,4,5,2,5,4,3,3,4,5]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)

# Create User-Item Matrix
user_item_matrix = df.pivot(index='user', columns='item', values='rating').fillna(0)

print("\nUser-Item Matrix:\n", user_item_matrix)


# =========================
# C. USER-BASED COLLABORATIVE FILTERING
# =========================

user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity,
                                   index=user_item_matrix.index,
                                   columns=user_item_matrix.index)

print("\nUser Similarity Matrix:\n", user_similarity_df)


def recommend_user_based(user, top_n=2):
    similar_users = user_similarity_df[user].sort_values(ascending=False)[1:]
    most_similar_user = similar_users.index[0]

    user_ratings = user_item_matrix.loc[user]
    similar_user_ratings = user_item_matrix.loc[most_similar_user]

    recommendations = similar_user_ratings[(user_ratings == 0) & (similar_user_ratings > 0)]
    return recommendations.sort_values(ascending=False).head(top_n)


print("\nUser-Based Recommendations for U1:")
print(recommend_user_based('U1'))


# =========================
# D. ITEM-BASED COLLABORATIVE FILTERING
# =========================

item_similarity = cosine_similarity(user_item_matrix.T)
item_similarity_df = pd.DataFrame(item_similarity,
                                   index=user_item_matrix.columns,
                                   columns=user_item_matrix.columns)

print("\nItem Similarity Matrix:\n", item_similarity_df)


def recommend_item_based(user, top_n=2):
    user_ratings = user_item_matrix.loc[user]
    rated_items = user_ratings[user_ratings > 0].index

    scores = {}

    for item in rated_items:
        similar_items = item_similarity_df[item].sort_values(ascending=False)[1:]
        for sim_item, sim_score in similar_items.items():
            if user_ratings[sim_item] == 0:
                scores[sim_item] = scores.get(sim_item, 0) + sim_score

    recommendations = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return recommendations[:top_n]


print("\nItem-Based Recommendations for U1:")
print(recommend_item_based('U1'))


# =========================
# E. HYBRID RECOMMENDER
# =========================

def hybrid_recommend(user):
    user_based = recommend_user_based(user)
    item_based = recommend_item_based(user)

    hybrid_items = list(user_based.index) + [i[0] for i in item_based]
    return set(hybrid_items)


print("\nHybrid Recommendations for U1:")
print(hybrid_recommend('U1'))


# =========================
# F. EVALUATION
# =========================

# Simple binary relevance evaluation
true_labels = [1, 1, 0, 1]
pred_labels = [1, 1, 0, 0]

precision = precision_score(true_labels, pred_labels)
recall = recall_score(true_labels, pred_labels)
f1 = f1_score(true_labels, pred_labels)

print("\nEvaluation Metrics:")
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
