import json
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
import numpy as np
import math
import re

studentid = os.path.basename(sys.modules[__name__].__file__)


def log(question, output_df, other):
    print("--------------- {}----------------".format(question))

    if other is not None:
        print(question, other)
    if output_df is not None:
        df = output_df.head(5).copy(True)
        for c in df.columns:
            df[c] = df[c].apply(lambda a: a[:20] if isinstance(a, str) else a)

        df.columns = [a[:10] + "..." for a in df.columns]
        print(df.to_string())


def average_latitude(df):
    df_dict = df['Cities'].split('|||')
    latitude = []
    for i in range(len(df_dict)):
        df_dict[i] = json.loads(df_dict[i])
        latitude.append(df_dict[i]['Latitude'])
    average_latitude = sum(latitude) / len(latitude)
    return average_latitude


def average_longitude(df):
    df_dict = df['Cities'].split('|||')
    longitude = []
    for i in range(len(df_dict)):
        df_dict[i] = json.loads(df_dict[i])
        longitude.append(df_dict[i]['Longitude'])
    average_longitude = sum(longitude) / len(longitude)
    return average_longitude


def replace_index(df):
    to_replace = {'North Korea': 'Korea, North', 'South Korea': 'Korea, South', 'United States': 'US',
                  'Russia': 'Russian Federation', 'Republic of the Congo': 'Congo',
                  'Democratic Republic of the Congo': 'Congo, Democratic Republic of'}
    df.replace(to_replace, inplace=True)


def population(df):
    df_dict = df['Cities'].split('|||')
    country_population = []
    for i in range(len(df_dict)):
        df_dict[i] = json.loads(df_dict[i])
        if df_dict[i]['Population'] is not None:
            country_population.append(df_dict[i]['Population'])
    return sum(country_population)


def draw(df10, continent, colour):
    df10_backup = df10.loc[df10['Continent'] == continent]
    x = df10_backup.copy()
    point_df = pd.DataFrame()
    x['Population'] = df10_backup.apply(population, axis=1)
    small_point_cont = 500000
    point_df['Population'] = x['Population'] / small_point_cont
    plt.scatter(df10_backup.avg_longitude, df10_backup.avg_latitude, color=colour, s=point_df['Population'],
                label=colour)


def non_population(df, population, city):
    df_dict = df['Cities'].split('|||')
    country_population = []
    for i in range(len(df_dict)):
        df_dict[i] = json.loads(df_dict[i])
        if df_dict[i]['Population'] is not None:
            country_population.append(df_dict[i]['Population'])
            population.append(df_dict[i]['Population'])
            city.append(df_dict[i]['City'])
    return country_population


def city_country(df, city, country):
    df_dict = df['Cities'].split('|||')
    country_city = []
    for i in range(len(df_dict)):
        df_dict[i] = json.loads(df_dict[i])
        country_city.append(df_dict[i]['City'])
        country.append(df_dict[i]['Country'])
        city.append(df_dict[i]['City'])
    return country_city


def question_1(exposure, countries):
    """
    :param exposure: the path for the exposure.csv file
    :param countries: the path for the Countries.csv file
    :return: df1
            Data Type: Dataframe
            Please read the assignment specs to know how to create the output dataframe
    """

    #################################################
    # Your code goes here ...
    exposure_df = pd.read_csv(exposure, sep=';', encoding='latin1')
    countries_df = pd.read_csv(countries)
    exposure_df.columns = exposure_df.columns.str.capitalize()
    exposure_df = exposure_df[exposure_df.Country.notna()]
    to_replace = {'Korea DPR': 'North Korea', 'Korea Republic of': 'South Korea',
                  'United States of America': 'United States', 'Viet Nam': 'Vietnam', 'Cabo Verde': 'Cape Verde',
                  'Brunei Darussalam': 'Brunei', 'Lao PDR': 'Laos', 'North Macedonia': 'Macedonia',
                  'Moldova Republic of': 'Moldova', 'Russian Federation': 'Russia', 'Eswatini': 'Swaziland',
                  'Congo': 'Republic of the Congo', 'Congo DR': 'Democratic Republic of the Congo',
                  'Palestine': 'Palestinian Territory', "Côte d'Ivoire": 'Ivory Coast'}
    exposure_df.replace(to_replace, inplace=True)
    df1 = pd.merge(exposure_df, countries_df, how='inner', on=['Country'])
    df1 = df1.set_index('Country')
    df1 = df1.sort_index(ascending=True)
    #################################################

    log("QUESTION 1", output_df=df1, other=df1.shape)
    return df1


