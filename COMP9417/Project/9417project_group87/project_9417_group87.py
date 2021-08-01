import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import median_absolute_error
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
import xgboost as xgb
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from lightgbm import LGBMRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
import warnings

warnings.filterwarnings("ignore")
df_train = pd.read_csv('./train.csv')
df_test = pd.read_csv('./test.csv')
df_sup=pd.read_csv('./Countries_usefulFeatures.csv')
feature_types = df_train.dtypes.value_counts()
feature_types.plot.pie(autopct='%1.1f%%')
plt.title('Proportion of Features')
missing_data = df_train.isnull().sum()
missing_proportion = df_train.isnull().sum() / df_train.shape[0] * 100
#check miss data
missing_dict = {'missing data': missing_data, 'missing proportion * 100%': missing_proportion}
df_missing = pd.DataFrame(missing_dict)
df_missing = pd.DataFrame(data=df_missing.values.T, columns=df_missing.index, index=df_missing.columns)
# deal with missing data(null values),if the province is null ,using country to fill it,if county is null, using province to fill it
# country->province->county
df_train['Province_State'][df_train['Province_State'].isnull()] = \
    df_train['Country_Region'][df_train['Province_State'].isnull()]
df_train['County'][df_train['County'].isnull()] = \
    df_train['Province_State'][df_train['County'].isnull()]
