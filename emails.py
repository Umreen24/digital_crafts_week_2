
email_file = "emails.txt"
new_file_name = "duplicate-free-emails.txt"

duplicate_free_emails = []

with open(email_file) as file_object:
    contents = file_object.read()
    contents = contents.replace("\n", "")

emails = contents.split(', ')

for email in emails:
    if email not in duplicate_free_emails:
        duplicate_free_emails.append(email)

#look up replace function in python

print(emails)


with open(new_file_name, "w") as file_object:
    for item in duplicate_free_emails:
        file_object.write(item + "\n|")