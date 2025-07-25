def clean_email_list(emails):
    processed_emails = map(lambda email: email.strip().lower(), emails)
    def is_valid(email):
        if email.count("@") != 1:
            return False
        splitted = email.split("@")
        if len(splitted[0]) > 0 and len(splitted[1]) > 0:
            return True
        return False
    valid_email = filter(is_valid, processed_emails)
    return list(valid_email)