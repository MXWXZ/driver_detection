grep Test $1 | grep "Iteration" | awk -F',' '{print $1}' | awk '{print $NF}'
