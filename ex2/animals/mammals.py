class Mammals:

        def __init__(self):
                self.members = ['Bat', 'Sugar Glider', 'Flying Squirrel']
                self.danger = [1, 0, 1]

        def printMembers(self):
                print('Printing the members of the Mammals class')
                for member in self.members:
                        print('\t%s' % member)
                
        def printDangerous(self):
                dangerous = []
                for i in range(len(self.danger)):
                        if self.danger[i] == 1:
                                dangerous.append(self.members[i])
                print('Printing dangerous members of the Mammals class')
                for i in dangerous:
                        print('\t%s' % i)
                
        def printHarmless(self):
                harmless = []
                for i in range(len(self.danger)):
                        if self.danger[i] != 1:
                                harmless.append(self.members[i])
                print('Printing harmless members of the Mammals class')
                for i in harmless:
                        print('\t%s' % i)

	
