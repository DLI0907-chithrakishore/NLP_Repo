import pandas as pd
import joblib
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from imblearn.over_sampling import SMOTE, ADASYN

# 1️⃣ Load Data
df = pd.read_csv("df_train_300.csv")

# 2️⃣ Encode Target Labels
label_encoder = LabelEncoder()
df["ncb_reason_encode"] = label_encoder.fit_transform(df["ncb_reason"])
joblib.dump(label_encoder, "label_encoder_300_svm.pkl")

# 3️⃣ Convert Text to TF-IDF Features
X = df["cleaned_data"]  # Independent variable (text)
y = df["ncb_reason_encode"]  # Target variable

tfidf = TfidfVectorizer(stop_words="english")  # max_features will be tuned
X_tfidf = tfidf.fit_transform(X.astype(str))

# Save TF-IDF model for future use
joblib.dump(tfidf, "tfidf_vectorizer_300_svm.pkl")

# 4️⃣ Split Data Before Oversampling
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42, stratify=y)

# 5️⃣ Apply SMOTE & ADASYN
smote = SMOTE(sampling_strategy="auto", random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

adasyn = ADASYN(random_state=42)
X_train_adasyn, y_train_adasyn = adasyn.fit_resample(X_train, y_train)

print("\nClass Distribution After SMOTE:\n", Counter(y_train_smote))
print("\nClass Distribution After ADASYN:\n", Counter(y_train_adasyn))

# 6️⃣ Hyperparameter Tuning using GridSearchCV
param_grid = {
    'tfidf__max_features': [3000, 5000, 7000, 10000],  # Tune TF-IDF features
    'svm__C': [0.1, 1, 10, 100],  # Regularization parameter
    'svm__gamma': ['scale', 'auto', 0.1, 1, 10],  # Kernel coefficient
    'svm__kernel': ['rbf']
}

from sklearn.pipeline import Pipeline

# Define pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words="english")),
    ('svm', SVC(probability=True))
])

# Perform Grid Search
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=2)
grid_search.fit(X_train_smote.astype(str), y_train_smote)

# Get Best Model
print("Best Parameters:", grid_search.best_params_)
best_model = grid_search.best_estimator_

# 7️⃣ Train Final Model with Best Parameters
best_model.fit(X_train_smote.astype(str), y_train_smote)

# Save trained model
joblib.dump(best_model, "svm_model_300.pkl")

# 8️⃣ Make Predictions & Evaluate Model
y_pred = best_model.predict(X_test.astype(str))

# Decode Labels
y_test_labels = label_encoder.inverse_transform(y_test)
y_pred_labels = label_encoder.inverse_transform(y_pred)

print("\nClassification Report:\n", classification_report(y_test_labels, y_pred_labels))
print("Model Accuracy:", accuracy_score(y_test_labels, y_pred_labels))

# 9️⃣ Plot Confusion Matrix
conf_matrix = confusion_matrix(y_test_labels, y_pred_labels)
class_labels = label_encoder.classes_

plt.figure(figsize=(4, 3))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=class_labels, yticklabels=class_labels)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
