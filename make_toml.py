with open("pyproject.toml", "w", encoding="utf-8") as f:
    f.write("""[project]
name = "health-app"
version = "1.0.0"
description = "Health Center App"
requires-python = ">=3.12,<3.13"
dependencies = [
    "flet==0.24.1"
]

[tool.flet]
product = "Health Center"
org = "com.healthcenter"
bundle_id = "com.healthcenter.app"
build_number = 1
""")