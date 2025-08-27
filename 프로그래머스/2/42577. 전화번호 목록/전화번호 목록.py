def solution(phone_book):
    phone_dict = {phone: True for phone in phone_book}
    for phone in phone_book:
        prefix = ""
        for c in phone[:-1]:
            # print(c)
            prefix += c
            if prefix in phone_dict:
                # print(prefix)
                return False
    return True