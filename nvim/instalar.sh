#!/bin/bash

sudo apt update
sudo apt install nvim
mkdirs ~/.config/nvim
touch ~/.config/nvim/init.vim

sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'