# akeyless-platform-engineering-port
Demo Dynamic Database Secrets for MySQL in Kubernetes with Wordpress


## Setting up Akeyless

```bash
# Create a MySQL producer
akeyless create-dynamic-secret \
  --name "mysql-wp-producer" \
  --producer-type mysql \
  --mysql-host "your-mysql-host" \
  --mysql-port 3306 \
  --mysql-username "admin-user" \
  --mysql-password "admin-password"

# Create a role for accessing this producer
akeyless create-role --name "wordpress-db-role"

# Attach the role to the producer
akeyless attach-role --name "wordpress-db-role" \
  --item-name "mysql-wp-producer" \
  --access-type "read"
```