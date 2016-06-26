# ansible-art
ansible apply role tool: ansible-art is a simple tool to apply role of ansible.

## abstract
To apply role of ansible, we need to write playbook for each role in conventional. By using ansible-art, we can apply role to machines directly, without writing playbook by ourself. ansible-art will create playbook instead of us.

## install
1. First, install ansible-art with `pip` command.
```
pip install ansible-art
```
2. Second, set the directory of roles installed in advance. Please specify the directory of roles installed in advance to `DIR`.
```
ansible-art role dir set DIR
```

## usage
```
usage: ansible-art [-h] [-V] {role,apply} ...

A simple tool to apply role of ansible

optional arguments:
  -h, --help     show this help message and exit
  -V, --version  show version and exit

subcommands:
  valid subcommands

  {role,apply}
    role         operate with roles used by ansible-art
    apply        apply role to machines
```

```
usage: ansible-art role [-h] {list,params,dir} ...

operate with roles used by ansible-art

optional arguments:
  -h, --help         show this help message and exit

subcommands:
  valid subcommands

  {list,params,dir}
    list             show roles in the dir set in advance by using command
                     "ansible-art dir set DIR"
    params           show parameters defined in defaults/main.yml of specified
                     role
    dir              operate with the roles dir used by ansible-art
```

```
usage: ansible-art role params [-h] ROLE

show parameters defined in defaults/main.yml of specified role

positional arguments:
  ROLE        the role whose parameters are wanted to show

optional arguments:
  -h, --help  show this help message and exit
```

```
usage: ansible-art role dir [-h] {show,set} ...

operate with the roles dir used by ansible-art

optional arguments:
  -h, --help  show this help message and exit

subcommands:
  valid subcommands

  {show,set}
    show      show the dir path set in advance by using command "ansible-art
              dir set DIR"
    set       set the dir of roles used by other subcommands of ansible-art
```

```
usage: ansible-art role dir set [-h] DIR

set the dir of roles used by other subcommands of ansible-art

positional arguments:
  DIR         the dir of roles used by ansible-art

optional arguments:
  -h, --help  show this help message and exit
```

```
usage: ansible-art apply [-h] [-t TARGET] [-p DIR] [-g DIR] [-v]
                         ROLE INVENTORY

apply role to machines

positional arguments:
  ROLE                  the role wanted to apply
  INVENTORY             an inventory file path

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        specify hostname, ip, or group name in inventory file
                        corresponding to target host or group
  -p DIR, --params DIR  specify the directory including host_vars files. if
                        this parameter is not specified, ansible-art search
                        "host_vars" dir as the directory including host_vars
                        files. If "host_vars" dir is not found, no host_vars
                        files are used
  -g DIR, --group-params DIR
                        specify the directory including group_vars files. if
                        this parameter is not specified, ansible-art search
                        "group_vars" dir as the directory including group_vars
                        files. If "group_vars" dir is not found, no group_vars
                        files are used
  -v, --verbose         verbose output option. if this option is specified,
                        ansible-art deliver this option to ansible-playbook
                        command. the more there is character "v", we can get
                        more detailed output. for example, the output of
                        "-vvvv" option is more detailed than the one of "-v"
```