# check missing data again
missing_data_2 = df_train.isnull().sum()
#diff days means the days of Date  to the last day(6-10)
df_train['Date'] = pd.to_datetime(df_train['Date'])
df_train['Diff_Days'] = df_train['Date'].apply(lambda x: x - df_train.loc[0,'Date'])
df_train['Diff_Days'] = df_train['Diff_Days'].apply(lambda x: int(str(x).replace(' days 00:00:00', '')))
# remove the - in date
df_train['Date'] = df_train['Date'].apply(lambda x: int(str(x).rstrip(' 00:00:00').replace('-', '')))
# add Avg_Population_by_County feature
#
count_county_dict = df_train['County'].value_counts().to_dict()
df_train['Count_County'] = df_train['County'].apply(lambda x: count_county_dict[x])
df_train['Avg_Population_by_County'] = df_train.apply(lambda x: x['Population'] / x['Count_County'], axis=1)
#merge the supplment dataset
df_train=df_train.merge(df_sup[['Country_Region','Tourism','Latitude','Longtitude','Mean_Age','Lockdown_Date','Lockdown_Type']], on='Country_Region', how='inner', sort=False)
# using labelcoder to give County，Province_State，Country_Region，Target labels
le = LabelEncoder()
encoder= le.fit(df_train["Country_Region"])
df_train["Country_Region"] = encoder.transform(df_train["Country_Region"])
encoder= le.fit(df_train["Province_State"])
df_train["Province_State"] = encoder.transform(df_train["Province_State"])
encoder= le.fit(df_train["County"])
df_train["County"] = encoder.transform(df_train["County"])
encoder= le.fit(df_train["Target"])
df_train["Target"] = encoder.transform(df_train["Target"])
##give lockdown type labels
df_train=df_train.replace(np.nan,"None")
encoder= le.fit(df_train["Lockdown_Type"])
df_train["Lockdown_Type"] = encoder.transform(df_train["Lockdown_Type"])   #2 is partial 0 is full 1 is none
#Calculates the duration of the lockdown
df_train=df_train.replace("None","2020-06-10")
df_train['Lockdown_Date'] = pd.to_datetime(df_train['Lockdown_Date'])
df_train['Lockdown_Days'] = df_train['Lockdown_Date'].apply(lambda x: pd.to_datetime("2020-06-10")-x)
df_train['Lockdown_Days'] = df_train['Lockdown_Days'].apply(lambda x: int(str(x).replace(' days 00:00:00', '')))
# change the Lockdown_Date type
df_train['Lockdown_Date'] = df_train['Lockdown_Date'].apply(lambda x: int(str(x).rstrip(' 00:00:00').replace('-', '')))
#separate the whole dataset to 2 sub-dataset(confirmcase and fatalities)
df_train_confirmcase=df_train[df_train['Target']==0].reset_index(drop=True)
df_train_fatalities=df_train[df_train['Target']==1].reset_index(drop=True)
corr = df_train.corr()  #get the corr
corr
sns.heatmap(corr, square=True)  #draw the heatmap
#drop some useless feature through the corr
df_train_confirmcase=df_train_confirmcase.drop(["Id",'Population',"Target"],axis=1)
df_train_fatalities=df_train_fatalities.drop(["Id",'Population',"Target"],axis=1)
#new corr
new_corr = df_train_confirmcase.corr()
new_corr
#new heat map
sns.heatmap(new_corr, square=True)
#get the data and label
df_train_confirmcase_x=df_train_confirmcase.drop(['TargetValue'],axis=1)
df_train_confirmcase_y=df_train_confirmcase['TargetValue']
df_train_fatalities_x=df_train_fatalities.drop(['TargetValue',"Latitude","Longtitude"],axis=1)
df_train_fatalities_y=df_train_fatalities['TargetValue']
#using the train_test_split to separate the dataset (80%for train 20%for test)
train_x_confirmcase, test_x_confirmcase, train_y_confirmcase, test_y_confirmcase = train_test_split(df_train_confirmcase_x, df_train_confirmcase_y, test_size=0.8, random_state=1)
train_x_fatalities, test_x_fatalities, train_y_fatalities, test_y_fatalities = train_test_split(df_train_confirmcase_x, df_train_confirmcase_y, test_size=0.8, random_state=1)
#linear regression for confirmcase
lr_model = LinearRegression()
lr_model.fit(train_x_confirmcase, train_y_confirmcase)
lr_predict = lr_model.predict(test_x_confirmcase)
lr_r2_score = r2_score(test_y_confirmcase, lr_predict)
MAE_lr = metrics.mean_absolute_error(test_y_confirmcase, lr_predict)
medianAE_lr=metrics.median_absolute_error(test_y_confirmcase, lr_predict)
print("mean_absolute_error(linear regression for confirmcase) is",MAE_lr)
print("median_absolute_error(linear regression for confirmcase) is",medianAE_lr)
print("r2 score(linear regression for confirmcase) is",lr_r2_score)
print("--------------------------------------------------------------")
#knn for confirmcase
#param_grid = [{'weights':['uniform'],
#               'n_neighbors':[k for k in range(1,8)],
#                },
#              {'weights':['distance'],
#               'n_neighbors':[k for k in range(1,8)],
#               }
#              ]
knn= KNeighborsRegressor(n_neighbors=10,weights="distance")
#grid_search = GridSearchCV(knn,param_grid=param_grid)
#grid_search.fit(train_x,train_y)
#knn = grid_search.best_estimator_
#best_param=grid_lr.best_params_
knn.fit(train_x_confirmcase,train_y_confirmcase)
knn_predict=knn.predict(test_x_confirmcase)
MAE_knn_confirmcase=metrics.mean_absolute_error(test_y_confirmcase, knn_predict)
medianAE_knn_confirmcase=metrics.median_absolute_error(test_y_confirmcase, knn_predict)
knn_r2_score_confirmcase=r2_score(test_y_confirmcase, knn_predict)
print("mean_absolute_error(Knn for confirmcase) is",MAE_knn_confirmcase)
print("median_absolute_error(Knn for confirmcase) is",medianAE_knn_confirmcase)
print("r2 score(Knn for confirmcase) is",knn_r2_score_confirmcase)
print("--------------------------------------------------------------")
#randomforest for confirmcase
rf_reg=RandomForestRegressor(n_estimators=100,min_samples_leaf=2,min_samples_split=3)
rf_reg.fit(train_x_confirmcase,train_y_confirmcase)
rf_reg_predict=rf_reg.predict(test_x_confirmcase)
MAE_rf_reg_confirmcase=metrics.mean_absolute_error(test_y_confirmcase, rf_reg_predict)
medianAE_rf_reg_confirmcase=metrics.median_absolute_error(test_y_confirmcase, rf_reg_predict)
rf_reg_r2_score_confirmcase=r2_score(test_y_confirmcase, rf_reg_predict)
print("mean_absolute_error(randomforest for confirmcase) is",MAE_rf_reg_confirmcase)
print("median_absolute_error(randomforest for confirmcase) is",medianAE_rf_reg_confirmcase)
print("r2 score(randomforest for confirmcase) is",rf_reg_r2_score_confirmcase)
print("--------------------------------------------------------------")
#xgboost for confirmcase
xgb_model = xgb.XGBRegressor(colsample_bylevel=0.9, subsample=0.7, max_depth=5, min_child_weight=1, alpha=20)
xgb_model.fit(train_x_confirmcase, train_y_confirmcase)
xgb_predict=xgb_model.predict(test_x_confirmcase)
MAE_xbg=metrics.mean_absolute_error(test_y_confirmcase, xgb_predict)
medianAE_xgb=metrics.median_absolute_error(test_y_confirmcase, xgb_predict)
xgb_r2_score=r2_score(test_y_confirmcase, xgb_predict)
print("mean_absolute_error(xgboost for confirmcase) is",MAE_xbg)
print("median_absolute_error(xgboost for confirmcase) is",medianAE_xgb)      #接近0好
print("r2 score(randomforest for confirmcase) is",xgb_r2_score)  #接近0好
print("--------------------------------------------------------------")
#GBR for confirmcase
gbr = GradientBoostingRegressor(learning_rate=0.5, n_estimators=100, subsample=1.0, min_samples_split=2,
                                min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_depth=3,
                                min_impurity_decrease=0.0, alpha=0.9)
