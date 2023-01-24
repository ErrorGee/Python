import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


def accuracy_score(real, predicted):
    """score=(y_true-y_pred)/len(y_true)"""
    print("this is the predicted {}".format(predicted))
    return round(float(sum(predicted == real)) / float(len(real))* 100,2)


def pre_processing(df):
    X = df.drop(df.columns[-1], axis=1)
    y = df[df.columns[-1]]

    return X,y

class NaiveBayes:
    """
    Posterior probability = (likelihoods*prior probability)/marginal probability
    """

    def __init__(self):

        # in here I just have to define the variables, initialization part can be done later.
        self.likelihoods = {}
        self.class_prior = {}
        self.pred_prior = {}  # these are the marginal probabilities
        self.features = []

        self. X_train = np.array
        self.y_train = np.array
        self.train_size = int

    def fit(self, X, y):
        #  here you can initialize the values
        self.features = list(X.columns)
        self.X_train = X
        self.y_train = y
        self.train_size = X.shape[0]

        for feature in np.unique(self.features):
            self.likelihoods[feature] = {}
            self.pred_prior[feature] = {}

            for feature_value in np.unique(self.X_train[feature]):
                self.pred_prior[feature].update({feature_value : 0})

                for outcome in np.unique(self.y_train):
                    self.likelihoods[feature].update({feature_value + "_" + outcome:0})
                    self.class_prior.update({outcome: 0})

        self._calc_class_prior()
        self._calc_likelihood()
        self._calc_pred_prior()

        # this is just for training the model
    def _calc_class_prior(self):
        for outcome in np.array(self.y_train):
            outcome_count = sum(self.y_train == outcome)
            self.class_prior[outcome] = outcome_count / self.train_size

    def _calc_likelihood(self):
        for feature in self.features:
            for outcome in np.unique(self.y_train):
                outcome_count = sum(self.y_train == outcome)
                feature_likelihood = self.X_train[feature][
                    self.y_train[self.y_train == outcome].index.values.tolist()].value_counts().to_dict()

                for feature_value, count in feature_likelihood.items():
                    self.likelihoods[feature][feature_value + "_" + outcome] = count/outcome_count
    def _calc_pred_prior(self):
        for feature in self.features:
            feature_val_count = self.X_train[feature].value_counts().to_dict()

            for feat_val, count in feature_val_count.items():
                self.pred_prior[feature][feat_val]=count /  self.train_size

    def predict(self, X):
            # now we have to pass the query of features in here so that our model predits the value.
        results = []
        X = np.array(X)
        for query in X:
            final_outcome = {}
            for outcome in np.unique(self.y_train):
                prior = self.class_prior[outcome]
                likelihood = 1
                evidence = 1

                for feature, feature_val in zip(self.features, query):
                    likelihood *=self.likelihoods[feature][feature_val + '_' + outcome]
                    evidence *= self.pred_prior[feature][feature_val]

                posterior_probability = (likelihood * prior) / evidence

                final_outcome[outcome] = posterior_probability

            result = max(final_outcome, key=lambda x: final_outcome[x])

            print("This is rsult {}".format(result))
            results.append(result)

        return np.array(results)

""" the following code snipped allows you to run the file when it is run as a script but not when it is imported as a module
"""
if __name__=="__main__":
    print("we have the weather dataset")

    df=pd.read_csv("weather.txt", sep=" ", header=0)

    # before fitting the data we need to preprocess it.
    X,y = pre_processing(df)
    NB=NaiveBayes()
    NB.fit(X,y)

    print("Train Accuracy: {}".format(accuracy_score(y, NB.predict(X))))

    # Query 1:
    query = np.array([['Rainy', 'Mild', 'Normal', 't']])
    print("Query 1:- {} ---> {}".format(query, NB.predict(query)))

    # Query 2:
    query = np.array([['Overcast', 'Cool', 'Normal', 't']])
    print("Query 2:- {} ---> {}".format(query, NB.predict(query)))
