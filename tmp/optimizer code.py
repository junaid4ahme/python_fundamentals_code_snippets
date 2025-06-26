## Import Libraries
from gekko import GEKKO
import numpy as np
import pandas as pd
import json
import re


## Import Input Files from JSON and Cloud


# TODO: Take from Snowflake
base_main_model_all_df = pd.read_csv('./INSIGHTS_REPO_MAINMODEL_TRANSFORMED.csv')
# model_parameters_all_df = pd.read_csv('./MAIN_MODEL_PARAMETER_TRANSFORMED.csv')
model_parameters_all_df = pd.read_csv('./MAIN_MODEL_PARAMETER_TRANSFORMED.csv')

# TODO: Take from UI
with open('./input_json_coded_DOTCOM.json', 'r') as json_file:
    input_json = json.load(json_file)

## Create Global Variables

CURRENT_BUDGET = input_json['actualValue']
NEW_BUDGET = input_json['actualValue']
CPM_DICT = {dict['mediaDriver']:dict['percentChangeCPM'] for dict in input_json['investmentConstraints']}
LB_DICT = {dict['mediaDriver']:dict['lowerLimit'] for dict in input_json['investmentConstraints']}
UB_DICT = {dict['mediaDriver']:dict['upperLimit'] for dict in input_json['investmentConstraints']}
KPI = input_json['kpi']
BU = input_json["bu"]

## Objective Function Calculation

printing_output = []

def gross_weekly_incremental(total_spend, paid_media_dict, driver, type, model):
    # Extracting values for Media Variable

    media_parameters = paid_media_dict[driver][type][model]

    a = media_parameters["a"]
    b = media_parameters["b"]
    c = media_parameters["c"]
    coeff = media_parameters["beta"]
    mat_activity = media_parameters["mat_activity"]
    mat_spends = media_parameters["mat_spends"]
    mat_gross_sale = media_parameters["mat_gross_sale"]
    woe = media_parameters["woe"]
    cpm = media_parameters["cpm"]*((100+CPM_DICT[driver])/100)
    factor_to_multiply = media_parameters['ns_factor'] if KPI == 'Net Sales' else media_parameters['am_factor']

    mat_avg_weekly = mat_activity/woe
    spend = total_spend/woe

    weekly_exec = spend/cpm

    hill = 1/(1+b*(((weekly_exec/(1-a))/mat_avg_weekly)**c))
    e_bx = np.e**(coeff*hill)

    uplift_perc = 1-1/e_bx

    gross_weekly_incremental = mat_gross_sale*uplift_perc*factor_to_multiply/52
    # print(f"gross_wee {gross_weekly_incremental}")
    # print(f"Mul \n a{a} b{b} c{c} coeff{coeff} spend {spend} \nwe {weekly_exec} maw {mat_avg_weekly} \nhill {hill} ebx{e_bx} up {uplift_perc} mat_gross_sale{mat_gross_sale} gross_weekly_incremental{gross_weekly_incremental}")

    total_incremental = gross_weekly_incremental*woe

    printing_output.append({
        'model':model,
        'type':type,
        'paid_media':driver,
        'a':a,
        'b':b,
        'c':c,
        'coeff':coeff,
        'raw_mat_activity':mat_activity,
        'raw_mat_spends':mat_spends,
        'raw_mat_gross_sale':mat_gross_sale,
        'raw_woe':woe,
        'raw_weekly_activity':mat_avg_weekly,
        'New_weekly_spend':spend,
        'calc_weekly_exec':weekly_exec,
        'transformed_x_hill':hill,
        'e_bx':e_bx,
        'uplift_perc':uplift_perc,
        'gross_weekly_incremental':gross_weekly_incremental,
        'total_incremental':total_incremental,
        'factor': factor_to_multiply,
    })
    # print(total_incremental)
    return total_incremental

