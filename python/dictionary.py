env_vars = {
    "APP_ENV": "production",
    "DB_HOST": "localhost",
    "DB_PORT": 5432
}

print("App Environment:", env_vars["APP_ENV"])

for key, value in env_vars.items():
    print(f"{key} = {value}")