from datetime import datetime

def log_action(user, role, query, tool, status):
    with open("audit_log.txt", "a") as f:
        f.write(f"{datetime.now()} | User: {user} | Role: {role} | Query: {query} | Tool: {tool} | Status: {status}\n")