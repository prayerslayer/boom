# boom

Using cgroups and namespaces ("containers") to perform actions that might go the wrong way.
E.g. reading user-submitted data.

## Instructions

(fish)

```
docker build -t boom .
docker run --rm -it -v (pwd):/foo -v /var/run/docker.sock:/var/run/docker.sock boom python3 /foo/run.py`
```
