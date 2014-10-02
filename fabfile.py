#!/usr/bin/python

from fabric.operations import local as lrun, run
from fabric.api import *
from fabric.state import env
import os

def localhost():
    env.hosts = ['localhost']


def install_base():
    pkgs = 'zsh python-pip git tmux curl wget htop python-dev cmake fontconfig slock xscreensaver'
    install_pkg(pkgs)


def install_pkg(pkgs):
    try:
        run('sudo pacman -S %s' % pkgs)
    except SystemExit:
        run('sudo apt-get install %s' % pkgs)

class zsh():
    def install():
        ## Install
        pkgs = 'zsh'
        install_pkg(pkgs)
        run('chsh -s $(which zsh)')

        run('git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"')
        run('ln -s ~/.zprezto/runcoms/zlogout ~/.zlogout')
        run('ln -s ~/.zprezto/runcoms/zlogin ~/.zlogin')
        run('ln -s ~/.zprezto/runcoms/zprofile ~/.zprofile')
        run('ln -s ~/.zprezto/runcoms/zshenv ~/.zshenv')

    def configure():
        ## Conf
        path = os.getcwd()
        run('ln -s %s/conf/zshrc ~/.zshrc' % path)
        run('ln -s %s/conf/zpreztorc ~/.zpreztorc' % path)
    #    put('conf/zshrc', '~/.zshrc')
    #    put('conf/zpreztorc', '~/.zpreztorc')

class vim():
    def install():
        ## Install
        pkgs = 'vim git cmake'
        install_pkg(pkgs)
        run('git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/vundle')
        run('vim +PluginInstall +qall')
        run('sleep 10')
        run('cd ~/.vim/bundle/YouCompleteMe/ && git submodule update --init --recursive && install.sh')

    def configure():
        ##  Conf
        path = os.getcwd()
        run('ln -s %s/conf/vimrc ~/.vimrc' % path)
    #    put('conf/vimrc', '~/.vimrc')

class tmux():
    def install():
        ## Install
        pkgs = 'tmux'
        install_pkg(pkgs)

    def configure():
        ##  Conf
        path = os.getcwd()
        run('ln -s %s/conf/tmux.conf ~/.tmux.conf' % path)
    #    put('conf/tmux.conf', '~/.tmux.conf')

class awesome():
    def install():
        ## Install
        pkgs = 'awesome vicious'
        install_pkg(pkgs)
    def configure():
        ## Conf
        run('git clone https://github.com/Epheo/awesomewm-retina.git ~/.config/awesomewm-retina')
        run('ln -s ~/.config/awesomewm-retina/awesome ~/.config/awesome')

def arch_mbp():
    run('sudo pacman -Sy packer')
    run('packer -Syu')
    run('packer -S otf-powerline-symbols-git')
    run('packer -S broadcom-wl-dkms')
    run('packer -S jmtpfs')
    run('packer -S lua-oocairo')
    run('packer -S sublime-text')

    run('sudo pacman -S smuxi')
    run('sudo pacman -S unzip')
    run('sudo pacman -S vicious')
    run('sudo pacman -S cheese ')
    run('sudo pacman -S alsamixer pulseaudio')
    run('sudo pacman -S gimp')
    run('sudo pacman -S cmake')
    run('sudo pacman -S fabric')
    run('sudo pacman -S openssh')

def rm_c():
    run('rm ~/.tmux.conf')
    run('rm ~/.zshrc')
    run('rm ~/.zpreztorc')
    run('rm ~/.vimrc ')

if __name__ == '__main__':
    path = os.getcwd()
    localhost()

#    install_base(self)

#    zsh.install(self)
#    zsh.configure(self, path)

#    vim.install(self)
#    vim.configure(self, path)
    
    tmux.install()
    tmux.configure(self, path)

#    awesome.install(self)
#    awesome.configure(self, path)