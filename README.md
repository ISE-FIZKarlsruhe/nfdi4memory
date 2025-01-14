# NFDI4Memory Knowledge Graph

This is where we create the knowledge graph for [NFDI4Memory](https://4memory.de/)

It can be viewed live at https://nfdi.fiz-karlsruhe.de/4memory/

## Development

To run the image locally for testing, use:

```shell
docker run --rm -p 8000:8000 -e DEBUG=1 -e MOUNT=/4memory/ -e DATA_LOAD_PATHS=/data/ -e FTS_PATH=/data/fts -e SITE_URI=https://nfdi.fiz-karlsruhe.de/  --name=nfdi4memory ghcr.io/ise-fizkarlsruhe/nfdi4memory:latest
```
