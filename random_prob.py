import random
import os
class RandomStringPicker:
    def __init__(self, strings, done_probs,easy_list):
        self.strings = strings
        self.history = self._add_as_set(done_probs)
        self.easy = self._add_as_set(easy_list)

    def _add_as_set(self,str_list):
        st = set()
        for word in str_list:
            st.add(word)
        return st

    def pick_random_string(self):
        remaining_strings = [s for s in self.strings if s not in self.history and s not in self.easy]
        if not remaining_strings:
            print("no more probs, resetting history")
            os.remove(probs_existing)
            return "Please Rerun"
        chosen_string = random.choice(remaining_strings)
        self.history.add(chosen_string)
        return chosen_string

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return [line.rstrip() for line in file]
    except FileNotFoundError:
        return []
    
def save_to_file(filename,string):
    with open(filename, 'a') as file:
        file.write(string)
        file.write("\n")
    
probs_list = "probs_backup.txt"
probs_existing = "probs_done.txt"
probs_easy = "probs_backup_easy.txt"
strings_list = read_file(probs_list)
easy_list = read_file(probs_easy)
done_probs = read_file(probs_existing)
picker = RandomStringPicker(strings_list,probs_existing,easy_list)
chosen_prob = picker.pick_random_string()
save_to_file(probs_existing,chosen_prob)
print(chosen_prob)