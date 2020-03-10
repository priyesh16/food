#!/usr/bin/env bash
ln -s /bld/blenderbpy/ /usr/local/lib/python3.6/site-packages/
ln -s /src/tree3/ /usr/local/lib/python3.6/site-packages/
cp /src/vimrc ~/.vimrc
cp /src/bashrc ~/.bashrc
cd /src/tree3
exec /bin/bash
