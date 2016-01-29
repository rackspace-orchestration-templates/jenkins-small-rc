Description
===========

#### Production - RCv3

A single Linux server running the lastest stable version of
[Jenkins CI](http://jenkins-ci.org/content/about-jenkins-ci) Server,
with up to 10 optional worker nodes (connected via Swarm).


Instructions
===========

#### Accessing Jenkins
In a browser, navigate to the URL provided in the output section. Once logged
in, you can immediately create a [new
job](https://wiki.jenkins-ci.org/display/JENKINS/Building+a+software+project)!
#### Logging in via SSH
The private key provided in the passwords section can be used to login as
root via SSH.  We have an article on how to use these keys with [Mac OS X and
Linux](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-linuxmac)
as well as [Windows using
PuTTY](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-windows).
#### Plugins
Jenkins offers a wide range of useful plugins that can be used to expand both
the features as well as capacity of your test environments. Check out the
[Jenkins
Plugins](https://wiki.jenkins-ci.org/display/JENKINS/Plugins#Plugins-Usingtheinterface)
documentation for information on how to easily install and use plugins
through the web interface.
#### Additional Notes
You can add or remove worker nodes to this deployment by updating the
"server_count" parameter for this stack.


Requirements
============
* A Heat provider that supports the following:
  * OS::Heat::ResourceGroup
  * OS::Heat::SoftwareConfig
  * OS::Heat::SoftwareDeployment
  * OS::Nova::KeyPair
  * OS::Nova::Server
  * Rackspace::Cloud::BackupConfig
  * Rackspace::RackConnect::PublicIP
* An OpenStack username, password, and tenant id.
* [python-heatclient](https://github.com/openstack/python-heatclient)
`>= v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual
environment](http://www.virtualenv.org/).

Parameters
==========
Parameters can be replaced with your own values when standing up a stack. Use
the `-P` flag to specify a custom parameter.

* `jenkins_email`: E-mail Address for Jenkins Admin User (Default: admin@example.com)
* `rc_network_name`: Name or UUID of RackConnected network to attach this server to 
* `flavor`: Flavor of Cloud Server to use for Jenkins (Default: 4 GB General Purpose v1)
* `slave_flavor`: Flavor of Cloud Server to use for Jenkins Workers (Default: 4 GB General Purpose v1)
* `server_count`: Number of secondary worker nodes (Default: 0)

Outputs
=======
Once a stack comes online, use `heat output-list` to see all available outputs.
Use `heat output-show <OUTPUT NAME>` to get the value of a specific output.

* `jenkins_public_ip`: Jenkins Public IP 
* `jenkins_public_url`: Jenkins Public URL 
* `ssh_private_key`: SSH Private Key 
* `secondary_ips`: Secondary Node IPs 

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.
