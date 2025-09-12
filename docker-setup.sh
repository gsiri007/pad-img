#!/usr/bin/env bash

if [[ "$SHELL" == "/usr/bin/bash" ]]; then

    echo "--- Building docker image ---"
    docker image build -t pad-img .

    echo "--- Adding alias to .bashrc---"
    echo 'alias pad-img="docker container run --rm -v .:/tmp pad-img:latest"' >> "$HOME/.bashrc"
    echo 'alias pad-img="docker container run --rm -v .:/tmp pad-img:latest"'

    echo "--- Success ---"
    echo "try running: pad-img"
    
fi 

if [[ "$SHELL" == "/usr/bin/zsh" ]]; then

    echo "--- Building docker image ---"
    docker image build -t pad-img .

    echo "--- Adding alias to .zshrc ---"
    echo 'alias pad-img="docker container run --rm -v .:/tmp pad-img:latest"' >> "$HOME/.zshrc"
    echo 'alias pad-img="docker container run --rm -v .:/tmp pad-img:latest"'

    echo "--- Success ---"
    echo "try running: pad-img"

fi 

