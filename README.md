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


**Table of Content**
<!-- TOC -->

- [kubectl-plugin-ssh-jump](#kubectl-plugin-ssh-jump)
    - [Pre-requistes](#pre-requistes)
    - [Installation](#installation)
        - [Install through krew](#install-through-krew)
        - [Manual Installation](#manual-installation)
    - [How to use](#how-to-use)
        - [Usage](#usage)
            - [Option parameters Cache](#option-parameters-cache)
            - [SSH Agent (ssh-agent)](#ssh-agent-ssh-agent)
        - [Examples](#examples)
            - [Scenario1 - You have private & public SSH key on your side](#scenario1---you-have-private--public-ssh-key-on-your-side)
            - [Scenario2 - You have .pem file but you don't have public key on your side](#scenario2---you-have-pem-file-but-you-dont-have-public-key-on-your-side)
    - [Useful Links](#useful-links)
    - [Contributing](#contributing)

<!-- /TOC -->


## Pre-requistes
This plugin needs the following programs:
* ssh(1)	
* ssh-agent(1)
* ssh-keygen(1)

## Installation

### Install through krew
This is a way to install kubectl-ssh-jump through [krew](https://krew.sigs.k8s.io/). After installing krew by following [this](https://krew.sigs.k8s.io/docs/user-guide/setup/install/), you can install kubectl-ssh-jump like this:

```sh
$ kubectl krew install ssh-jump
```

Expected output would be like this:
```
Updated the local copy of plugin index.
Installing plugin: ssh-jump
CAVEATS:
\
 |  This plugin needs the following programs:
 |  * ssh(1)
 |  * ssh-agent(1)
 |
 |  Please follow the documentation: https://github.com/yokawasa/kubectl-plugin-ssh-jump
/
Installed plugin: ssh-jump
```

Once it's installed, run:
```sh
$ kubectl plugin list

The following kubectl-compatible plugins are available:

/Users/yoichika/.krew/bin/kubectl-krew
/Users/yoichika/.krew/bin/kubectl-ssh_jump

$ kubectl ssh-jump
```

### Manual Installation

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
  Scenario1 - You have .pem file
  $ kubectl ssh-jump -u ec2-user -i ~/.ssh/mykey.pem hostname
```

## Useful Links

- [Extend kubectl with plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/)
- [Write your own kubectl subcommands](https://ahmet.im/blog/kubectl-plugins/)
- [SSH-AGENT - SINGLE SIGN-ON USING SSH](https://www.ssh.com/ssh/agent)

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/yokawasa/kubectl-plugin-ssh-jump
