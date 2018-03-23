import csv
import math


class ID3:
    """ID3 Class that creates a decision tree on the data set provided by 'data_file'.
        the data_set can be changed by calling ID3.changeDataSet()
    """
    class Node:
        """
        basic Node class for the problem, trees will generally be small in test cases.
        """
        def __init__(self, children=None, parent=None, value=None, is_leaf=False):
            self.children = children
            self.parent = parent

            self.value = value
            self.isLeaf = is_leaf

    def __init__(self, data_file=None, att_file=None):
        """
        :param data_file: the CSV file that contains the values of the attributes
        :param att_file: Names of the attributes used, purely aesthetic.
        :return: void
        """
        self.decisions = []
        self.decisionTree = None
        self.number_of_attributes = 0
        self.number_of_examples = 0
        self.root = self.Node()
        if data_file is not None:
            self.data = csv.reader(open(data_file))
            self.dataSet = []
            self.storeData()
        if att_file is not None:
            self.attributes = csv.reader(open(att_file)).next()

    def storeData(self):
        """
        function that stores the rows of the data set, stripped of whitespaces.
        the number of examples is also counted and stored in the global self.number_of_examples
        :return: void
        """
        for row in self.data:
            for i in range(len(row)):
                row[i] = row[i].strip()
            self.dataSet.append(row)

        self.sortData()

    def sortData(self):
        """
        sorts the raw data stored in dataSet.
        the number of examples and attributes is also counted and stored in the global self.number_of_examples
        and self.number_of_attributes
        :return: void
        """
        self.number_of_attributes = len(self.dataSet[0]) - 1  # the last column holds decisions and not attributes
        self.number_of_examples = len(self.dataSet)
        for data in self.dataSet:
            self.decisions.append(data[self.number_of_attributes])

    def ID3(self):
        self.decisionTree = self.__ID3(self.decisions, self.dataSet, self.root)

    def __ID3(self, examples, attributes, node):
        if examples is None:
            return node
        if self.isExamplesPure(examples):
            return examples[0]

        informationPerAttribute = []
        for i in range(self.number_of_attributes):
            informationPerAttribute.append(self.informationGain(examples, i))

        attributeNumber = informationPerAttribute.index(max(informationPerAttribute))
        node = self.__ID3(self.getExamplesByAttribute(attributeNumber),)
        return node

    def isExamplesPure(self, examples):
        decision = examples[0]
        for example in examples:
            if not example == decision:
                return False
        return True

    def data_et(self):
        for examples in self.dataSet:
            print examples

