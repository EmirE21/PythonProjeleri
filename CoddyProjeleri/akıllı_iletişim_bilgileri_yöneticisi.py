def organize_contacts(contact_list):
  def is_valid_email(email):
    return "@" in email and "." in email and " " not in email
  def clean_phone(phone):
    # Add a check to ensure the input is a string
    if not isinstance(phone, str):
      return None
    digits = "".join(filter(str.isdigit, phone))
    return digits if len(digits) == 10 else None
  def clean_contact(contact):
    return {
        "name": contact["name"],
        "email": contact["email"].lower(),
        "phone": clean_phone(contact["phone"])
    }
  cleaned_contacts = []
  seen_emails = set()
  seen_phones = set()
  for contact in contact_list:
    cleaned = clean_contact(contact)
    valid_email = is_valid_email(cleaned["email"])
    if not valid_email or cleaned["phone"] is None:
      continue
    if cleaned["email"] in seen_emails or cleaned["phone"] in seen_phones:
      continue
    seen_emails.add(cleaned["email"])
    seen_phones.add(cleaned["phone"])
    cleaned_contacts.append(cleaned)
  return cleaned_contacts

contact_list = [{"name": "John Doe", "email": "JOHN@email.com", "phone": "123-456-7890"}, {"name": "Jane Doe", "email": "jane@email.com", "phone": "123.456.7890"}, {"name": "Bob Smith", "email": "invalid.email", "phone": "12345"}]
print(organize_contacts(contact_list))