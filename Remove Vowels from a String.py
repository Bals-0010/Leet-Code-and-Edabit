# instructions pending


def testing(string):
    
    vowels_list = ['a','e','i','o','u','A','E','I','O','U']
    str_list = [i for i in string if i not in vowels_list]
    final_list = "".join(str_list)
    
    return final_list 

print(testing("thisi is a string example"))