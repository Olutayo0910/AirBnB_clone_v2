#!/bin/bash

# Create destination directories if they don't exist
mkdir -p web_flask/static/images

# Copy CSS files to the destination directory
cp web_static/styles/3-footer.css web_flask/static/styles/
cp web_static/styles/3-header.css web_flask/static/styles/
cp web_static/styles/4-common.css web_flask/static/styles/
cp web_static/styles/6-filters.css web_flask/static/styles/

# Copy image files to the destination directory
cp web_static/images/icon.png web_flask/static/images/
cp web_static/images/logo.png web_flask/static/images/

# Update .popover class in 6-filters.css
sed -i 's/\.popover/\.popover { overflow-y: auto; max-height: 300px; }/g' web_flask/static/styles/6-filters.css

# Print a message indicating completion
echo "Files copied and updated successfully."
