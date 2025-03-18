df = pd.read_csv("df_train_300.csv")
# cleaned_data       ncb_reason 

# Encode labels
label_encoder = LabelEncoder()
df["ncb_reason_encode"] = label_encoder.fit_transform(df["ncb_reason"])
 # Save LabelEncoder for future use
joblib.dump(label_encoder, "label_encoder_300_svm.pkl")

X = df["cleaned_data"]  # Independent variable (text)
y = df["ncb_reason_encode"]  # Target variable (encoded class)
# 2️⃣ Convert text to features using TF-IDF
tfidf = TfidfVectorizer(max_features=5000, stop_words="english")
#X_tfidf = tfidf.fit_transform(X.astype(str)).toarray()
X_tfidf = tfidf.fit_transform(X)

# Save TF-IDF model for future use
joblib.dump(tfidf, "tfidf_vectorizer_300_svm.pkl")

# 6️⃣ Split data before applying SMOTE
y = df["ncb_reason_encode"]
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42, stratify=y)

# 7️⃣ Apply SMOTE only on training data
smote = SMOTE(sampling_strategy="auto", random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

print("\nClass Distribution After SMOTE (Train Set Only):\n", Counter(y_train_resampled))

# 8️⃣ Train SVM Classifier
svm_model = SVC(kernel="rbf", C=1.0, gamma="scale", probability=True)
svm_model.fit(X_train_resampled, y_train_resampled)
# Save trained RandomForest model
joblib.dump(svm_model, "svm_model_300.pkl")

# 9️⃣ Make predictions
y_pred = svm_model.predict(X_test)

# 8️⃣ Evaluate Model
# Decode the labels back to original class names
y_test_labels = label_encoder.inverse_transform(y_test)
y_pred_labels = label_encoder.inverse_transform(y_pred)
print("\nClassification Report:\n", classification_report(y_test_labels, y_pred_labels))
print("Model Accuracy:", accuracy_score(y_test_labels, y_pred_labels))
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Compute confusion matrix
conf_matrix = confusion_matrix(y_test_labels, y_pred_labels)

# Get the class labels
class_labels = label_encoder.classes_

# Plot confusion matrix
plt.figure(figsize=(4, 3))  #plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=class_labels, yticklabels=class_labels)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()



