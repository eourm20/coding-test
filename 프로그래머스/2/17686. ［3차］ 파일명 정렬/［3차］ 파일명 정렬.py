def split_term(s, idx):
    global file_dict
    file_dict[s] = {'head': '', 'number': None, 'tail': ''}

    n = ''
    cnt = 0
    tail_mode = False

    for c in s:
        if not c.isdigit() and file_dict[s]['number'] is None and n == '' and not tail_mode:
            # HEAD
            file_dict[s]['head'] += c

        elif c.isdigit() and not tail_mode:
            # NUMBER(최대 5자리)
            if cnt < 5:
                n += c
                cnt += 1
            else:
                # 6번째 자리부터는 TAIL
                tail_mode = True
                # number 저장
                if file_dict[s]['number'] is None:
                    file_dict[s]['number'] = int(n) if n != '' else 0
                    file_dict[s]['head'] = file_dict[s]['head'].lower()
                file_dict[s]['tail'] += c  # 현재 자리도 tail에 포함

        else:
            # 숫자 이후 TAIL
            if not tail_mode:
                tail_mode = True
                if file_dict[s]['number'] is None:
                    file_dict[s]['number'] = int(n) if n != '' else 0
                    file_dict[s]['head'] = file_dict[s]['head'].lower()
            file_dict[s]['tail'] += c

    # 문자열이 숫자로 끝난 경우 TAIL 없음
    if file_dict[s]['number'] is None:
        file_dict[s]['number'] = int(n) if n != '' else 0
        file_dict[s]['head'] = file_dict[s]['head'].lower()

    return (s, file_dict[s]['head'], file_dict[s]['number'], idx)


def solution(files):
    global file_dict
    file_dict = {}
    files_list = []

    for idx, s in enumerate(files):
        files_list.append(split_term(s, idx))

    files_list.sort(key=lambda x: (x[1], x[2], x[3]))
    return [file[0] for file in files_list]