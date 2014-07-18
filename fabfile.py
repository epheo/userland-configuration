#!/usr/bin/python

from fabric.operations import local as lrun, run
from fabric.api import *
from fabric.state import env

def localhost():
    env.hosts = ['localhost']

def remote():
    env.hosts = ['some.remote.host']

def install_base():
    run('sudo apt-get install zsh python-pip git tmux curl wget htop python-dev cmake fontconfig')
    run('git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"')
    run('pip install --user git+git://github.com/Lokaltog/powerline')
    run('git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/vundle')
    run('vim +PluginInstall +qall')
    run('cd ~/.vim/bundle/YouCompleteMe/ && git submodule update --init --recursive && install.sh')
    run('ln -s ~/.zprezto/runcoms/zlogout ~/.zlogout')
    run('ln -s ~/.zprezto/runcoms/zlogin ~/.zlogin')
    run('ln -s ~/.zprezto/runcoms/zprofile ~/.zprofile')
    run('ln -s ~/.zprezto/runcoms/zshenv ~/.zshenv')

#def xx():
#    echo 'if [ -d "$HOME/.local/bin" ]; then
#            PATH="$HOME/.local/bin:$PATH"
#          fi' >> ~/.profile

def rm_c():
    run('rm ~/.tmux.conf')
    run('rm ~/.zshrc')
    run('rm ~/.zpreztorc')
    run('rm ~/.vimrc ')

def ln_c():
    put('conf/tmux.conf', '~/.tmux.conf')
    put('conf/zshrc', '~/.zshrc')
    put('conf/zpreztorc', '~/.zpreztorc')
    put('conf/vimrc', '~/.vimrc')

def refresh_c():
    rm_c()
    ln_c()