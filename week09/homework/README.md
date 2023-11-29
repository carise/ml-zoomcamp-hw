## Testing the lambda locally

```
curl -X POST "http://localhost:8080/2015-03-31/functions/function/invocations"  -H 'Content-Type: application/json' -d '{"url": "https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg"}'
{"prediction": 0.4453350305557251}
```
