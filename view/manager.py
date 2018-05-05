import service.csv_file_service as cfs
from service.oxford_data_controller import get_data_and_parse_it
import time


def process(path_to_file):
    word_set = cfs.get_words_to_process_from_file(path_to_file)
    prepared_list_of_words = []
    for word in word_set:
        prepared_list_of_words += get_data_and_parse_it(word)
        time.sleep(1)
    cfs.prepare_file_to_upload_for_quizlet(prepared_list_of_words)
