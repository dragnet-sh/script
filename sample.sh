# Bulk rename files that contains Spaces
# ToDo - Find a better one liner to do this !!

for f in ./*; do mv "$f" "${f//-Table 1/}"; done
