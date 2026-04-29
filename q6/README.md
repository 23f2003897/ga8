# Question 6: MLOps Bash Script

## Objective
Create a deterministic bash script commonly used in MLOps workflows to create directories, generate dummy run files, and compute a chain of SHA-256 hashes to ensure data integrity.

## Application Logic
1. Creates a target directory (`data`).
2. Generates 5 empty files (`run_1.txt` to `run_5.txt`).
3. Computes the SHA-256 hash for each filename (first 8 characters).
4. Concatenates all individual hashes.
5. Computes a final combined SHA-256 hash of the concatenated string.

## Execution Result (Assignment Submission)
DIR:data|FILES:5|HASH:fd9b54db

## Tech Stack
- Language: Bash
- Core Commands: mkdir, touch, seq, sha256sum, cut, echo

## How to Run
Ensure you are in a Bash environment (like Git Bash or WSL) and run:
bash process.sh
