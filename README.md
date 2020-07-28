# Scrubber

Redact/replace content in text files.

* upload to S3
* lambda scrubs content
* output to S3, original trashed


## Test

```
aws s3 cp file.txt s3://jex-scrubber/in/file.txt
```


## Lambda


### Run Locally

```sh
python3 lambda_function.py
```

### Update Lambda

```sh
zip package.zip lambda_function.py

aws lambda update-function-code \
  --function-name scrubber \
  --zip-file fileb://package.zip
```




## Next

Dynamic blacklist
