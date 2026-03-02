import hashlib
import random
import itertools
from collections import defaultdict

similarity_levels = [0.6, 0.8]
num_runs = 5
mod_prime = 200003

band_configs = {
    50:  [(5, 10)],
    100: [(5, 20)],
    200: [(5, 40), (10, 20)]
}

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

def generate_candidates(signature_map, rows, bands):
    buckets = defaultdict(list)

    for user, sig in signature_map.items():
        for band in range(bands):
            start = band * rows
            end = start + rows
            key = (band, tuple(sig[start:end]))
            buckets[key].append(user)

    candidates = set()
    for group in buckets.values():
        if len(group) > 1:
            for pair in itertools.combinations(group, 2):
                candidates.add(tuple(sorted(pair)))

    return candidates

user_data = load_ratings("u.data")
user_list = list(user_data.keys())

exact_similarity = {}
for u1, u2 in itertools.combinations(user_list, 2):
    exact_similarity[(u1, u2)] = jaccard_score(user_data[u1], user_data[u2])

for level in similarity_levels:
    print("\nThreshold =", level)

    true_pairs = {pair for pair, score in exact_similarity.items() if score >= level}

    for hash_count, config_list in band_configs.items():
        for rows, bands in config_list:
            total_fp = 0
            total_fn = 0

            for _ in range(num_runs):
                family = create_hash_family(hash_count)

                signatures = {}
                for user in user_list:
                    signatures[user] = build_signature(user_data[user], family)

                candidates = generate_candidates(signatures, rows, bands)

                normalized_candidates = {tuple(sorted(p)) for p in candidates}

                false_positive = len(normalized_candidates - true_pairs)
                false_negative = len(true_pairs - normalized_candidates)

                total_fp += false_positive
                total_fn += false_negative

            print("t =", hash_count, "r =", rows, "b =", bands)
            print("Average False Positives:", total_fp / num_runs)
            print("Average False Negatives:", total_fn / num_runs)
