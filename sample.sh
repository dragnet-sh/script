# Bulk rename files that contains Spaces
# ToDo - Find a better one liner to do this !!

for f in ./*; do mv "$f" "${f//-Table 1/}"; done

# Extracting specific words from Annotations
grep "Highlight.*\:\s[a-zA-Z]\+:\?$" ./ETS_Big_Verbal.txt | cut -d ':' -f 2 | awk '{print tolower($0);}'

# Extracting the task title from doing and creating a new entry
doing recent 1 | egrep -o ">(.*?)@" | sed -r 's/>\s|\s@//g' | xargs doing now

# Extracting the frist word of each line
cat VMain__* | awk '{print tolower($1);}' | sort >> archive.txt
