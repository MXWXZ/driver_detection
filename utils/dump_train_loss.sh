grep 'Iteration.*loss' $1 | awk '{print $(NF-3) $NF}'
