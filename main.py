import sys
import fileProcess as fp
#import XXsolver 
import NNsolver #example
#import SVMsolver
import pandas as pd
def main(argv):
    # My code here
    if (len(argv))
    if (argv[1] is "train"):
        if (len(argv) > 3 and argc[3] is "-x"):
            fp.extractFiles(dataPath)
        traindataPath = argv[2]
        dfsTrain = fp.getDataframes(dataPath) 
        NNsolver.train(dfsTrain)
    elif (argv[1] is "test"):
        testdataPath = argv[2]
        dfTest = fp.getDataframe(dataPath)
        NNsolver.test(dfTest)
    else:
        print("Please specify train/test phase and data path")
        sys.exit(0)
    


if __name__ == '__main__':
    main(sys.argv)