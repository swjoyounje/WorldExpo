
from collections import Counter

nouns_counter = Counter(nouns)
nouns_counter.most_common(10)

r = str(r[1].values)
r = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", r)
r = okt.morphs(r, stem=True)
r = [word for word in r if not word in stopwords]
encoded = tokenizer.texts_to_sequences([r])
pad_new = pad_sequences(encoded, maxlen=max_len)
score = float(loaded_model.predict(pad_new))
if score > 0.5:
    emotion.append(1)
else:
    emotion.append(0)