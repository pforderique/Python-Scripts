# This script is meant to help with loan payment decisions
class LoanFile:
    def __init__(self, fileloc) -> None:
        self.fileloc = fileloc

    def scanlines(self):
        with open(self.fileloc, 'r') as lf:
            for line in lf:
                if r'\n' not in line:
                    print(line)


if __name__ == "__main__":
    # define file location
    fileloc = r'C:\Users\fabri\OneDrive\Documents\DasText_and_Data\DasText\loandetailinfo.txt'

    loanfile = LoanFile(fileloc=fileloc)
    loanfile.scanlines()
