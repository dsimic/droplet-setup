from fabric.contrib.files import exists
from fabric.api import env, sudo

env.use_ssh_config = True
env['sudo_prefix'] += '-H '
env.proj_src_dir = './src/licode'


def setup(user):
    if not exists('/home/%s' % user):
        sudo('adduser --home /home/%s %s' % (user, user))
        sudo('adduser %s sudo' % user)
        sudo('service sudo restart')
        sudo('echo "%s ALL=(ALL) NOPASSWD:ALL" | tee -a /etc/sudoers' % user)
    if not exists('/home/%s/.ssh' % user):
        sudo('mkdir -p /home/%s/.ssh' % user)
        sudo('cp /root/.ssh/authorized_keys /home/%s/.ssh/' % user)
        sudo('chown -R %s /home/%s/.ssh' % (user, user))
        sudo('chgrp -R %s /home/%s/.ssh' % (user, user))
