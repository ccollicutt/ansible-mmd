#!/bin/bash

for s in 1 2 3; do
    echo "INFO: Deleting mm$s..."
    nova delete mm${s}
    sleep 2
    echo "INFO: Deleting ms$s..."
    nova delete ms${s}
    sleep 2
done

echo "INFO: Done!"
    
