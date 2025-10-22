#!/bin/bash
# PostgreSQL Installation Guide Script
# This script provides commands for installing PostgreSQL on different operating systems
# Usage: Choose your operating system section and uncomment the relevant commands

# Print header information
cat << 'EOF'
PostgreSQL Installation Guide
============================

This script contains commands for installing PostgreSQL on different operating systems.
Please uncomment the appropriate commands for your system before running.

EOF

#####################################################
# 1. MACOS INSTALLATION (using Homebrew)
#####################################################
cat << 'EOF'
1. MACOS INSTALLATION (using Homebrew)
-------------------------------------
EOF

# Update Homebrew
# brew update

# Install PostgreSQL
# brew install postgresql

# Start PostgreSQL service
# brew services start postgresql

# Verify installation
# postgres --version
# psql --version

#####################################################
# 2. WINDOWS INSTALLATION
#####################################################
cat << 'EOF'

2. WINDOWS INSTALLATION
---------------------
EOF

# Windows installation is typically done through the installer
# Download the installer from: https://www.postgresql.org/download/windows/
# Run the installer and follow the installation wizard
# Make note of the password you set for the postgres user
# The installer will also install pgAdmin by default

# Verify installation by opening Command Prompt and typing:
# psql -U postgres

#####################################################
# 3. LINUX INSTALLATION (Ubuntu/Debian)
#####################################################
cat << 'EOF'

3. LINUX INSTALLATION (Ubuntu/Debian)
----------------------------------
EOF

# Update package lists
# sudo apt update

# Install PostgreSQL and contrib package
# sudo apt install postgresql postgresql-contrib

# Verify installation
# sudo systemctl status postgresql

# Connect to PostgreSQL
# sudo -u postgres psql

#####################################################
# 4. BASIC CONFIGURATION
#####################################################
cat << 'EOF'

4. BASIC CONFIGURATION
-------------------
EOF

# Connect to PostgreSQL (all platforms)
# psql -U postgres

# Inside psql, you can:
# - List all databases: \l
# - Connect to a database: \c database_name
# - List all tables: \dt
# - Get help: \?
# - Quit: \q

#####################################################
# 5. FIRST CONNECTION
#####################################################
cat << 'EOF'

5. FIRST CONNECTION
----------------
EOF

# For macOS/Linux:
# psql -U postgres

# For Windows:
# psql -U postgres
# (You'll be prompted for the password you set during installation)

cat << 'EOF'

Note: This is a reference script. Please uncomment the commands for your system before running.
To use this script:
1. Edit this file and uncomment the commands for your operating system
2. Make it executable: chmod +x installation_guide.sh
3. Run it: ./installation_guide.sh
EOF