gbr.fit(train_x_confirmcase, train_y_confirmcase)
gbr_predict = gbr.predict(test_x_confirmcase)
MAE_gbr_confirmcase = metrics.mean_absolute_error(test_y_confirmcase, gbr_predict)
medianAE_gbrp_confirmcase = metrics.median_absolute_error(test_y_confirmcase, gbr_predict)
gbr_r2_score_confirmcase = r2_score(test_y_confirmcase, gbr_predict)
print("mean_absolute_error(GBR for confirmcase) is", MAE_gbr_confirmcase)
print("median_absolute_error(GBR for confirmcase) is", medianAE_gbrp_confirmcase)
print("r2 score(GBR for confirmcase) is", gbr_r2_score_confirmcase)
print("--------------------------------------------------------------")
#mlp for confirmcase
mlp = MLPRegressor(hidden_layer_sizes=10, activation='relu', solver='adam', alpha=0.001, batch_size='auto',
                    learning_rate='constant', learning_rate_init=0.001, power_t=0.5, max_iter=200, tol=1e-4)
mlp.fit(train_x_confirmcase, train_y_confirmcase)
mlp_predict = mlp.predict(test_x_confirmcase)
MAE_mlp_confirmcase = metrics.mean_absolute_error(test_y_confirmcase, mlp_predict)
medianAE_mlp_confirmcase = metrics.median_absolute_error(test_y_confirmcase, mlp_predict)
mlp_r2_score_confirmcase = r2_score(test_y_confirmcase, mlp_predict)
print("mean_absolute_error(MLP for confirmcase) is", MAE_mlp_confirmcase)
print("median_absolute_error(MLP for confirmcase) is", medianAE_mlp_confirmcase)
print("r2 score(MLP for confirmcase) is", mlp_r2_score_confirmcase)
print("--------------------------------------------------------------")
#decision tree for confirmcase
DecisionTree = DecisionTreeRegressor(criterion='mse', min_samples_split = 5, min_samples_leaf = 2, max_depth=75)
DecisionTree.fit(train_x_confirmcase, train_y_confirmcase)
DecisionTree_predict = DecisionTree.predict(test_x_confirmcase)
DecisionTree_r2_score = r2_score(test_y_confirmcase, DecisionTree_predict)
MAE_Decision = metrics.mean_absolute_error(test_y_confirmcase, DecisionTree_predict)
medianAE_dt_confirmcase = metrics.median_absolute_error(test_y_confirmcase, DecisionTree_predict)
print("mean_absolute_error(DT for confirmcase) is", MAE_Decision)
print("median_absolute_error(DT for confirmcase) is", medianAE_dt_confirmcase)
print("r2 score(DT for confirmcase) is", DecisionTree_r2_score)
print("--------------------------------------------------------------")
#lgbm for confirmcase
lgbm = LGBMRegressor(n_estimators=1500,max_depth=50,learning_rate=0.1,num_leaves=32)
lgbm.fit(train_x_confirmcase,train_y_confirmcase)
lgbm_predict = lgbm.predict(test_x_confirmcase)
lgbm_r2_score = r2_score(test_y_confirmcase, lgbm_predict)
MAE_lgbm = metrics.mean_absolute_error(test_y_confirmcase, lgbm_predict)
medianAE_lgbm_confirmcase = metrics.median_absolute_error(test_y_confirmcase, lgbm_predict)
print("mean_absolute_error(lgbm for confirmcase) is", MAE_lgbm)
print("median_absolute_error(lgbm for confirmcase) is", medianAE_lgbm_confirmcase)
print("r2 score(lgbm for confirmcase) is", lgbm_r2_score)
print("--------------------------------------------------------------")
#ABR for confirmcase
regr = AdaBoostRegressor(random_state=0, n_estimators=50)
regr.fit(train_x_confirmcase,train_y_confirmcase)
regr_predict = regr.predict(test_x_confirmcase)
regr_r2_score = r2_score(test_y_confirmcase, regr_predict)
MAE_regr = metrics.mean_absolute_error(test_y_confirmcase, regr_predict)
medianAE_regr_confirmcase = metrics.median_absolute_error(test_y_confirmcase, regr_predict)
print("mean_absolute_error(regr for confirmcase) is", MAE_regr)
print("median_absolute_error(regr for confirmcase) is", medianAE_regr_confirmcase)
print("r2 score(regr for confirmcase) is", regr_r2_score)
print("--------------------------------------------------------------")
#linear regression for fatalities
lr_model = LinearRegression()
lr_model.fit(train_x_fatalities, train_y_fatalities)
lr_predict = lr_model.predict(test_x_fatalities)
lr_r2_score = r2_score(test_y_fatalities, lr_predict)
MAE_lr = metrics.mean_absolute_error(test_y_fatalities, lr_predict)
medianAE_lr=metrics.median_absolute_error(test_y_fatalities, lr_predict)
print("mean_absolute_error(linear regression for fatalities) is",MAE_lr)
print("median_absolute_error(linear regression for fatalities) is",medianAE_lr)
print("r2 score(linear regression for fatalities) is",lr_r2_score)
print("--------------------------------------------------------------")
#knn for fatalities
knn= KNeighborsRegressor(n_neighbors=5,weights="distance")
knn.fit(train_x_fatalities,train_y_fatalities)
knn_predict=knn.predict(test_x_fatalities)
MAE_knn_fatalities=metrics.mean_absolute_error(test_y_fatalities, knn_predict)
medianAE_knn_fatalities=metrics.median_absolute_error(test_y_fatalities, knn_predict)
knn_r2_score_fatalities=r2_score(test_y_fatalities, knn_predict)
print("mean_absolute_error(Knn for fatalities) is",MAE_knn_fatalities)
print("median_absolute_error(Knn for fatalities) is",medianAE_knn_fatalities)
print("r2 score(Knn for fatalities) is",knn_r2_score_fatalities)
print("--------------------------------------------------------------")
##randomforest for fatalities
rf_reg=RandomForestRegressor(n_estimators=100,min_samples_leaf=1,min_samples_split=2)
rf_reg.fit(train_x_fatalities,train_y_fatalities)
rf_reg_predict=rf_reg.predict(test_x_fatalities)
MAE_rf_reg_fatalities=metrics.mean_absolute_error(test_y_fatalities, rf_reg_predict)
medianAE_rf_reg_fatalities=metrics.median_absolute_error(test_y_fatalities, rf_reg_predict)
rf_reg_r2_score_fatalities=r2_score(test_y_fatalities, rf_reg_predict)
print("mean_absolute_error(randomforest for fatalities) is",MAE_rf_reg_fatalities)
print("median_absolute_error(randomforest for fatalities) is",medianAE_rf_reg_fatalities)
print("r2 score(randomforest for fatalities) is",rf_reg_r2_score_fatalities)
print("--------------------------------------------------------------")
##xgboost for fatalities
xgb_model = xgb.XGBRegressor(colsample_bylevel=0.9, subsample=0.7, max_depth=5, min_child_weight=1, alpha=20)
xgb_model.fit(train_x_fatalities, train_y_fatalities)
xgb_predict=xgb_model.predict(test_x_fatalities)
MAE_xbg=metrics.mean_absolute_error(test_y_fatalities, xgb_predict)
medianAE_xgb=metrics.median_absolute_error(test_y_fatalities, xgb_predict)
xgb_r2_score=r2_score(test_y_fatalities, xgb_predict)
print("mean_absolute_error(xgboost for fatalities) is",MAE_xbg)
print("median_absolute_error(xgboost for fatalities) is",medianAE_xgb)      #接近0好
print("r2 score(randomforest for fatalities) is",xgb_r2_score)  #接近0好
print("--------------------------------------------------------------")
#GBR for fatalities
gbr = GradientBoostingRegressor(learning_rate=0.5, n_estimators=100, subsample=1.0, min_samples_split=2,
                                min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_depth=3,
                                min_impurity_decrease=0.0, alpha=0.9)
