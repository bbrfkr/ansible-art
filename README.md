# ansible-art
ansible apply role tool: ansible-art is a simple tool to apply role of ansible.

## abstract
To apply role of ansible, we need to write playbook for each role in conventional. By using ansible-art, we can apply role to machines without writing playbook by ourself. ansible-art will create playbook instead of us.

## install
```
pip install ansible-art
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
ansible-art apply <role> <inventory> [-t <target>] [-p <dir>] [-g <dir>]
```

- ansible-art [help]

 show help message and exit.
 
- ansible-art version

 show version and exit.

- ansbile-art role list

 show roles in the dir set in advance by using command "ansible-art dir set \<dir\>".

- ansible-art role params \<role\>

 show parameters defined in defaults/main.yml of specified role.
 
- ansible-art role dir show

 show the dir in advance by using command "ansible-art dir set \<dir\> ".

- ansible-art role dir set \<dir\>

 set dir to use other subcommands of ansible-art.
 
- ansible-art apply \<role\> \<inventory\> \[-t \<target\>\] \[-p \<dir\>\] \[-g \<dir\>\]  

 apply role target machine. in \<role\>, specify role wanted to apply. in \<inventory\>, specify inventory file path to use. in \<target\>, specify target host or group in inventory file. If \<target\> is not specified, \<role\> is used for target group. in \<dir\>, specify the directory includding host_vars files or group_vars files. If \<dir\> is not specified, `host_vars` dir or `group_vars` dir searched as host_vars dir or group_vars dir. If `host_vars` dir or `group_vars` dir is not exist, no host_vars files or group_vars files are used. 
