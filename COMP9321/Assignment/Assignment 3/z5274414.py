import pandas as pd
import sys
from collections import defaultdict
from sklearn import metrics
from scipy.stats import pearsonr
from sklearn.ensemble import RandomForestRegressor, GradientBoostingClassifier

path1 = sys.argv[1]
path2 = sys.argv[2]
training_df = pd.read_csv(path1)
original_training_df = training_df.copy()
validation_df = pd.read_csv(path2)
original_validation_df = validation_df.copy()


def preprocess(training_df):
    # process the cast
    cast_dict = defaultdict(int)
    for i in range(len(training_df['cast'])):
        cast_df = eval(training_df['cast'][i])
        for j in range(len(cast_df)):
            cast_dict[cast_df[j]['name']] += 1
    ten_list = sorted(cast_dict.items(), key=lambda item: item[1], reverse=True)[0:10]
    first_ten_list = [ten_list[i][0] for i in range(len(ten_list))]
    for n in first_ten_list:
        column = [0] * len(training_df['cast'])
        for i in range(len(training_df['cast'])):
            cast_df = eval(training_df['cast'][i])
            for j in range(len(cast_df)):
                if cast_df[j]['name'] == n:
                    column[i] = 1
        training_df[n] = column
    training_df = training_df.drop(columns=['cast'], axis=1)

    # process the crew
    crew_dict = defaultdict(int)
    for i in range(len(training_df['crew'])):
        crew_df = eval(training_df['crew'][i])
        for j in range(len(crew_df)):
            crew_dict[crew_df[j]['name']] += 1
    ten_list = sorted(crew_dict.items(), key=lambda item: item[1], reverse=True)[0:10]
    first_ten_list = [ten_list[i][0] for i in range(len(ten_list))]
    for n in first_ten_list:
        column = [0] * len(training_df['crew'])
        for i in range(len(training_df['crew'])):
            crew_df = eval(training_df['crew'][i])
            for j in range(len(crew_df)):
                if crew_df[j]['name'] == n:
                    column[i] = 1
        training_df[n] = column
    training_df = training_df.drop(columns=['crew'], axis=1)

    # process the homepage
    homepage_list = []
    for i in range(len(training_df['homepage'])):
        if isinstance(training_df['homepage'][i], float):
            homepage_list.append(0)
        else:
            homepage_list.append(1)
    training_df['homepage'] = homepage_list

    # process the original language
    language_list = []
    for i in range(len(training_df['original_language'])):
        if training_df['original_language'][i] == 'en':
            language_list.append(1)
        else:
            language_list.append(0)
    training_df['original_language'] = language_list

    # process the production companies
    production_companies_dict = defaultdict(int)
    for i in range(len(training_df['production_companies'])):
        production_companies_df = eval(training_df['production_companies'][i])
        for j in range(len(production_companies_df)):
            production_companies_dict[production_companies_df[j]['name']] += 1
    ten_list = sorted(production_companies_dict.items(), key=lambda item: item[1], reverse=True)[0:10]
    first_ten_list = [ten_list[i][0] for i in range(len(ten_list))]
    for n in first_ten_list:
        column = [0] * len(training_df['production_companies'])
        for i in range(len(training_df['production_companies'])):
            production_companies_df = eval(training_df['production_companies'][i])
            for j in range(len(production_companies_df)):
                if production_companies_df[j]['name'] == n:
                    column[i] = 1
        training_df[n] = column
    training_df = training_df.drop(columns=['production_companies'], axis=1)

    # process the production countries
    countries_list = [len(eval(training_df['production_countries'][i])) for i in
                      range(len(training_df['production_countries']))]
    training_df['production_countries'] = countries_list

    # process the release date
    date_list = []
    for i in range(len(training_df['release_date'])):
        if '01' <= training_df['release_date'][i][5:7] <= '03':
            date_list.append(1)
        elif '04' <= training_df['release_date'][i][5:7] <= '06':
            date_list.append(2)
        elif '07' <= training_df['release_date'][i][5:7] <= '09':
            date_list.append(3)
        else:
            date_list.append(0)
        # date_list.append(eval(training_df['release_date'][i][0:4]))
    training_df['release_date'] = date_list

    # process the spoken language
    spoken_list = [len(eval(training_df['spoken_languages'][i])) for i in range(len(training_df['spoken_languages']))]
    training_df['spoken_languages'] = spoken_list

    training_df = training_df.drop(
        columns=['movie_id', 'genres', 'keywords', 'original_title', 'overview', 'status', 'tagline', 'rating',
                 'revenue'],
        axis=1)
    return training_df


df_train = preprocess(training_df)
df_test = preprocess(validation_df)
x_train = df_train.values
x_test = df_test.values

# part 1
movie_ids = original_validation_df['movie_id']
y_train_revenue = original_training_df['revenue'].values
y_test_revenue = original_validation_df['revenue'].values
rfr_model = RandomForestRegressor(random_state=0)
rfr_model.fit(x_train, y_train_revenue)
y_predicted_revenue = rfr_model.predict(x_test)
msr = metrics.mean_squared_error(y_test_revenue, y_predicted_revenue)
pcc = pearsonr(y_predicted_revenue, y_test_revenue)[0]
pd.DataFrame({'movie_id': movie_ids, 'predicted_revenue': y_predicted_revenue}, columns=[
    'movie_id', 'predicted_revenue']).to_csv('z5274414.PART1.output.csv', index=False)
pd.DataFrame([['z5274414', round(msr, 2), round(pcc, 2)]], columns=['zid', 'MSR', 'correlation']).to_csv(
    'z5274414.PART1.summary.csv', index=False)

# part 2
y_train_rating = original_training_df['rating'].values
y_test_rating = original_validation_df['rating'].values
gbc_classifier = GradientBoostingClassifier()
gbc_classifier.fit(x_train, y_train_rating)
y_predicted_rating = gbc_classifier.predict(x_test)
reports = metrics.classification_report(y_test_rating, y_predicted_rating, output_dict=True)
average_precision = round(reports['macro avg']['precision'], 2)
average_recall = round(reports['macro avg']['recall'], 2)
accuracy = round(reports['accuracy'], 2)
pd.DataFrame({'movie_id': movie_ids, 'predicted_rating': y_predicted_rating},
             columns=['movie_id', 'predicted_rating']).to_csv('z5274414.PART2.output.csv', index=False)
pd.DataFrame([['z5274414', average_precision, average_recall, accuracy]],
             columns=['zid', 'average_precision', 'average_recall', 'accuracy']).to_csv('z5274414.PART2.summary.csv',
                                                                                        index=False)