gbr.fit(train_x_fatalities, train_y_fatalities)
gbr_predict = gbr.predict(test_x_fatalities)
MAE_gbr_confirmcase = metrics.mean_absolute_error(test_y_fatalities, gbr_predict)
medianAE_gbr_confirmcase = metrics.median_absolute_error(test_y_fatalities, gbr_predict)
gbr_r2_score_confirmcase = r2_score(test_y_fatalities, gbr_predict)
print("mean_absolute_error(GBR for confirmcase) is", MAE_gbr_confirmcase)
print("median_absolute_error(GBR for confirmcase) is", medianAE_gbrp_confirmcase)
print("r2 score(GBR for confirmcase) is", gbr_r2_score_confirmcase)
print("--------------------------------------------------------------")
#mlp for falities
mlp = MLPRegressor(hidden_layer_sizes=10, activation='relu', solver='adam', alpha=0.001, batch_size='auto',
                    learning_rate='constant', learning_rate_init=0.001, power_t=0.5, max_iter=200, tol=1e-4)
mlp.fit(train_x_fatalities, train_y_fatalities)
mlp_predict = mlp.predict(test_x_fatalities)
MAE_mlp_confirmcase = metrics.mean_absolute_error(test_y_fatalities, mlp_predict)
medianAE_mlp_confirmcase = metrics.median_absolute_error(test_y_fatalities, mlp_predict)
mlp_r2_score_confirmcase = r2_score(test_y_fatalities, mlp_predict)
print("mean_absolute_error(MLP for fatalities) is", MAE_mlp_confirmcase)
print("median_absolute_error(MLP for fatalities) is", medianAE_mlp_confirmcase)
print("r2 score(MLP for fatalities) is", mlp_r2_score_confirmcase)
print("--------------------------------------------------------------")
#decision tree for fatalities
DecisionTree = DecisionTreeRegressor(criterion='mse', min_samples_split = 5, min_samples_leaf = 2, max_depth=75)
DecisionTree.fit(train_x_fatalities, train_y_fatalities)
DecisionTree_predict = DecisionTree.predict(test_x_fatalities)
DecisionTree_r2_score = r2_score(test_y_fatalities, DecisionTree_predict)
MAE_Decision = metrics.mean_absolute_error(test_y_fatalities, DecisionTree_predict)
medianAE_dt_confirmcase = metrics.median_absolute_error(test_y_fatalities, DecisionTree_predict)
print("mean_absolute_error(DT for fatalities) is", MAE_Decision)
print("median_absolute_error(DT for fatalities) is", medianAE_dt_confirmcase)
print("r2 score(DT for fatalities) is", DecisionTree_r2_score)
print("--------------------------------------------------------------")
#lgbm for fatalities
lgbm = LGBMRegressor(n_estimators=1500,max_depth=50,learning_rate=0.1,num_leaves=32)
lgbm.fit(train_x_fatalities,train_y_fatalities)
lgbm_predict = lgbm.predict(test_x_fatalities)
lgbm_r2_score = r2_score(test_y_fatalities, lgbm_predict)
MAE_lgbm = metrics.mean_absolute_error(test_y_fatalities, lgbm_predict)
medianAE_lgbm_fatalities = metrics.median_absolute_error(test_y_fatalities, lgbm_predict)
print("mean_absolute_error(lgbm for fatalities) is", MAE_lgbm)
print("median_absolute_error(lgbm for fatalities) is", medianAE_lgbm_fatalities)
print("r2 score(lgbm for fatalities) is", lgbm_r2_score)
print("--------------------------------------------------------------")
#ABR for fatalities
regr = AdaBoostRegressor(random_state=0, n_estimators=50)
regr.fit(train_x_fatalities,train_y_fatalities)
regr_predict = regr.predict(test_x_fatalities)
regr_r2_score = r2_score(test_y_fatalities, regr_predict)
MAE_regr = metrics.mean_absolute_error(test_y_fatalities, regr_predict)
medianAE_regr_fatalities = metrics.median_absolute_error(test_y_fatalities, regr_predict)
print("mean_absolute_error(regr for fatalities) is", MAE_regr)
print("median_absolute_error(regr for fatalities) is", medianAE_regr_fatalities)
print("r2 score(regr for fatalities) is", regr_r2_score)
print("--------------------------------------------------------------")

