import docker

client = docker.from_env()
c = client.containers.run(
    "ghcr.io/ise-fizkarlsruhe/nfdi4memory:latest",
    remove=True,
    ports={8000: 8085},
    environment=[
        "MOUNT=/4memory/",
        "DEBUG=1",
        "MOUNT=/4memory/",
        "DATA_LOAD_PATHS=/data/",
        "FTS_FILEPATH=/data/fts",
        "SITE_URI=https://nfdi.fiz-karlsruhe.de/",
    ],
    name="nfdi4memory",
    detach=True,
)
