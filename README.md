# ansible-art
ansible apply role tool: ansible-art is a simple tool to apply role of ansible.

## abstract
To apply role of ansible, we need to write playbook for each role in conventional. By using ansible-art, we can apply role to machines directly, without writing playbook by ourself. ansible-art will create playbook instead of us.

## install
First, install ansible-art with `pip` command.
```
pip install ansible-art
```
Second, set the directory of roles installed in advance. Please specify the directory of roles installed in advance to `DIR`.
```
ansible-art role dir set DIR
```

## usage
```
*** usage ***
ansible-art [help]
ansible-art version
ansible-art role list
ansible-art role params <role>
ansible-art role dir show
ansible-art role dir set <dir>
ansible-art apply <role> <inventory> [-t <target>] [-p <dir>] [-g <dir>] [-v]
```

- `ansible-art [help]`

 Show help message and exit.

- `ansible-art version`

 Show version and exit.

- `ansbile-art role list`

 Show roles in the dir set in advance by using command `ansible-art dir set <dir>`.

- `ansible-art role params <role>`

 Show parameters defined in defaults/main.yml of specified role.

- `ansible-art role dir show`

 Show the dir in advance by using command `ansible-art dir set <dir>` ".

- `ansible-art role dir set <dir>`

 Set dir to use other subcommands of `ansible-art`.

- `ansible-art apply <role> <inventory> [-t <target>] [-p <dir>] [-g <dir>]`[-v]

 Apply role target machine. In `<role>`, specify role wanted to apply. In `<inventory>`, specify inventory file path to use. In `<target>`, specify target host or group in inventory file. If `<target>` is not specified, `<role>` is used for target group. In `<dir>`, specify the directory including host_vars files or group_vars files. If `<dir>` is not specified, `host_vars` dir or `group_vars` dir searched as host_vars dir or group_vars dir. If `host_vars` dir or `group_vars` dir is not exist, no host_vars files or group_vars files are used. `-v` opton is specified, ansible-art deliver this option to ansible-playbook command. The more there is character `v`, we can get more detailed output. For example, the output of `-vvvv` option is more detailed than the one of `-v`