###draw the bar picture
MAE_list=[MAE_lr,MAE_knn_confirmcase,MAE_rf_reg_confirmcase,MAE_xbg,MAE_gbr_confirmcase,MAE_Decision,MAE_lgbm,MAE_regr]
medianAe_list=[medianAE_lr,medianAE_knn_confirmcase,medianAE_rf_reg_confirmcase,medianAE_xgb,medianAE_gbrp_confirmcase,medianAE_dt_confirmcase,medianAE_lgbm_confirmcase,medianAE_regr_confirmcase]
r2_score_list=[lr_r2_score,knn_r2_score_confirmcase,rf_reg_r2_score_confirmcase,xgb_r2_score,gbr_r2_score_confirmcase,DecisionTree_r2_score,lgbm_r2_score,regr_r2_score]
model=("LR","knn","RF","XGB","gbr","DT","lgbm","AdaR")
plt.bar(model, MAE_list)
plt.title("mean_absolute_error of different models")
for a, b in zip(model, MAE_list):
    plt.text(a, b, round(b,2), ha='center', va='bottom')
plt.bar(model, medianAe_list)
plt.title("median_absolute_error of different models")
for a, b in zip(model, medianAe_list):
    plt.text(a, b, round(b, 2), ha='center', va='bottom')
plt.bar(model, r2_score_list)
plt.title("r2 score of different models")
for a, b in zip(model, r2_score_list):
    plt.text(a, b, round(b,2), ha='center', va='bottom')