def question_2(df1):
    """
    :param df1: the dataframe created in question 1
    :return: df2
            Data Type: Dataframe
            Please read the assignment specs to know how to create the output dataframe
    """

    #################################################
    # Your code goes here ...
    df2 = df1
    df2['avg_latitude'] = df2.apply(average_latitude, axis=1)
    df2['avg_longitude'] = df2.apply(average_longitude, axis=1)
    #################################################

    log("QUESTION 2", output_df=df2[["avg_latitude", "avg_longitude"]], other=df2.shape)
    return df2


def question_3(df2):
    """
    :param df2: the dataframe created in question 2
    :return: df3
            Data Type: Dataframe
            Please read the assignment specs to know how to create the output dataframe
    """

    #################################################
    # Your code goes here ...
    df3 = df2
    dLat = df3['avg_latitude'] - 30.5928
    dLon = df3['avg_longitude'] - 114.3055
    dLat = dLat * math.pi / 180
    dLon = dLon * math.pi / 180
    c = np.sin(dLat / 2) ** 2 + np.cos(30.5928 * math.pi / 180) * np.cos(df3['avg_latitude'] * math.pi / 180) * np.sin(
        dLon / 2) ** 2
    d = 2 * np.arctan2(np.sqrt(c), np.sqrt(1 - c)) * 6373
    df3['distance_to_Wuhan'] = d
    df3 = df3.sort_values(by=['distance_to_Wuhan'])
    #################################################

    log("QUESTION 3", output_df=df3[['distance_to_Wuhan']], other=df3.shape)
    return df3


def question_4(df2, continents):
    """
    :param df2: the dataframe created in question 2
    :param continents: the path for the Countries-Continents.csv file
    :return: df4
            Data Type: Dataframe
            Please read the assignment specs to know how to create the output dataframe
    """

    #################################################
    # Your code goes here ...
    continent_df = pd.read_csv(continents)
    df4_backup = df2
    replace_index(df4_backup)
    df4_backup = pd.merge(df4_backup, continent_df, how='inner', on=['Country']).set_index('Country')
    df4_backup = df4_backup.loc[df4_backup['Covid_19_economic_exposure_index'] != 'x']
    df4_backup['Covid_19_economic_exposure_index'] = df4_backup['Covid_19_economic_exposure_index'].str.replace(',',
                                                                                                                '.')
    df4_backup['Covid_19_economic_exposure_index'] = pd.to_numeric(df4_backup['Covid_19_economic_exposure_index'])
    df4 = df4_backup.groupby('Continent').mean()
    df4.rename(columns={'Covid_19_economic_exposure_index': 'average_covid_19_Economic_exposure_index'}, inplace=True)
    df4 = df4.drop('avg_latitude', axis=1)
    df4 = df4.drop('avg_longitude', axis=1)
    df4 = df4.sort_values(by='average_covid_19_Economic_exposure_index')

    #################################################

    log("QUESTION 4", output_df=df4, other=df4.shape)
    return df4


def question_5(df2):
    """
    :param df2: the dataframe created in question 2
    :return: df5
            Data Type: dataframe
            Please read the assignment specs to know how to create the output dataframe
    """
    #################################################
    # Your code goes here ...
    df5_backup = df2
    df5_backup = df5_backup.loc[df5_backup['Net_oda_received_perc_of_gni'] != 'No data']
    df5_backup = df5_backup.loc[df5_backup['Foreign direct investment'] != 'x']
    df5_backup['Foreign direct investment'] = df5_backup['Foreign direct investment'].str.replace(',', '.')
    df5_backup['Foreign direct investment'] = pd.to_numeric(df5_backup['Foreign direct investment'])
    df5_backup['Net_oda_received_perc_of_gni'] = df5_backup['Net_oda_received_perc_of_gni'].str.replace(',', '.')
    df5_backup['Net_oda_received_perc_of_gni'] = pd.to_numeric(df5_backup['Net_oda_received_perc_of_gni'])
    df5_backup.rename(columns={'Income classification according to wb': 'Income Class'}, inplace=True)
    df5 = df5_backup.groupby('Income Class').mean()
    df5.rename(columns={'Foreign direct investment': 'Avg Foreign direct investment'}, inplace=True)
    df5.rename(columns={'Net_oda_received_perc_of_gni': 'Avg_Net_ODA_received_perc_of_GNI'}, inplace=True)
    df5 = df5.drop('avg_latitude', axis=1)
    df5 = df5.drop('avg_longitude', axis=1)
    df5 = df5[['Avg Foreign direct investment', 'Avg_Net_ODA_received_perc_of_GNI']]
    #################################################

    log("QUESTION 5", output_df=df5, other=df5.shape)
    return df5