def gross_weekly_incremental_add(total_spend, paid_media_dict, driver, type, model):
    media_parameters = paid_media_dict[driver][type][model]

    a = media_parameters["a"]
    b = media_parameters["b"]
    c = media_parameters["c"]
    coeff = media_parameters["beta"]
    mat_activity = media_parameters["mat_activity"]
    mat_spends = media_parameters["mat_spends"]
    mat_gross_sale = media_parameters["mat_gross_sale"]
    woe = media_parameters["woe"]
    cpm = media_parameters["cpm"]*((100+CPM_DICT[driver])/100)
    factor_to_multiply = media_parameters['ns_factor'] if KPI == 'Net Sales' else media_parameters['am_factor']

    mat_avg_weekly = mat_activity/woe
    spend = total_spend/woe

    weekly_exec = spend/cpm

    gross_weekly_incremental = coeff*(1/(1+b*(((weekly_exec/(1-a))/mat_avg_weekly)**c)))

    uplift_perc = gross_weekly_incremental*mat_gross_sale*factor_to_multiply

    total_incremental = gross_weekly_incremental*factor_to_multiply*woe

    printing_output.append({
        'model':model,
        'type':type,
        'paid_media':driver,
        'a':a,
        'b':b,
        'c':c,
        'coeff':coeff,
        'raw_mat_activity':mat_activity,
        'raw_mat_spends':mat_spends,
        'raw_mat_gross_sale':mat_gross_sale,
        'raw_woe':woe,
        'raw_weekly_activity':mat_avg_weekly,
        'New_weekly_spend':spend,
        'calc_weekly_exec':weekly_exec,
        'transformed_x_hill':0,
        'e_bx':0,
        'uplift_perc':uplift_perc,
        'gross_weekly_incremental':gross_weekly_incremental,
        'total_incremental':total_incremental,
        'factor': factor_to_multiply,

    })

    return total_incremental

def objective_function_scurve(input_df, optimizing_column, get_details = False):
    return_dict = {}
    media_incremental = 0

    for i, media_row in input_df.iterrows():
        media = media_row['Media Variables']
        x = media_row[optimizing_column]

        one_media_incremental = 0
        parent_media_dict = PAID_MEDIA_DICT[media]

        for type in parent_media_dict.keys():
            if("Multiplicative" == type ):
                media_dict = parent_media_dict["Multiplicative"]

                for model in media_dict.keys():
                    woe = media_dict[model]['woe']
                    incremental = gross_weekly_incremental(x, PAID_MEDIA_DICT, media, "Multiplicative", model )
                    media_incremental += incremental
                    one_media_incremental += incremental

            elif("Additive" == type ):
                media_dict = parent_media_dict["Additive"]

                for model in media_dict.keys():
                    woe = media_dict[model]['woe']

                    incremental = gross_weekly_incremental_add(x, PAID_MEDIA_DICT, media, "Additive", model)
                    media_incremental += incremental
                    one_media_incremental += incremental

        if get_details:
            roi = one_media_incremental/x
            return_dict[media] = [x, x/woe, one_media_incremental, roi]
            # print(f"{model} for {media} with {x[i]} and weekly {x[i]/woe} total incremental {media_incremental} gives an ROI of {roi}")

    if get_details:
        return return_dict
    return -media_incremental

### Create Media Dictionary with Data Aavaiable in Snowflake

(INSIGHTS_REPO_MAINMODEL_TRANSFORMED, MAIN_MODEL_PARAMETER_TRANSFORMED)

main_model_parameters_df = model_parameters_all_df[model_parameters_all_df['Level 1'] == 'Paid Media']
base_main_model_df = base_main_model_all_df[base_main_model_all_df['Date']>'2022-10-07']

