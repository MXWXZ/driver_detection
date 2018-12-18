grep Test $1 | grep "$2" | awk '{print $(NF-1)}'
