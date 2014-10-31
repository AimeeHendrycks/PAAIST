#PAAIST - Personal Assistant Artificial Intelligence Strength Test

import random

def getList(nameOfFile):
    '''
    Input the text file's name of the form 'nameOfFile.txt'.
    Give a name of a file that links to a .txt file. The name should be >= 4 in length.
    Outputs a list where each element is a line from the text file.
    This is an auxiliary function.
    '''
    #if they did not include a '.txt' extension
    if nameOfFile[-4:] != '.txt': nameOfFile += '.txt'

    f = open(nameOfFile)
    l = f.readlines()
    f.close()

    #removes the newline character from list elements
    l = map(lambda s: s.strip('\n'), l)

    return l

def sampleWR(population, k):
    '''
    Chooses k elements from population with replacement.
    Population is a list of integers each representing a query structure.
    This is an auxiliary function.
    '''

    sample = ()
    for i in xrange(k):
        #adds a number from population to the sample
        sample += ( random.choice(population) ,)

    return sample

#auxiliary functions end here
#query generating functions begin here

def chemistryQueries(numOfQueries = 10):
    '''
    Input the number of chemistry queries to output.
    Outputs are from the elementQueries and compoundQueries function.
    '''

    #this function is called at the end of chemistryQueries
    def elementQueries(numOfQueries):
        '''
        Input the number of chemistry element queries to output.
        Outputs may have similar query structures.
        '''

        #gets element names from text file and adds the names to list elementNames
        elementNames = getList('STEM\Chemistry\elementNames.txt')

        #loops through a list of 0's and 1's. 1 is the 1st query structure, 0 the 2nd
        for num in sampleWR([0,1], numOfQueries):

            #prints the question "What is the <property> of <element>?"
            if num == 0:
                print 'What is the', random.choice(
                ('density', 'molar mass', 'atomic number',
                'atomic mass', 'electronegativity', 'melting point', 'boiling point',
                'atomic radius', 'covalent radius', 'van der Waals radius', 'year of discovery',
                'ionization energy', 'cost', 'price', 'vapor pressure', 'odor', 'appearance',
                'specific gravity', 'origin of the name', 'etymology', 'period number',
                'group number', 'specific heat capacity', 'half-life', 'Lewis structure',
                'number of valence electrons', 'principle quantum number',
                'magnetic quantum number', 'angular momentum quantum number',
                'number of orbitals', 'total number of electrons', 'electrode potential')
                ), 'of', random.choice(elementNames) + '?'

            #prints the question "Is <element> <with this property>?"
            elif num == 1:
                print 'Is', random.choice(elementNames), random.choice(
                ('an element', 'a covalent substance', 'covalent', 'an ionic substance',
                'ionic', 'poisonous', 'deadly', 'toxic', 'carcinogenic', 'flammable',
                'cancerous', 'explosive', 'radioactive', 'mined', 'soluble', 'stable',
                'malleable', 'able to float on water', 'a liquid at room temperature',
                'a solid at room temperature', 'a gas at room temperature', 'artificial',
                'red', 'green', 'blue', 'yellow', 'pink', 'purple', 'black', 'brown',
                'white', 'orange', 'found in the ocean', 'found underground', 'found in the air',
                'inert', 'a noble gas', 'an alkali metal', 'an alkaline earth metal',
                'a transition metal', 'an halogen', 'a metalloid', 'a lathanide', 'an actinide',
                'in a(n) ' + random.choice( getList('STEM\Chemistry\ediblesAndDrinkables.txt') ) )
                ) + '?'

    #this function is called at the end of chemistryQueries
    def compoundQueries(numOfQueries):
        '''
        Input the number of popular chemistry compound queries to output.
        Outputs may have similar query structures.
        '''

        #gets compound names from text file and adds the names to list compoundNames
        compoundNames = getList('STEM\Chemistry\compoundNames.txt')

        #loops through a random list of 0's and 1's. 0: 1st query structure, 1: 2nd
        #we pass [0,1,1,1] to sampleWR to make the second query structure more likely
        for num in sampleWR([0,1,1,1], numOfQueries):

            #prints the question "What is the <property> of <compound>?"
            if num == 0:
                print 'What is the', random.choice(
                ('density', 'molar mass', 'atomic number', 'atomic mass',  'melting point',
                'boiling point', 'year of discovery', 'cost', 'price', 'odor', 'appearance',
                'color', 'specific gravity', 'pH')
                ), 'of', random.choice(compoundNames) + '?'

            #prints the question "Is <compound> <with this property>?"
            elif num == 1:
                print 'Is', random.choice(compoundNames), random.choice(
                ('polar', 'nonpolar', 'acidic', 'an acid', 'a strong acid', 'a weak acid',
                'basic', 'a base', 'a strong base', 'a weak base', 'alkaline', 'neutral',
                'aromatic', 'a salt', 'an alcohol', 'an alkane', 'an alkene', 'an alkyne',
                'an ether', 'an aldehyde', 'a ketone',  'a hydrocarbon', 'a carbohydrate',
                'an ester', 'an amine', 'a carboxylic acid', 'a protein', 'organic',
                'found in humans', 'tetrahedral', 'trigonal-pyrimidal', 'a linear molecule',
                'an alloy', 'amorphous', 'poisonous', 'deadly', 'toxic', 'carcinogenic',
                'flammable', 'cancerous', 'explosive', 'radioactive', 'soluble', 'stable',
                'a molecule', 'able to float on water', 'a liquid at room temperature',
                'a solid at room temperature', 'a gas at room temperature', 'artificial',
                'red', 'green', 'blue', 'yellow', 'pink', 'purple', 'black', 'brown',
                'white', 'orange', 'found in the ocean', 'found underground', 'found in the air',
                'in a(n)' + random.choice( getList('STEM\Chemistry\ediblesAndDrinkables.txt') ))
                ) + '?'

    #makes a random list of integers from of length numOfQueries, and the list
    #is comprised of integers from the first parameter. 0 activates the first function, 1 the 2nd
    randList = sampleWR([0,1], numOfQueries)

    elementQueries(randList.count(0))
    compoundQueries(randList.count(1))

