import NNsolver #finish later
import SVMsolver #finish later
from dataProcess import dp
import pandas as pd
#public interface
def train(df, method):
    if (method is "SVM"): #example
        SVMsolver.train(df)
def test(method):
    pass




#Usage: only for unit testing
def main():
    df1 = pd.read_csv("clean_data/xxx.csv")
    df2 = pd.read_csv("clean_data/xxx.csv")
    # call preprocess function with needed parameters
    # def preprocess(dfs, method = "slides window", win_size = 5, step = 0.5)
    df = dp.preprocess([df1, df2])
    train(df)
main()
