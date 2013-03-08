ping -q -c 4 $1 | grep 'packets received' | awk {'print $4'}
