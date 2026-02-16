"""
Question 5: Association Rule Mining
Grocery Store Transaction Dataset
"""

# =========================
# IMPORT LIBRARIES
# =========================
import pandas as pd
from itertools import combinations
from collections import defaultdict

# =========================
# B. DATASET
# =========================

# Sample Grocery Transactions
transactions = [
    ["milk", "bread", "butter"],
    ["bread", "butter"],
    ["milk", "bread"],
    ["milk", "butter"],
    ["bread", "butter"],
    ["milk", "bread", "butter"],
    ["milk", "bread"],
    ["milk", "butter"],
    ["bread"],
    ["milk", "bread", "butter"]
]

print("Total Transactions:", len(transactions))
print("\nSample Transactions:")
for t in transactions[:5]:
    print(t)


# =========================
# C. GENERATING ITEMSETS
# =========================

def get_item_support(transactions):
    """Calculate support of single items"""
    item_count = defaultdict(int)
    total_transactions = len(transactions)

    for transaction in transactions:
        for item in transaction:
            item_count[item] += 1

    support = {}
    for item, count in item_count.items():
        support[item] = count / total_transactions

    return support


single_item_support = get_item_support(transactions)

print("\nSingle Item Supports:")
for item, sup in single_item_support.items():
    print(f"{item}: {sup:.2f}")


# =========================
# D. APRIORI ALGORITHM
# =========================

def apriori(transactions, min_support):
    total_transactions = len(transactions)
    itemsets = []

    # Generate 1-itemsets
    single_items = set(item for transaction in transactions for item in transaction)
    current_itemsets = [{item} for item in single_items]

    while current_itemsets:
        frequent_itemsets = []

        for itemset in current_itemsets:
            count = 0
            for transaction in transactions:
                if itemset.issubset(transaction):
                    count += 1

            support = count / total_transactions

            if support >= min_support:
                frequent_itemsets.append(itemset)
                itemsets.append((itemset, support))

        # Generate next level combinations
        next_itemsets = []
        for i in range(len(frequent_itemsets)):
            for j in range(i + 1, len(frequent_itemsets)):
                union_set = frequent_itemsets[i] | frequent_itemsets[j]
                if len(union_set) == len(frequent_itemsets[i]) + 1:
                    next_itemsets.append(union_set)

        current_itemsets = next_itemsets

    return itemsets


min_support = 0.4
frequent_itemsets = apriori(transactions, min_support)

print("\nFrequent Itemsets (min_support=0.4):")
for itemset, support in frequent_itemsets:
    print(f"{set(itemset)}: {support:.2f}")


# =========================
# E. ASSOCIATION RULES
# =========================

def generate_rules(frequent_itemsets, min_confidence):
    rules = []

    for itemset, support in frequent_itemsets:
        if len(itemset) > 1:
            for i in range(1, len(itemset)):
                for antecedent in combinations(itemset, i):
                    antecedent = set(antecedent)
                    consequent = itemset - antecedent

                    antecedent_support = next(
                        sup for iset, sup in frequent_itemsets if iset == antecedent
                    )

                    confidence = support / antecedent_support

                    if confidence >= min_confidence:
                        lift = confidence / next(
                            sup for iset, sup in frequent_itemsets if iset == consequent
                        )

                        rules.append((antecedent, consequent, support, confidence, lift))

    return rules


min_confidence = 0.6
rules = generate_rules(frequent_itemsets, min_confidence)

print("\nAssociation Rules (min_confidence=0.6):")
for antecedent, consequent, support, confidence, lift in rules:
    print(f"{antecedent} -> {consequent} | "
          f"Support: {support:.2f}, "
          f"Confidence: {confidence:.2f}, "
          f"Lift: {lift:.2f}")


# =========================
# F. EVALUATION
# =========================

print("\nHigh Lift Rules (>1 indicates strong association):")
for antecedent, consequent, support, confidence, lift in rules:
    if lift > 1:
        print(f"{antecedent} -> {consequent} | Lift: {lift:.2f}")
