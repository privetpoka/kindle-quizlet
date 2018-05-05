def prepare_file_to_upload_for_quizlet(data: []):
    f = open('./result.txt', 'wb')
    for line in data:
        try:
            f.write(line.encode('utf-8') + b'\n')
        except UnicodeEncodeError:
            print(line, 'failed')
        except TypeError:
            print(line, 'type')
    f.close()


def get_words_to_process_from_file(file_name) -> set:
    word_set = set()
    with open(file_name,'r',encoding='utf-8') as file:
        for line in file:
            word_set.add(line.strip())
    return word_set
