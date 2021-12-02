import spacy
from spacy.language import Language
from rel_component.scripts.rel_pipe import make_relation_extractor, score_relations
from rel_component.scripts.rel_model import create_relation_model, create_classification_layer, create_instances
import random
import typer
from pathlib import Path
from spacy.tokens import DocBin, Doc
from spacy.training.example import Example

nlp = spacy.load("C:\\Users\\spate113\\Desktop\\Pycharm Projects\\NERAnnotation\\output\\model-last")

text = ['''India won 2 times in Australia, won odi Series in Australia, South Africa, New zealand. Also won T20 
series in all SENA Countries.''' ]

for doc in nlp.pipe(text, disable=["tagger"]):
    print(f"spans: {[(e.start, e.text, e.label_) for e in doc.ents]}")

nlp2 = spacy.load("rel_component/training_old/training/model-best")

for name, proc in nlp2.pipeline:
    doc = proc(doc)

# print(doc._.rel.items())

# for value, rel_dict in doc._.rel.items():
#     for sent in doc.sents:
#         for e in sent.ents:
#             for b in sent.ents:
#                 if e.start == value[0] and b.start == value[1]:
#                     if rel_dict['INVOLVEDIN'] >= 0.9:
#                         print(f" entities: {e.text, b.text} --> predicted relation: {rel_dict}")


for value, rel_dict in doc._.rel.items():
        for e in doc.ents:
            for b in doc.ents:
                if e.start == value[0] and b.start == value[1]:
                    if rel_dict['WONAGAINST'] >= 1.00e-10:
                        print(f" entities: {e.text, b.text} --> predicted relation: {rel_dict}")