def weatherQueries(numOfQueries = 10):
    '''
    Input the number of weather queries to output.
    Outputs may have similar query structures.
    '''

    #gets city names from text file and adds the names to list cityNames
    cityNames = getList('Misc/cityNames.txt')

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd
    for num in sampleWR([0,1], numOfQueries):

        timePoints = ('today', 'tomorrow', 'in two days', 'in three days', 'next week',
        'in seven days', 'a week from now', 'the day after tomorrow', 'Sunday',
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
        'this weekend', 'next weekend', 'tonight', 'this afternoon', 'this evening',
        'tomorrow morning')

        #prints the question "What will be the weather in <city> <point in time>?"
        #we multiply the city name by 0 or 1 to include or exclude the city name
        if num == 0:
            print 'What will be the weather' + \
            random.choice([0,1]) * str( ' in ' + random.choice(cityNames) ),\
            random.choice(timePoints) + '?'

        #prints questions answered with weather forecasts
        elif num == 1:
            print 'Will', random.choice(
            ('it rain', 'it snow', 'it freeze', 'it be hot', 'it be windy',
            'it be cold', 'I need a jacket', 'I need a scarf', 'I need an umbrella',
            'I need a raincoat', 'I need mittens', 'I need snowboots', 'I need sunglasses')
            ), random.choice(timePoints) + '?'

def movieQueries(numOfQueries = 10):
    '''
    Input the number of movie queries to output.
    Outputs may have similar query structures.
    '''

    #gets movie names from text file and adds the names to list movieTitles
    movieTitles = getList('Entertainment\movieTitles.txt')

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR(range(10), numOfQueries):

        if num == 0:
            print 'What is the genre of the movie', random.choice(movieTitles) + '?'

        elif num == 1:
            print 'Who are some of the actors in the movie', random.choice(movieTitles) + '?'

        elif num == 2:
            print 'What is the rating of the movie', random.choice(movieTitles) + '?'

        elif num == 3:
            print 'What accolades did the movie', random.choice(movieTitles), 'receive?'

        elif num == 4:
            print 'Who is the director of the movie', random.choice(movieTitles) + '?'

        elif num == 5:
            print 'How long is the movie', random.choice(movieTitles) + '?'

        #prints the question "Is the movie <movie> on <video provider>?"
        elif num == 6:
            print 'Is the movie', random.choice(movieTitles), 'on',\
            random.choice(['Netflix', 'Hulu', 'Amazon Instant Video']) + '?'

        elif num == 7:
            print 'Tell me a summary of the movie', random.choice(movieTitles) + '.'

        elif num == 8:
            print 'What movies are in the movie theaters now?'

        elif num == 9:
            print 'What movies are like', random.choice(movieTitles) + '?'

def showQueries(numOfQueries = 10):
    '''
    Input the number of TV show queries to output.
    Outputs may have similar query structures.
    '''

    #gets TV series names from text file and adds the names to list showNames
    showNames = getList('Entertainment\showNames.txt')

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR(range(10), numOfQueries):

        if num == 0:
            print 'What is the genre of the show', random.choice(showNames) + '?'

        elif num == 1:
            print 'Who are some of the actors in the show', random.choice(showNames) + '?'

        elif num == 2:
            print 'What is the rating of the show', random.choice(showNames) + '?'

        elif num == 3:
            print 'What accolades did the show', random.choice(showNames), 'receive?'

        elif num == 4:
            print 'Who is the director of the series', random.choice(showNames) + '?'

        elif num == 5:
            print 'How long is an episode of', random.choice(showNames) + '?'

        #prints the question "Is the series <show> on <video provider>?"
        elif num == 6:
            print 'Is the series', random.choice(showNames), 'on',\
            random.choice(['Netflix', 'Hulu', 'Amazon Instant Video']) + '?'

        elif num == 7:
            print 'Who are some of the writers of the show', random.choice(showNames) + '?'

        elif num == 8:
            print 'Tell me a summary of the show', random.choice(showNames) + '.'

        elif num == 9:
            print 'What shows are like', random.choice(showNames) + '?'

        elif num == 10:
            print 'Recommend me a show of the', random.choice(
            ('sci-fi', 'drama', 'comedy', 'fantasy', 'romantic', 'action', 'crime')
            ), 'genre' + '.'

