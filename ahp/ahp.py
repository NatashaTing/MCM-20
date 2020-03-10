
import numpy as np
import json
from pyahp import parse

def main():

    with open('current_un_model.json') as json_model:
        model = json.load(json_model)

    ahp_model = parse(model)
    priorities = ahp_model.get_priorities()
    print('the priorities are: ', priorities)

if __name__ == "__main__":
    main()




