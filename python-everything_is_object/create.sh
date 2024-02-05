#!/bin/bash

# Array of file names
declare -a files=("0-answer.txt"
                  "1-answer.txt"
                  "2-answer.txt"
                  "3-answer.txt"
                  "4-answer.txt"
                  "5-answer.txt"
                  "6-answer.txt"
                  "7-answer.txt"
                  "8-answer.txt"
                  "9-answer.txt"
                  "10-answer.txt"
                  "11-answer.txt"
                  "12-answer.txt"
                  "13-answer.txt"
                  "14-answer.txt"
                  "15-answer.txt"
                  "16-answer.txt"
                  "17-answer.txt"
                  "18-answer.txt"
                  "19-copy_list.py"
                  "20-answer.txt"
                  "21-answer.txt"
                  "22-answer.txt"
                  "23-answer.txt"
                  "24-answer.txt"
                  "25-answer.txt"
                  "26-answer.txt"
                  "27-answer.txt"
                  "28-answer.txt")

# Loop through the array and create each file
for file in "${files[@]}"
do
   touch "$file"
done

