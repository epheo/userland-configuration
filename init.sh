#!/bin/sh

sudo apt-get install zsh python-pip git tmux curl wget htop python-dev cmake fontconfig


##  ZSH  ##
git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"

##  POWERLINE  ##
pip install --user git+git://github.com/Lokaltog/powerline

echo 'if [ -d "$HOME/.local/bin" ]; then
  PATH="$HOME/.local/bin:$PATH"
fi' >> ~/.profile

##  VIM  ##
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/vundle

vim +PluginInstall +qall
~/.vim/bundle/YouCompleteMe/install.sh

##Create config
rm ~/.tmux.conf 
rm ~/.zlogout  
rm ~/.zlogin 
rm ~/.zprofile 
rm ~/.zshenv 
rm ~/.zshrc 
rm ~/.zpreztorc 
rm ~/.vimrc  

ln -s ~/.zprezto/runcoms/zlogin ~/.zlogin
ln -s ~/.zprezto/runcoms/zlogout ~/.zlogout
ln -s ~/.zprezto/runcoms/zprofile ~/.zprofile
ln -s ~/.zprezto/runcoms/zshenv ~/.zshenv
ln -s `pwd`/zshrc ~/.zshrc
ln -s `pwd`/zpreztorc ~/.zpreztorc
ln -s `pwd`/tmux.conf ~/.tmux.conf
ln -s `pwd`/vimrc ~/.vimrc
