#!/usr/bin/env bash

timezone="Asia/Shanghai"
# List of valid timezones: wikipedia.org/wiki/List_of_tz_database_time_zones
script="${0##*/}"
rootdir=$(cd `dirname "${BASH_SOURCE[0]}"` && pwd)
logfile="$script.log"
log="$rootdir/$logfile"
now=$(TZ=":$timezone" date)
# Uncomment 'mailto=' (remove #) to enable emailing the log upon completion
#mailto="your@email.com"
mailsubj="$script log from $now"
logging() {
  now=$(TZ=":$timezone" date)
  if [[ -z "$1" || -z "$2" ]]; then
    echo "$now [ERROR] Nothing to log. Use:\nlogging <level> <result>"
    exit 2
  else
    echo "$now [$1] $2" >> $log
  fi
}
if [ -z "$1" ]; then
  echo "$now [ERROR] Missing file input. Use:\n$rootdir/$script /path/to/urls.txt"
  exit 2
else
  input="$1"
fi
logging "INFO" "Reading file: $input"
cat $input|while read line; do
  if [ ! -z $line ]; then
      echo "INFO" "Crawling URL: $line"
      logging "INFO" "Crawling URL: $line"
      curlstart=$(date +"%s")
      #curlresult=`curl -sSL -w '%{http_code} %{url_effective}' $line -o ../data/$input/$curlstart.html`
      curlresult=`curl -sSL -w '%{http_code} %{url_effective}' $line |  iconv -sc -t utf-8 > ../data/$input/$curlstart.html`
      # curl parameters: -sS = silent; -L = follow redirects; -w = custom output format; -o = trash output
      logging "INFO" "$curlresult"
      curldone=$(date +"%s")
      difftime=$(($curldone-$curlstart))
      logging "INFO" "Crawl-time: $(($difftime / 3600)):$(($difftime / 60)):$(($difftime % 60))"
  fi
done
logging "INFO" "Done reading file: $input"
if [ ! -z "$mailto" -a "$mailto" != " " ]; then
  logging "INFO" "Sending Email to: $mailto"
  # Using postfix mail command to email the logfile contents
  cat $log | mail -s "$mailsubj" $mailto
fi
exit