def collegeQueries(numOfQueries = 10):
    '''
    Input the number of college and university queries to output.
    Outputs may have similar query structures.
    Moreover, Some outputs may be nonsensical; e.g., What is Princeton's business
    school ranking? For this example, note Princeton doesn't have a business school.
    The AI ought to manage with such nonsensical queries.
    '''

    #gets college names from text file and adds the names to list collegeTitles
    collegeTitles = getList('Misc/collegeAndUniversityNames.txt')

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR([0,1,2], numOfQueries):

        #prints the question "What is <college or university>'s rank in <field>?"
        if num == 0:
            field = getList('Misc/disciplineTitles.txt')

            print 'What is', random.choice(collegeTitles) + '\'s rank in',\
            random.choice(field) + '?'

        #prints the question "What's the <attribute> of <college or university>?"
        elif num == 1:
            print 'What\'s the',\
            random.choice(
            ('average financial aid package', 'cost of tuition', 'estimated overall cost',
             'total number of undergraduates', 'in-state tuition', 'out-of-state tuition',
             'application deadline', 'early application deadline', 'application fee'
             'required standardized tests', 'most common major', 'freshman acceptance rate',
             'acceptance rate', 'early acceptance rate', 'yield rate', 'transfer acceptance rate',
             'precentage of men', 'percentage of women', 'percentage of whites',
             'percentage of Asians', 'percentage of blacks', 'percentage of Hispanics',
             'percentage of students in-state', 'percentage of students out of state',
             'percentage of part-time students', 'percentage of undergraduates living in college housing',
             'percentage of men who join fraternities', 'percentage of women who join sororities',
             'NCAA division level', 'mascot', 'motto', 'average SAT score', 'average ACT score',
             'typical high school GPA','maximum credits from another institution for transfer students',
             'application requirements', 'retention', 'graduation rate')
            ), 'at', random.choice(collegeTitles) + '?'

        #prints the question "Which colleges <description>?"
        elif num == 2:
            print 'Which colleges',\
            random.choice(
            ('have a high prevalence of suicide', 'are need-blind', 'do not accept transfers',
            'are top ranked in ' + random.choice( getList('Misc/disciplineTitles.txt') ),
            'meet 100% of demonstrated financial need', 'are Ivy League schools',
            'are selective', 'are very selective', 'are in ' + random.choice(getList('Misc/cityNames.txt')),
            'are good in ' + random.choice( getList('Misc/disciplineTitles.txt') ), 'are private',
            'are public', 'have students with an average high school GPA of 3.9 or greater',
            'have an acceptance rate of less than 10%', 'have a student faculty ratio less than 7:1',
            'do not require the SAT', 'do not require the ACT', 'offer ROTC', 'are in the top 10 on USNews',
            'are non-profit', 'are for-profit')
            ) + '?'

def mathQueries(numOfQueries = 10):
    '''
    Input the number of mathematics queries to output.
    Outputs are from the algebra, calculus, and geometry functions within.
    '''

    #gets content names from text file and adds the listed content to the appropriate var
    functions = getList('STEM\Mathematics\elementaryFunctions.txt')
    constants = getList('STEM\Mathematics\constants.txt')

    #this function is called at the end of mathQueries
    def algebraQueries(numOfQueries):
        '''
        Input the number of algebra queries to output.
        Outputs may have similar query structures.
        '''

        #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
        for num in sampleWR(range(6), numOfQueries):

            #prints the command "Solve for x if <function in x> = <number>?"
            if num == 0:
                print 'Solve for x if', random.choice(functions), '=', random.choice(constants) + '.'

            #prints the command "Factor <polynomial>."
            elif num == 1:
                exponents = [n+1 for n in range(9)]    #list of postive integers
                #without replacement, choose some exponents some number of times, and sort descending
                exponentSet = sorted( random.sample(exponents, random.choice(exponents)), reverse = True )

                polynomial = ''
                for e in exponentSet:
                    #sign, coefficient, variable, exponent
                    polynomial += random.choice([' -',' +']) + str(random.choice(exponents)) + 'x^' + str(e)

                print 'Factor', polynomial + '.'

            #prints the command "Find the partial fraction decomposition of <rational expression>"
            elif num == 2:
                exponents = [n+1 for n in range(9)]    #list of postive integers
                #without replacement, choose some exponents some number of times, and sort descending
                exponentSet = sorted( random.sample(exponents, random.choice(exponents)), reverse = True )

                fraction = '('
                for i in range(2):
                    for e in exponentSet:
                        fraction += random.choice([' -',' +']) +\
                        str( random.choice(exponents) ) + 'x^' + str(e)
                    if i == 1:
                        fraction += ')'
                        break
                    #get new exponents for the denominator
                    exponentSet = sorted( random.sample(exponents, random.choice(exponents)) )
                    fraction += ') / ('

                print 'Find the partial fraction decomposition of', fraction + '.'

            #prints the command "Solve the system <system of equations>."
            elif num == 3:

                system = ''
                for i in range( random.randrange(1, 5) ):#parameter is # of rows
                    #builds rows of the system
                    for j in range( random.randrange(1, 5) ):#param is # of vars
                        system += random.choice([' -',' +']) +\
                        str( random.randrange(1, 10) ) +\
                        random.choice(['w','x','y','z'])
                    #gets something for the expression to equal
                    system += ' = ' + random.choice(['-','']) +\
                    str( random.randrange(1, 10) ) + ', '

                print 'Solve the system', system[:-2] + '.'     #[:-2] removes a ', ' from system

            #prints the command
            #"Rationalize the denominator of <fraction with possibly irrational denominator>."
            elif num == 4:
                #line 2: numerator; line 3: base w/o exponent; 4: exponent
                print 'Rationalize the denominator of',\
                str(random.randrange(1, 10)) + ' / [' +\
                str(random.randrange(1, 10)) + ' - ' + str(random.randrange(1, 10)) +\
                '^(' + str(random.randrange(1, 10)) + '/' + str(random.randrange(1, 10)) + ')].'

            #this is a statistics question barely qualifying as algebra
            elif num == 5:
                print 'Find the F-score if precision is', random.randrange(0, 100,)/100.,\
                'and recall is', str(random.randrange(0, 100,)/100.) + '.'

    #this function is called at the end of mathQueries
    def calculusQueries(numOfQueries):
        '''
        Input the number of calculus queries to output.
        Outputs may have similar query structures.
        '''

        #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
        for num in sampleWR(range(7), numOfQueries):

            #prints the command "Differentiate <function in x> with respect to x."
            if num == 0:
                print 'Differentiate', random.choice(functions), 'with respect to x.'

            #prints the command "Integrate <function in x> with respect to x."
            elif num == 1:
                print 'Integrate', random.choice(functions), 'with respect to x.'

            #prints the command "Find the derivative of <function in x> at x = <a>"
            elif num == 2:
                print 'Find the derivative of', random.choice(functions), 'at', random.choice(constants) + '.'

            #prints the command "Integrate <function in x> with respect to x from <a> to <b>."
            elif num == 3:
                print 'Integrate', random.choice(functions), 'with respect to x from',\
                random.choice(constants), 'to', random.choice(constants) + '.'

            #prints the question "What are the inflection points of <function>?"
            elif num == 4:
                print 'What are the inflection points of', random.choice(functions) + '?'

            #prints the question "What are the <'local' or 'global'> extrema of <function>?"
            elif num == 5:
                print 'What are the', random.choice(['local','global']),\
                'extrema of', random.choice(functions) + '?'

            #prints the command "Find the limit of <function> as x approaches <number>."
            elif num == 6:
                print 'Find the limit of', random.choice(functions), 'as x approaches',\
                str( random.choice([random.choice(constants), 'infinity', 'negative infinity']) ) + '.'

    #this function is called at the end of mathQueries
    def geometryQueries(numOfQueries):
        '''
        Input the number of geometry queries to output.
        Outputs may have similar query structures.
        '''

        #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
        for num in sampleWR(range(5), numOfQueries):

            if num == 0:
                print 'Find the volume of a sphere with radius', random.choice(constants) + '.'

            elif num == 1:
                print 'If it exists, find the area of a triangle with the sidelengths',
                random.choice(constants), random.choice(constants), random.choice(constants) + '.'

            elif num == 2:
                print 'Determine the volume of a', random.choice(
                ('cube', 'tetrahedron', '8-dimensional cube', 'icosahedron', 'tessarect')
                ), 'with side length', random.choice(constants) + '.'

            elif num == 3:
                print 'Find the volume of a', random.choice(('cylinder', 'cone')),\
                'with radius', random.choice(constants), 'and height', random.choice(constants) + '.'

            elif num == 4:
                print 'Determine the interior angles of a rhombus with side lengths',\
                random.randrange(1, 10), 'and', random.randrange(1, 10) + '.'

    #makes a random list of integers from of length numOfQueries, and the list
    #is comprised of integers from the first parameter. 0 activates the first function, 1 the 2nd,...
    randList = sampleWR([0,1,2], numOfQueries)

    algebraQueries(randList.count(0))
    calculusQueries(randList.count(1))
    geometryQueries(randList.count(2))

