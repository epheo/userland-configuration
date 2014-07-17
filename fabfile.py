#!/usr/bin/python

from fabric.operations import local as lrun, run
from fabric.api import *
from fabric.state import env

def localhost():
    env.run = lrun
    env.hosts = ['localhost']

def remote():
    env.run = run
    env.hosts = ['some.remote.host']

def install_base():
    env.run('sudo apt-get install zsh python-pip git tmux curl wget htop python-dev cmake fontconfig')
    env.run('git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"')
    env.run('pip install --user git+git://github.com/Lokaltog/powerline')
    env.run('git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/vundle')

    env.run('ln -s ~/.zprezto/runcoms/zlogout ~/.zlogout')
    env.run('ln -s ~/.zprezto/runcoms/zlogin ~/.zlogin')
    env.run('ln -s ~/.zprezto/runcoms/zprofile ~/.zprofile')
    env.run('ln -s ~/.zprezto/runcoms/zshenv ~/.zshenv')

def vim_plugin_install():
    env.run('vim +PluginInstall +qall')
    env.run('~/.vim/bundle/YouCompleteMe/install.sh')

#def xx():
#    echo 'if [ -d "$HOME/.local/bin" ]; then
#            PATH="$HOME/.local/bin:$PATH"
#          fi' >> ~/.profile

def rm_c():
    env.run('rm ~/.tmux.conf')
    env.run('rm ~/.zshrc')
    env.run('rm ~/.zpreztorc')
    env.run('rm ~/.vimrc ')

def ln_c():
    put('tmux.conf', '~/.tmux.conf')
    put('zshrc', '~/.zshrc')
    put('zpreztorc', '~/.zpreztorc')
    put('vimrc', '~/.vimrc')
