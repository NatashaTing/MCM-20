
import numpy as np
import json

def main():

    matrix_criteria = ["1-individual-choice", "2-economic-stability",
                        "3-degree-being-impacted", "4-distance",
                        "5-cultural-proximity", "6-Human-right-politics",
                        "7-biocapacity", "8-public-health"]
    k = len(matrix_criteria)

    rank_criteria_vec = [1, 6, 8, 5, 2, 6, 7, 1]
    all_rank_by_criteria = [[1, 4, 3, 2],
                            [1, 3, 2, 4],
                            [1, 2, 3, 4],
                            [4, 1, 3, 2],
                            [3, 1, 2, 4],
                            [1, 2, 3, 4],
                            [2, 1, 3, 4],
                            [1, 3, 4, 2]]

    mymatrix = rankthem(rank_criteria_vec, 'Main Criteria Matrix')
    criteria = {}

    f = open('test.json', 'w')
    f.write(
        "{\n \"name\": \"UN Policy Decision\", \n \"method\": \"approximate\", \n \"criteria\": [\"1-individual-choice\", \"2-economic-stability\" , \"3-degree-being-impacted\", \"4-distance\",\"5-cultural-proximity\", \"6-Human-right-politics\", \"7-biocapacity\", \"8-public-health\"], \n  \"subCriteria\": {}, \n \"alternatives\": [\"policyA\", \"policyB\", \"policyC\", \"policyD\"], \n \"preferenceMatrices\": { \n")
    f.close()

    val = 1
    np_ndarray_to_json("criteria", mymatrix, val)

    for i in range(0, k):
        rank_vec = all_rank_by_criteria[i]
        criteria['criteria'+str(i)] = rankthem(rank_vec, 'Criteria'+str(i)+' Matrix')
        temp_matrix = criteria['criteria'+str(i)]
        print('Did i = ', i, ' with matrix output size ', criteria['criteria'+str(i)].shape)
        val = 0 if i == k-1 else 1
        np_ndarray_to_json('alternatives:'+matrix_criteria[i], criteria['criteria'+str(i)], val)

    f = open('test.json', 'a')
    f.write('] \n } \n }')
    f.close()


def np_ndarray_to_json(title, mat, val):
    print('hello np_ndarray_to_json')
    I = mat.shape[0]
    J = mat.shape[1]
    f = open('test.json', 'a')
    heading = "\"{}\": [\n".format(title)
    f.write(heading)
    for i in range(I):
        f.write('[ ')
        for j in range(J):
            f.write(str(mat[i, j]))
            if not j == J-1:
                f.write(str(', '))
        f.write(']')
        if not i == I - 1:
            f.write(',')
        f.write('\n')
    if val > 0:
        f.write('], \n')
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




