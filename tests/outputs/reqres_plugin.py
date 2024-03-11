from locust import run_single_user, task

import re

from svs_locust import RestUser


class reqres_in(RestUser):
    default_headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "sv,en;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    }

    @task
    def t(self):
        with self.rest("POST", "/api/register", json={"email": "eve.holt@reqres.in", "password": "pistol"}) as resp:
            job = re.findall('"token":"([^"]*)"', resp.text)[0] if resp.text else None
        with self.rest("PATCH", "/api/users/2", json={"name": "morpheus", "job": job}) as resp:
            pass


if __name__ == "__main__":
    run_single_user(reqres_in)
