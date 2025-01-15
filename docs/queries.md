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

### Example 2: Find resources and their intended purpose.
```sparql
PREFIX nfdicore: <https://nfdi.fiz-karlsruhe.de/ontology/>
PREFIX memo: <https://nfdi.fiz-karlsruhe.de/4memory/ontology/>
SELECT ?resource ?intendedPurpose
WHERE {
  ?resource a nfdicore:Resource ;
             memo:intendedPurpose ?intendedPurpose .
}
```
