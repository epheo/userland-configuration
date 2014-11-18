FROM base/arch
MAINTAINER Thibaut Lapierre <root@epheo.eu>
## Devellopment environment

RUN pacman -Syu --noconfirm
RUN pacman -S vim zsh python-pip git tmux curl wget htop cmake --noconfirm

#zprezto
RUN git clone --recursive https://github.com/sorin-ionescu/prezto.git
RUN ln -s .zprezto/runcoms/zlogout .zlogout
RUN ln -s .zprezto/runcoms/zlogin .zlogin
RUN ln -s .zprezto/runcoms/zprofile .zprofile
RUN ln -s .zprezto/runcoms/zshenv .zshenv

ADD conf/zshrc /root/.zshrc
ADD conf/zpreztorc /root/.zpreztorc

RUN pip install tox

RUN git clone https://github.com/Epheo/nova-docker.git "/root/nova-docker"
RUN  pip install -r /root/nova-docker/requirements.txt -r /root/nova-docker/test-requirements.txt

RUN git clone https://github.com/Epheo/octopenstack.git "/root/octopenstack"
RUN pip install -r /root/octopenstack/requirements.txt -r /root/octopenstack/test-requirements.txt

WORKDIR /root/


CMD /usr/bin/tmux