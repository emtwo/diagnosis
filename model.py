'''
  This is where we do any pre-processing required to generate a model that will predict
  the disease given the keywords.

  Some possible pre-processing ideas:
  * Concept 1: certain keywords are usually used to find certain diseases
    Supervised (ANN, SVM, LR, MOG): training data consists of keywords as inputs and matching disease as output
    => lots of issues. Where to get the training data? sparse input mapping of words
    => can potentially take user behaviour as feedback.
       E.g. If a user searchs "pain on side of head" and chooses the 5th item on the result list,
       that choice can serve as a training sample.

  * Concept 2: the keywords in documents related to a disease are likely search keywords
    Naive Bayes + TF-IDF:
    => Probability of class <disease> given document <keywords> = P(keywords | disease) * P(disease) / P(keywords)
    => can find P(keywords | disease) by:
      1) TF-IDF to find salient keywords in documents related to each disease
      2) P(keywords | disease) = P(k1 | disease) * P(k2 | disease) ... * P(kn | disease) => count the keywords in each document

  For now, provide these probabilities at random.

  @return a mock model that returns weighted matches containing the input substring.

'''
import random

def generate_model(diagnosis_dictionary):
  # Expects a string of keywords
  # (though they're not actually used in this mock model)
  def diagnosis_model(keywords):
    model = {}
    for disease in diagnosis_dictionary:
      model[disease.lower()] = round(random.uniform(0, 1.0), 10)

    return model

  return diagnosis_model