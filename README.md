# Diagnosis Keyword Lookup

## Approach
The approach I took is essentially summarized in the comments at the top of diagnose.py. I return the top 10 matches that may be decided based on a model and/or substring matching.
In model.py I mention a couple of ideas for how a model could be trained but the implementation is simply a mock for the purpose of this work sample. I also decided to implement this as a web service since a client-side implementation would leave less room for computational complexity in the future.

## Tradeoffs
The main tradeoff is simplicity vs. accuracy - Substring matching is the simplest approach possible, but some keywords may have nothing to do with the name of the disease itself. Using a trained model is more complex and time consuming but would have more accurate results.

## Expected Outcomes
I expect that the model types described in model.py would be fairly accurate whether someone decided to search for a disease by name, by symptoms, or by description. Furthermore, we can improve the results overtime by allowing the models to learn from user behaviour.

## Tools to Investigate
* I'd do some research on how others have solved similar types of search problems and attempt to use the tools they used. For example, there may be better ways to generate the model than the two I proposed.

* I'd also investigate tools that assist with paging in a web API. For now the API returns only the top 10 diseases. What if there are many more potential diseases but we only want to return a few at a time to the client?

## Evaluation Critera
I didn't have time to write them for this work sample, but I would definitely need some unit tests for the algorithm in diagnose.py. Once there was sufficient training data and we had a model, we'd need to run some validation tests on it to ensure it generalizes reasonably well. Probably, we'd also want to give out some software to doctors to user-test this API.

## Time constraints
I'd say a minimum viable product could be ready within 1 month using one of the proposed models, if all goes well. That's still a bit optimistic since a bunch of thought and effort would need to be put into how we gather the data required to train the models. And there is always a risk that the model does not generalize well.

If the time constraint is 1 week, I would probably only end up with a prototype of this idea. It's possible it would not be the best approach and may not be production-ready code. Alternatively, if it needs to be in production witihn 1 week, the substring matching approach is very easily feasible within that time constraint.

If the time constraint is 1 month, as I mentioned this might be enough for an implementation of this approach if all goes well.

If the time constraint is 4 months, this is enough to really perfect things. This leaves enough time to do some prior research on best practices for solving similar problems, software tools that come in handy, experimenting with several approaches in order to choose the best one, writing thorough tests and doing thorough code reviews and perhaps even doing some user testing.