with open("pyproject.toml", "w", encoding="utf-8") as f:
    f.write("""[project]
name = "health-app"
version = "1.0.0"
description = "My Health Home - Home Health Application"
requires-python = ">=3.12,<3.13"
dependencies = [
    "flet==1.0.2"
]

[tool.flet]
product = "???? ????? ??"
org = "com.healthcenter"
bundle_id = "com.healthcenter.myhealthhome"
build_number = 1

[tool.flet.app]
assets = "assets"

[tool.flet.android]
icon = "assets/icon.png"
""")