import requests

def get_answer(question, context):
    r = requests.post("http://127.0.0.1:5000/answer", json={'context': context, 'question': question})
    return r.text

"""
Experiment I: ELIZA --> https://en.wikipedia.org/wiki/ELIZA
"""
eliza_context='ELIZA is an early natural language processing computer program created from 1964 to 1966 at \
            the MIT Artificial Intelligence Laboratory by Joseph Weizenbaum. Created to demonstrate \
            the superficiality of communication between humans and machines, Eliza simulated \
            conversation by using a "pattern matching" and substitution methodology that gave users an \
            illusion of understanding on the part of the program, but had no built in framework for \
            contextualizing events. Directives on how to interact were provided by "scripts", \
            written originally in MAD-Slip, which allowed ELIZA to process user inputs and engage \
            in discourse following the rules and directions of the script. The most famous script, \
            DOCTOR, simulated a Rogerian psychotherapist (in particular, Carl Rogers, who was \
            well-known for simply parroting back at patients what they would just said), and used \
            rules, dictated in the script, to respond with non-directional questions to user inputs. \
            As such, ELIZA was one of the first chatterbots and one of the first programs capable of \
            attempting the Turing test.'

question_1='What programming language was ELIZA written in?'
print("question #1: {} --> answer: {}".format(question_1, get_answer(question_1, eliza_context)))

question_2='Who invented ELIZA?'
print("question #2: {} --> answer: {}".format(question_2, get_answer(question_2, eliza_context)))

question_3='What is ELIZA?'
print("question #3: {} --> answer: {}".format(question_3, get_answer(question_3, eliza_context)))

question_4='Is ELIZA a human?'
print("question #4: {} --> answer: {}".format(question_4, get_answer(question_4, eliza_context)))

question_5='Where was ELIZA created at?'
print("question #5: {} --> answer: {}".format(question_5, get_answer(question_5, eliza_context)))

question_6='Did ELIZA pass Turing test?'
print("question #6: {} --> answer: {}".format(question_6, get_answer(question_6, eliza_context)))


"""
Experiment II: Noam Chomsky --> https://en.wikipedia.org/wiki/Noam_Chomsky
"""
noam_context='Avram Noam Chomsky (born December 7, 1928) is an American linguist, philosopher, cognitive \
        scientist, historian, social critic, and political activist. Sometimes called "the father of \
        modern linguistics", Chomsky is also a major figure in analytic philosophy and one of the \
        founders of the field of cognitive science. He holds a joint appointment as Institute \
        Professor Emeritus at the Massachusetts Institute of Technology (MIT) and Laureate Professor \
        at the University of Arizona, and is the author of more than 100 books on topics such as \
        linguistics, war, politics, and mass media. Ideologically, he aligns with anarcho-syndicalism \
        and libertarian socialism.'

question_1="When was Chomsky born?"
print("question #1: {} --> answer: {}".format(question_1, get_answer(question_1, noam_context)))

question_2="What month was Chomsky born?"
print("question #2: {} --> answer: {}".format(question_2, get_answer(question_2, noam_context)))

question_3="Who is Noam Chomsky?"
print("question #2: {} --> answer: {}".format(question_3, get_answer(question_3, noam_context)))

question_4="What universities is Chomsky a professor at?"
print("question #3: {} --> answer: {}".format(question_4, get_answer(question_4, noam_context)))

question_5="How many books Chomsky has been author of?"
print("question #4: {} --> answer: {}".format(question_5, get_answer(question_5, noam_context)))

question_6="What topics has Chomsky written books in?"
print("question #5: {} --> answer: {}".format(question_6, get_answer(question_6, noam_context)))

question_7="What is Chomsky first name?"
print("question #7: {} --> answer: {}".format(question_7, get_answer(question_7, noam_context)))

question_8="What is Noam Chomsky nationality?"
print("question #8: {} --> answer: {}".format(question_8, get_answer(question_8, noam_context)))

"""
Experiment III: Donald Trump --> https://en.wikipedia.org/wiki/Donald_Trump
"""
trump_context="Trump was born and raised in Queens, a borough of New York City, and received a \
            bachelor's degree in economics from the Wharton School. He took charge of his family's \
            real-estate business in 1971, renamed it The Trump Organization, and expanded its \
            operations from Queens and Brooklyn into Manhattan. Trump later started various side \
            ventures, mostly by licensing his name. He bought the Miss Universe brand of beauty \
            pageants in 1996, and sold it in 2015. Trump and his businesses have been involved in \
            more than 4,000 state and federal legal actions, including six bankruptcies. He produced \
            and hosted The Apprentice, a reality television series, from 2003 to 2015. As of 2020, \
            Forbes estimated his net worth to be $2.1 billion."

question_1="When was Trump born?"
print("question #1: {} --> answer: {}".format(question_1, get_answer(question_1, trump_context)))

question_2="Where was Trump born?"
print("question #2: {} --> answer: {}".format(question_2, get_answer(question_2, trump_context)))

question_3="What is Trump business?"
print("question #3: {} --> answer: {}".format(question_3, get_answer(question_3, trump_context)))

question_4="How much is Trump wealth?"
print("question #4: {} --> answer: {}".format(question_4, get_answer(question_4, trump_context)))

question_5="What is Trump nationality??"
print("question #5: {} --> answer: {}".format(question_5, get_answer(question_5, trump_context)))

question_6="How many times Trump businesses have declared bankruptcies?"
print("question #6: {} --> answer: {}".format(question_6, get_answer(question_6, trump_context)))

question_7="What school did Trump go to?"
print("question #7: {} --> answer: {}".format(question_7, get_answer(question_7, trump_context)))