from pathlib import Path

package_name = "{{cookiecutter.package_name}}".strip()
if package_name == "":
    # This project does not contain a Python package, hence, remove setup.py.
    Path("setup.py").unlink(missing_ok=True)

license = "{{cookiecutter.open_source_license}}"
if license == "No license file":
    Path("LICENSE").unlink(missing_ok=True)

# Display next steps.
message = [
    "#" * 80,
    "# Congratulations, your project has been initialized!",
    "#",
    "# Recommended next steps:",
    "# - git init",
    "# - pre-commit autoupdate",
    "# - pre-commit install",
    "# - review README.md",
]
if license != "No license file":
    message.append("# - review LICENSE")
if package_name != "":
    message += [
        "# - review and update setup.py, then remove the exception at the end.",
        "# - consider to adopt versioneer to version your package.",
    ]
message += [
    "# - git add .",
    "# - git commit",
    "#" * 80,
]
print(*message, sep="\n")
