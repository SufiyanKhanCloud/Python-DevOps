tool_versions = {"docker": "20.10", "kubernetes": "1.23"}
print(tool_versions["docker"])

tool_versions["terraform"] = "1.1"
print(tool_versions)

del tool_versions["docker"]
print(tool_versions)

for tool, version in tool_versions.items():
    print(tool, version)