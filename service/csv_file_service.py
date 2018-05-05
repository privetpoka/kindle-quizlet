def prepare_file_to_upload_for_quizlet(data: []):
    f = open('./result.txt', 'w')
    for line in data:
        f.write(line + '\n')
    f.close()


def get_words_to_process_from_file(file_name) -> set:
    word_set = set()
    with open(file_name) as file:
        for line in file:
            word_set.add(line.strip())
    return word_set
