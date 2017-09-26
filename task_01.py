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
