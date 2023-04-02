import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
from smart_answer import SmartAnswer
from sys import argv

sa = SmartAnswer("./qna_sample.csv")
############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    #Eric Wang: Does not seem to be used
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    print("\n--------------top 3 matches --------\n")
    for text in request.text:
        # TODO Add code here
        ary = sa.answer(text)
        if not ary:
            print("Sorry, I am just a chat bot trained on 50 science trivia questions. I do not know the answer.")
            output.append(None)
            continue
        (question, answer) = ary
        print(f"\nmatched question: {question}\nanswer:{answer}")
        output.append(answer)

    return SimpleText(dict(text=output))

if __name__ == "__main__":
    execute(SimpleText(dict(text=[argv[1]])), None)
