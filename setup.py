import setuptools


setuptools.setup(
    name='yinglish',
    version='0.0.1',
    author='RimoChan',
    author_email='the@librian.net',
    description='yinglish',
    long_description=open('readme.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RimoChan/yinglish',
    packages=[
        'yinglish',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'jieba>=0.42.1',
        'spacy>=2.3.0,<2.4.0',
        'https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.0/en_core_web_sm-2.3.0.tar.gz'
    ],
)
