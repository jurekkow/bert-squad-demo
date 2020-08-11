First, let's create a conda evvironment called `lang`, then we can follow the rest of instructiosn for the demo as outlined in the README.

# To activate this environment, use
#
#     $ conda activate lang
#
# To deactivate an active environment, use
#
#     $ conda deactivate

`unset PYTHONPATH`

`pip install -r requirements.txt`

# bert-squad-demo
Demo web server app that shows how BERT model trained on SQuAD dataset deals with the machine
comprehension task.

It was implemented for the purposes of presentation on STX Next Tech Power Summit 2019.
Slides from the presentation are available [here](slides/whats_new_in_word_vectors.pdf).

## Quick guide

Before running the app, please make sure that you have all [requirements](requirements.txt) installed 
and [download](model/README.md) BERT model for machine comprehension.

To run the server, navigate into the main project's directory and type

```
$ flask run
```

Requests sent to the BERT web server should have the following form:

```json
{
  "context": "Bert is a yellow Muppet character...",
  "question": "Who was the first Bert performer?"
}  
```

You can expect answers of the form:

```json
{
    "answer": "Frank Oz"
}
```