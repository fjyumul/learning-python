class TextAnalyzer(object):
    
    rawText = ""
    fmtText = ""

    def __init__ (self, text):
        # assign raw text
        self.rawText = text

        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

analyzer = TextAnalyzer(givenstring)

print("Raw Text: " + analyzer.rawText)
print("Formatted Text: " + analyzer.fmtText)

freqMap = analyzer.freqAll()
print("Frequency All: ",freqMap)

word = "lorem"
print("Frequency of ", word ,": " , analyzer.freqOf(word))