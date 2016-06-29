# ansible-art
ansible apply role tool: ansible-art is a simple tool to apply role of ansible.

## abstract
To apply role of ansible, we need to write playbook for each role in conventional. By using ansible-art, we can apply role to machines directly, without writing playbook by ourself. ansible-art will create playbook instead of us.

## install
First, install ansible-art with `pip` command.
```
pip install ansible-art
```
Second, edit config file to set the dir of roles installed in advance.
```
ansible-art config
```
before
```
roles_path = /etc/ansible/roles
```
after
```
roles_path = <DIR>
```
please specify the dir of roles as `<DIR>`

## usage
```
*** usage ***
ansible-art [-h] [-V]
ansible-art role list
ansible-art role params <role>
ansible-art config
ansible-art apply <role> <inventory> [-p <dir>] [-g <dir>] [-a <args>]
```

- `ansible-art [-h]`

 Using option `[-h]`, show help message and exit. Using option `[-V]`, show version and exit.

- `ansbile-art role list`

 Show roles in the dir specified in config file.

- `ansible-art role params <role>`

 Show parameters defined in defaults/main.yml of specified role.

- `ansible-art config`

 Edit config file.

- `ansible-art apply <role> <inventory> [-p <dir>] [-g <dir>] [-a <args>]`

 Apply role to machines. In `<role>`, specify role wanted to apply. In `<inventory>`, specify inventory file path to use. In `<dir>`, specify the directory including host_vars files or group_vars files. If `<dir>` is not specified, `host_vars` dir or `group_vars` dir searched as host_vars dir or group_vars dir. If `host_vars` dir or `group_vars` dir is not exist, no host_vars files or group_vars files are used. In `<args>`, we can specify some arguments of the command "ansible-playbook". Since ansible-art apply role to "all" group by default, if necessary, specify target group, ip or hostname by using `-l` option of the command "ansible-playbook".
