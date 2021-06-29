# CLI

See elg version 

```bash
elg --version
```

Response: `0.4.8`


Create the docker image

```bash
docker build -t test .
```

Test it

```python
from elg import Service

s = Service.from_docker_image("test:latest", "http://localhost:8000/process", 8997) # -> need to run the docker image with the command displayed
s("test", sync_mode=True)
```
