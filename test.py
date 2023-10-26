def extract_url(string):
    first_quote = string.find('"')
    string = string[first_quote + 1:]
    second_quote = string.find('"')
    string = string[:second_quote]

    return string