def pokemonQueries(numOfQueries = 10):
    '''
    Input the number of Pokemon queries to output.
    Outputs may have similar query structures.
    '''

    #gets Pokemon names from text file and adds the names to list pokemonNames
    pokemonNames = getList('Entertainment\pokemonNames.txt')

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR(range(7), numOfQueries):

        if num == 0:
            print 'What type or types is the Pokemon', random.choice(pokemonNames) + '?'

        elif num == 1:
            print 'Show me the sprite for the Pokemon', random.choice(pokemonNames) + '.'

        elif num == 2:
            print 'Does the Pokemon', random.choice(pokemonNames), 'evolve?'

        elif num == 3:
            print 'What is the special ability of the Pokemon', random.choice(pokemonNames) + '?'

        #prints the question "Is <pokemon> a <pokemon type> type?"
        elif num == 4:
            print 'Is', random.choice(pokemonNames), 'a', random.choice(
            ('Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock',
            'Bug', 'Ghost', 'Steel', 'Fire', 'Water', 'Grass', 'Electric',
            'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy')
            ), 'type?'

        elif num == 5:
            print 'Is the Pokemon', random.choice(pokemonNames), 'legendary?'

        elif num == 6:
            print 'Where is the Pokemon', random.choice(pokemonNames), 'found?'

def videoGameQueries(numOfQueries = 10):
    '''
    Input the number of video game queries to output.
    Outputs may have similar query structures.
    '''

    #gets video game titles from text file and adds the names to list videoGameTitles
    videoGameTitles = getList('Entertainment/videoGameTitles.txt')

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR(range(6), numOfQueries):

        if num == 0:
            print 'What is the genre of the game', random.choice(videoGameTitles) + '?'

        elif num == 1:
            print 'How are the reviews of the game', random.choice(videoGameTitles) + '?'

        elif num == 2:
            print 'Which systems are the game', random.choice(videoGameTitles), 'available on?'

        elif num == 3:
            print 'How long does it typically take to complete the game', random.choice(videoGameTitles) + '?'

        elif num == 4:
            print 'Who composed music for the game', random.choice(videoGameTitles) + '?'

        elif num == 5:
            print 'Which studio developed the game', random.choice(videoGameTitles) + '?'

def cityAndCountryQueries(numOfQueries = 10):
    '''
    Input the number of city or country queries to output.
    Outputs may have similar query structures.
    '''

    #gets city and country names from text file and adds the names to list cityNames and countryNames
    cityNames = getList('Misc/cityNames.txt')
    countryNames = getList('Misc/countryNames.txt')

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    #we unequally weight the first question's likelihood by making the list primarily 0's
    for num in sampleWR([0,0,0,1], numOfQueries):

        #prints the question "What is <attribute> <country or city>?
        if num == 0:
            print 'What is the', random.choice(
            ('population of', 'median home income in', 'median home value in',
            'price of electricity in', 'percentage of obese people in', 'crime like in',
            'male to female ratio in', 'homicide rate', 'air quality index of',
            'largest employer in', 'unemployment rate in', 'number of universities in',
            'minimum wage in', 'percentage of self-employed workers in', 'racial diversity of',
            'ratio of part time workers in', 'trade surplus of', 'per capita income in',
            'population below the poverty line in', 'cost of living index in', 'governmental leader of',
            'total sales tax rate in', 'elevation of', 'area of', 'population density of', 'climate of',
            'average temperature of', 'currency used in')
            ), random.choice(random.choice([cityNames, countryNames])) + '?'

        #prints the question "What is <attribute> <country>?
        if num == 1:
            print 'What is the', random.choice(
            ('percentage of obese people in', 'real GDP per capita', 'trade surplus of',
             'trade deficit of', 'prevalence of religion in', 'human development index in',
             'soft power ranking of', 'human development index in education in', 'number of lakes in',
             'type of government of', 'main export of')
            ), random.choice(countryNames) + '?'

