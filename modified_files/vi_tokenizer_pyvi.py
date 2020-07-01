import re
from typing import Any, Dict, List, Text
from rasa.nlu.tokenizers.tokenizer import Token, Tokenizer
from rasa.nlu.training_data import Message

from rasa.nlu.constants import TOKENS_NAMES, MESSAGE_ATTRIBUTES
from pyvi import ViTokenizer
class VietnameseTokenizer_pyvi(Tokenizer):

    provides = [TOKENS_NAMES[attribute] for attribute in MESSAGE_ATTRIBUTES]

    def __init__(self, component_config: Dict[Text, Any] = None) -> None:
        super().__init__(component_config)

    def tokenize(self, message: Message, attribute: Text) -> List[Token]:
        text = message.get(attribute)
        words = ViTokenizer.tokenize(text).split()
        words_ = []
        for word in words:
            words_.append(word.replace("_", " "))

        return self._convert_words_to_tokens(words_, text)
