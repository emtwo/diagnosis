'''
  Goal: return a list of top 10 possible diagnoses.

  Algorithm:
  1) Do a substring match for the keywords.
  2) If fewer than 10 results exist, show those results followed by the top model matches
     for a total of 10
  3) If more than 10 exist, choose the top 10 sorted by the model probabilities.
'''
import operator

def diagnose_from_keywords(model, dictionary, keywords):
  matched = []
  probabilities = model(keywords)
  sorted_probabilities = sorted(probabilities.items(), key=operator.itemgetter(1))
  sorted_probabilities.reverse()

  # 1) Find string matches.
  for disease in dictionary:
    if disease.lower().find(keywords) != -1:
      matched.append(disease)


  # 2) If fewer than 10 substring matches exist, append model recommendations.
  if len(matched) < 10:
    for disease in sorted_probabilities:
      disease_name = disease[0]
      if (disease_name not in matched):
        matched.append(disease_name)
        if len(matched) == 10:
          break
  # 3) If >= 10 substring matches exist, sort them based on model probabilities.
  else:
    # Get a dict of the subset of matches and their corresponding probabilities
    weighted_matches = {x: probabilities[x] for x in matched if x in probabilities}

    # Sort these matches in descending order based on probabilities
    sorted_matches = sorted(weighted_matches.items(), key=operator.itemgetter(1))
    sorted_matches.reverse()

    # We only need the top 10 elements.
    sorted_matches = sorted_matches[:10]

    # Strip out the probabilities so that we only return a list of diseases.
    matched = reduce(lambda prev_val, element: prev_val + [element[0]], sorted_matches, [])

  return matched
