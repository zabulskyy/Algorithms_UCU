def sort(input):
  for i in range(len(input)):
      j = i

      while j != 0 and (
          (input[j] % 2 == 1 and input[j] > input[j - 1]) or
          (input[j] % 2 == 0 and input[j] < input[j - 1]) or
          (input[j - 1] % 2 == 1 and input[j] % 2 == 0)
      ):
          if (input[j - 1] % 2 == 0 and input[j] % 2 == 1):
              break
          input[j], input[j-1] =  input[j-1], input[j]
          j -= 1

  return input

if __name__ == "__main__":
    sort([1,9,0,0,8,5,6,7,7,4,2,3,8,7,6,33,55,66,77,55,33,22,56,65,98,0,1282])
