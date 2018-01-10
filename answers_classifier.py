# interchangeable model loader
# a model is supposed to be trained externally
from sklearn.externals import joblib

from answers_downloader import download_answer_sheet
from answers_transform import transform_answers
from fill_data import write_results

timestamp_param = "Horodateur"

sheet_filled = download_answer_sheet()
sheet_classifiable = transform_answers(sheet_filled)

classifier_model = joblib.load("logistic_regression_trained.mod")
probs = classifier_model.predict_proba(X=sheet_classifiable)

print probs

write_results(probs, sheet_filled[timestamp_param].values)

