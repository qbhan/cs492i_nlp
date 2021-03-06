# nsml: nsml/ml:cuda10.1-cudnn7-pytorch1.3keras2.3

from distutils.core import setup

setup(
    name='kaist-korquad-test',
    version='1.0',
    install_requires=[
        'boto3', 'regex', 'sacremoses', 'filelock', 'tokenizers',
        'tqdm', 'konlpy', 'sentencepiece==0.1.91.', 'dataclasses',
        'transformers==3.1.0'
    ]
)
