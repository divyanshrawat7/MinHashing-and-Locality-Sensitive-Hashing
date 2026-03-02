import random
import itertools

docs = {
    "D1": "apple ceo tim cook is spending some time in canada this week and yesterday he attended a hockey game and visited the eaton centre apple store in toronto cook today stopped by the offices of canadian ecommerce platform shopify where he spoke to the financial post about augmented reality apps and the homepod on the topic of the homepod cook said that apples deep integration between hardware and software will help to differentiate the smart speaker from competing products like amazons alexa and the google home competition makes all of us better and i welcome it cook said but if you are both trying to license something and compete with your licensees this is a difficult model and it remains to be seen if it can be successful or not cook also said a quality very immersive audio experience was one thing missing from the smart speaker market which apple is aiming to fix music deserves that kind of quality as opposed to some kind of squeaky sound he said the homepod which at in the united states is more expensive than competing products features a tweeter array an apple designed inch upward facing woofer and spatial awareness all of which is designed to provide the best possible sound during his interview with the financial post cook also spoke about augmented reality a topic he is covered many times in the past cook said ar is the most profound technology of the future thats able to amplify human experience instead of substitute it cook said developers across canada are adopting ar at a very fast rate and that he couldnt be happier with developer interest in arkit cooks full interview which includes additional comments on augmented reality and details on features coming to shopify can be read over at the financial post website",
    "D2": "apple ceo tim cook is spending some time in canada this week and yesterday attended a hockey game and visited the eaton centre apple store in toronto tim cook today stopped by the offices of canadian ecommerce platform shopify where he spoke to the financial post about augmented reality apps and the homepod on the topic of the homepod cook said that apples deep integration between hardware and software will help to differentiate the smart speaker from competing products like amazons alexa and the google home competition makes all of us better and i welcome it cook said but if you are trying to license something and compete with your licensees this is a difficult model and it remains to be seen if it can be successful or not cook also said a quality very immersive audio experience was one thing missing from the smart speaker market which the company is aiming to fix music deserves that kind of quality as opposed to some kind of xxx sound he said the homepod which at in the united states is more expensive than competing products features a tweeter array an apple designed inch upward facing woofer and spatial awareness all of which is designed to provide the best possible sound during his interview with the financial post cook also spoke about augmented reality a topic he is covered many times in the past cook said ar is the most profound technology of the future thats able to amplify human experience instead of substitute it cook said developers across canada are adopting ar at a very fast rate and that he couldnt be happier with developer interest in arkit cooks full interview which includes additional comments on augmented reality and details on features coming to shopify can be read over at the financial post website",
    "D3": "as part of his one day tour of canada yesterday tim cook offered an interview to the financial post following his visit to ecommerce platform shopifys headquarters cook used the interview as an opportunity to tout apples efforts in augmented realty as well as talk about the homepod regarding ar cook reiterated his bullish views on the technology saying that he sees it as the most profound technology in the future because of how it amplifies human performance furthermore he says he believes that ar will continue to gain adoption at a fast rate i believe that ar is the most profound technology of the future cook said it amplifies human performance it amplifies humans not substitutes and doesnt isolate im a huge believer in it i see ar taking off very quickly he added i see developers across canada adopting at a very fast rate bringing their craft to market and i couldnt be happier with it also in the interview given on the eve of apples homepod release announcement cook offered some color as to what sets its smart speaker apart from competitors while some have criticized the homepod for being a me too product in response to efforts from amazon and google cook says thats not the case the apple ceo explained that the integration between the homepod hardware and ios is one thing that will make it unique competition makes all of us better and i welcome it cook said but if you are both trying to license something and compete with your licensees this is a difficult model and it remains to be seen if it can be successful or not he also adds that sound quality is a differentiating factor of homepod saying that one thing that was missing from the smart speaker market was quality audio we think one thing that was missing from this market was a quality audio experience a very immersive audio experience cook said music deserves that kind of quality as opposed to some kind of squeaky sound the full interview is definitely worth a read and can be found here do you agree with cooks beliefs that sound quality and integration with ios are what set homepod apart from the competition let us know down in the comments",
    "D4": "president trump who warned as a candidate about the false song of globalism is marching straight into the maw of the global beast this week and he is singing his own tune trump is attending the global economic conclave in davos switzerland not because he has come around to the views broadly shared by the sort of international financial elite government figures and academics who gather annually in a swiss ski town he is going because he wants to say i told you so after a year in office america first the nativist cry that helped propel trump to the presidency is the backbone of a trump economic and foreign policy trump is expected to argue has benefited the united states exactly the way he said it would as he does at home trump will crow about a soaring stock market low unemployment the return of some jobs from overseas and the passage of his tax cut package among the plutocrats at the world economic forum trump will also try to turn on the salesmans charm president trump will reiterate that a prosperous america benefits the world when the united states grows so does the world white house economic adviser gary cohn told reporters ahead of the trip the president is going to davos to speak to world leaders about investing in the united states moving businesses to the united states hiring american workers changing the direction of our economy to be one of the biggest and best and most efficient economies in the world"
}

