import importlib, sys
import setting.setup as setup

def runScript(scrfile):
    scriptmodule = importlib.import_module(scrfile)
    scriptmodule.runsample(setup.getPicturesDir())

if __name__ == "__main__":
    print('execute sample script')
    print(dir(setup))
    print(setup.getPicturesDir())
    runScript(sys.argv[1])
