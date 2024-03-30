import random
import string

pass_len=12
passvalue=string.ascii_letters+string.digits+string.punctuation

res="".join([random.choice(passvalue) for i in range(pass_len)])

print(res)

