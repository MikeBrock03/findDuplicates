## assumption: plz (for now) delete all letters from the array you insert into array.txt until i test stuff more. don't worry about blank carriage returns though!

## you can just copy/paste from google sheets to notes (or notepad) then paste into array.txt

def find_duplicates(file_path):
  # use this one for typical dupes (mqid etc)
  numbers = []
  duplicates = []
  with open(file_path) as f:
    for line in f:
      # i think we should do line.isnumeric() but it messed things up and led to empty []
      if line.strip():
        line = line.strip()
        line = line.replace(",", "")
        number = int(line)
        if number in numbers:
          duplicates.append(number)
        else:
          numbers.append(number)

  return duplicates


def find_same_beside(file_path):
  # use this one when trying to find duplicate sequences (same side by side)
  # returns index as the key (which is an ESTIMATE, the actual value is usually further ahead) and number as the value
  duplicates = {}
  prev_num = 0
  index = 0
  with open(file_path) as f:
    for line in f:
      if line.strip():
        line = line.strip()
        line = line.replace(",", "")
        number = int(line)
        if number == prev_num:
          duplicates[index] = number
        prev_num = number
        print(prev_num)
        index += 1
  return duplicates


file_name = 'array.txt'

## SUBSTITUE BELOW LINE FOR WHICH FUNCTION YOU'RE USING THIS FOR
duplicates = find_same_beside(file_name)
print(duplicates)
