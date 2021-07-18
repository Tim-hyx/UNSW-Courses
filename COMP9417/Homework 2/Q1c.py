import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss, accuracy_score
from sklearn.model_selection import GridSearchCV, KFold

c_grid = []
i = 0.0001
while i <= 0.6:
    c_grid.append(round(i, 4))
    i += 0.006
# The data.csv is located in the desktop, so I hardcode the file name
df = pd.read_csv('C:/Users/TimHuang/Desktop/Q1.csv')
df_x = df.drop(['Y'], axis=1)
train_x = df_x[:500]
train_y = df[:500]['Y']
text_x = df_x[500:]
test_y = df[500:]['Y']
total_log_loss_list = []
for c in c_grid:
    cls = LogisticRegression(C=c, solver='liblinear', penalty="l1")
    log_loss_list = []
    i = 0
    while i < 10:
        fit_x = train_x.drop(labels=range(i * 50, (i + 1) * 50), axis=0)
        fit_y = train_y.drop(labels=range(i * 50, (i + 1) * 50), axis=0)
        cls.fit(fit_x, fit_y)
        log_loss_x = train_x[i * 50:(i + 1) * 50]
        log_loss_y = train_y[i * 50:(i + 1) * 50]
        pred_y = cls.predict_proba(log_loss_x)
        log_loss_list.append(log_loss(log_loss_y, pred_y))
        i += 1
    total_log_loss_list.append(log_loss_list)

param_grid = {'C': c_grid}
clf = GridSearchCV(estimator=LogisticRegression(penalty='l1', solver='liblinear'), cv=KFold(n_splits=10),
                   param_grid=param_grid,
                   scoring='neg_log_loss')
clf.fit(train_x, train_y)
predict_train = clf.predict(train_x)
predict_test = clf.predict(text_x)
train = accuracy_score(train_y, predict_train)
test = accuracy_score(test_y, predict_test)
print('The best C is ', clf.best_params_)
print('The train accuracy is', train)
print('The test accuracy is', test)
