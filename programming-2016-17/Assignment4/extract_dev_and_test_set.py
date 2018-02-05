import sys, random
from os import listdir, makedirs
from os.path import join, isdir
from shutil import move, rmtree

extract_size = 100
target_dir = "extractedFiles"
dev_dir = join(target_dir, "dev-set")
test_dir = join(target_dir, "test-set")
dev_keys = join(target_dir, "dev_keys.txt")
test_keys = join(target_dir, "test_keys.txt")
# padding is neede to change duplicate names in data set
padding_nums = list(range(20))
random.shuffle(padding_nums)

def main(args):
    global dev_keys
    global test_keys
    global dev_dir
    global test_dir

    corpus_path = args[0]

    if isdir(target_dir):
        rmtree(target_dir)

    makedirs(target_dir)
    makedirs(dev_dir)
    makedirs(test_dir)

    for dir in listdir(corpus_path):
        print(dir)
        pad = str(padding_nums.pop())

        topic_path = join(corpus_path, dir)
        files = listdir(topic_path)
        dev_files = random.sample(files, extract_size)
        files = list(filter(lambda x : x not in dev_files, files))
        test_files = random.sample(files, extract_size)

        move_files(join(corpus_path, dir), dev_files, dev_dir, pad)
        move_files(join(corpus_path, dir), test_files, test_dir, pad)

        write_keys(dev_keys, dev_files, dir, pad)
        write_keys(test_keys, test_files, dir, pad)


def move_files(root_dir, file_list, destination, pad):
    for text_file in file_list:
        move(join(root_dir, text_file), join(destination, text_file + pad))

def write_keys(target_file, keys, value, pad):
    with open(target_file, "a") as target:
            for file_name in keys:
                target.write(file_name + pad + "\t" + value + "\n")

if __name__ == '__main__':
    main(sys.argv[1:])
