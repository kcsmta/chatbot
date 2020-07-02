from pyvi import ViTokenizer
# subwords = ViTokenizer.tokenize("Trường đại học bách khoa hà nội")
# print(subwords)

import json
with open('nlu.json') as json_file:
    data = json.load(json_file)

sentence_list = data['rasa_nlu_data']['common_examples']
# data['rasa_nlu_data']['regex_features']
# data['rasa_nlu_data']['lookup_tables']
# data['rasa_nlu_data']['entity_synonyms']

new_data = {}
new_data['rasa_nlu_data'] = {}
new_data['rasa_nlu_data'].update([('common_examples', []), ('regex_features', []), ('lookup_tables', []), ('entity_synonyms',[])])

for sentence in sentence_list:
    new_sentence = {}

    text = sentence['text']

    new_text = ViTokenizer.tokenize(text)
    new_entities = []
    try:
        entities = sentence['entities']
        for entity in entities:
            new_entity = {}
            new_entity.update([('start', entity['start']), ('end', entity['end']), ('value', entity['value'].replace(" ", "_")), ('entity', entity['entity'])])
            new_entities.append(new_entity)
    except:
        pass

    new_intent = sentence['intent']

    if len(new_entities)>0:
        new_sentence.update( [ ('intent', new_intent) , ('entities', new_entities), ('text', new_text)] )
    else:
        new_sentence.update([('intent', new_intent), ('text', new_text)])

    # print("original sentence: ", sentence)
    # for key, value in sentence.items() :
    #     print(key)
    #     print(value)
    # print("new sentence     : ", new_sentence)
    new_data['rasa_nlu_data']['common_examples'].append(new_sentence)

# print(data)
# print(new_data)
with open('nlu_phoBert.json', 'w', encoding='utf8') as outfile:
    json.dump(new_data, outfile, ensure_ascii=False)