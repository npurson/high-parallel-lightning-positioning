import os
import numpy as np
from tdoa import tdoa


def get_files(root = '.'):
    files_lst = []
    for path, dirs, files in os.walk(root):
        file_lst = []
        for file in files:
            if file.endswith('csv'):
                file_lst.append(os.path.join(path,file))
        if len(file_lst):
            files_lst.append(file_lst)
    return files_lst


def main():
    tdoas = []
    files = get_files(root='../data/data7.16')
    print('Loading files')
    for i in range(len(files)):
        datas, trigger_time = [], []
        slices = files[i]
        for j in range(len(slices)):
            with open(slices[j], 'r') as f:
                trigger_time.append(np.double('.' + os.path.basename(slices[j]).split('_')[3]))
                data = [int(line.strip()) for line in f.readlines()]
                datas.append(data)
        print('Calling matlab')
        tdoa_ = tdoa(trigger_time, datas)
        tdoa_ = np.array(tdoa_).squeeze().round(7)
        print('Finished')

        np.savetxt(os.path.join(os.path.dirname(files[i][0]), 'tdoa.csv'), tdoa_, delimiter=',')
        tdoas.append(tdoa_)
    tdoas = np.array(tdoas)
    print(f'Shape of tdoas is {tdoas.shape}')


if __name__ == '__main__':
    main()
