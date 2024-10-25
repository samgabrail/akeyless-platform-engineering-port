# Overview

This is our standard Boilterplate Python Flask app in our organization. It uses Akeyless to dynamically rotate database credentials for a MySQL database.

## Version Management

To release a new version:

1. Make your code changes
2. Create and push a new tag: `git tag -a v1.0.1 -m "Release version 1.0.1"`
3. Push the tag: `git push origin v1.0.1`

This will:
- Trigger the build workflow
- Build and push a new versioned container image
- Keep 'latest' tag updated with most recent version