## Examples

### Example 1: Retrieve all MEMO Data Portals.

```sparql
PREFIX nfdicore: <https://nfdi.fiz-karlsruhe.de/ontology/>
SELECT ?portal ?label
WHERE {
  ?portal a nfdicore:DataPortal ;
          rdfs:label ?label .
}
```
