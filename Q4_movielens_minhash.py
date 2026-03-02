import hashlib
import random
import itertools
from collections import defaultdict

threshold = 0.5
hash_sizes = [50, 100, 200]
num_runs = 5
mod_prime = 200003

def load_ratings(path):
    user_items = defaultdict(set)
    with open(path, "r") as file:
        for line in file:
            user_id, movie_id, _, _ = line.strip().split("\t")
            user_items[int(user_id)].add(int(movie_id))
    return user_items

def jaccard_score(a, b):
    return len(a & b) / len(a | b)

def hash_value(x):
    return int(hashlib.md5(str(x).encode()).hexdigest(), 16)

def create_hash_family(count):
    family = []
    for _ in range(count):
        a = random.randint(1, mod_prime - 1)
        b = random.randint(0, mod_prime - 1)
        family.append((a, b))
    return family

def build_signature(item_set, family):
    signature = []
    for a, b in family:
        smallest = float("inf")
        for item in item_set:
            base_hash = hash_value(item)
            value = (a * base_hash + b) % mod_prime
            if value < smallest:
                smallest = value
        signature.append(smallest)
    return signature

def signature_similarity(sig_a, sig_b):
    matches = sum(1 for i in range(len(sig_a)) if sig_a[i] == sig_b[i])
    return matches / len(sig_a)

user_data = load_ratings("u.data")
user_list = list(user_data.keys())

print("Total users:", len(user_list))

exact_similar_pairs = set()

for u1, u2 in itertools.combinations(user_list, 2):
    score = jaccard_score(user_data[u1], user_data[u2])
    if score >= threshold:
        exact_similar_pairs.add((u1, u2))

print("Exact pairs with similarity >=", threshold, ":", len(exact_similar_pairs))

for size in hash_sizes:
    total_fp = 0
    total_fn = 0

    for _ in range(num_runs):
        family = create_hash_family(size)

        signatures = {}
        for user in user_list:
            signatures[user] = build_signature(user_data[user], family)

        estimated_pairs = set()
        for u1, u2 in itertools.combinations(user_list, 2):
            est_score = signature_similarity(signatures[u1], signatures[u2])
            if est_score >= threshold:
                estimated_pairs.add((u1, u2))

        false_positive = len(estimated_pairs - exact_similar_pairs)
        false_negative = len(exact_similar_pairs - estimated_pairs)

        total_fp += false_positive
        total_fn += false_negative

    print()
    print("t =", size)
    print("Average False Positives:", total_fp / num_runs)
    print("Average False Negatives:", total_fn / num_runs)
