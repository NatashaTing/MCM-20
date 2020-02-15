
import pandas as pd

def main():
    path = 'OfficialNominalCatches_16Sep2019/ICESCatchDataset2006-2017.csv'
    # f = open('OfficialNominalCatches_16Sep2019/ICESCatchDataset2006-2017.csv', 'r')
    dat = pd.read_csv(path)
    print(type(dat))


if __name__== "__main__":
    main()

