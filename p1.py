in.py


    def pred(self, model, le, text):

        # Transform the text data using the TF-IDF vectorizer
        transformed_text = self.vectorizer.transform([text])
        # transformed_text = self.vectorizer.transform([text]).toarray()

        # Predict the probabilities using svc model
        # predicted_probabilities = model.predict([text])
        predicted_probabilities = model.predict(transformed_text)

        # Get the index of the highest probability
        predicted_intent_index = np.argmax(predicted_probabilities)

        # Decode the predicted intent
        predicted_intent = le.inverse_transform([predicted_intent_index])
        # print("pred_num", predicted_intent_index)
        # print("pred_text", predicted_intent)
        return predicted_intent
I have to modify this code as while model building and testing I used:

# Load the preprocessing objects and model
label_encoder = joblib.load('label_encoder_300_svm.pkl')
tfidf = joblib.load('tfidf_vectorizer_300_svm.pkl')
svm_model = joblib.load('svm_model_300.pkl')

# Preprocess the test data
X_test = df_test["cleaned_data"]
X_test_tfidf = tfidf.transform(df_test['cleaned_data'])

label_encoder = LabelEncoder()
df_test["ncb_reason_encode"] = label_encoder.fit_transform(df_test["ncb_reason"])
y_test = df_test['ncb_reason_encode']

y_pred = svm_model.predict(X_test_tfidf)

# Decode the labels back to original class names
y_test_labels = label_encoder.inverse_transform(y_test)
y_pred_labels = label_encoder.inverse_transform(y_pred)

# 🔟 Evaluate Model
print("\nClassification Report:\n", classification_report(y_test_labels, y_pred_labels))
print("Model Accuracy:", accuracy_score(y_test_labels, y_pred_labels))
we avoid '
 # Get the index of the highest probability
        predicted_intent_index = np.argmax(predicted_probabilities)'
in model testing

def pred(self, model, le, text):
    # Transform the text data using the TF-IDF vectorizer
    transformed_text = self.vectorizer.transform([text])

    # Predict the class using the SVM model
    predicted_label = model.predict(transformed_text)

    # Decode the predicted label to its original class name
    predicted_intent = le.inverse_transform(predicted_label)

    return predicted_intent[0]  # Return as a string instead of a list
            