def build_char_grams(text, k):
    return {text[i:i+k] for i in range(len(text) - k + 1)}

def build_word_grams(text, k):
    tokens = text.split()
    return {" ".join(tokens[i:i+k]) for i in range(len(tokens) - k + 1)}

def jaccard_similarity(a, b):
    return len(a & b) / len(a | b)

char2 = {}
char3 = {}
word2 = {}

for name, content in docs.items():
    char2[name] = build_char_grams(content, 2)
    char3[name] = build_char_grams(content, 3)
    word2[name] = build_word_grams(content, 2)

print("\n----------------------------------")
print("Exact Jaccard Similarities")
print("----------------------------------")

doc_pairs = list(itertools.combinations(docs.keys(), 2))

print("\nCharacter 2-grams:")
for x, y in doc_pairs:
    score = jaccard_similarity(char2[x], char2[y])
    print(f"{x}-{y}: {score:.4f}")

print("\nCharacter 3-grams:")
for x, y in doc_pairs:
    score = jaccard_similarity(char3[x], char3[y])
    print(f"{x}-{y}: {score:.4f}")

print("\nWord 2-grams:")
for x, y in doc_pairs:
    score = jaccard_similarity(word2[x], word2[y])
    print(f"{x}-{y}: {score:.4f}")

print("\n----------------------------------")
print("MinHash Approximation (D1 vs D2)")
print("----------------------------------")

def create_hash_family(count, mod_value):
    family = []
    for _ in range(count):
        a = random.randint(1, mod_value)
        b = random.randint(0, mod_value)
        family.append((a, b))
    return family

def minhash_signature(gram_set, family, mod_value):
    signature = []
    for a, b in family:
        smallest = float("inf")
        for g in gram_set:
            value = (a * hash(g) + b) % mod_value
            if value < smallest:
                smallest = value
        signature.append(smallest)
    return signature

def signature_similarity(sig_a, sig_b):
    matches = sum(1 for i in range(len(sig_a)) if sig_a[i] == sig_b[i])
    return matches / len(sig_a)

d1_set = char3["D1"]
d2_set = char3["D2"]

true_value = jaccard_similarity(d1_set, d2_set)
print(f"\nExact Jaccard (3-gram): {true_value:.4f}")

hash_counts = [20, 60, 150, 300, 600]
mod_large = 10**9 + 7

for count in hash_counts:
    family = create_hash_family(count, mod_large)
    sig_a = minhash_signature(d1_set, family, mod_large)
    sig_b = minhash_signature(d2_set, family, mod_large)
    estimate = signature_similarity(sig_a, sig_b)
    print(f"t = {count} -> Estimated Jaccard: {estimate:.4f}")
