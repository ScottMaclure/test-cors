# Test Cors

Testing cors with Authorization header.

/etc/hosts and/or C:\Windows\System32\drivers\etc\hosts
```
127.0.0.1       foo.local
127.0.0.1       bar.local
```

Run
```
uvicorn main:app --reload
```

http://foo.local:8000/static/index.html

Then the XHR will be configured for http://bar.local:8000/static/index.html

## Read More

Client:
* https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
* https://github.com/github/fetch#sending-cookies

Server:
* https://fastapi.tiangolo.com/tutorial/cors/
* https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials
