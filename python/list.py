tools = ["docker", "github", "jenkins"]
print(tools)
print(tools[0])
print(tools[1])
print(tools[2])

tools.append("gitlab")
print(tools)
tools.remove("docker")
print(tools)

for tool in tools:
    print(tool)