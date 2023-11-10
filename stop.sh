plist=`ps -ef | grep -Ev grep | grep gunicorn | awk '{print $2}'`
for pid in ${plist}
do
    kill -9 $pid
done

