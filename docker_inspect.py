import json
import subprocess


def get_port_of_docker_container(container_id) -> int:
    cmd = f"docker inspect {container_id}"
    result = subprocess.run(cmd.split(), check=True, capture_output=True)
    container_data: str = result.stdout
    return get_host_port_from_docker_inspect_output(container_data)


def get_host_port_from_docker_inspect_output(data: str):
    data = json.loads(data)
    all_ports_data = data[0]['NetworkSettings']['Ports']
    port_data = all_ports_data[tuple(all_ports_data.keys())[0]][0]
    assert port_data['HostIp'] in ('0.0.0.0', '127.0.0.1')

    return int(port_data['HostPort'])
