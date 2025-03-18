print("Class distribution before resampling:", Counter(y_train))
Class distribution before resampling: Counter({3: 1600, 2: 1600, 1: 928, 4: 169, 0: 147})
# # 8️⃣ Train SVM Classifier  initially used
svm_model = SVC(kernel="rbf", C=1.0, gamma=0.1,class_weight ='balanced', probability=True)#gamma="scale"
svm_model.fit(X_train_smote, y_train_smote)

from imblearn.over_sampling import RandomOverSampler
from collections import Counter

# Define desired class distribution
desired_distribution = {3: 1600, 2: 1600, 1: 1600, 4: 1000, 0: 1000}

# Initialize RandomOverSampler
ros = RandomOverSampler(sampling_strategy=desired_distribution, random_state=42)

# Resample the dataset
X_train_resampled, y_train_resampled = ros.fit_resample(X_train, y_train)

# Print new class distribution
print("Class distribution after upsampling:", Counter(y_train_resampled))