def bookQueries(numOfQueries = 10):
    '''
    Input the number of book queries to output.
    Outputs may have similar query structures.
    '''

    #gets book titles from text file and adds the names to list bookTitles
    bookTitles = getList('Entertainment/bookTitles.txt')

     #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR(range(6), numOfQueries):

        if num == 0:
            print 'Who wrote', random.choice(bookTitles) + '?'

        elif num == 1:
            print 'What is the genre of', random.choice(bookTitles) + '?'

        elif num == 2:
            print 'How many words are in', random.choice(bookTitles) + '?'

        elif num == 3:
            print 'What was the release date of', random.choice(bookTitles) + '?'

        elif num == 4:
            print 'Which company published', random.choice(bookTitles) + '?'

        elif num == 5:
            print 'Tell me a summary of', random.choice(bookTitles) + '.'

def organismQueries(numOfQueries = 10):
    '''
    Input the number of book queries to output.
    Outputs may have similar query structures.
    '''

    #gets organism names from text file and adds the names to list organismNames
    organismNames = getList('STEM\Biology\organismNames.txt')

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR(range(7), numOfQueries):

        if num == 0:
            print 'What animals is', random.choice(organismNames), 'related to?'

        elif num == 1:
            print 'Where can a', random.choice(organismNames), 'be found?'

        elif num == 2:
            print 'What is the diet of a', random.choice(organismNames) + '?'

        elif num == 3:
            print 'What is the color of a', random.choice(organismNames) + '?'

        elif num == 4:
            print 'What are the dimensions of a', random.choice(organismNames) + '?'

        elif num == 5:
            print 'What is the lifespan of a', random.choice(organismNames) + '?'

        elif num == 6:
            print 'What is the mass of a', random.choice(organismNames) + '?'

def famousPeopleQueries(numOfQueries = 10):
    '''
    Input the number of famous people queries to output.
    Outputs may have similar query structures.
    '''

    #gets names of famous people from text file and adds the names to list famousPeople
    famousPeople = getList('Misc/famousPeople.txt')

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR(range(11), numOfQueries):

        if num == 0:
            print 'Who is', random.choice(famousPeople) + '?'

        elif num == 1:
            print 'What is', random.choice(famousPeople), 'known for?'

        elif num == 2:
            print 'Where and when was', random.choice(famousPeople), 'born?'

        elif num == 3:
            print 'Who are relatives of', random.choice(famousPeople) + '?'

        elif num == 4:
            print 'Tell me a random fact about', random.choice(famousPeople) + '.'

        elif num == 5:
            print 'Show me a picture of', random.choice(famousPeople) + '.'

        elif num == 6:
            print 'Show me a picture of', random.choice(famousPeople) + '.'

        elif num == 7:
            print 'What ideas or fields are closely associated with', random.choice(famousPeople) + '?'

        elif num == 8:
            print 'What notable books did', random.choice(famousPeople), 'write, if any?'

        elif num == 9:
            print 'Is', random.choice(famousPeople), 'alive?'

        elif num == 10:
            print 'Did', random.choice(famousPeople), 'set any records or get any awards?'

def occupationQueries(numOfQueries = 10):
    '''
    Input the number of occupation queries to output.
    Outputs may have similar query structures.
    '''

    #gets occupation titles from text file and adds the names to list occupationTitles
    occupationTitles = getList('Misc/occupationTitles.txt')

    #prints the question "What is the <aspect of a job> of <job>."
    for i in range(numOfQueries):
        print 'What is the', random.choice(
        ('job outlook', 'employment outlook', 'job satisfaction', 'pay',
         'median pay', 'midcareer salary', 'risk of automation', 'typical bonus',
         'mortality rate', 'typical stress level', 'typical day')
         ), 'of a', random.choice(occupationTitles) + '?'

