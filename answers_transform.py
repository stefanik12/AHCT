import copy
import numpy as np

mapping = {
    "What level of independence does the subject have in their daily life?":
        {"Able to live independently": 1, "Requires some assistance with complex activities": 2,
         "Requires som assistance with basic activities": 3, "Completely dependent": 4, "Unknown": np.nan, "alias": "INDEPEND"},
    "Taking care of themselves?":
        {"No impairment": 0, "Questionable impairment": 0.5, "Mild impairment": 1, "Moderate impairment": 2,
         "Severe impairment": 3, "alias" : "PERSCARE"},
    "Shopping for groceries or other household necessities?":
        {"Normal": 0, "Has difficutly, but does by self": 1, "Requires assistance": 2, "Dependent": 3,
         "Not applicable (e.g., never did)": np.nan, "Unknown": np.nan, "alias": "SHOPPING"},
    "Traveling out of the neighborhood, driving or using public transportation?":
        {"Normal": 0, "Has difficutly, but does by self": 1, "Requires assistance": 2, "Dependent": 3,
         "Not applicable (e.g., never did)": np.nan, "Unknown": np.nan, "alias":"TRAVEL"},
    "Playing a game of skill such as bridge or chess, working on a hobby?":
        {"Normal": 0, "Has difficutly, but does by self": 1, "Requires assistance": 2, "Dependent": 3,
         "Not applicable (e.g., never did)": np.nan, "Unknown": np.nan, "alias": "GAMES"},
    "Assembling tax records, business affairs, or other papers?":
        {"Normal": 0, "Has difficutly, but does by self": 1, "Requires assistance": 2, "Dependent": 3,
         "Not applicable (e.g., never did)": np.nan, "Unknown": np.nan, "alias": "TAXES"},
    "Does the subject suffer from any impairment on their orientation?":
        {"No impairment": 0, "Questionable impairment": 0.5, "Mild impairment": 1, "Moderate impairment": 2,
         "Severe impairment": 3, "alias": "ORIENT"},
    "What symtom was first recognized as a decline in the subject's motor function?":
        {"No motor symptoms": 0, "Gait disorder": 1, "Falls": 2, "Tremor": 3, "Slowness": 4, "Unknown": np.nan, "alias":"NACCMOTF"},
    "On what level of intensy are the motor symptoms occuring?":
        {"No motor symptoms": 0, "Gradual": 1, "Subacute": 2, "Abrupt": 3, "Other": 4, "Unknown": np.nan, "alias":"NOMODE"},
    "Does the subject suffer from dementia?":
        {"No": 0, "Yes": 1, "alias":"DEMENTED"},
    "Does the subject suffer from any impairment on their memory?":
        {"No impairment": 0, "Questionable impairment": 0.5, "Mild impairment": 1, "Moderate impairment": 2,
         "Severe impairment": 3, "alias":"MEMORY"},
    "Does the subject suffer from a fluctuating cognition? Showing different level of awareness over a period of time.":
        {"No": 0, "Yes": 1, "Unknown": np.nan, "alias":"COGFLUC"},
    "Has the subject had any problems keeping track of current events?":
        {"Normal": 0, "Has difficulty, but does by self": 1, "Requires assistance": 2, "Dependent": 3,
         "Not applicable (e.g., never did)": np.nan, "Unknown": np.nan, "alias":"EVENTS"},
    "Has the subject had any difficulty paying attention to e.g. TV program, book or magazine?":
        {"Normal": 0, "Has difficulty, but does by self": 1, "Requires assistance": 2, "Dependent": 3,
         "Not applicable (e.g., never did)": np.nan, "Unknown": np.nan, "alias":"PAYATTN"},
    "Indicate the domain that was first recognized as a change in the subject":
        {"Cognition": 1, "Behaviour": 2, "Motor function": 3, "Not applicable": np.nan, "Unknown": np.nan, "alias":"FRSTCHG"}
}


def transform_answers(df):
    out_df = copy.deepcopy(df)
    for attribute in mapping.keys():
        for attr_answer, attr_value in mapping[attribute].items():
            out_df[attribute].loc[df[attribute] == attr_answer] = attr_value

            return out_df

    # TODO remove the timestamp attribute, to make a dataframe classifiable

