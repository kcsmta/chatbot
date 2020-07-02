## Convert data in the file `nlu.md` to appropriate type for `PhoBERT` model
### Step 1: Convert `nlu.md` to `nlu.json` by running following command:
```shell script
$ rasa data convert nlu --data nlu.md --out nlu.json --format json 
```

### Step 2: Word segmentation use pyvi, run following command:
```shell script
$ python convert_
``` 