import copy
import numpy as np


mapping = {"Playing a game of skill such as bridge or chess, working on a hobby?":
               {"Normal": 0, "Requires assistance": 1, "No data": np.nan},
           "Assembling tax records, business affairs, or other papers?":
               {"Has difficulty, but does by self": 0, "Normal": 1, "Not applicable (e.g., never did)": np.nan}
           "What symtom was first recognized as a decline in the subject's motor function?":
               {"No motor symptoms": 0, "Gait disorder": 1, "Falls": 2, "Tremor": 3, "Slowness":4, "Unknown": np.nan},
           "On what level of intensy are the motor symptoms occuring?":
               {"No motor symptoms": 0, "Gradual": 1, "Subacute": 2, "Abrupt": 3, "Other": 4, "Unknown": np.nan},
           "Does the subject suffer from dementia?": 
               {"No": 0, "Yes": 1},
           "Does the subject suffer from any impairment on their memory?":
               {"No impairment": 0, "Questionable impairment": 0.5, "Mild impairment": 1, "Moderate impairment": 2, "Severe impairment": 3},
           "Does the subject suffer from a fluctuating cognition? Showing different level of awareness over a period of time.":
               {"No": 0, "Yes": 1, "Unknown": np.nan},
           "Has the subject had any problems keeping track of current events?":
               {"Normal": 0, "Has difficulty, but does by self": 1, "Requires assistance": 2, "Dependent": 3, "Not applicable (e.g., never did)": np.nan, "Unknown": np.nan},
           "Has the subject had any difficulty paying attention to e.g. TV program, book or magazine?":
               {"Normal": 0, "Has difficulty, but does by self": 1, "Requires assistance": 2, "Dependent": 3, "Not applicable (e.g., never did)": np.nan, "Unknown": np.nan}
         
          }


def transform_answers(df):
    out_df = copy.deepcopy(df)
    for attribute in mapping.keys():
        for attr_answer, attr_value in mapping[attribute].items():
            out_df[attribute].loc[df[attribute] == attr_answer] = attr_value

    return out_df
