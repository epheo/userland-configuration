#!/usr/bin/python

from fabric.operations import local as lrun, run
from fabric.api import *
from fabric.state import env
import os

def localhost():
    env.hosts = ['localhost']

def install_base():
    pkgs = 'zsh python-pip git tmux curl wget htop python-dev cmake fontconfig slock xscreensaver'
    try:
        run('sudo pacman -S %s' % pkgs)
    except SystemExit:
        run('sudo apt-get install %s' % pkgs)
    
    run('git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"')
    run('pip install --user git+git://github.com/Lokaltog/powerline')
    run('git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/vundle')
    run('vim +PluginInstall +qall')
    run('cd ~/.vim/bundle/YouCompleteMe/ && git submodule update --init --recursive && install.sh')
    run('ln -s ~/.zprezto/runcoms/zlogout ~/.zlogout')
    run('ln -s ~/.zprezto/runcoms/zlogin ~/.zlogin')
    run('ln -s ~/.zprezto/runcoms/zprofile ~/.zprofile')
    run('ln -s ~/.zprezto/runcoms/zshenv ~/.zshenv')

def rm_c():
    run('rm ~/.tmux.conf')
    run('rm ~/.zshrc')
    run('rm ~/.zpreztorc')
    run('rm ~/.vimrc ')

def cp_c():
    put('conf/tmux.conf', '~/.tmux.conf')
    put('conf/zshrc', '~/.zshrc')
    put('conf/zpreztorc', '~/.zpreztorc')
    put('conf/vimrc', '~/.vimrc')

def ln_c():
    path = os.getcwd()
    run('ln -s %s/conf/zshrc ~/.zshrc' % path)
    run('ln -s %s/conf/vimrc ~/.vimrc' % path)
    run('ln -s %s/conf/zpreztorc ~/.zpreztorc' % path)
    run('ln -s %s/conf/tmux.conf ~/.tmux.conf' % path)

def init_c():
    rm_c()
    ln_c()

def awesomewm_conf():
    run('mkdir ~/.config/awesome/')
    put('rc.lua', '~/.config/awesome/rc.lua')
