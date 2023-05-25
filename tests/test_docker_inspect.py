import unittest

from docker_inspect import get_host_port_from_docker_inspect_output

docker_inspect_output = '''
[
    {
        "Id": "bea5052ef7438f9265ed706dc54fe91d281c0645b8c9a86dee7127fc56ebc9c1",
        "Created": "2023-05-25T11:27:52.370596112Z",
        "Path": "docker-entrypoint.sh",
        "Args": [
            "redis-server",
            "--loadmodule",
            "/usr/lib/redis/modules/rejson.so"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 252667,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-05-25T11:27:52.736813017Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:a560d2f25517d8ac37a512a0e4fdf329f05e7328926d533b175100341e367098",
        "ResolvConfPath": "/var/lib/docker/containers/bea5052ef7438f9265ed706dc54fe91d281c0645b8c9a86dee7127fc56ebc9c1/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/bea5052ef7438f9265ed706dc54fe91d281c0645b8c9a86dee7127fc56ebc9c1/hostname",
        "HostsPath": "/var/lib/docker/containers/bea5052ef7438f9265ed706dc54fe91d281c0645b8c9a86dee7127fc56ebc9c1/hosts",
        "LogPath": "/var/lib/docker/containers/bea5052ef7438f9265ed706dc54fe91d281c0645b8c9a86dee7127fc56ebc9c1/bea5052ef7438f9265ed706dc54fe91d281c0645b8c9a86dee7127fc56ebc9c1-json.log",
        "Name": "/redis",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "6379/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "0"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                34,
                141
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/1c990d5ffb9d051a13ab89c6f814f27bad149a97932713a482394763fa1fcaa3-init/diff:/var/lib/docker/overlay2/b61bc8c91bb9d8a66a30b2a9f2c5b2190b8a961ad60264e47bc38dbbc8df6106/diff:/var/lib/docker/overlay2/76f28dd62288b90322e902a5657279efe70bd37597fb5f3d214e19ae01c202fd/diff:/var/lib/docker/overlay2/97d170bf7648a9ed888f038630e0f05231113c17707e6b931ff51eaafc24dafa/diff:/var/lib/docker/overlay2/406b021c63091578bd6fd503bea535b0f433101e865911da4e37649abcddd622/diff:/var/lib/docker/overlay2/05b2a9303779d6e47f95660e6a19fe5ba1197bc15ce7365a86fe9225fe1ad4b3/diff:/var/lib/docker/overlay2/9aa10c7c237e4512664e8be55d4fc5f2126d7c53d37c1b44954ae01bf1ce08ad/diff:/var/lib/docker/overlay2/15008dc611942e97d6e07f7532b6568541723d58d3c2b915a44fb4ca0d928154/diff:/var/lib/docker/overlay2/da60f95271da1dc2b54f5335220b9cb7308990c0236688ebeea65bd8195a2571/diff:/var/lib/docker/overlay2/1ae49381431bf04bc719c9afb8b18bef8ee947bb945ae005f6c336c0cd046bcd/diff:/var/lib/docker/overlay2/b07e20e830ea5d4027c6e6cb1c43d1fff1146ee728a31945663d96b43d3d1c70/diff:/var/lib/docker/overlay2/b3ea4c173b6fc05bef47d16e56c9d5f01a8f7d331d18c9fceac8e61bee700013/diff:/var/lib/docker/overlay2/d5b64de10d7b7e9084129b58ed4fb15bc1f3bb89c55203d58ca73f4bcbc8d93d/diff:/var/lib/docker/overlay2/eb37a555619fb20ab5f187f2d84db7d0a2b739e9556005a3ae88e55a95bd5961/diff:/var/lib/docker/overlay2/8346c3581551f92db2106d0319949687c78ca464c223cd85477cdfb042d07442/diff:/var/lib/docker/overlay2/9b48a95132ff2c7b270379403ddac381a886735986606b10e0d08312e60396c5/diff:/var/lib/docker/overlay2/9b01da42b68bfaa1bdb52c98b59d93ae76474d5a950f9092c48e007d586604de/diff:/var/lib/docker/overlay2/3c3c99701cbc6b7656e7ef6124271255b4fb70434e304676b55ea6c2963a7a5d/diff:/var/lib/docker/overlay2/5b602eefe0628e48289e1496b70ac96f732fff92964a68e8d66f1ba0f9762d71/diff:/var/lib/docker/overlay2/bc109dc65f2157590f721bec804e7b3f1889b9210725239cb5f729e443057404/diff:/var/lib/docker/overlay2/0c5347f87a3c9605a5ebaa477ec5827f965efd9fdecc363d08c1de4df17289ed/diff:/var/lib/docker/overlay2/9b0d16e3e1b5caced2f25ec8df6b810a407c6abb3fd2a889d463a07728837758/diff",
                "MergedDir": "/var/lib/docker/overlay2/1c990d5ffb9d051a13ab89c6f814f27bad149a97932713a482394763fa1fcaa3/merged",
                "UpperDir": "/var/lib/docker/overlay2/1c990d5ffb9d051a13ab89c6f814f27bad149a97932713a482394763fa1fcaa3/diff",
                "WorkDir": "/var/lib/docker/overlay2/1c990d5ffb9d051a13ab89c6f814f27bad149a97932713a482394763fa1fcaa3/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [
            {
                "Type": "volume",
                "Name": "a03b7966ad73d9c4f44f4e6ef878091f430429aa3bdb3756b4bc9e1d55369a5b",
                "Source": "/var/lib/docker/volumes/a03b7966ad73d9c4f44f4e6ef878091f430429aa3bdb3756b4bc9e1d55369a5b/_data",
                "Destination": "/data",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ],
        "Config": {
            "Hostname": "bea5052ef743",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "6379/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "redis-server",
                "--loadmodule",
                "/usr/lib/redis/modules/rejson.so"
            ],
            "Image": "redislabs/rejson",
            "Volumes": {
                "/data": {}
            },
            "WorkingDir": "/data",
            "Entrypoint": [
                "docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "8e385b718f9fbfa0dec40b25a0277bcf6e0fcd39531b4b2e8499dc42aae69167",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "6379/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "32769"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "32769"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/8e385b718f9f",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "bca12db5851b6ceb46ddd639f2d42b034338419b096ba90601d90c019db73cc1",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.3",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:03",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "2b75952ea6e1e39b60112a3f038860b4b2d110a858b11d600b92312f1c6965de",
                    "EndpointID": "bca12db5851b6ceb46ddd639f2d42b034338419b096ba90601d90c019db73cc1",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.3",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:03",
                    "DriverOpts": null
                }
            }
        }
    }
]
'''


class TestGetHostPortOfContainer(unittest.TestCase):
    def test_get_host_port_from_docker_inspect(self):
        result = get_host_port_from_docker_inspect_output(
            docker_inspect_output)
        target = 32769
        self.assertEqual(result, target)
