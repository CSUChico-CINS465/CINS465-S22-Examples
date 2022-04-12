#!/bin/bash

docker-compose run wasm wasm-pack build --target web
sudo chown -R bryandixon:bryandixon hello-wasm
