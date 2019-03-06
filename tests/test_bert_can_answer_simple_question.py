"""
This is NOT the module containing unit tests for the project.
It just checks if trained BERT model for question answering
can answer some simple questions.
"""

import json

from run_squad import answer_question


def test_bert_can_answer_question(context, question, expected_answer):
    answer = answer_question(context, question)
    assert expected_answer == answer


def run_test():
    with open('tests/questions_with_answers.json') as questions_with_answers_file:
        examples = json.load(questions_with_answers_file)['examples']
    for example in examples:
        test_bert_can_answer_question(**example)


if __name__ == '__main__':
    run_test()