def foodAndDrinkQueries(numOfQueries = 10):
    '''
    Input the number of food/drink queries to output.
    Outputs may have similar query structures.
    '''

    #gets food names from text file and adds the names to list foodsAndDrinks
    foodsAndDrinks = getList('STEM\Chemistry\ediblesAndDrinkables.txt')

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR(range(11), numOfQueries):

        if num == 0:
            print 'What are', random.choice(['vegan', 'kosher', '']), 'recipes involving',\
            random.choice(foodsAndDrinks), 'if available?'

        elif num == 1:
            print 'Where, near here, can I get', random.choice(foodsAndDrinks) + '?'

        #prints the question "How much <ingredient> is in <food>?"
        elif num == 2:
            print 'How much', random.choice(
            ('total fat', 'saturated fat', 'trans fat', 'cholesterol', 'sodium',
            'dietary fiber', 'sugar', 'protein', 'vitamin A', 'vitamin B',
            'vitamin C', 'vitamin D', 'vitamin D3', 'vitamin E', 'calcium',
            'thiamin', 'biotin', 'vitamin B6', 'folate', 'phosphorus', 'magnesium',
            'vitamin K', 'vitamin B12', 'niacin', 'folic acid', 'choline',
            'panthothenic acid', 'iodine', 'magnesium', 'selenium', 'copper',
            'N-Acetyl L-Cysteine', 'Bromelain', 'Alpha Lipoic Acid', 'Coenzyme Q10')
            ), 'is in', random.choice(foodsAndDrinks) +'?'

        elif num == 3:
            print 'How many calories are in', random.choice(foodsAndDrinks) + '?'

        elif num == 4:
            print 'How is', random.choice(foodsAndDrinks), 'made?'

        elif num == 5:
            print 'What is the nutritional benefit and health harms associated with',\
            random.choice(foodsAndDrinks) + '?'

        elif num == 6:
            print 'What is the typical cost of', random.choice(foodsAndDrinks) + '?'

        elif num == 7:
            print 'Are there low, medium, or high greenhouse gas emmissions associated with',\
            random.choice(foodsAndDrinks) + '?'

        elif num == 8:
            print 'What is the shelf life of', random.choice(foodsAndDrinks) + '?'

        elif num == 9:
            print 'What is the origin of', random.choice(foodsAndDrinks) + '?'

        elif num == 10:
            print 'What is the serving size of', random.choice(foodsAndDrinks) + '?'

def localQueries(numOfQueries = 10):
    '''
    Input the number of queries about the surrounding location of the user to output.
    Outputs may have similar query structures, and some queries pertaining to local phenomena
    are managed in other functions (e.g., weatherQueries).
    '''

    locations = ('restraunts', 'museums', 'zoos', 'movie theaters', 'theatres',
         'bistros', 'diners', 'bakeries', 'bars', 'drive-ins', 'fast food restraunts',
         'fancy restaurants', 'Chinese restaurants', 'sandwich restaurants', 'soup kitchens',
         'ice cream shops', 'fruit shake shops', 'coffeeshouses', 'vegan-friendly restaurants',
         'vegan restaurants', 'vegetarian restaurants', 'vegetarian-friendly restaurants',
         'healthy restaurants', 'quick restaurants', 'restaurants with an all-you-can-eat buffet',
         'malls', 'bowling allies', 'strip clubs', 'antique shops', 'are some things to do',
         'parks', 'history museums', 'art museums', 'libraries', 'places that offer tours',
         'amusement parks', 'opera houses', 'clothing stores', 'jewelry stores',
         'airports', 'rivers', 'arenas', 'cathedrals', 'prisons', 'universities',
         'factories', 'factories looking for employees', 'gas stations', 'baseball fields',
         'hospitals', 'donut stores', 'car dealerships', 'pet stores', 'abortion clinics')

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR(range(2), numOfQueries):

        if num == 0: print 'What', random.choice(locations), 'are near here?'

        elif num == 1:
            print 'Give me directions to the nearest', random.choice(locations) + '.'

def diseaseQueries(numOfQueries = 10):
    '''
    Input the number of disease queries to output.
    Outputs may have similar query structures.
    '''

    #gets disease names from text file and adds the names to list diseases
    diseases = getList('STEM\Health\diseasesNames.txt')

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR(range(4), numOfQueries):

        if num == 0:
            print 'Is', random.choice(diseases), 'contagious?'

        elif num == 1:
            print 'Is susceptibility to', random.choice(diseases), 'heritable?'

        elif num == 2:
            print 'Does', random.choice(diseases), 'go away on its own?'

        elif num == 3:
            print 'What are', random.choice(
            ('some of the affects of', 'some solutions to mitigate',
            'symptoms associated with', 'complications associated with',
            'treatments for', 'drugs for', 'ways to prevent', 'statistics about')
            ), random.choice(diseases) + '?'

def financeQueries(numOfQueries = 10):
    '''
    Input the number of finance queries to output.
    Outputs may have similar query structures.
    '''

    #returns a string of a random amount of money from $100 to $9000
    def randMoney():
        return '$' + str( random.randrange(1, 10) * 100 * random.choice([10, 1]) )

    #returns a discount rate as a string
    #the second term added ensures the discount rate is not 0
    def randDiscount():
        return str( round( random.choice([n/float(n+50) for n in range(9)]), 3 ) +\
        random.randrange(1, 10)/100.0 )

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR([0,0,1,2,3,4,5,5,6,6,6], numOfQueries):

        #prints the question "What is the <"present" or "future"> value of an
        #object worth <money amount> <number of years> years from now if the
        #<word meaning 'discount rate'> is <discount rate>?
        #Compound <time interval>."
        if num == 0:
            print 'What is the', random.choice(['present', 'future']),\
            'value of an object worth', randMoney(), random.randrange(1,30),\
            'years from now if the', random.choice(['cost of capital', 'discount rate']),\
            'is', randDiscount() + '?',  'Compound', random.choice(['monthly', 'annually', 'every half-year']) + '.'

        #prints the question "What is the net present value of <money amount>...
        #if the initial investment was <investment amount> and the discount rate is <discount rate>?"
        elif num == 1:
            print 'What is the net present value of', randMoney(), randMoney(), randMoney(),\
            randMoney(), 'if the initial investment was', '-' + randMoney(),\
            'and the discount rate is', randDiscount() + '?'

        #prints the question "What is the net present value of <money amount>...?"
        elif num == 2:
            print 'What is the IRR of', '-' + randMoney(), randMoney(), randMoney(),\
            randMoney() + '?'

        #prints the question "What is my monthly payment if I have a <number>-year mortgage
        #at a <rate> APR?
        elif num == 3:
            print 'What is my monthly payment if I have a', str(random.randrange(1,35,5)) +\
            '-year mortgage at a', str( 100 * float( randDiscount() ) ) + '%', 'APR?'

        #prints the question "What is is the YTM of a zero-coupon bond with a face
        #value of <face value amount>, a current price of <amount less than face value>,
        #and a maturity of <number> years?"
        elif num == 4:
            faceValue = randMoney()
            print 'What is the YTM of a zero-coupon bond with a face value of',\
            faceValue, 'a current price of', int(faceValue[1:]) - 500, 'and a maturity of',\
            random.randrange(1, 30), 'years?'

        #prints the question "What is <company>'s <attribute>?"
        elif num == 5:
            #gets company names from text file and adds the names to list companies
            companies = getList('Misc/companyStockSymbolsAndNames.txt')

            print 'What is', random.choice(companies) + '\'s', random.choice(
            ('market cap', 'EPS', 'share price', 'asking price', 'bidding price',
             'opening price', 'CEO name', 'revenue', 'beta', 'total assets', 'profit')) + '?'

        #prints the question "What is <amount> <currency1> in <currency2>"
        elif num == 6:
            currencies = ('Dinars', 'Dollars', 'Euros', 'Pesos', 'Rands', 'Rupees', 'Shekels', 'Yen', 'Yuans')

            print 'What is', randMoney()[1:], random.choice(currencies), 'in', random.choice(currencies) + '?'