def question_6(df2):
    """
    :param df2: the dataframe created in question 2
    :return: cities_lst
            Data Type: list
            Please read the assignment specs to know how to create the output dataframe
    """
    cities_lst = []
    #################################################
    # Your code goes here ...
    df6 = df2
    df6 = df6.loc[df6['Income classification according to wb'] == 'LIC']
    city_list = []
    population_list = []
    df6.apply(lambda x: non_population(x, population_list, city_list), axis=1)
    copy_population = population_list.copy()
    copy_population.sort(reverse=True)
    cities_lst = [city_list[population_list.index(i)] for i in copy_population[0:5]]
    lst = cities_lst
    #################################################
    log("QUESTION 6", output_df=None, other=cities_lst)
    return lst


def question_7(df2):
    """
    :param df2: the dataframe created in question 2
    :return: df7
            Data Type: Dataframe
            Please read the assignment specs to know how to create the output dataframe
    """

    #################################################
    # Your code goes here ...
    df7_backup = df2
    city_country_dict = {}
    city_list = []
    city_country_list = []
    df7_backup.apply(lambda x: city_country(x, city_list, city_country_list), axis=1)
    for i in range(len(city_list)):
        city_country_dict[city_list[i]] = set()
    for i in range(len(city_list)):
        city_country_dict[city_list[i]].add(city_country_list[i])
    res_dict = {}
    for i in city_country_dict:
        city_country_dict[i] = sorted(list(city_country_dict[i]))
        if len(city_country_dict[i]) > 1:
            res_dict[i] = city_country_dict[i]
    df7 = pd.DataFrame(res_dict.items(), columns=['city', 'countries']).set_index('city')
    #################################################

    log("QUESTION 7", output_df=df7, other=df7.shape)
    return df7


def question_8(df2, continents):
    """
    :param df2: the dataframe created in question 2
    :param continents: the path for the Countries-Continents.csv file
    :return: nothing, but saves the figure on the disk
    """

    #################################################
    # Your code goes here ...
    df8 = df2
    continent_df = pd.read_csv(continents)
    replace_index(df8)
    df8 = pd.merge(df8, continent_df, how='inner', on=['Country']).set_index('Country')
    x = df8.copy()
    point_df = pd.DataFrame()
    x['Population'] = df8.apply(population, axis=1)
    point_df['Population'] = x['Population']
    world_total_population = sum(point_df['Population'].tolist())
    df8 = df8.loc[df8['Continent'] == 'South America']
    x = df8.copy()
    south_america_df = pd.DataFrame()
    x['Population'] = df8.apply(population, axis=1)
    south_america_df['Population'] = x['Population'] / world_total_population * 100
    sa_country_list = south_america_df.index.tolist()
    sa_country_popu_list = south_america_df['Population'].tolist()
    plt.title('Percentage of the world population living in each South American country')
    plt.xlabel('South America country name')
    plt.ylabel('Percentage of the world population')
    plt.bar(sa_country_list, sa_country_popu_list, tick_label=sa_country_list)
    plt.xticks(sa_country_list, sa_country_list, rotation='vertical')
    #################################################

    plt.savefig("{}-Q11.png".format(studentid))


