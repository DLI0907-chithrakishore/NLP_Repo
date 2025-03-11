in.py

# 2️⃣ Convert text to features using TF-IDF
tfidf = TfidfVectorizer(max_features=5000, stop_words="english")
# X_tfidf = tfidf.fit_transform(X.astype(str)).toarray()
X_tfidf = tfidf.fit_transform(X)


