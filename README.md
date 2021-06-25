# kubectl-plugin-ssh-jump

[![kubectl plugin](https://img.shields.io/badge/kubectl-plugin-blue.svg)](https://github.com/topics/kubectl-plugin)

A kubectl plugin to SSH into Kubernetes nodes using a SSH jump host Pod

A `jump host` Pod is an intermediary Pod or an SSH gateway to Kubernetes node machines, through which a connection can be made to the node machines.

Here is an scenario where you want to connect to Kubernetes node, but you have to go through a jump host Pod, because of firewalling, access privileges. etc. There is a number of valid reasons why the jump hosts are needed...

![](assets/arch-ssh-jumphost.png)

> [NOTE]
> - Kubectl versions >= `1.12.0` (Preferred)
>   - As of Kubernetes 1.12, kubectl now allows adding external executables as subcommands. For more detail, see [Extend kubectl with plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/)
>   - You can run the pluin with `kubectl ssh-jump ...`
> - Kubectl versions < `1.12.0`
>   - You still can run the plugin directly with `kubectl-ssh-jump ...`

## Pre-requistes
This plugin needs the following programs:
* ssh
* ssh-agent
* ssh-keygen

## Installation

Install the plugin by copying the script in the $PATH of your shell.

```sh
# Get source
$ git clone https://github.com/yokawasa/kubectl-plugin-ssh-jump.git
$ cd kubectl-plugin-ssh-jump
$ chmod +x kubectl-ssh-jump
# Add kubeclt-ssh-jump to the install path.
$ sudo cp -p kubectl-ssh-jump /usr/local/bin
```

Once in the $PATH, run:
```sh
$ kubectl plugin list

The following kubectl-compatible plugins are available:
/usr/local/bin/kubectl-ssh-jump

$ kubectl ssh-jump
```

## How to use

### Usage

```TXT
Usage:
  kubectl ssh-jump <dest_node> [options]

Options:
  <dest_node>                     Destination node name or IP address
                                  dest_node must start from the following letters:
                                  ASCII letters 'a' through 'z' or 'A' through 'Z',
                                  the digits '0' through '9', or hyphen ('-')
  -u, --user <sshuser>            SSH User name
  -i, --identity <identity_file>  Identity key file, or PEM(Privacy Enhanced Mail)
  -P, --port <port>               SSH port for target node SSH server (default:22)
  -a, --args <args>               Args to exec in ssh session
  -h, --help                      Show this message

Example:
  $ kubectl ssh-jump -u admin -i ~/.ssh/mykey.pem rabbit.internal.prod
```

## Useful Links

- [Extend kubectl with plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/)
- [Write your own kubectl subcommands](https://ahmet.im/blog/kubectl-plugins/)
- [SSH-AGENT - SINGLE SIGN-ON USING SSH](https://www.ssh.com/ssh/agent)

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/tomislater/kubectl-plugin-ssh-jump
