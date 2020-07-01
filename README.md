<h2 align='center'>Meeyland Chatbot</h2>
<p align="center">
<img src="resources/logo.jpg" width="100" height="100" title="Multi-task learning model">
</p>

<!-- Table of content-->
## Table of contents
* [Introduction](#introduction)
* [Installation](#installation)
* [Usage](#usage)
* [Contact](#contact)

## Introduction
[Rasa](https://rasa.com/) + pyvi, underthesea (tokenizer for Vietnamese) + PhoBERT (pretrained model for Vietnamese based on RoBERTa)

## Installation
* Python 3.5+ is required.

**1. Clone project**

``` shell script
$ git clone https://github.com/kcsmta/chatbot.git
```

**2. Install pip3 first**
```shell script
$ sudo apt-get install python3-pip
```

**3. Install virtualenv using pip3**
```shell script
$ sudo pip3 install virtualenv
```

**4. Create virtual environment**
```shell script
$ virtualenv -p /usr/bin/python3.6 chatbot-env
```

**5. Active virtual environment**
```shell script
$ source chatbot-env/bin/activate 
```

**6. Install requirement packages by running following command**
```shell script
(chatbot-env)$ pip install rasa
(chatbot-env)$ pip install rasa[spacy]
(chatbot-env)$ python -m spacy download en_core_web_md
(chatbot-env)$ python -m spacy link en_core_web_md en
(chatbot-env)$ pip install git+https://github.com/mit-nlp/MITIE.git
(chatbot-env)$ pip install rasa[mitie]
(chatbot-env)$ pip install rasa[transformers]
# For tokenizers
(chatbot-env)$ pip install pyvi
(chatbot-env)$ pip install underthesea
```

**7. To use `pyvi` and `underthesea` as custom tokenizer in Rasa**: 
* Copy file `/modified_files/vi_tokenizer_pyvi.py` and `/modified_files/vi_tokenizer_underthesea.py`
to the folder `chatbot-env/lib/python3.6/site-packages/rasa/nlu/tokenizers`

<!-- 
2. Registry new tokenizers by adding following lines into file
`chatbot-env/lib/python3.6/site-packages/rasa/nlu/registry.py`:
```shell script
from rasa.nlu.tokenizers.vi_tokenizer_underthesea import VietnameseTokenizer_underthesea
from rasa.nlu.tokenizers.vi_tokenizer_pyvi import VietnameseTokenizer_pyvi
```

And then add to `component_classes` list:

```
VietnameseTokenizer_underthesea,
VietnameseTokenizer_pyvi
```
-->

* Replace file `chatbot-env/lib/python3.6/site-packages/rasa/nlu/registry.py` by file 
`/modified_files/registry.py`

* Use the config file: `/config_files/config_custom_tokenizer.yml`

* For testing\
**Create rasa project**: Create folder contains project (e.g. MeeylandBot). Move to the folder 
and run following command:
```shell script
(chatbot-env)$ rasa init --no-prompt
(chatbot-env)$ rasa train nlu -c ../config_files/config_custom_tokenizer.yml
```

**8. To use `PhoBERT` as custom embedding in Rasa**
* Replace file `chatbot-env/lib/python3.6/site-packages/rasa/nlu/registry.py` by file 
`/modified_files/registry.py`
* Use the config file: `/config_files/config_custom_PhoBERT.yml`
* For testing: run following command:
```shell script
(chatbot-env)$ rasa train nlu -c ../config_files/config_custom_PhoBERT.yml
```

## Usage


## Contact
Authors: \
Khanh Duy Tung Nguyen : khanhndt@meeyland.com