######this part is some examples cod for tuning(decision tree)

min_samples_leaf_list = range(1,30,3)
DecisionTree_r2_score_list = []
MAE_Decision_list = []
medianAE_dt_confirmcase_list=[]

for item in min_samples_leaf_list:
    DecisionTree = DecisionTreeRegressor(min_samples_leaf = item)
    DecisionTree.fit(train_x_confirmcase, train_y_confirmcase)
    DecisionTree_predict = DecisionTree.predict(test_x_confirmcase)
    DecisionTree_r2_score = r2_score(test_y_confirmcase, DecisionTree_predict)
    MAE_Decision = metrics.mean_absolute_error(test_y_confirmcase, DecisionTree_predict)
    medianAE_dt_confirmcase = metrics.median_absolute_error(test_y_confirmcase, DecisionTree_predict)
    DecisionTree_r2_score_list.append(DecisionTree_r2_score)
    MAE_Decision_list.append(MAE_Decision)
    medianAE_dt_confirmcase_list.append(medianAE_dt_confirmcase)

# color = ['red','brown', 'green']
# label = ['r2_score','MAE','AE']
# DTres = [pd.DataFrame(DecisionTree_r2_score_list),pd.DataFrame(MAE_Decision_list),pd.DataFrame(medianAE_dt_confirmcase_list)]

