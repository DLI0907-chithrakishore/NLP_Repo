print("Class distribution before resampling:", Counter(y_train))
Class distribution before resampling: Counter({3: 1600, 2: 1600, 1: 928, 4: 169, 0: 147})
# # 8️⃣ Train SVM Classifier  initially used
svm_model = SVC(kernel="rbf", C=1.0, gamma=0.1,class_weight ='balanced', probability=True)#gamma="scale"
svm_model.fit(X_train_smote, y_train_smote)


