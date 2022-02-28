def powitanie(name, gender = 'Mr'):
    result = ""
    result = result + "Witaj %s" % gender
    for n in name:
        result = result + "%s" % name
    return result

if __name__ == "__main__":
    name_text = input("Type Your name:")
    name = name_text.splitlines()
    name_result = powitanie(name)
    print(name_result)