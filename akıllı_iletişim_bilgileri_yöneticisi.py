def organize_contacts(contact_list):
    def is_valid_email(email):
        return '@' in email and '.' in email and " " not in email
    
    def clean_phone(phone):
        digits = ''.join(filter(str.isdigit, phone))
        return digits if len(digits) == 10 else None
    
    def clean_contact(contact):
        return {
            'name': contact['name'],
            'email': contact['email'].lower(),
            'phone': clean_phone(contact['phone'])
        }

    cleaned_contacts = []
    seen_emails = set()
    seen_phones = set()
    for contact in contact_list:
        cleaned = clean_contact(contact)
        if not is_valid_email(cleaned['email']) or cleaned['phone'] is None:
            continue
        if cleaned['email'] in seen_emails or cleaned['phone'] in seen_phones:
            continue
        seen_emails.add(cleaned['email'])
        seen_phones.add(cleaned['phone'])
        cleaned_contacts.append(cleaned)
        
    return cleaned_contacts