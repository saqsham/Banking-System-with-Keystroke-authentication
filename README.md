# Banking-System-with-Keystroke-authentication

Project basically consists of a basic bank website with keystroke dynamics as an extra layer of security.
The main idea is that, the keystroke of individual people are very unique(like fingerprints). Using this fact, we can extract patterns from a users typing style and authenticate him based on that. If the typing style of the user matches his pattern stored in dataset, then he is authenticated. Otherwise, he is considered an imposter.

The Front end is built on HTML,CSS and JS while the backend is on MongoDB. Flask is used as connection

The bank website has 2 logins, client and admin. The client login has transaction history, account details and the ability to transfer funds between accounts. The admin login has the ability to delete/modify clients and view all the clients registered under that particular admin.

The Keystroke is taken in using Javascript.
*3 Main Values are calculated-   UP-DOWN time(UD)    DOWN-DOWN time(DD) and HOLD time.*
HOLD times is calculated as UD-DD

![Image of Keystroke Times](https://github.com/VaibhavBhandari2999/Banking-System-with-Keystroke-authentication/blob/master/static/img/timing_explanation.png)


We are taking the CMU dataset for keystroke values which includes 57 users typing the keystroke in 8 batches of 50 keystrokes per batch.This is the only major dataset avaiable for keystroke patterns. In this program, the CMU dataset is saved as keystroke.trial.csv

It is possible to make our own dataset with the only hurdle being time and manpower to get this amount of data.

During Registeration, the client is asked to type a specific phrase ".tie5Roanl" 20 times to capture his/her keystroke. 
The UD,DD and Hold times are calculated and put in a CSV. The username of the Client, taken from the previous registeration screen, is taken via cookies to the keystroke page and put as the 1st column in the CSV file. This CSV file is then appended to the end of the CMU dataset CSV. This essentially meanse, the client is adding his keystroke pattern to the dataset.

During Login, the client is asked to type the same phrase ".tie5Roanl" only once. This solitary set of values is pasted in a CSV which is then appended to the end of the CMU dataset.

The main algorithm doing the work is SVM which is implemented using python. With the SVM, we get an EER(Estimated Error Rate). 
Through trial and error, we have determined that between EER=0.4 and EER=0.15, the right person is authenticated. If the value is outside this range, the user is seen as an imposter and is not logged in.
