import pandas as pd
import joblib
from collections import Counter
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import SMOTE, ADASYN
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load Dataset
df = pd.read_csv("df_train_300.csv")

# 2️⃣ Encode labels
label_encoder = LabelEncoder()
df["ncb_reason_encode"] = label_encoder.fit_transform(df["ncb_reason"])

# Save LabelEncoder for future use
joblib.dump(label_encoder, "label_encoder_300_svm.pkl")

# 3️⃣ Convert text to features using TF-IDF
X = df["cleaned_data"]
y = df["ncb_reason_encode"]

tfidf = TfidfVectorizer(max_features=5000, stop_words="english")
X_tfidf = tfidf.fit_transform(X)

# Save TF-IDF model
joblib.dump(tfidf, "tfidf_vectorizer_300_svm.pkl")

# 4️⃣ Split data before applying SMOTE/ADASYN
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42, stratify=y)

print("Class distribution before resampling:", Counter(y_train))

# 5️⃣ Apply SMOTE and ADASYN separately for comparison
smote = SMOTE(random_state=42)
adasyn = ADASYN(random_state=42)

X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)
X_train_adasyn, y_train_adasyn = adasyn.fit_resample(X_train, y_train)

print("\nClass distribution after SMOTE:", Counter(y_train_smote))
print("Class distribution after ADASYN:", Counter(y_train_adasyn))

# 6️⃣ Hyperparameter Tuning with GridSearchCV
param_grid = {
    "C": [0.1, 1, 10, 100],  # Regularization parameter
    "gamma": ["scale", "auto", 0.1, 1, 10],  # Kernel coefficient
    "kernel": ["rbf"]
}

# Initialize SVM
svm = SVC(probability=True)

# GridSearch on SMOTE data
grid_search_smote = GridSearchCV(svm, param_grid, cv=5, scoring="accuracy", n_jobs=-1)
grid_search_smote.fit(X_train_smote, y_train_smote)

# GridSearch on ADASYN data
grid_search_adasyn = GridSearchCV(svm, param_grid, cv=5, scoring="accuracy", n_jobs=-1)
grid_search_adasyn.fit(X_train_adasyn, y_train_adasyn)

# Best model selection
best_model_smote = grid_search_smote.best_estimator_
best_model_adasyn = grid_search_adasyn.best_estimator_

print("\nBest Parameters (SMOTE):", grid_search_smote.best_params_)
print("\nBest Parameters (ADASYN):", grid_search_adasyn.best_params_)

# 7️⃣ Train Best SVM Model (Choose between SMOTE & ADASYN)
final_model = best_model_smote  # Change to best_model_adasyn if ADASYN performs better
final_model.fit(X_train_smote, y_train_smote)

# Save the trained model
joblib.dump(final_model, "svm_model_300.pkl")

# 8️⃣ Predictions
y_pred = final_model.predict(X_test)

# 9️⃣ Evaluation
y_test_labels = label_encoder.inverse_transform(y_test)
y_pred_labels = label_encoder.inverse_transform(y_pred)

print("\nClassification Report:\n", classification_report(y_test_labels, y_pred_labels))
print("Model Accuracy:", accuracy_score(y_test_labels, y_pred_labels))

#  🔟 Confusion Matrix
conf_matrix = confusion_matrix(y_test_labels, y_pred_labels)
class_labels = label_encoder.classes_

plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=class_labels, yticklabels=class_labels)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()



#
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

# Define parameter grid for TF-IDF and SVM
param_grid = {
    'tfidf__max_features': [3000, 5000, 7000, 10000],  # Vary feature size
    'svm__C': [0.1, 1, 10, 100],  # Regularization parameter
    'svm__gamma': ['scale', 'auto', 0.1, 1, 10],  # Kernel coefficient
    'svm__kernel': ['rbf']
}

# Define pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words="english")),
    ('svm', SVC(probability=True))
])

# Perform Grid Search
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=2)
grid_search.fit(X.astype(str), y)

# Get best parameters
print("Best Parameters:", grid_search.best_params_)
best_model = grid_search.best_estimator_

# Evaluate performance
y_pred = best_model.predict(X_test.astype(str))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Model Accuracy:", accuracy_score(y_test, y_pred))
