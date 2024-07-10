import os
import sys
project_root_path = os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(project_root_path)
import my_library.Trainer as Trainer

preprocessed_train_data_path = "../data/train_preprocessed.pkl"

trainer = Trainer.Trainer()
X, y = trainer.load_data(preprocessed_train_data_path)

hyperparameters = [0.1, 0.5, 1, 5]
degrees = [1, 10, 100]
coef0s = [0.1, 1, 10, 100]

trainer.gridsearch_svm(hyperparameters, degrees, coef0s, X, y)
