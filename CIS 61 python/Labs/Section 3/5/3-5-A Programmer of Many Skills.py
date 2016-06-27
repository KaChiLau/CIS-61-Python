class Programmer:
    def __init__(self, name):
        self.Name = name
    def print(self):

        print("Name: ", self.Name, "\n")
        
        print("SKills: SQL, JAVA, C++, C\n")

        print("SQL  is a special-purpose programming language designed for managing data held in a relational database management system (RDBMS), or for stream processing in a relational data stream management system (RDSMS).\n")

        print("JAVA is a computer programming language that is concurrent, class-based, object-oriented, and specifically designed to have as few implementation dependencies as possible.\n")

        print("C++ is a general purpose programming language. It has imperative, object-oriented and generic programming features, while also providing the facilities for low level memory manipulation.\n")

        print("C  is a general-purpose programming language initially developed by Dennis Ritchie between 1969 and 1973 at AT&T Bell Labs.\n")


P = Programmer('Ken')

P.print()
