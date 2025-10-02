#!/usr/bin/env bash

if [[ "$SHELL" == "/usr/bin/bash" ]] || [[ "$SHELL" == "/bin/bash" ]]; then

    echo "--- Building docker image ---"
    docker image build -t pad-img .

    echo "--- Adding alias to .bashrc---"
    echo 'alias pad-img="docker container run --rm -v .:/tmp pad-img:latest" --network none' >> "$HOME/.bashrc"
    echo 'alias pad-img="docker container run --rm -v .:/tmp pad-img:latest" --network none'

    echo "--- Success ---"
    echo "try running: pad-img"
    
fi 

if [[ "$SHELL" == "/usr/bin/zsh" ]] || [[ "$SHELL" == "/bin/zsh" ]]; then

    echo "--- Building docker image ---"
    docker image build -t pad-img .

    echo "--- Adding alias to .zshrc ---"
    echo 'alias pad-img="docker container run --rm -v .:/tmp pad-img:latest" --network none' >> "$HOME/.zshrc"
    echo 'alias pad-img="docker container run --rm -v .:/tmp pad-img:latest" --network none'

    echo "--- Success ---"
    echo "try running: pad-img"

fi 

