import sklearn.svm as SVM
import sklearn.ensemble as Ensemble
from sklearn.model_selection import GridSearchCV
import pickle
import numpy

class Trainer:
    def __init__(self):
        """
        Trainerクラスのコンストラクタ。
        """
        self.model = None  # モデルを格納するインスタンス変数を初期化
    def load_data(self, file_path):
        """
        データセットのファイルパスからデータを読み込み、特徴量とラベルを分けて返す。
        Args:
            file_path (str): データセットのファイルパス

        Returns:
            X (numpy.ndarray): 前処理済みの訓練データ
            y (numpy.ndarray): ラベルデータ
        """        
        with open(file_path, 'rb') as f:
            X, y = pickle.load(f)        
        return X, y
        
    def dump_model(self, file_path):
        """
        学習したモデルを指定されたファイルパスに保存する。
        Args:
            file_path (str): モデルを保存するファイルパス
        """ 
        with open(file_path, 'wb') as f:
            pickle.dump(self.model, f)

    def train_SVM(self, hyperparameter, degreeh, coef0h, X, y):
        """
        SVMによる学習をおこなう。正則化パラメータの値を指定する
        Args:
            hyperparameter(float): 正則化パラメータの値
            degreeh(int): 多項式カーネルの次数
            coef0h(int): 高次多項式と低次多項式からどの程度の影響を認めるかのパラメータ
            X (numpy.ndarray): 前処理済みの訓練データ
            y (numpy.ndarray): ラベルデータ
        """     
        self.model = Pipeline([
            ("scaler", StandardScaler()),
            ("svm_clf", SVM(kernel="poly", degree = degreeh, coef0 = coef0h, C = hyperparameter))
        ])
        self.model.fit(X,y)
    
    def gridsearch_svm(self, hyperparameter_list, degree_list, coef0_list, X, y):
        param_grid = [
            {"degree": degree_list, "coef0": coef0_list, "C": hyperparameter_list},
        ]
        svm_cls = SVM.SVC()
        grid_search = GridSearchCV(svm_cls, param_grid, cv=3, return_train_score=True)
        grid_search.fit(X, y)
        cvres = grid_search.cv_results_
        for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
            print(mean_score, params)

    def train_RF(self, hyperparameter, X, y):
        """
        RandomForestによる学習をおこなう。各決定木の最大深さを指定する
        Args:
            hyperparameter(float): 最大深さの値
            X (numpy.ndarray): 前処理済みの訓練データ
            y (numpy.ndarray): ラベルデータ
        """     
        self.model = Ensemble.RandomForestClassifier(max_depth=hyperparameter)
        self.model.fit(X,y)