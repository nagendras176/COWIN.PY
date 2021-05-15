#!/bin/bash
echo ENTER PIN CODES TO BE ENTERED 
read PINCODE

while :
do
  python3 cowinphn.py ${PINCODE}
  echo ****************************************************************
  echo  DECRYPTION PROBLEM OCCURED 
  echo  RUNNING PROGRAM AGAIN
  echo ****************************************************************
done
}

