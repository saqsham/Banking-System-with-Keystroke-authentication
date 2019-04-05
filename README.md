<h2>Authentication using keystroke dynamins implemented on a banking management system via captcha concept
<br>
<br>Client side functionality </h2>
<p>(hopefully will develop this project for server side too.)</p>
<h3>Restrictions</h3>
<p>(mentioning restrictions first since it is important to understand this project, also includes the conclusions which I came to after hours of my hardwork & dedication.)
<br>Skip to <strong>Working</strong> after reading the following:
<br>While taking keyprints enter normally, no need to rush or stop.
<br>While typing for the keyword ".tie5Roanl" don't use any other keys like num, space, backspace , delete etc., didn't made cases for them.
<br>Try integrating the login and captcha in one page, I tried but wasn't able to and didn't try later.
<br>The time is counted if the cursor is blinking, click outside of the box area to stop that.
<br>Don't use backspace to erase the keyword in registration, use the refresh or select whole of the text by mouse and start typing, need to find better way for this.
<br>I have only used one SVM machine due to time restrictions, you can add more than 1 or as per your need but(should be) the range for EER values will be different.
</p>
<h3>Prerequisites & languages used/required</h3>
<p><h4>Python (3.7)</h4>
(if possible find a better way to import in py3.7)
<br>Packages
<br>- pymongo
<br>- sklearn.svm
<br>- pandas
<br>- numpy
<br>Framework
<br>- Flask
<br><h4>Javascript</h4>
Libraries 
<br>- jQuery
<br>- Chart js
<br>- D3 js
<br>- NVD3 js
<br>- table2csv
<br><h4>Dataset</h4>
- Used CMU dataset
<br>- consists of 50 users which have typed the keyword 400 times each
</p>
<hr>
<p><h4>Concepts</h4>
(Didn't include the most basic concepts for keystoke dynamics.)
<br>We have used  the  Keystroke concepts as mentioned here and studied them well, I recommend to read this article and also see their project/source code on github:
<br>https://appliedmachinelearning.blog/2017/07/26/user-verification-based-on-keystroke-dynamics-python-code
<br>We have only used a single SVM machine for this project as per our requirement, may or may not advance this project further .
</p>
<hr>
<p><h4>Working</h4>
So how does this captcha system works ?
In short, first we take keyprints from a Client/user who wishes to join this bank(or may be any other institution etc.), i.e, registration process which consists of
keystroke prints of the user by making him type the keyword ".tie5Roanl" 20 times(a minimum of 15 is recommended). 
<br> After the registration is done a download button shows after 20 times, and no need to worry if he/she has written the keyword wrong since the js will only take 
the input for that keyword only and append the prints to a table made dynamically using jsDOM, download and save that file, by default name user.csv, in the same path as specified 
in app.py, basically converted the table to csv using js library (you can directly edit csv in php, node.js etc), the username is edited to the csv using a cookie
and those 20 prints are appended to our keystroke.dataset.csv using python(code in app.py).
<br>So registration is done, now comes the login part the <strong>real part</strong> of our project, here we first we confirm the existence of the 
Client/user by authenticaiton his/her username and password and that is out 1st factor authentication, and captcha acts as a 2nd factor authentication.
<br>In authentication we ask the Client to input the keywork ".tie5Roanl" again but only once and then download the file, default name user.csv, and save it in
the directory as you specified in app.py, and now click on submit button and voila ! he/she is logged in if it's a real user or logged out if it's an imposter.
<br>A bunch of process happens when that "submit" button is clicked, first the user.csv is appended to our dataset and then SVM comes into play here
what it does is makes the input values as a standard and then using machine learning algorithms calculates the user(20 prints from registration process) 
and imposter scores(the rest of the users in the dataset, takes their 20 prints only too) and then compares that value to these scores and then another
algorithmn to calculate the EER value(equal equvalence rate) is calculated, the lesser the value the more orignal the user is, after stdying these these 
values by locally creating a dataset I have come to a conclusion that the nice range for determining if the user is genuine or not is between 0.4 and 0.18,
although the lesser the bettter is said but that doesn't fit right for this particular SVM machine which is comparatively simple but well thought.
<br>And so the authentication system came into fruitation.
</p>
<hr>
<p><h4>Refrences</h4>
To understand how keyprints are taken refer to this repo:
<br>https://github.com/bezoar17/bezoar17.github.io/tree/master/keystroke
<br>I have edited the code and made it work for last character except "Enter", and removed what I didn't need for this project
<br>(will refer some paper in next edit)
</p>
<hr>
<h4>Thank you</h4>
<h3>For reading this far</h3>
