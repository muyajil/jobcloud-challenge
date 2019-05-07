# Jobcloud Challenge

## Prepare data

- To prepare the data run the Juptyer Notebook from top to bottom, it will generate the files needed for the application
- Make sure the file `jobcloud_published_job_titles.csv` is available
- Verify that the notebook generated the file `jobname_app/labels_by_input.json`

## Run application

- The application comes ready with a docker file to run it run the following steps:
  1. `cd jobname_app`
  2. `docker build -t jobname_app:latest .`
  3. `docker run --rm -p 5000:5000 jobname_app:latest`

- Get Recommendations for a given user input:
  1. `curl http://localhost:5000/input=<USER_INPUT>`
  2. The application will return a list of recommendations for autocompletions sorted by relevance

## Improvements

- This is just a crude prototype that allows two things:
  - Dependant teams can quickly use the existing API to integrate this feature (maybe just for a small subset of users)
  - Allows to get feedback quickly and iteratively improve the model
- Until now we have no real "predictive" power. We can only predict already seen words in Job Titles
- However in this context getting predictive power is rather difficult, since generating words is a difficult problem
- Also due to limited training data, training sophisticated models is not really feasible.
- But we could do any number of the following:
  - Use pretrained word embeddings (might be difficult to find, but can be trained on wikipedia for example)
  - Add more text, maybe the job descriptions, to get more context for the job titles, which allows to train more complex models
  - Add external data
  - ...