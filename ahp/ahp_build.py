
import numpy as np
import json

def main():

    matrix_criteria = ["1-individual-choice", "2-economic-stability",
                        "3-degree-being-impacted", "4-distance",
                        "5-cultural-proximity", "6-Human-right-politics",
                        "7-biocapacity", "8-public-health"]

    k = len(matrix_criteria)

    rank_criteria_vec = [1, 2, 3, 4, 5, 6, 7, 8]
    all_rank_by_criteria = [[1, 2, 3, 4],
                            [1, 2, 3, 4],
                            [1, 2, 3, 4],
                            [1, 2, 3, 4],
                            [1, 2, 3, 4],
                            [1, 2, 3, 4],
                            [1, 2, 3, 4],
                            [1, 2, 3, 4]]

    mymatrix = rankthem(rank_criteria_vec, 'Main Criteria Matrix')

    criteria = {}
    alljsons = {}

    for i in range(0, k):
        rank_vec = all_rank_by_criteria[i]
        criteria['criteria'+str(i)] = rankthem(rank_vec, 'Criteria'+str(i)+' Matrix')
        temp_matrix = criteria['criteria'+str(i)]
        print('Did i = ', i, ' with matrix output size ', criteria['criteria'+str(i)].shape)

    np_ndarray_to_json('criteria0', criteria['criteria0'])

    #with open('mymodel.json') as f:
    #    myjson = json.dumps(json_model)
    #    f.write(myjson)


def np_ndarray_to_json(title, mat):
    print('hello np_ndarray_to_json')
    I = mat.shape[0]
    J = mat.shape[1]
    f = open('test.json', 'w')
    heading = "\"{}\": [\n".format(title)
    f.write(heading)
    for i in range(I):
        f.write('[ ')
        for j in range(J):
            f.write(str(mat[i, j]))
            if not j == J-1:
                f.write(str(', '))
        f.write('], \n')

    f.write(']')
    f.close()


def rankthem(rank_vec, title):

    n = len(rank_vec)
    matrix_out = np.ones([n, n])

    for i in range(len(rank_vec)):
        base = rank_vec[i]
        for j in range(i+1, len(rank_vec)):
            if not i == len(rank_vec):
                this = rank_vec[j]
                if this > base:
                    importance = this - base + 1
                    matrix_out[j, i] = importance
                    matrix_out[i, j] = round(1 / importance, 4)
                else:
                    importance = base - this + 1
                    matrix_out[i, j] = importance
                    matrix_out[j, i] = round(1 / importance, 4)
            else:
                print('what now?')


    #print('-------------Rank successful for ', title, '------------')
    #print('Input rank vector: ', rank_vec)
    #print('Output matrix size: ', matrix_out.shape)
    ##print(ndtotext(matrix_out))
    #print(repr(matrix_out))
    return matrix_out

if __name__ == "__main__":
    main()




