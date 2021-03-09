# https://github.com/cookiecutter/cookiecutter/issues/913#issuecomment-683764686

from pathlib import Path

package_name = "{{cookiecutter.package_name}}".strip()

# This project does not contain a Python package, hence, remove setup.py.
if package_name == "":
    Path("setup.py").unlink(missing_ok=True)

# Display next steps.
message = [
    "#" * 80,
    "# Congratulations, your project has been initialized!",
    "#",
    "# Recommended next steps:",
    "# - git init",
    "# - pre-commit autoupdate",
    "# - pre-commit install",
]
if package_name != "":
    message += [
        "# - review and update setup.py, then remove the exception at the end.",
        "# - consider to adopt versioneer to version your package.",
    ]
message.append("#" * 80)
print(*message, sep="\n")
