#!/usr/bin/env bash

ZIPS_COMMA=$(ls zips/* | tr "\n" ',')
ZIPS=${ZIPS_COMMA::-1}
curl -n -T "{$ZIPS}" ftp://ftp.online.net/opendata/
