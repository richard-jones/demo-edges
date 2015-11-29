#!/usr/bin/env bash
curl -XPOST http://localhost:9200/edges/constituencies/_bulk --data-binary "@constituencies.es"