final_dict = {}
bu_mat_spends_dict = {bu_:{} for bu_ in main_model_parameters_df['BU'].unique()}
for index, row in main_model_parameters_df.iterrows():

    country =  row["Country"]
    row_bu = row["BU"]
    category = row["Category"]
    var = row["Variable"]
    level_1 = row["Level 1"]
    level_3 = row["Level 3"]
    beta = row["S_Curve_Beta"]
    model_type = row["Model Type"]
    a = row["a'"]
    b = row["b'"]
    c = row["c'"]

    if(level_3.lower() in ['signage',
                           #   'influencers',
                           #   'affiliates',
                           #   'affiliates print'
                           ]):
        print(f"Skipping {level_3} in {category} | {row_bu}")
        continue

    if re.search(r'(?i)paid.*search', var):
        level_3 = category.strip() + "_" + level_3.strip()
    else:
        level_3

    row_bu_df = base_main_model_df[(base_main_model_df['BU'] ==  row_bu) & (base_main_model_df['Country'] == country)]
    category_df = row_bu_df[(row_bu_df["Category"] == category) & (row_bu_df["Driver Category"] == category)]
    var_df = category_df[category_df['Variable'] == var]

    if(row_bu not in final_dict.keys()):
        final_dict[row_bu] = {}

    if(level_3 not in final_dict[row_bu].keys()):
        final_dict[row_bu][level_3] = {}

    if(model_type not in final_dict[row_bu][level_3].keys()):
        final_dict[row_bu][level_3][model_type] = {}

    if(category not in final_dict[row_bu][level_3][model_type].keys()):
        final_dict[row_bu][level_3][model_type][category] = {}

    mat_gross_sale = category_df["Gross Sales"].sum()
    net_sale = category_df["Net Sales"].sum()
    adjust_margins_sale = category_df["Adjusted Margin"].sum()

    factor_gross_sale = mat_gross_sale

    factor_gross_sale = var_df["Gross Sales"].sum()
    net_sale = var_df["Net Sales"].sum()
    adjust_margins_sale = var_df["Adjusted Margin"].sum()

    mat_activity = category_df[category_df['Variable'] == var]["Support"].sum()
    mat_spends = category_df[category_df['Variable'] == var]["Spends"].sum()
    woe = sum(category_df[category_df['Variable'] == var]["Spends"]>0)

    final_dict[row_bu][level_3][model_type][category]["mat_gross_sale"] = mat_gross_sale
    final_dict[row_bu][level_3][model_type][category]["mat_activity"] = mat_activity
    final_dict[row_bu][level_3][model_type][category]["mat_spends"] = mat_spends
    final_dict[row_bu][level_3][model_type][category]["woe"] = woe
    final_dict[row_bu][level_3][model_type][category]["cpm"] = mat_spends/mat_activity
    final_dict[row_bu][level_3][model_type][category]["ns_factor"] = net_sale/factor_gross_sale
    final_dict[row_bu][level_3][model_type][category]["am_factor"] = adjust_margins_sale/factor_gross_sale

    if(mat_spends == 0):
        print("")
        print(f"0 Spends  {level_3} | {mat_activity} | {mat_spends} | {var} | {row_bu} | {category}")

    final_dict[row_bu][level_3][model_type][category]["a"] = a
    final_dict[row_bu][level_3][model_type][category]["b"] = b
    final_dict[row_bu][level_3][model_type][category]["c"] = c
    final_dict[row_bu][level_3][model_type][category]["beta"] = beta

    bu_mat_spends_dict[row_bu][level_3] = mat_spends

### Filter out BU level details

PAID_MEDIA_DICT = final_dict[BU]
current_mat_spends_dict = bu_mat_spends_dict[BU]

# final_dict
# bu_mat_spends_dict

# PAID_MEDIA_DICT = final_dict["SBA"]
# current_mat_spends_dict = bu_mat_spends_dict["SBA"]

# current_mat_spends_dict

## Gekko Optimization

m  =  GEKKO(remote = False)

input_df = pd.DataFrame([current_mat_spends_dict]).T.reset_index().rename(columns={'index':'Media Variables', 0:'Current Spends'})

# current_mat_spends_dict

# LB_DICT

# Create Variable for Gekko optimization
optimizing_list = []
for i in range(len(input_df)):
    var = input_df['Media Variables'].iloc[i]
    optimizing_list.append(m.Var(value = input_df['Current Spends'].iloc[i],
                                 lb = float(input_df['Current Spends'].iloc[i])*float(1+LB_DICT[var]),
                                 ub = float(input_df['Current Spends'].iloc[i])*float(1+UB_DICT[var])))

input_df['optimizing_var'] = optimizing_list


# input_df

m.Equation(input_df['optimizing_var'].sum() == NEW_BUDGET)
m.Minimize(objective_function_scurve(input_df, 'optimizing_var'))

len(str(input_df.sum().optimizing_var))

