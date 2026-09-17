from collections import Counter

log_file = "sample_logs.txt"

failed_logins = []

with open(log_file, "r") as file:
    for line in file:
        if "Failed login" in line:
            failed_logins.append(line.strip())

print("=== Cybersecurity Log Analysis ===")
print(f"Total failed login attempts: {len(failed_logins)}")

usernames = []
ip_addresses = []

for log in failed_logins:
    parts = log.split()

    for part in parts:
        if part.startswith("username="):
            usernames.append(part.split("=")[1])

        if part.startswith("source_ip="):
            ip_addresses.append(part.split("=")[1])

print("\nFailed login attempts by username:")
for username, count in Counter(usernames).items():
    print(f"{username}: {count}")

print("\nFailed login attempts by IP address:")
for ip, count in Counter(ip_addresses).items():
    print(f"{ip}: {count}")

print("\nPotentially suspicious activity:")

for ip, count in Counter(ip_addresses).items():
    if count >= 5:
        print(f"WARNING: {ip} generated {count} failed login attempts.")
