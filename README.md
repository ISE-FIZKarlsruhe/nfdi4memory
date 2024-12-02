# NFDI4Memory Knowledge Graph

This is where we create the knowledge graph for [NFDI4Memory](https://4memory.de/)

It can be viewed live at https://nfdi.fiz-karlsruhe.de/4memory/

## Development

To run the image locally for testing, use:

```shell
docker run -v $(pwd)/data:/data -e DATA_LOAD_PATHS=/data -p 8000:8000 ghcr.io/ise-fizkarlsruhe/nfdi4memory:v1
```
