def split_sequences(s):
    seqs = []
    current_num = s[0]
    i = 0
    current_subseq = ""
    while i < len(s):
        while i < len(s) and s[i] == current_num:
            current_subseq += s[i]
            i += 1
        seqs.append(current_subseq)
        if i < len(s):
            current_num = s[i]
            current_subseq = ""
    return seqs

def parse_to_countable(arr):
    result = ""
    for elem in arr:
        result += str(len(elem)) + elem[0]
    return result

def countAndSay(n: int):
    encoding = "1"
    i = 1
    while i < n:
        encoding = parse_to_countable(split_sequences(encoding))
        i += 1
    return encoding
    
print(countAndSay(30))