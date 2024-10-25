# Overview

This is our standard Boilerplate Python Flask app in our organization. It uses Akeyless to dynamically rotate database credentials for a MySQL database.

## Initial Setup

Before starting development, ensure package access is configured:

1. Navigate to Package Settings
   - Go to GitHub profile > Packages
   - Select the `flask-todo` package
   - Click "Package settings"
   - Or directly visit: `https://github.com/users/[YOUR_USERNAME]/packages/container/flask-todo/settings`

2. Configure Repository Access
   - Under "Manage Actions access"
   - Click "Add Repository"
   - Search for and select this repository
   - Click "Add repository"
   - Change role to "Write"

## Development Workflow

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Your changes"
   ```

3. Push your branch and create a PR:
   ```bash
   git push origin feature/your-feature-name
   ```

4. After PR review and approval, merge to main

5. After verifying the changes in main, create and push a version tag:
   ```bash
   git checkout main
   git pull
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

This will:
- Build and push a new versioned container image
- Update the deployment manifest
- Trigger ArgoCD to deploy the new version

## Troubleshooting

If GitHub Actions fail to push new container images:
1. Verify package access is configured correctly
2. Ensure this repository is listed under "Manage Actions access" in package settings
3. Contact your platform team if issues persist
