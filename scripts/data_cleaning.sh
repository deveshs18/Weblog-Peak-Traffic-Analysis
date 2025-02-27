
emove headers and fix log formatting
awk -F, 'NR==1 {print "IP,Time,URL,Status"; next} 
{gsub(/\[|\]/,"",$2); gsub(/ HTTP.*/,"",$3); print $1","$2","$3","$4}' weblog.csv > cleaned_weblog.csv

echo "Log file cleaned successfully. Output: cleaned_weblog.csv"

