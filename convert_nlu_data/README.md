## Convert data in the file `nlu.md` to appropriate type for `PhoBERT` model
Active virtual environment first:
```shell script
$ source chatbot-env/bin/activate
```
### Step 1: Convert `nlu.md` to `nlu.json` by running following command:
```shell script
(chatbot-env)$ rasa data convert nlu --data nlu.md --out nlu.json --format json 
```

### Step 2: Word segmentation use pyvi, run following command:
```shell script
(chatbot-env)$ python convert_nlu.py
``` 