def question_9(df2):
    """
    :param df2: the dataframe created in question 2
    :return: nothing, but saves the figure on the disk
    """
    #################################################
    # Your code goes here ...
    plt.cla()
    df9 = df2
    df9 = df9.loc[df9['Covid_19_economic_exposure_index_ex_aid_and_fdi'] != 'x']
    df9 = df9.loc[df9['Covid_19_economic_exposure_index_ex_aid_and_fdi_and_food_import'] != 'x']
    df9 = df9.loc[df9['Foreign direct investment, net inflows percent of gdp'] != 'x']
    df9 = df9.loc[df9['Foreign direct investment'] != 'x']
    df9['Covid_19_economic_exposure_index_ex_aid_and_fdi'] = df9[
        'Covid_19_economic_exposure_index_ex_aid_and_fdi'].str.replace(',', '.')
    df9['Covid_19_economic_exposure_index_ex_aid_and_fdi'] = pd.to_numeric(
        df9['Covid_19_economic_exposure_index_ex_aid_and_fdi'])
    df9['Covid_19_economic_exposure_index_ex_aid_and_fdi_and_food_import'] = df9[
        'Covid_19_economic_exposure_index_ex_aid_and_fdi_and_food_import'].str.replace(',', '.')
    df9['Covid_19_economic_exposure_index_ex_aid_and_fdi_and_food_import'] = pd.to_numeric(
        df9['Covid_19_economic_exposure_index_ex_aid_and_fdi_and_food_import'])
    df9['Foreign direct investment, net inflows percent of gdp'] = df9[
        'Foreign direct investment, net inflows percent of gdp'].str.replace(',', '.')
    df9['Foreign direct investment, net inflows percent of gdp'] = pd.to_numeric(
        df9['Foreign direct investment, net inflows percent of gdp'])
    df9['Foreign direct investment'] = df9['Foreign direct investment'].str.replace(',', '.')
    df9['Foreign direct investment'] = pd.to_numeric(df9['Foreign direct investment'])
    df9 = df9.groupby('Income classification according to wb').mean()
    df9 = df9.drop('avg_latitude', axis=1)
    df9 = df9.drop('avg_longitude', axis=1)
    first = df9['Covid_19_economic_exposure_index_ex_aid_and_fdi'].tolist()
    second = df9['Covid_19_economic_exposure_index_ex_aid_and_fdi_and_food_import'].tolist()
    third = df9['Foreign direct investment, net inflows percent of gdp'].tolist()
    forth = df9['Foreign direct investment'].tolist()
    class_list = ['HIC', 'LIC', 'MIC']
    index = np.arange(3)
    bar_width = 0.2
    plt.bar(index, first, width=bar_width)
    plt.bar(index + bar_width, second, width=bar_width)
    plt.bar(index + bar_width + bar_width, third, width=bar_width)
    plt.bar(index + bar_width + bar_width + bar_width, forth, tick_label=class_list, width=bar_width, align='center')
    plt.title('Compare figures of three income class')
    plt.xlabel('Income classification')
    plt.ylabel('Index of metrics')
    plt.legend(('FDI_index', 'FDI_index_food_import', 'investment_and_net', 'investment'))
    #################################################

    plt.savefig("{}-Q12.png".format(studentid))


def question_10(df2, continents):
    """
    :param df2: the dataframe created in question 2
    :return: nothing, but saves the figure on the disk
    :param continents: the path for the Countries-Continents.csv file
    """

    #################################################
    # Your code goes here ...
    plt.cla()
    df10 = df2
    continent_df = pd.read_csv(continents)
    replace_index(df10)
    df10 = pd.merge(df10, continent_df, how='inner', on=['Country']).set_index('Country')
    draw(df10, 'Africa', 'black')
    draw(df10, 'Asia', 'yellow')
    draw(df10, 'Europe', 'orange')
    draw(df10, 'North America', 'blue')
    draw(df10, 'Oceania', 'red')
    draw(df10, 'South America', 'green')
    plt.title('population of the country')
    plt.xlabel('average longitude')
    plt.ylabel('average latitude')
    plt.legend(loc='best')
    #################################################

    plt.savefig("{}-Q13.png".format(studentid))


if __name__ == "__main__":
    df1 = question_1("exposure.csv", "Countries.csv")
    df2 = question_2(df1.copy(True))
    df3 = question_3(df2.copy(True))
    df4 = question_4(df2.copy(True), "Countries-Continents.csv")
    df5 = question_5(df2.copy(True))
    lst = question_6(df2.copy(True))
    df7 = question_7(df2.copy(True))
    question_8(df2.copy(True), "Countries-Continents.csv")
    question_9(df2.copy(True))
    question_10(df2.copy(True), "Countries-Continents.csv")