def productQueries(numOfQueries = 10):
    '''
    Input the number of miscellaneous queries to output.
    Outputs may have similar query structures.
    '''

    #gets food names from text file and adds the names to list foodsAndDrinks
    products = getList('Misc/products.txt')

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR(range(4), numOfQueries):

        if num == 0:
            print 'Who invented', random.choice(products) + '?'

        elif num == 1:
            print 'What is the first known usage of', random.choice(products) + '?'

        elif num == 2:
            print 'What is the cost of', random.choice(products) + '?'

        elif num == 3:
            print 'What is a', random.choice(['complementary product', 'substitute']),\
            'for', random.choice(products) + '?'

        elif num == 5:
            print 'What sells', random.choice(products), 'and where?'

def translationQueries(numOfQueries = 10):
    '''
    Input the number of translation queries to output.
    Outputs may have similar query structures.
    '''

    #gets common words from text file and adds the names to list words
    words = getList('Misc/commonWords.txt')
    #gets languages from text file and adds the names to list languages
    languages = getList('Misc/languages.txt')

    print 'What is' + ' "' + random.choice(words) + '" ' + 'translated to',\
    random.choice(languages) + '?'

def sportsQueries(numOfQueries = 10):
    '''
    Input the number of sports queries to output.
    Outputs may have similar query structures.
    '''

    #gets common words from text file and adds the names to list words
    #it first decides what sports category to use
    category = random.choice(('nfl', 'nba', 'mlb'))
    teams = getList('Sports/' + category + 'Teams.txt')

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR(range(6), numOfQueries):

        #prints the question "What is the <attribute> of the <team>?"
        if num == 0:
            print 'What is the', random.choice(
            ('overall rank', 'roster', 'schedule', 'insignia')
            ), 'of the', random.choice(teams) + '?'

        #prints the question "Who is the <member specificaiton> of the <team>?"
        elif num == 1:
            print 'Who is the', random.choice(
            ('coach of', 'highest scorer on', 'tallest member of')
            ), 'the', random.choice(teams) + '?'

        elif num == 2:
            print 'When is the next game involving the', random.choice(teams) + '?'

        elif num == 3:
            print 'Who do the', random.choice(teams), 'play next?'

        elif num == 4:
            print 'Who is injured on the', random.choice(teams) + '?'

        elif num == 5: print 'Did the', random.choice(teams), 'win?'

def imageVideoQueries(numOfQueries = 10):
    '''
    Input the number of image or video queries to output.
    Outputs may have similar query structures.
    '''

    for i in range(numOfQueries):

        #prints the command "Show me <emotion adjective> <'images' xor 'videos'>
        #related to <thing>."
        print 'Show me', random.choice(('sad', 'funny', 'high-quality', 'animated', '')),\
        random.choice(('images', 'videos')), 'related to',\
        random.choice( getList(random.choice(
        ('Misc/landmarks.txt' , 'Misc/countryNames.txt', 'Misc/cityNames.txt',
        'STEM/Biology/organismNames.txt', 'Entertainment/showNames.txt', 'Entertainment/movieTitles.txt')
        )) ) + ', if available.'

def argumentQueries(numOfQueries = 10):
    '''
    Input the number of argument/contention queries to output.
    Outputs may have similar query structures.
    '''

    for i in range(numOfQueries):

        #prints the command "Tell me an argument for and against the claim, <statement>."
        print 'Tell me an argument for and against the claim,', random.choice(
        ('"The sale of violent videogames to minors should be banned."',
         '"The US ought to decriminalize marajuana."', '"Justice requires reparations to Black Americans."',
         '"Sin taxes are just."', '"Just governments ought to ensure food security for their citizens."',
         '"A progressive income tax is more just than a flat income tax."', '"Infanticide is morally permissible like abortion."',
         '"Ephebophilia is natural and acceptable."', '"There are differences in IQ among races."',
         '"Compulsory inclusion of non-felons\' DNA in any government database is just."',
         '"Artificial Intelligence poses a significant existential risk to humanity in the future."',
         '"The atomic bombing of Hiroshima was immoral."', '"Justice requires the recognition of animal rights."',
         '"A just society ought to presume consent for organ procurement from the deceased."',
         '"Targeted killing is a morally permissible foreign policy tool."', '"The Catholic church is an immoral force."',
         '"It is morally permissible to kill one innocent person to save the lives of more innocent people."',
         '"Military conscription is unjust."', '"Reprogenetics ought to be legal."', '"Monetarism is correct."',
         '"The pursuit of scientific knowledge ought to be constrained by concern for societal good."')
        )

