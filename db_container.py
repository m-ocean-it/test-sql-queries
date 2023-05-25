import subprocess
import time

from docker_inspect import get_port_of_docker_container


class DbContainer:
    db_password = 'my_password'
    set_up_db_cmd = f"docker run -e POSTGRES_PASSWORD={db_password} -p 0:5432 -d --rm postgres"

    def __init__(self):
        process_result = subprocess.run(self.set_up_db_cmd.split(),
                                        check=True, capture_output=True)

        self.container_id = process_result.stdout.decode('utf-8')
        self.mapped_port = get_port_of_docker_container(self.container_id)

        self.check_db_health_cmd = f"docker exec {self.container_id} pg_isready -U postgres -d postgres"
        self.tear_down_db_cmd = f"docker stop {self.container_id}"

    def wait_until_ready(self):
        healthcheck_count = 0
        while True:
            if healthcheck_count > 20:
                raise TimeoutError
            if self.is_ready():
                break
            healthcheck_count += 1
            time.sleep(1)

    def is_ready(self) -> bool:
        process_result = subprocess.run(self.check_db_health_cmd.split(),
                                        capture_output=True, check=False)
        return process_result.returncode == 0

    def stop(self):
        subprocess.run(self.tear_down_db_cmd.split(),
                       check=True, capture_output=True)
