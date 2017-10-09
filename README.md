# cs632
Deep Learning


Basic useful feature list:

 * Ctrl+S / Cmd+S to save the file
 * Ctrl+Shift+S / Cmd+Shift+S to choose to save as Markdown or HTML
 * Drag and drop a file into here to load it
 * File contents are saved in the URL so you can share files


This assignment is divided in two parts:-


 1) 1. Import Scikit learn iris data and divide into train and test data in the ratio 70:30.
    2. Create a custom classifier to train the training data and predict the accuracy.
    3. Implement fit , predict and constructor method similar to k nearest neighbour classifier
    4. Input number of nearest neighbour k in classifier method and display accuracy

 2) 1. Retireve 50 emails with labels as spam/ not spam.
    2. Use dataframe to clean the data and divide the data in 50:50 ratio of training data to test data.
    3  Implement classiifer developed in part one and train  models.
    4. put value of nearest neighbour as 3(or any) and test the training data.
    5. Display acurracy of training data.

Look, a list!

 IRIS training data:-
    array([[ 5.8,  4. ,  1.2,  0.2],
       [ 5.1,  2.5,  3. ,  1.1],
       [ 6.6,  3. ,  4.4,  1.4],
       [ 5.4,  3.9,  1.3,  0.4],
       [ 7.9,  3.8,  6.4,  2. ],
       [ 6.3,  3.3,  4.7,  1.6],
       [ 6.9,  3.1,  5.1,  2.3],
       [ 5.1,  3.8,  1.9,  0.4],
       [ 4.7,  3.2,  1.6,  0.2],.....

 IRIS testing data:-
     array([[ 5. ,  3.4,  1.6,  0.4],
       [ 6.8,  2.8,  4.8,  1.4],
       [ 5. ,  3.5,  1.6,  0.6],
       [ 4.8,  3.4,  1.9,  0.2],
       [ 6.3,  3.4,  5.6,  2.4],
       [ 5.6,  2.8,  4.9,  2. ],
       [ 6.8,  3.2,  5.9,  2.3],
       [ 5. ,  3.3,  1.4,  0.2],
       [ 5.1,  3.7,  1.5,  0.4],
       [ 5.9,  3.2,  4.8,  1.8],
       [ 4.6,  3.1,  1.5,  0.2],
       [ 5.8,  2.7,  5.1,  1.9],.......

 Spam email :- 
     Bodyfile:-
       	
            0	One of a kind Money maker! Try it for free!Fro...
            1	link to my webcam you wanted Wanna see sexuall...
            2	Re: How to manage multiple Internet connection...
            3	[SPAM] Give her 3 hour rodeoEnhance your desi...
            4	Best Price on the netf5f8m1 (suddenlysusan@Sto...
            5	linux.ie mailing list memberships reminderThis...
            6	Re: Apple Sauced...againAt 1:16 AM -0400 on 10...
            7	Re: results for giant mass-check (phew)I never...
            8	Re: RPM's %post, %postun etcHave you tried reb...    

      LabelFile:-
                    label	Name
            0	0	00000.txt
            1	0	00001.txt
            2	1	00002.txt
            3	0	00003.txt
            4	0	00004.txt
            5	1	00005.txt
            6	1	00006.txt
            7	1	00007.txt
            8	1	00008.txt
            9	1	00009.txt
            10	1	00010.txt
            11	0	00011.txt       

And here's some code! :+1:

Classifier:-
  class myCustomClassifier():
    def __init__(self,n_number = 3):
        self.n_number = n_number
    
    def fit(self,iris_X_train,iris_y_train):
        self.iris_X_train = iris_X_train
        self.iris_y_train = iris_y_train
        
    def closest(self,row):
        
        tempDist = []
        tempFull = []
       
        counter = 0
        
        for i in range(1,len(iris_X_train)):
            
            dist = eucledean(row,self.iris_X_train[i])
            tempDist.append((dist,self.iris_y_train[i]))
           
        
        tempFull = [i[1] for i in sorted(tempDist)[:self.n_number]]
        voteResult = Counter(tempFull).most_common(1)[0][0]
     
        #Take vote of k number of closest train data and return one with most vote      
        return voteResult
    
    
        
    def predict(self,x_test):
        
        predictions = []
        for row in x_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions




### Stuff used to make this:

 * [markdown-it](https://github.com/markdown-it/markdown-it) for Markdown parsing
 * [CodeMirror](http://codemirror.net/) for the awesome syntax-highlighted editor
 * [highlight.js](http://softwaremaniacs.org/soft/highlight/en/) for syntax highlighting in output code blocks
 * [js-deflate](https://github.com/dankogai/js-deflate) for gzipping of data to make it fit in URLs
