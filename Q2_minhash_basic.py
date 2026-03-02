import hashlib
import random
import time

docs = {
    "D1": "apple ceo tim cook is spending some time in canada this week and yesterday he attended a hockey game and visited the eaton centre apple store in toronto cook today stopped by the offices of canadian ecommerce platform shopify where he spoke to the financial post about augmented reality apps and the homepod on the topic of the homepod cook said that apples deep integration between hardware and software will help to differentiate the smart speaker from competing products like amazons alexa and the google home competition makes all of us better and i welcome it cook said but if you are both trying to license something and compete with your licensees this is a difficult model and it remains to be seen if it can be successful or not cook also said a quality very immersive audio experience was one thing missing from the smart speaker market which apple is aiming to fix music deserves that kind of quality as opposed to some kind of squeaky sound he said the homepod which at in the united states is more expensive than competing products features a tweeter array an apple designed inch upward facing woofer and spatial awareness all of which is designed to provide the best possible sound during his interview with the financial post cook also spoke about augmented reality a topic he is covered many times in the past cook said ar is the most profound technology of the future thats able to amplify human experience instead of substitute it cook said developers across canada are adopting ar at a very fast rate and that he couldnt be happier with developer interest in arkit cooks full interview which includes additional comments on augmented reality and details on features coming to shopify can be read over at the financial post website",
    "D2": "apple ceo tim cook is spending some time in canada this week and yesterday attended a hockey game and visited the eaton centre apple store in toronto tim cook today stopped by the offices of canadian ecommerce platform shopify where he spoke to the financial post about augmented reality apps and the homepod on the topic of the homepod cook said that apples deep integration between hardware and software will help to differentiate the smart speaker from competing products like amazons alexa and the google home competition makes all of us better and i welcome it cook said but if you are trying to license something and compete with your licensees this is a difficult model and it remains to be seen if it can be successful or not cook also said a quality very immersive audio experience was one thing missing from the smart speaker market which the company is aiming to fix music deserves that kind of quality as opposed to some kind of xxx sound he said the homepod which at in the united states is more expensive than competing products features a tweeter array an apple designed inch upward facing woofer and spatial awareness all of which is designed to provide the best possible sound during his interview with the financial post cook also spoke about augmented reality a topic he is covered many times in the past cook said ar is the most profound technology of the future thats able to amplify human experience instead of substitute it cook said developers across canada are adopting ar at a very fast rate and that he couldnt be happier with developer interest in arkit cooks full interview which includes additional comments on augmented reality and details on features coming to shopify can be read over at the financial post website"
}

def create_3grams(text):
    return {text[i:i+3] for i in range(len(text) - 2)}

def jaccard_score(a, b):
    return len(a & b) / len(a | b)

def hash_value(item):
    return int(hashlib.md5(item.encode()).hexdigest(), 16)

def build_hash_family(count, modulus):
    family = []
    for _ in range(count):
        a = random.randint(1, modulus - 1)
        b = random.randint(0, modulus - 1)
        family.append((a, b))
    return family

def build_signature(gram_set, family, modulus):
    signature = []
    for a, b in family:
        smallest = float("inf")
        for gram in gram_set:
            base_hash = hash_value(gram)
            value = (a * base_hash + b) % modulus
            if value < smallest:
                smallest = value
        signature.append(smallest)
    return signature

def compare_signatures(sig_a, sig_b):
    matches = sum(1 for i in range(len(sig_a)) if sig_a[i] == sig_b[i])
    return matches / len(sig_a)

mod_prime = 1000003

d1_set = create_3grams(docs["D1"])
d2_set = create_3grams(docs["D2"])

exact_value = jaccard_score(d1_set, d2_set)

print("\nExact Jaccard Similarity (3-grams, D1 vs D2):", round(exact_value, 4))
print()

hash_sizes = [20, 60, 150, 300, 600]

for size in hash_sizes:
    start = time.time()

    family = build_hash_family(size, mod_prime)

    sig_a = build_signature(d1_set, family, mod_prime)
    sig_b = build_signature(d2_set, family, mod_prime)

    approx = compare_signatures(sig_a, sig_b)

    end = time.time()

    print("t =", size)
    print("Estimated Jaccard Similarity =", round(approx, 4))
    print("Time =", round(end - start, 6), "seconds\n")
