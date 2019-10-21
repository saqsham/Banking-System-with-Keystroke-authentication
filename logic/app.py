import csv
import os
import importlib.util
import datetime 
import importlib
import pandas as pd
from sklearn.svm import OneClassSVM
import numpy as np
np.set_printoptions(suppress=True)
from sklearn.metrics import roc_curve

r1 = open("F:\\me lazy\\keystroke-dynamics\\src\\user.csv") # Here your csv file
r=csv.reader(r1)
lines = list(r)
lines[0][0] = tempvalue
writer1 = open("F:\\me lazy\\keystroke-dynamics\\src\\user.csv", 'w')
writer=csv.writer(writer1)
writer.writerows(lines)
writer1.close()
r1.close()
r1=open("F:\\me lazy\\keystroke-dynamics\\src\\user.csv")
fout=open("F:\\me lazy\\keystroke-dynamics\\src\\user.csv\\keystroke.dataset.csv","a")
for line in r1:
        fout.write(line)
fout.close()

def evaluateEER(user_scores, imposter_scores):
    labels = [0] * len(user_scores) + [1] * len(imposter_scores)
    fpr, tpr, thresholds = roc_curve(labels, user_scores + imposter_scores)
    missrates = 1 - tpr
    farates = fpr
    dists = missrates - farates
    idx1 = np.argmin(dists[dists >= 0])
    idx2 = np.argmax(dists[dists < 0])
    x = [missrates[idx1], farates[idx1]]
    y = [missrates[idx2], farates[idx2]]
    a = (x[0] - x[1]) / (y[1] - x[1] - y[0] + x[0])
    eer = x[0] + a * (y[0] - x[0])
    return eer

class SVMDetector:
        # just the training() function changes, rest all remains same.

    def __init__(self, subjects):
        self.u_scores = []
        self.i_scores = []
        self.mean_vector = []
        self.subjects = subjects

    def training(self):
        self.clf = OneClassSVM(kernel='rbf', gamma=26)
        self.clf.fit(self.train)

    def testing(self):
        self.u_scores = -self.clf.decision_function(self.test_genuine)
        self.i_scores = -self.clf.decision_function(self.test_imposter)
        self.u_scores = list(self.u_scores)
        self.i_scores = list(self.i_scores)

    def evaluate(self):
        eers = []

        for subject in subjects:
                genuine_user_data = data.loc[data.subject == tempvalue,"H.period":"UD.l.Return"]

                imposter_data = data.loc[data.subject != tempvalue, :]

                self.train = genuine_user_data[-1:]
                self.test_genuine = genuine_user_data[:20]
                self.test_imposter = imposter_data.groupby("subject"). \
                                         head(20).loc[:, "H.period":"UD.l.Return"]

                self.training()
                self.testing()
                eers.append(evaluateEER(self.u_scores, \
                                        self.i_scores))
                break
        return np.mean(eers)

path = "C:/Users/Dell/Desktop/Software Implem/credit/Trial_fromt end/src/keystroke.dataset.csv"
data = pd.read_csv(path)
subjects = data["subject"].unique()
print(SVMDetector(subjects).evaluate())
if(SVMDetector(subjects).evaluate()<0.4 and SVMDetector(subjects).evaluate()>0.18):
    return render_template('clienthome.html', message=message if message is not None else None)
else :
    return render_template('index.html',message=message if message is not None else None)


def redirect_reg_captcha(message=None):
    import csv
    import pandas as pd
    from sklearn.svm import OneClassSVM
    import numpy as np
    np.set_printoptions(suppress=True)

    r1 = open('C:/Path-to-your-file/user.csv')  # Here your csv file
    r = csv.reader(r1)
    lines = list(r)
    for i in range(20):
        lines[i][0] = tempvalue_reg
    writer1 = open('C:/Path-to-your-file/user.csv', 'w')
    writer = csv.writer(writer1)
    writer.writerows(lines)
    writer1.close()
    r1.close()
    r1 = open("C:/Path-to-your-file/user.csv")
    fout = open("C:/Path-to-your-file/keystroke.dataset.csv", "a")
    for line in r1:
        fout.write(line)
    fout.close()

    return render_template('index.html',message=message if message is not None else None)
