# bert-squad-demo
Demo web server app that shows how BERT model trained on SQuAD dataset deals with the machine
comprehension task.

It was implemented for the purposes of presentation on STX Next Tech Power Summit 2019.
Slides from the presentation are available [here](slides/whats_new_in_word_vectors.pdf).

Let's create a conda environment called `lang`, then we can follow the rest of instructiosn for the demo as outlined in the README.

# Create conda env:

```
$ conda create -n lang python=3.6.1
```

# To activate this environment, use

```
$ conda activate lang
```
(on MacOS, you might also need to run: `unset PYTHONPATH`)

# To deactivate an active environment, use

```
$ conda deactivate
```


## Quick guide

Before running the app, please make sure that you have all [requirements](requirements.txt) installed 
and [download](model/README.md) BERT model for machine comprehension.  You can install all requirements in your conda env as follows:

```
$ pip install -r requirements.txt
````

To run the server, navigate into the main project's directory and type

```
$ flask run
```

To see our experiments visit the demo page.  To run the test we have a simple python script in which we provide the question and asnwer and then send the request to the server.

## Demos
We have tested the BERT modle with a few contexts to to demosntrate stengths and weakness of BERT in the closed form question answering.

# Experiment I: [ELIZA](https://en.wikipedia.org/wiki/ELIZA)
We took the first paragraph and posed a few questions. See [experiment script](run_experiments.py).

```
question='What programming language was ELIZA written in?'
```

```
{"answer":"MAD-Slip"}
```

```
question='Did ELIZA pass Turing test?'
```

```
{"answer":"ELIZA was one of the first chatterbots and one of the first programs capable of attempting the Turing test"}
```

As you see, although the model is successful in answering well formed questions with an explicit answer present in the context, it fails at the language comprehension test.

# Experiment II: [Noam Chomsky](https://en.wikipedia.org/wiki/Noam_Chomsky)
We took the first from Noam Chomsky wikipedia article and posed a number of questions as follows:


```
question="What is Chomsky first name?"
```

```
{"answer":"Avram Noam"}
```

```
question="What month was Chomsky born?"
```

```
{"answer":"December 7, 1928"}
```

# Experiment III: [Donal Trump](https://en.wikipedia.org/wiki/Donald_Trump)
Again, we took the first from Trump wikipedia article and posed a number of questions as follows:

```
question="When was Trump born?"
```

```
{"answer":"1971"}
```

```
question="What is Trump nationality?"
```

```
{"answer":"born and raised in Queens"}
```