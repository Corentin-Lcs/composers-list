def search_lines(file, search):
    found_lines = []
    with open(file, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            if search.lower() in line.lower():
                found_lines.append((i, line.strip()))
    return found_lines

file = 'composers.txt'
user_search = input("Enter your search : ")

found_lines = search_lines(file, user_search)

if len(found_lines) > 0:
    print("\nSearch results :\n")
    for line in found_lines:
        print(f"Line {line[0]} : {line[1]}")
else:
    print("\nNo results found for the specified search.")

print("\nNote : The .txt file is written in French.")