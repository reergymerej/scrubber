# Scrubber

Redact/replace content in text files.

* upload to S3
* lambda scrubs content
* output to S3, original trashed


```
aws s3 cp file.txt s3://jex-scrubber/in/file.txt
```

## Next

Remove blacklisted patterns
