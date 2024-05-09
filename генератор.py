
def all_variants(s):
    for length in range(1, len(s) + 1):
        for start in range(len(s) - length + 1):
            yield s[start:start + length]


input_string = "abc"
for subs in all_variants(input_string):
    print(subs)
