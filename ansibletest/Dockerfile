FROM ubuntu:14.04
MAINTAINER Jeganathan Swaminathan <jegan@tektutor.org> <http://www.tektutor.org>
ENV http_proxy 'http://10.19.16.165:8080'
ENV https_proxy 'https://10.19.16.165:8080'

RUN apt-get -y update && apt-get -y install ssh openssh-server
RUN sed -ri 's/^session\s+required\s+pam_loginuid.sos/session optional pam_loginuid.so/' /etc/pam.d/sshd 
RUN useradd -m -g sudo -p 'tektutor' tektutor
RUN echo 'tektutor:tektutor' | chpasswd

COPY sshd_config /etc/ssh/sshd_config

RUN mkdir -m 755 /var/run/sshd

RUN mkdir /home/tektutor/.ssh
RUN chown tektutor /home/tektutor/.ssh
COPY authorized_keys /home/tektutor/.ssh/authorized_keys

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