# for i in range(0,3):
#     plt.plot(list(min_samples_leaf_list),DTres[i].values ,color[i],label=label[i])

plt.figure(figsize=(20,12))

plt.subplot(2,2,1)
plt.plot(list(min_samples_leaf_list),DecisionTree_r2_score_list,'ro-',label='r2_score')
plt.plot(list(min_samples_leaf_list),medianAE_dt_confirmcase_list,'go-',label='medianAE')
plt.title('different min_samples_leaf', fontsize=12)
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(list(min_samples_leaf_list), MAE_Decision_list,'bo-',label='MAE')
plt.title('different min_samples_leaf', fontsize=12)
plt.legend()


min_samples_split_list = range(2,30,3)
DecisionTree_r2_score_list = []
MAE_Decision_list = []
medianAE_dt_confirmcase_list=[]

for item in min_samples_split_list:
    DecisionTree = DecisionTreeRegressor(min_samples_split = item)
    DecisionTree.fit(train_x_confirmcase, train_y_confirmcase)
    DecisionTree_predict = DecisionTree.predict(test_x_confirmcase)
    DecisionTree_r2_score = r2_score(test_y_confirmcase, DecisionTree_predict)
    MAE_Decision = metrics.mean_absolute_error(test_y_confirmcase, DecisionTree_predict)
    medianAE_dt_confirmcase = metrics.median_absolute_error(test_y_confirmcase, DecisionTree_predict)
    DecisionTree_r2_score_list.append(DecisionTree_r2_score)
    MAE_Decision_list.append(MAE_Decision)
    medianAE_dt_confirmcase_list.append(medianAE_dt_confirmcase)

plt.subplot(2,2,3)
plt.plot(list(min_samples_split_list),DecisionTree_r2_score_list,'ro-',label='r2_score')
plt.plot(list(min_samples_split_list),medianAE_dt_confirmcase_list,'go-',label='medianAE')
plt.title('different min_samples_split', fontsize=12)
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(list(min_samples_leaf_list), MAE_Decision_list,'bo-',label='MAE')
plt.title('different min_samples_split', fontsize=12)
plt.legend()

plt.show()

print("--------------------------------------------------------------")


######this part is some examples cod for tuning(LGBMRegressor)
n_estimators_list = range(100, 1000, 50)
lgbm_r2_score_list = []
MAE_lgbm_list = []
medianAE_lgbm_confirmcase_list = []

for item in n_estimators_list:
    lgbm = LGBMRegressor(n_estimators=item)
    lgbm.fit(train_x_confirmcase, train_y_confirmcase)
    lgbm_predict = lgbm.predict(test_x_confirmcase)
    lgbm_r2_score = r2_score(test_y_confirmcase, lgbm_predict)
    MAE_lgbm = metrics.mean_absolute_error(test_y_confirmcase, lgbm_predict)
    medianAE_lgbm_confirmcase = metrics.median_absolute_error(test_y_confirmcase, lgbm_predict)
    lgbm_r2_score_list.append(lgbm_r2_score)
    MAE_lgbm_list.append(MAE_lgbm)
    medianAE_lgbm_confirmcase_list.append(medianAE_lgbm_confirmcase)

plt.figure(figsize=(16, 8))

plt.subplot(1, 2, 1)
plt.plot(list(n_estimators_list), lgbm_r2_score_list, 'ro-', label='r2_score')
plt.plot(list(n_estimators_list), medianAE_lgbm_confirmcase_list, 'go-', label='medianAE')
plt.title('different n_estimators', fontsize=12)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(list(n_estimators_list), MAE_lgbm_list, 'bo-', label='MAE')
plt.title('different n_estimators', fontsize=12)
plt.legend()

plt.show()

print("--------------------------------------------------------------")