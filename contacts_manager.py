contact_list =[{
    "name": "hillary",
    "phone":"1",
    "email":"win"},{
    "name": "willy",
    "phone": "1",
    "email": "win"}]
search_name  = "hillary"
matching_contacts =[]


for contact in contact_list:
    if search_name.lower() == contact["name"].lower():
        matching_contacts.append(contact)
if len(matching_contacts)==0:
    print("Contact not found")
else:
    print(f"{len(matching_contacts)} contacts found")
    print(matching_contacts)
unique_names= set(contact["name"] for contact in contact_list)
unique_contacts = set(contact["phone"] for contact in contact_list)
print(unique_names)
print(unique_contacts)
