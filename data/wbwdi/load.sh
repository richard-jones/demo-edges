#!/usr/bin/env bash
curl -XPOST http://localhost:9200/edges/wdi/_bulk --data-binary "@wbwdi_selected.es"