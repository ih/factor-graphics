import os, sys, pickle, random

if __name__ == "__main__":
    args=pickle.load(sys.stdin)
    args.reverse()
    pickle.dump(args,sys.stdout)
