# Write a method palindrome_chain_length which takes a positive number and returns the number of 
# special steps needed to obtain a palindrome. The special step is: "reverse the digits, and add to the original number". 
# If the resulting number is not a palindrome, repeat the procedure with the sum until the resulting number is a palindrome.

def palindrome_chain_length(n):
    count = 0
    pol = n
    while str(pol) != str(pol)[::-1]:
        pol += int(str(pol)[::-1])
        count += 1
    return count

# Рекурсия ляпота best solution

def palindrome_chain_length(n, count=0):
    if str(n) == str(n)[::-1]: return count
    else: return palindrome_chain_length(n + int(str(n)[::-1]), count+1)