def miscHowQueries(numOfQueries = 10):
    '''
    Input the number of "How" questions to output.
    '''

    #gets questions starting with "How" from text file and adds the names to list questions
    questions = getList('Misc/howQuestions.txt')

    for i in range(numOfQueries):

        #prints questions starting with "How"
        print 'How', random.choice(questions) + '?'

def miscWhyQueries(numOfQueries = 10):
    '''
    Input the number of "Why" questions to output.
    '''

    #gets questions starting with "Why" from text file and adds the names to list questions
    questions = getList('Misc/whyQuestions.txt')

    for i in range(numOfQueries):

        #prints questions starting with "Why"
        print 'Why', random.choice(questions) + '?'

def eventQueries(numOfQueries = 10):
    '''
    Input the number of date questions about events to output.
    '''

    #gets events from text file and adds the names to list questions
    events = getList('Misc/events.txt')

    for i in range(numOfQueries):
        print random.choice(('When','How far away')), 'is the next', random.choice(events) + '?'

def triviaQueries(numOfQueries = 10):
    '''
    Input the number of trivia questions to output.
    '''

    #gets trivia questions from text file and adds the names to list questions
    questions = getList('Misc/trivia.txt')

    for i in range(numOfQueries):
        print random.choice(questions) + '?'

def physicsQueries(numOfQueries = 10):
    '''
    Input the number of physics queries to output.
    Outputs may have similar query structures.
    '''

    #loops through a random list of integers. 0: 1st query structure, 1: 2nd,...
    for num in sampleWR(range(6), numOfQueries):

        if num == 0:
            print 'If a truck has a linear acceleration of', random.randrange(1,5000),\
            'm/s^2 and the wheels have an angular acceleration of', random.randrange(1,5000),\
            'rad/s^2, what is the diameter of the truck\'s wheels?'

        elif num == 1:
            print 'You use a', random.randrange(1,500), 'cm long wrench to remove the lug',\
            'nuts on a car wheel If you pull up on the end of the wrench with a force of',\
            random.randrange(1,5000) * 10, 'N at an angle of', random.randrange(1,180),\
            'degrees; what is the torque on the wrench?'

        elif num == 2:
            print 'A', random.randrange(5, 500)/1000., 'kg hockey puck moving at',\
            random.randrange(1,100), 'm/s is caught and held by a', random.randrange(50,150),\
            'kg goalie at rest. With what speed does the goalie slide on the ice?'

        elif num == 3:
            print 'Zelda strikes a', random.randrange(5, 500)/1000., 'kg golf ball with a force of',\
            random.randrange(20,800), 'N and gives it a velocity of', random.randrange(1,100),\
            'm/s. How long was Zelda\'s club in contact with the ball?'

        elif num == 4:
            print 'Sphere A, with a charge of', random.randrange(1,1000), 'micro C,',\
            'is located near another charged sphere B. Sphere B has a charge of',\
            random.randrange(1, 1000), 'micro C, and is located', random.randrange(1, 1000)/10.,\
            'cm to the right of A. What is the force of sphere B on sphere A?'

        elif num == 5:
            print 'A straight wire carrying a', random.randrange(1,100)/10.,\
            'A current is in a uniform magnetic field oriented at right angles to the wire.',\
            'When', random.randrange(1,100)/10., 'm of the wire is in the field, the force on',\
            'the wire is', random.randrange(1,100), 'N. What is the strength of the magnetic field B?'

def musicQueries(numOfQueries = 10):
    '''
    Input the number of music queries to output.
    Outputs may have similar query structures.
    '''

    for i in range(numOfQueries):

        print 'Play me a song or piece in the genre', random.choice(
        ('blues', 'opera', 'classical', 'orchestral', 'bluegrass', 'techno',
         'trance', 'industrial', 'hip-hop', 'gangsta rap', 'christmas',
         'trad jazz', 'K-pop', 'teen pop', 'metal', 'contemporary folk',
         'hawaii', 'inspirational', 'swing', 'disco', 'motown', 'cajun'
        )) + '.'

def miscCommands(numOfQueries = 10):
    '''
    Input the number of commands to output.
    Some outputs may overlap with queries from other functions.
    '''

    #gets commnands from text file and adds the names to list commands
    commands = getList('Misc/commands.txt')

    for i in range(numOfQueries): print random.choice(commands) + '.'

def scienceAdviceQueries(numOfQueries = 10):
    '''
    Input the number of questions answerable by scientific studies to output.
    Some outputs may overlap with queries from other functions.
    '''

    #gets objectives from text file and adds the names to list objectives
    objectives = getList('Misc/objectives.txt')

    for i in range(numOfQueries):

        #this may contain split infinitives
        print 'Advise me how to', random.choice(objectives) + '.'

#calls functions for queries
chemistryQueries(2)
weatherQueries(2)
movieQueries(2)
showQueries(2)
collegeQueries(2)
mathQueries(2)
pokemonQueries(2)
videoGameQueries(2)
cityAndCountryQueries(2)
bookQueries(2)
organismQueries(2)
famousPeopleQueries(2)
occupationQueries(2)
foodAndDrinkQueries(2)
localQueries(2)
diseaseQueries(2)
financeQueries(2)
productQueries(2)
translationQueries(2)
sportsQueries(2)
imageVideoQueries(2)
argumentQueries(2)
miscHowQueries(2)
miscWhyQueries(2)
eventQueries(2)
triviaQueries(2)
physicsQueries(2)
musicQueries(2)
miscCommands(2)
scienceAdviceQueries(2)