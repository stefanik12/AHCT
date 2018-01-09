import copy
import numpy as np


mapping = {"Playing a game of skill such as bridge or chess, working on a hobby?":
               {"Normal": 0, "Requires assistance": 1, "No data": np.nan},
           "Assembling tax records, business affairs, or other papers?":
               {"Has difficulty, but does by self": 0, "Normal": 1, "Not applicable (e.g., never did)": np.nan}}


def transform_answers(df):
    out_df = copy.deepcopy(df)
    for attribute in mapping.keys():
        for attr_answer, attr_value in mapping[attribute].items():
            out_df[attribute].loc[df[attribute] == attr_answer] = attr_value

    return out_df