# Andrii Baranov's Suggestions

# how to check convergence
# Build some algorithm to by taking some random values and compare the output with the gekko

# What are the watchouts?
# 1. There is number of character formula limit on crossing n, it might give some error
# 2. Try with different engines/kernels
# 3.

# Can I increase in number of iterations?
# Check with tolerance

m.solve(disp=True)

## Using Output of Gekko

input_df['optimized_spends'] = input_df['optimizing_var'].apply(lambda x: x[0])
# input_df

our_print_dict_of = objective_function_scurve(input_df, 'Current Spends', get_details=True)
printing_output = []
print_dict_of = objective_function_scurve(input_df, 'optimized_spends', get_details=True)

optimized_df = pd.DataFrame(print_dict_of).T.reset_index().rename(columns = {'index' : 'Channel', 0:'Optimal Spends', 1:'Weekly Optimal Spends', 2:'Optimal Media Incremental', 3: 'Optimal ROI'})
current_df = pd.DataFrame(our_print_dict_of).T.reset_index().rename(columns = {'index' : 'Channel', 0:'Current Spends', 1:'Weekly Current Spends', 2:'Current Media Incremental', 3: 'Current ROI'})
current_optimized_df = current_df.merge(optimized_df, on ='Channel', how='left')

# current_optimized_df

current_optimized_df.sum()

# pd.DataFrame(printing_output)

pd.DataFrame(printing_output).to_csv(f'./Channel_{BU}_{KPI}_all.csv')

current_optimized_df.to_csv(f'./Channel_Driver_Optimzed_{BU}_{KPI}_Factor.csv')

### Convert Output to JSON

def get_mine_dict(current_optimized_df):

    total_optimized = current_optimized_df.sum()

    # Separate between category level and driver level data
    paid_search_details = current_optimized_df[current_optimized_df['Channel'].str.contains(r'(?i)paid.*search', regex=True)]
    non_paid_search_details = current_optimized_df[~current_optimized_df['Channel'].str.contains(r'(?i)paid.*search', regex=True)]

    # create list to be used into the json
    optimized_spends_by_driver = non_paid_search_details[['Channel', 'Current Spends', 'Optimal Spends']].to_dict(orient='records')
    optimized_contribution_by_driver = non_paid_search_details[['Channel', 'Current Media Incremental', 'Optimal Media Incremental']].to_dict(orient='records')
    optimized_roi_by_driver = non_paid_search_details[['Channel', 'Current ROI', 'Optimal ROI']].to_dict(orient='records')

    optimized_spends_by_category = paid_search_details[['Channel', 'Current Spends', 'Optimal Spends']].to_dict(orient='records')
    optimized_contribution_by_category = paid_search_details[['Channel', 'Current Media Incremental', 'Optimal Media Incremental']].to_dict(orient='records')
    optimized_roi_by_category = paid_search_details[['Channel', 'Current ROI', 'Optimal ROI']].to_dict(orient='records')

    # Create sub dictionary to be used in json
    total_impact = {"totalMediaContribution":
        [{
            "actual_contribution" : total_optimized['Current Media Incremental'],
            "optimized_contribution" : total_optimized['Optimal Media Incremental']
        }],
        "mediaROI":
            [{
                "actual_ROI" : total_optimized['Current Media Incremental']/total_optimized['Current Spends'],
                "optimized_ROI" :total_optimized['Optimal Media Incremental']/total_optimized['Optimal Spends']
            }]
    }

    driver_level_impact = {
        "driverLevelImpact": {
            "mediaContribution" : optimized_contribution_by_driver,
            "mediaContribution" : optimized_roi_by_driver
        }
    }

    cateogry_level_impact = {
        "categoryLevelImpact": {
            "mediaContribution" : optimized_contribution_by_category,
            "mediaContribution" : optimized_roi_by_category
        }
    }

    # Final json format
    final_json = {
        "optimizedSpendsByDriver": optimized_spends_by_driver,
        "optimizedSpendsByCategory": optimized_spends_by_category,
        "total_impact": total_impact,
        "driverLevelImpact": driver_level_impact,
        "categoryLevelImpact": cateogry_level_impact
    }

    return final_json