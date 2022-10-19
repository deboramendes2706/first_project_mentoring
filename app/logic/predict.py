import pickle
import pandas as pd
from .config import *


def preprocess(sample):
    # print(f"---------Sample: {sample}")
    with open(LABELENCONDER_INTEREST, 'rb') as f:
        labelenconder_interest = pickle.load(f)
    with open(NORMALIZADOR_PARENT_SALARY, 'rb') as f:
        normalizador_parent_salary = pickle.load(f)
    with open(NORMALIZADOR_AVERAGE_GRADES, 'rb') as f:
        normalizador_average_grades = pickle.load(f)

    subs_type_school = {
        "Academic": 0,
        "Vocational": 1
    }

    subs_school_accreditation = {
        "A": 0,
        "B": 1
    }

    subs_gender ={
        "Male": 0,
        "Female": 1
    }

    subs_residence ={
        "Rural": 0,
        "Urban": 1
    }

    df_new_sample = pd.DataFrame(
        columns=['type_school', 'school_accreditation', 'gender', 'interest',
       'residence', 'parent_salary', 'average_grades', 'parent_was_in_college'])
    df_new_sample.loc[0, 'type_school'] = subs_type_school[sample.type_school]
    # print(f"---------type_school_column: {df_new_sample['type_school']}")
    df_new_sample.loc[0, 'school_accreditation'] = subs_school_accreditation[sample.school_accreditation]
    df_new_sample.loc[0, 'gender'] = subs_gender[sample.gender]
    # df_new_sample['gender'] = df_new_sample['gender'].replace(['Male','Female'],[0,1])
    df_new_sample['interest'] = labelenconder_interest.transform([sample.interest])
    df_new_sample.loc[0, 'residence'] = subs_residence[sample.residence]
    # df_new_sample['residence'] = df_new_sample['residence'].replace(['Urban','Rural'],[0,1])
    df_new_sample['parent_salary'] = normalizador_parent_salary.transform([[sample.parent_salary]])
    df_new_sample['average_grades'] = normalizador_average_grades.transform([[sample.average_grades]])
    df_new_sample['parent_was_in_college'] = sample.parent_was_in_college

    return df_new_sample


def perform_prediction(sample):
    # print(f"Sample: {sample}")
    # print(sample.Parch)
    new_sample = preprocess(sample)
    print(new_sample)

    with open(CLASSIFICADOR, 'rb') as f:
        clf = pickle.load(f)

    will_go_to_college = clf.predict(new_sample)

    will_go_to_college = will_go_to_college[0]
    print(will_go_to_college)

    if will_go_to_college == 0:
        will_go_str = 'Não vai para a faculdade'
    else:
        will_go_str = 'Vai para a faculdade'

    return will_go_to_college, will_go_str
