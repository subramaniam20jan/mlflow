import requests
from jinja2 import Template

def find_latest_pkg_version(pkg_name: str = "mlflow"):
    pkg_url = f"https://pypi.org/pypi/{pkg_name}/json"

    response = requests.get(pkg_url)
    assert response.status_code == 200

    response_payload = response.json()
    release_map = [(release, response_payload["releases"][release][0]["upload_time"]) for release in response_payload["releases"]]
    latest_release = sorted(release_map, key=lambda tup: tup[1], reverse=True)[0][0]

    return latest_release

def apply_to_template(file_name: str, values: dict):
    with open(f"templates/{file_name}", "r") as file:
        file_content = file.read()

    file_template = Template(file_content)
    rendered_file = file_template.render(**values)

    with open(file_name, "w") as file:
        file.write(rendered_file)

if __name__ == "__main__":
    apply_to_template("requirements.txt", {"mlflow_version": find_latest_pkg_version("mlflow")})
    apply_to_template("Dockerfile", {"python_version": "3.10"})
