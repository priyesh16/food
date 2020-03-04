#!/usr/bin/env bash
ln -s /bld/blenderbpy/ /usr/local/lib/python3.6/site-packages/
ln -s /src/tree3/ /usr/local/lib/python3.6/site-packages/
echo 'alias b=/src/tree3/dabba/dabba.py' >> ~/.bashrc
echo 'alias vi=vim' >> ~/.bashrc
cp /src/vimrc ~/.vimrc
/src/tree3/dabba/dabba.py
cd /src/tree3
exec /bin/bash
