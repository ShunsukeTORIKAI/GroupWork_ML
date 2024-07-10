import os
import sys
project_root_path = os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(project_root_path)
import my_library.Trainer as Trainer

preprocessed_train_data_path = "../data/train_preprocessed.pkl"  #input("Enter the path for the preprocessed data:")
model_dump_path_base = "../models"   #input("Enter the path for the directory to save the models:")

trainer = Trainer.Trainer()
X, y = trainer.load_data(preprocessed_train_data_path)

hyperparameters = [0.1, 0.5, 1, 5]
degrees = [1, 10, 100]
coef0s = [0.1, 1, 10, 100]

best_parameter = trainer.gridsearch_svm(hyperparameters, degrees, coef0s, X, y)
besthy, bestde, bestco = best_parameter["C"], best_parameter["degree"], best_parameter["coef0"]
trainer.train_SVM(besthy, bestde, bestco, X, y)
model_dump_path = os.path.join(model_dump_path_base , "SVM_"+str(besthy)+"_"+str(bestde)+"_"+str(bestco)+".pkl")
trainer.dump_model(model_dump_path)
"""
hyperparameters = [0.1,1,10,100,1000]
for h in hyperparameters:   #SVM
    model_dump_path = os.path.join(model_dump_path_base , "SVM_"+str(h)+".pkl")
    trainer.train_SVM(h, X, y)
    trainer.dump_model(model_dump_path)


for h in hyperparameters:   #ランフォレ
    model_dump_path = os.path.join(model_dump_path_base , "RF_"+str(h)+".pkl")
    trainer.train_RF(h, X, y)
    trainer.dump_model(model_dump_path)
"""