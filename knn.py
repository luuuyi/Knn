'''
Created on Mar 24, 2017

@author: Luuuyi
'''

from numpy import *
import operator
import matplotlib.pyplot as plt
import matplotlib

def createTmpData():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify0(in_data,datas,labels,k):
    datas_height = datas.shape[0]
    diff_array = tile(in_data,[datas_height,1]) - datas
    diff_array_power2 = diff_array**2
    distance_array = diff_array_power2.sum(axis=1)
    distance_array = distance_array**0.5
    sorted_index = distance_array.argsort()
    labels_dict = {}
    for i in range(k):
        label = labels[sorted_index[i]]
        labels_dict[label] = labels_dict.get(label,0) + 1
    sorted_datas = sorted(labels_dict.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sorted_datas[0][0]

def loadDataFromFile(file_name):
    fd = open(file_name)
    lines = fd.readlines()
    lens = len(lines)
    datas = zeros((lens,3))
    labels = []
    for i in range(lens):
        tmp = lines[i].strip().split('\t')
        datas[i] = tmp[0:3]
        labels.append(int(tmp[-1]))
    return datas,labels

def drawImage(datas,labels):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datas[:,1],datas[:,2],5.0*array(labels),15.0*array(labels))
    plt.show()

def autoNormal(datas):
    height = datas.shape[0]
    max_array = datas.max(0)
    min_array = datas.min(0)
    range_array = max_array - min_array
    normaled_data = (datas-tile(min_array,(height,1)))/tile(range_array,(height,1))
    return normaled_data, range_array, min_array

def datingClassTest():
    datas, labels = loadDataFromFile('datingTestSet2.txt')
    height = datas.shape[0]
    ratio = 0.1
    test_nums = int(0.1*height)
    normaled_datas, range_array, min_array = autoNormal(datas)
    test_datas = normaled_datas[0:test_nums,:]
    error_count = 0.0
    for i in range(test_nums):
        result_label = classify0(test_datas[i],normaled_datas[test_nums:,:],labels[test_nums:],3)
        print "The class result is: %d, the real answer is %d" % (result_label,labels[i])
        if(result_label != labels[i]):  error_count += 1.0
    print "The Total error rate is: %f" % (error_count/int(0.1*height))

def datingClassPerson():
    result_labels = ['not like', 'a little like', 'like']
    percents_of_play = float(raw_input('Enter your percents_of_play:'))
    fly_distance = float(raw_input('Enter your fly_distance:'))
    ice = float(raw_input('Enter your ice:'))
    '''percents_of_play = 12.273169
    fly_distance = 35483
    ice = 1.508053'''
    datas, labels = loadDataFromFile('datingTestSet2.txt')
    normaled_datas, range_array, min_array = autoNormal(datas)
    test_data = array([fly_distance,percents_of_play,ice])
    classed_label = classify0((test_data-min_array)/range_array,normaled_datas,labels,3)
    print "The Result is: %s" % (result_labels[classed_label-1])

if __name__ == '__main__':
    '''datas, labels = createTmpData()
    res = classify0([0,0],datas,labels,3)
    print res35483	12.273169	1.508053'''
    datas, labels = loadDataFromFile('datingTestSet2.txt')
    #print datas, labels
    #drawImage(datas,labels)
    #datingClassTest()
    datingClassPerson()