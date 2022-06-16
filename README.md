<h1 align="center">MS3 Final Cocktails</h1>

[View the live project here.](https://rhysmoggs.github.io/ms3-final-cocktails/)

Here is the brand new launch for the geography quiz: Globe Trotter Quiz.

<h2 align="center"><img src="assets/readme-images/am-i-responsive.png"></h2>

This is the first interactive quiz the company has launched, announcing themselves to the world. Globe Trotter Quiz is a passion project, birthed from the creators love of travel and adventure. Having been fortunate enough to travel the world, the creator still longs and obsesses over memories and places visited, and loves to to be reminded about all travel-related things. The creator has a desire to share that love with a greater audience: like-minded people and travellers, keen quizzers, families and students - all are welcome to challenge themselves! The creator is excited to launch their quiz and hope to attract more and more players from across the world.

### Quiz Concept and Rules:

A classic geography quiz, suitable to single or multiple players of all ages. The Globe Trotter Quiz is a multiple-choice quiz where the user is presented with 10 questions, each correct answer worth 2500 miles. The goal? To answer 10 correct answers totalling a whopping 25,000 miles - about the same distance it is to fly around the world! See if you can travel to the top of the High Scores list!

The quiz will clearly display information for new and returning customers including the creators contact information via social media links. The quiz is fully responsible on a range of devices - from hand-held devices to larger screens such as monitors or even TVs. This is to ensure that as many people as possible can play the quiz and enjoy this journey.

The quiz can be played by one person or as many as would like to partake. There are rumours of a more child-friendly version to follow with additions of sound and pictures and even theme changes.

The quiz generates 1 question at a time, with 4 multiple choice options as answers.
The player clicks on the buttons/answers and the quiz gives a visual prompt via the colour change to signify the players selection is correct (gold) or incorrect (red).
The quiz automatically displays the next question after a short delay.
There are a total of 10 questions to answer.
The end screen for the quiz gives the total amount of 'miles travelled'.
A player can enter their name to save their high score to the High Scores list.

## User Stories

Following are the goals that the quiz should provide for each user.

#### As a New User :
* I want to to be able to access and play quiz on the device I'm using.
* I want to to be able to play with ease.
* I want to to be able to understand the quiz immediately.
* I want to to be able to access instructions if need be.
* I want to to be able to contact the quiz developers if I wish to.
* I want there to be plenty of variety.

#### As a Returning User :
* I want to find information about the company's background, their story and growth.
* I want to find the best way to get in contact with the company with any questions I may have.
* I want to be able to contact the company in many different ways.
* I want to be able to view my high scores.
* I want to be able to save my score after the quiz.
* I want to to be able to access and play the quiz on a range of devices/browsers.

## Design
Once the user goals and the projects intentions were set out, the next step was to design the aesthetic aspects of the Globe Trotter quiz.

### Wireframes
Wireframes were drawn using [Balsamiq](https://balsamiq.com/) at the beginning of the project. They were referenced throughout the design and building of the quiz. Following are a series of images showing the Globe Trotter Quiz on the three main screen sizes: desktop, tablet and mobile. Every major section of the quiz is also included.

#### Desktop

- Home Page Wireframe

<img src="wireframes/desktop-index.png">

- Quiz Wireframe

<img src="wireframes/desktop-quiz.png">

- How To Play Wireframe

<img src="wireframes/desktop-how-to.png">

- Contact Wireframe

<img src="wireframes/desktop-contact.png">

- High Scores Wireframe

<img src="wireframes/desktop-highscore.png">

- End Screen Wireframe

<img src="wireframes/desktop-end.png">

#### Tablet

- Home Page Wireframe

<img src="wireframes/tablet-index.png">

- Quiz Wireframe

<img src="wireframes/tablet-quiz.png">

- How To Play Wireframe

<img src="wireframes/tablet-how-to.png">

- Contact Wireframe

<img src="wireframes/tablet-contact.png">

- High Scores Wireframe

<img src="wireframes/tablet-highscore.png">

- End Screen Wireframe

<img src="wireframes/tablet-end.png">

#### Mobile

- Home Page Wireframe

<img src="wireframes/mobile-index.png">

- Quiz Wireframe

<img src="wireframes/mobile-quiz.png">

- How To Play Wireframe

<img src="wireframes/mobile-how-to.png">

- Contact Wireframe

<img src="wireframes/mobile-contact.png">

- High Scores Wireframe

<img src="wireframes/mobile-highscore.png">

- End Screen Wireframe

<img src="wireframes/mobile-end.png">

#### Colour Palette
- The colour palette has an old-fashioned, nostalgic theme which pays homage to classic travel and adventure when combined with the imagery. This contrasted well with a modern and functional quiz in terms of layout, and the general theme of travelling around the world by plane. The background image (maps.jpg) provides an array of browns, yellows, black and some shaded/darker colours.
- The heading and the game container use the same colour (rgba(230,236,240)), with a slight opacity for the container, allowing the background image to be seen, but not interfere too much with the flow and visibility of the quiz/content.
- By default, all buttons have a colour of "cultured/ whitesmoke" (rgb(239, 239, 239)) and that simplicity allows other colours and content to shine.
- The text colour is mostly black (rgb(0,0,0)) to ensure a greater contrast between the buttons and container colours. 
- The most important text is a gold or "cyber yellow" (rgb(255,210,0)) colour. This colour is synonymous with victory, champions and has forever been a highly desirable and attractive colour. The reason for choosing this colour is obviously to entice the user to keep totalling up the golden numbers during the quiz, and also to challenge the users to reach the top of the High Scores list.
- A slightly opaque antique brass (rgb(187 148 133) is often for shadows, to help bring depth and highlight some interactive features such as buttons.

<img src="assets/readme-images/palette.png">

- It was decided early on in the design stage that the gold (cyber yellow) colour would be important for the quiz. Some of the other colours were chosen around having this colour in mind, especially to ensure the colour was a focal point - always drawing the user's eyes to it and never obstructed or poorly contrasted by other colours. Therefore, the black font colour and the container and button colours provided the perfect colours to balance this. These combinations helped highlight the importance of providing a visually appealing quiz but also with high contrast and readability a priority.

- Here is the [Contrast Checker](https://webaim.org/resources/contrastchecker/) tool used to support this:

<img src="assets/readme-images/contrast.png">



#### Images
- The use of photography is vital in creating allure and desire, especially for an interactive quiz. Users are drawn by what they see. The maps.jpg background image is large and provides a fantastic colour to build an interface on. It also provided contrast and highlighted the actual game area from the background itself. 

- It's vital for the theme to be clear and obvious. The background image makes the quiz recognizable and memorable so people recall and return to it, which will draw more eyes to the quiz. This, along with the CSS styling and colour palette, helps build and clarify that the quiz is travel related. The following image was used.

<img src="assets/readme-images/maps.jpg">

Logo

<img src="assets/images/logo.png">

Plane

<img src="assets/images/plane.png">

#### Font
-  The Globe Trotter Quiz uses the Poppins font. It provides that clean, clear style without compromising on readability - a vital design feature for any quiz. This is available for free via [Google Fonts](https://fonts.google.com/) and imported via CSS. Sans Serif is used as a secondary option in case of failure to import  the font into the quiz correctly. Poppins is a clean font used frequently in designs, so it is both attractive and appropriate.

## Accessibility
Extremely important aspect.
-   Semantic design.
-   The use of alt to describe images and other content.
-   Aria-labelledby to link sections.
-   Colour and contrast considerations and testing.
-   Adding labels to forms.

## Features

-   Responsive on all device sizes - from 320px upwards to larger desktops reaching 1200px and more.

Here are the 3 mains sections of the quiz:

### - The main menu

<img src="assets/readme-images/main-menu.png">

### - The quiz area

<img src="assets/readme-images/quiz.png">

### - The end screen

<img src="assets/readme-images/end-screen.png">

## Interactive Elements

-   Following is a list of all interactive elements of the Globe Trotter Quiz.

#### Quiz Logo

As shown on the images below, the quiz logo and title is very clear and bright. The centrepiece, always there and clickable. It shows off the quiz nicely, it's obviously related to geography and serves as a constant reminder to the user about where they are and what they are playing. The logo itself is a clickable link (a cursor appears when hovering over), and returns the user back to the home page at any time. 

<img src="assets/readme-images/logo-click.png">

```javascript
logoReload.addEventListener("click", reloadGame);

function reloadGame() {
    window.location.assign('index.html');
}
```

#### Toggle Menu Elements

Listed are the main features of the main menu of the quiz. The user simply clicks to show or hide the buttons to display info or return back to the main menu.

#### - How to Play

<img src="assets/readme-images/how-to-container.png">

```javascript
howToButton.onclick = function () {
    if (howToDiv.style.display !== "block") {
        howToDiv.style.display = "block";
        startButton.classList.add('hide');
        contactButton.classList.add('hide');
        highscoresButton.classList.add('hide');
    } else {
        howToDiv.style.display = "none";
        startButton.classList.remove('hide');
        contactButton.classList.remove('hide');
        highscoresButton.classList.remove('hide');
    }
};
```

#### - Contact

Each icon for the social media links turn gold when the user hovers over them to highlight the focused icon.

<img src="assets/readme-images/contact-container.png">
<img src="assets/readme-images/contact-container-hover.png">

```javascript
contactButton.onclick = function () {
    if (contactDiv.style.display !== "block") {
        contactDiv.style.display = "block";
        startButton.classList.add('hide');
        howToButton.classList.add('hide');
        highscoresButton.classList.add('hide');
    } else {
        contactDiv.style.display = "none";
        startButton.classList.remove('hide');
        howToButton.classList.remove('hide');
        highscoresButton.classList.remove('hide');
    }
};
```

The social media links on smaller screens (below 481px - such as mobile phones) have a more mobile-friendly layout.

<img src="assets/readme-images/mobile-social-links.jpg">

#### - High Scores

<img src="assets/readme-images/highscores-container.png">

````javascript
highscoresButton.onclick = function () {
    if (highscoresDiv.style.display !== "block") {
        highscoresDiv.style.display = "block";
        startButton.classList.add('hide');
        howToButton.classList.add('hide');
        contactButton.classList.add('hide');
    } else {
        highscoresDiv.style.display = "none";
        startButton.classList.remove('hide');
        howToButton.classList.remove('hide');
        contactButton.classList.remove('hide');
    }
};
````

#### Buttons

#### - General Buttons

- Almost every button is styled to look the same. A clean and clear button to make for user readability and speed, paramount to elite quizzing.

<img src="assets/readme-images/button.png">

- The colours simply invert when a cursor hovers over them. A simple visual indicator and keeping in line with the colour palette.

<img src="assets/readme-images/button-hover.png">

#### - High Scores Button

- The few exception to the rule is the High Scores button (and mention the disabled button). Due to the nature of this button and it's significance, it was decided to style this differently with a golden (#) hue/ . This is pure bragging rights and to entice the players to compete for the highest score. it will be big factor for returning players.

<img src="assets/readme-images/button-highscore.png">

#### - Save Button
- The Save button is set as disabled as a default. Once the user inputs their name, the button returns to a normal state, just like the others.

<img src="assets/readme-images/button-disabled.png">

#### - Correct Answer Button

- Gold (rgb(255,210,0)) indicates a correct answer.

<img src="assets/readme-images/button-correct.png">

#### - Incorrect Answer Button

- Red (rgb(255,0,0)) indicates an incorrect answer.

<img src="assets/readme-images/button-incorrect.png">

#### - Input

- The 'Enter your name' input field has a very basic style applied. IF the user chooses not to enter their name, then the Save button remains disabled and the user will not be able to save their score to the High Scores section.

<img src="assets/readme-images/input.png">

#### - Progress Bar

- The progress bar indicates the progress made by the user via the golden colour-fill and plane image. Every correct answer adds 10% to the progress bar - with the user's aim to reach 100%, a total of 10/10 correct answers and maximum score.

Here is the code that increments the score and allows the plane image to track the progress bar with each correct answer. This all happens simultaneously.

```javascript
if(classToApply === 'correct') {
    correctAnswers = (correctAnswers + 1);
    
    incrementScore(SCORE_POINTS);
    progressBarFull.style.width = `${correctAnswers * 10}%`;
    plane.style.left = "100%";
}
```

<img src="assets/readme-images/progressbar.png">


#### - API
The URL in the JS code below were preselected by the developer. The categories for the quiz are:
- Number of Questions - 10
- Category - Geography
- Difficulty - Easy
- Type - Multiple Choice
- Default Encoding

```javascript
fetch(
    'https://opentdb.com/api.php?amount=10&category=22&difficulty=easy&type=multiple'
)
    .then((res) => {
        return res.json();
    })
```

#### - Alternative Ending

This snippet of code shows two possible outcomes when the user answers all 10 questions. The first outcome displays the message if the maximum score (25000) is reached, if not, the else statement triggers. It gives added importance and attention to those users capable of answering 10 correct questions.

```javascript
if (mostRecentScore == 25000) {
    finalScore.innerHTML = `<span id="span-score"> ${mostRecentScore} miles travelled!<br><br>You successfully travelled the world!</span>`;
  } else {
    finalScore.innerHTML = `<span id="span-score"> ${mostRecentScore} miles travelled</span>`;
}
```

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries, Programs and Tools Used

1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts is used to import the 'Poppins' font into the style.css file which is used on all fonts within the quiz.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome is used on all pages throughout the quiz to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery is used to simplify and manipulate some tasks instead of regular JS.
1. [Git:](https://git-scm.com/)
    - Git is used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq is used to create the [wireframes](#wireframes) during the design process.
1. [Eye Dropper:](https://eyedropper.org/).
    - This colour picker tool was used to to pick and experiment with colours.
1. [Coolors:](https://coolors.co/)
    - This tool was used to to setup the colour palette [here](#colour-palette).
1. [Canva:](https://www.canva.com/)
    - Canva is used to create the quiz logo and small plane image seen in the progress bar.
1. [TinyPNG:](https://tinypng.com/)
    - TinyPNG is used to optimize images used in the quiz and this README.
1. [Miscrosoft Paint:](https://support.microsoft.com/en-us/windows/get-microsoft-paint-a6b9578c-ed1c-5b09-0699-4ed8115f9aa9)
    - Microsoft Paint is used to crop and resize images and editing photos for the project.
1. [Snip & Sketch:](https://www.microsoft.com/en-gb/p/snip-sketch/9mz95kl8mr0l)
    - Snip & Sketch is used to screenshot the majority of images used for this README.
1. [WPS Office:](https://www.wps.com/)
    - WPS Office is used to create the table for the [Testing Quiz Flow and Functionality](#testing-quiz-flow-and-functionality) and README.md spell-checking.
1. [Am I Responsive?:](http://ami.responsivedesign.is/)
    - Used to create the image at the very top of this document.

## Testing

The W3C Markup Validator, W3C CSS Validator and JSHint tools were used to validate every page of the project to ensure there were no syntax errors in the project. If any were found during development, they were addressed.

-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input)

index.html

<img src="assets/readme-images/validator.png">

end.html

<img src="assets/readme-images/validator2.png">

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

style.css

<img src="assets/readme-images/jigsaw.png">

-   The Warnings(1), also seen on the above screenshot, references the Google imported style sheet, and that it won't check that.

<img src="assets/readme-images/jigsaw-error.png">

-   [JSHint](https://jshint.com/) 

main.js

<img src="assets/readme-images/jshint.png">

end.js

<img src="assets/readme-images/jshint2.png">

## Testing Original User Stories

Following are the original [User Stories](#user-stories) set out in the early design stages of the project. They were individually tested to see if each goal was satisfied against the completed project.

#### As a New User :
* I want to to be able to access and play quiz on the device I'm using.
    - The quiz has been tested for ease of access and responsiveness on dozens of devices (handheld devices such as mobile phones and tablets, laptops, desktop computers and larger Samsung TVs) and is fully responsible from at least a minimum of 320px up to at least 1200px. See [here](#further-testing) for more testing related tasks.
* I want to to be able to play with ease.
    - Part of the biggest draw to quiz by nature is their simplicity and easy of use. The quiz is a click-and-play format and the interactive prompts and layout make it very clear to understand for any first-time user.
* I want to to be able to understand the quiz immediately.
    - The style and layout, along with the interactive features and prompts enable first-time users to understand the quiz, the theme and it's purpose.
* I want to to be able to access instructions if need be.
    - The How to Play [button](#how-to-play) is clear and obvious from the first screen the user is presented with. A minimal styling setup and only 4 buttons ensure that information is displayed clearly and to not overwhelm users. All instructions are found after clicking on this button.
* I want to to be able to contact the quiz developers if I wish to.
    - The Contact [button](#contact) is clear and obvious from the first screen the user is presented with. A minimal styling setup and only 4 buttons ensure that information is displayed clearly and to not overwhelm users. All contact information is found after clicking on this button.
* I want there to be plenty of variety.
    - Thanks to the API automatically generating questions from a deep database and also having the answers randomly ordered from the 4 possible choice-containers, the variety and quiz is never the same.

#### As a Returning User :
* I want to find information about the developer's background, their story and growth.
    - The Contact [button](#contact) provides links to all the developers social media [links](#contact) (twitter, YouTube, instagram and LinkedIn). The contact information can be found on those platforms. For example the developers contact information is on each profile of these social media websites, there are YouTube vlogs of the company's developing stage, snippets of inside-info on instagram and all professional history and access via LinkedIn.
* I want to find the best way to get in contact with the company with any questions I may have.
    - Once the Contact [button](#contact) is clicked., it provides links to all the developers social media links (twitter, YouTube, instagram and LinkedIn). The contact information can be found on those platforms and provides a quick and direct link to the users queries.
* I want to be able to contact the company in many different ways.
    - Once the Contact [button](#contact) is clicked, it gives access to 4 social media options the user can choose to contact the developer through.
* I want to be able to view my high scores.
    - Once the High Scores [button](#high-scores) is clicked, it gives access to the high scores list, with a maximum of 5 user names and scores capable of being displayed.
* I want to be able to save my score after the quiz.
    - After completing all 10 questions, the quiz displays the [end screen](#the-end-screen) to the user. Here, the user can choose to enter their name in the prompted [input field](#input) and the previously disabled Save [button](#save-button) is made clickable. If clicked, the user name is saved to the High Scores list if it made the top 5 high scores.
* I want to to be able to access and play the quiz on a range of devices/browsers.
    - The quiz has been tested for ease of access and responsiveness on dozens of devices (handheld devices such as mobile phones and tablets, laptops, desktop computers and larger Samsung TVs) and is fully responsible from at least a minimum of 320px up to at least 1200px. it also works on multiple browsers as stated [here](#further-testing).

## Google Chrome Lighthouse Test

Following are the Google Chrome Lighthouse results for each page.

- Main menu and quiz area/ index.html

<img src="assets/readme-images/lighthouse-index.png">

- End page / end.html

<img src="assets/readme-images/lighthouse-end.png">

### Testing Quiz Flow and Functionality

All of the following tests were repeated multiple times to ensure a fair test. The same tests were then repeated multiple times on different browsers (Google Chrome, Mozilla Firefox, Microsoft Edge and Opera) and then finally the same tests were repeated again on multiple occasions and for different devices (mobile phones, tablets, laptops and larger screen sizes).

#### - Main Menu Test
<img src="assets/readme-images/main-menu-test.png">

#### - Quiz Area Test
<img src="assets/readme-images/quiz-area-test.png">
<img src="assets/readme-images/quiz-area-test2.png">

#### - End Screen Test
<img src="assets/readme-images/end-screen-test.png">

### Further Testing

-   Testing was predominantly made using Google Chrome's own developer tools and 'Inspect Mode', although testing was done sporadically on alternative browsers with each major addition to the quiz e.g new content, style updates and responsive changes via media queries.
-   Console.log() function was used for JavaScript code development.
-   All interactive elements of the quiz were tested. Button functions, clicking, hiding/showing content, user input, links and general flow of quiz. Bugs were fixed as they arose.
-   The quiz was tested on Google Chrome, Mozilla Firefox, Microsoft Edge and Opera browsers and ran efficiently on each one. There were slight stylistic differences when testing between browsers, but these were resolved afterwards. See below for an example when testing on the Opera browser:
<img src="assets/readme-images/opera-test.png">
To resolve this, the background-colour was specified in the style.css file, instead of allowing the browsers default styling/button colours decide. This encouraged further testing and ensuring that all important style factors were specified.
-   The quiz was viewed on a variety of devices such as Desktop, Laptop, iPad & iPhoneX.
-   Feedback from friends and family, testing the quiz with no prior instruction or expectations. Adjustments were made if necessary to satisfy the [User Targets](#as-a-new-user).

### Bug Fixes
Bug fixes were predominantly completed in real-time as soon as any issues arose. This was to ensure the project would continue developing smoothly without serious, unmanageable bugs arising later that could drastically reduce development time or the layout and functioning of the quiz.

-   As seen from the style.css file, there is a lot of custom CSS. Media queries were used at different breakpoints - although time consuming, it was vital to invest time into this to ensure the quiz was functioning correctly on various displays to ensure a major [User Targets](#as-a-new-user) was met. Some JavaScript tweaks were also implemented to alter the class width at different stages of the quiz e.g. the main menu, quiz itself or the end.

-   Placed a background-colour behind the score for readability purposes as a Lighthouse test had brought up contrast issues between the gold text colour and the lighter background.

-   Added rel-"noopener" to external links opening in new tabs for security purposes.

### Known Bugs

-   The background image (maps.jpg) repeats slightly towards the very bottom of the Surface Pro 7 (912px x 1368px) device. It can also do this on larger TVs or wide-display devices such as tablets.

### Future Updates

There are many planned updates arranged for the Globe Trotter Quiz that include but are not limited to:

-   Introduction of difficulty level choices i.e. Easy, Normal, Hard.
-   Introduction of images, linked to the questions.
-   Sound effects and music.
-   More questions.
-   Theme/colour palette toggle.
-   Timer to add more difficulty.

## Deployment

### GitHub Pages
The following instructions are taken from Code Institutes [README.md template](https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md)

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code
-   At the early stages of the development, the [How to Make a Quiz App using HTML CSS Javascript - Vanilla Javascript Project for Beginners Tutorial](https://www.youtube.com/watch?v=f4fB9Xg2JEY&list=FLoLMoJL7IfiYl8F3sN_CEqQ&index=16) tutorial was followed and the code was used as the basis of the quiz. Supporting GitHub code [here](https://github.com/briancodex/quiz-app-js). Original code was later added alongside that found in the YouTube video to suit the quiz. Code tweaks were made to suit this quiz, pre-determined code edited or removed along with adjustments and restyling to the majority of the CSS found in the credited video. Upon further searching, it seems that [Build a Quiz App - Intro](https://www.youtube.com/watch?v=u98ROZjBWy8&list=PLDlWc9AfQBfZIkdVaOQXi1tizJeNJipEx) and that playlist of videos may be what that YouTube video was also inspired by.

-   'Web Dev Simplified' YouTube [video](https://www.youtube.com/watch?v=riDzcEQbX6k&list=FLoLMoJL7IfiYl8F3sN_CEqQ&index=13) was also used and combined with the above videos to help shape the Globe Trotter Quiz. Supporting GitHub code [here](https://github.com/WebDevSimplified/JavaScript-Quiz-App).

-   The API aspect of the quiz was introduced thanks to the [Build a Quiz App (11) - Fetch API to Load Questions API](https://www.youtube.com/watch?v=3aKOQn2NPFs&list=PLDlWc9AfQBfZIkdVaOQXi1tizJeNJipEx&index=12) tutorial, to which edits were then made. Supporting link to GitHub [here](https://github.com/jamesqquick/Build-A-Quiz-App-With-HTML-CSS-and-JavaScript).

-   The ability to toggle (show and hide) content via the How To Play, Contact and High Scores buttons on the main menu screen came from W3Schools documentation found [here](https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp), and a separate source [here](https://sebhastian.com/javascript-show-hide-div-onclick-toggle/) which was then edited to suit the project, along with additional customization.

-   This README.md document was based on Code Institutes [SampleREADME](https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md). The template was used as a guide, then filled with content related to this website. The MS2 Quiz [README.md](https://github.com/rhysmoggs/ms2-quiz/blob/main/README.md) file - the developers personal MS2 submission for the Code Institute course - was also used and then edited to suit this project.

### Inspiration

-   The Code Institute Slack community, especially projects from the peer-code-review channel.

### Content & Media

-   The questions and answers are all generated via an API from [The Open Trivia Database](https://opentdb.com/api_config.php).

-   The main background image (maps.jpg) - Photo by Andrew Neel from Pexels found [here](https://www.pexels.com/photo/assorted-map-pieces-2859169/).

-   The logo (logo.png) was created using Canva.

-   The plane (plane.png) image for the progress bar was created using Canva.

-   Unless mentioned in the [Code](#code) section, all other code is written by the developer.

### Acknowledgements

-   Stack Overflow [website](https://stackoverflow.com/) for general problem solving.

-   My Mentor for helpful feedback and input, especially with help towards the [progress bar](#progress-bar) development.

-   Tutor support at Code Institute.

technologies used:

- python
- JS
- CSS3
- HTML5

- PostgreSQL - 
- MongoDB - 
- PsycoPG2 - database adapter. library for connecting Python to PostgreSQL.
- SQLAlchemy - ORM lirbary
- PyMongo - 
- Flask - 
- Flash - 
- dnspython - 
- Jinja2? - template
- jquery
- materialize(sp?) - 
- fontawesome - icons
- google fonts
- heroku - 
- git, gitpod, github

- image editing websites/software here
- balsamiq
- era database/ design




Data Schema:

link both together through...


- Relational Database:


    PostgreSQL - open-source, Object-Relational Databse Management System (ORDBMS). fre use, licencing? good for future projects or launching this one if needs be.

    primary key - A unique ID that identifies individual records regardless of any changes that occur



- Non-Relational Database:
    mongoDB - 

------



deployment of website:

1. If you wish to - use Code Institute's template from here:  / copy this projects link/url?
2. install two python packages. Flask and SQLAlchemy to work with Postgres databases. psycopg2 is necessary to work with Postgres database. In command line type: `pip3 install Flask-SQLAlchemy psycopg2`
3. create "env.py" file
4. Create a ".gitignore" file if you choose not to use Code Institute's template. Add `env.py` and the soon to be generated `__pyache__/` to it. All hidden and sensitive files/folders to be added here.
5. in "env.py", type following:
    ```
    import os

    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", "any_secret_key")
    os.environ.setdefault("DEBUG", "True")
    os.environ.setdefault("DEVELOPMENT", "True")
    os.environ.setdefault("DB_URL", "postgresql:///<DATABASE>")
    ```

    The `any_secret_key` can be called whatever you wish: `os.environ.setdefault("SECRET_KEY", "any_secret_key")`or generate a random and secure password here: https://randomkeygen.com/

    make sure to change `os.environ.setdefault("DEBUG", "True")` to "False" before deploying/launching project.

    `<DATABASE>` points to the databse to be created, in this case "my_cocktails".
6. create a folder (in this case, folder is named "cocktails") in the root of your project.
7. within that newly created folder, create a file called `__init__.py`
8. write the following in the new file:
    ```
    import os
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    if os.path.exists("env.py"):
        import env  # noqa


    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

    db = SQLAlchemy(app)

    from cocktails import routes  # noqa
    ```
9. create a "routes.py" file within the "cocktails" folder
10. within that "routes.py" file, write the following:
    ```
    from flask import render_template
    from cocktails import app, db


    @app.route("/")
    def home():
        return render_template("base.html")
    ```
11. in root of project, create "run.py" file
12. within "run.py", write the following:
    ```
    import os
    from cocktails import app


    if __name__ == "__main__":
        app.run(
            host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG")
        )
    ```
13. within "cocktails" folder, create a new "templates" folder. This is where Flask will search for any html templates to be rendered.
14. create a new file "base.html" within the "templates" folder.
15. within the "base.html" file, write whatever you wish to be presented on your website.
16. in the terminal, write `python3 run.py` to launch the project.
17. add, commit and push.


Setting up Databse - postgreSQL database:

make sure you have postgreSQL installed locally if you are not using CI's template?
set up the databse schema as follows:
1. define our models by creating a "models.py" file within the "cocktails" folders
2. write the following in the "models.py" file and create the tables:
    ```
    from cocktails import db


    class Category(db.Model):
        # schema for the Category model
        id = db.Column(db.Integer, primary_key=True)
        category_name = db.Column(db.String(25), unique=True, nullable=False)

        def __repr__(self):
            # __repr__ to represent itself in the form of a string
            return self.category_name


    class Users(db.Model):
        # schema for the Users model
        id = db.Column(db.Integer, primary_key=True)
        user_name = db.Column(db.String(20), unique=True, nullable=False)
        password = db.Column(db.String(260), nullable=False)

        def __repr__(self):
            # __repr__ to represent itself in the form of a string
            return self.user_name
    ```
3. in "routes.py", import these newly created models:
    ```
    from cocktails.models import Category, Users
    ```
4. log in to postgreSQL terminal by typing psql in terminal.
5. type `CREATE DATABASE cocktails;`
6. then `\c cocktails;` to connect to the newly created database.
7. finally `\q` to exit.
8. use python to generate and migrate the models into the database. if any changes are made to this database, you must repeat the same steps to refresh and update your database. in the terminal, type `python3`.
9. type `from cocktails import db`
10. type `db.create_all()`
11. if you wish to check that the tables exist, type `psql -d cocktails` followed by `\dt` then `\q` to quit, otherwise just exit via `exit()`.
12. commit then push


Setting up Database - MongoDB database:

Make sure to that you have a MongoDB account.

1. Create a cluster (https://www.mongodb.com/basics/clusters/mongodb-cluster-setup). This project uses a shared cluster. Choose the closest region to you which is free to use. Free cluster tier and then name your `<CLUSTER>` ("myFirstCluster", in this project).
2. In Database Access, add a new database user (https://www.mongodb.com/docs/atlas/security-add-mongodb-users/#add-database-users).
3. In Network Access, click add IP address and choose 'Allow Access From Anywhere'. Input the IP of your hosts here to add further security.
4. In the newly created `<CLUSTER>`, click on Create a Database and under Database Name, enter a `<DATABASE>` name, ("my_cocktails", in this project)
5. Under collection name, enter `<COLLECTION>` ("cocktails", in this project).
6. Within the `<DATABASE>` ("my_cocktails"), click on Create Collection button and enter any other collections you wish to store.
7. Within each collection, click on Insert Document, and enter the key-value pairs you wish to store in your document. For this project, the following key names and value data types were stored:
    ```
    _id: <ObjectId>
    cocktail_name: <string>
    category_name: <string>
    cocktail_img: <string>
    cocktail_description: <string>
    created_by: <string>
    main_ingredient: <string>
    method: <string>
    other_ingredients: <array>
    prep_time: <Int32> with a default value of "0"
    servings: <Int32> with a default value of "0"
    ```
8. In the terminal, install dnspython `pip3 install dnspython`
9. Install pymongo too `pip3 install flask-pymongo`
10. on the mongo website, in your collection, connect your cluster. Choose 'Connect your application' and choose Python and your version (3.6 or later, in this project).
11. Copy the connection string.
12. In the "env.py" file, add the following environment variables to the already present ones:
    ```
    os.environ.setdefault("MONGO_URI", "mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER>.1megs.mongodb.net/<DATABASE>?retryWrites=true&w=majority")
    os.environ.setdefault("MONGO_DBNAME", "<DATABASE>")
    ```
    Make sure to insert your own information for `<USERNAME>`, `<PASSWORD>`, `<CLUSTER>` and `<DATABASE>`.
13. In "__init__.py" add  `from flask_pymongo import PyMongo`.
14. Add and update:
    ```
    app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

    mongo = PyMongo(app)
    ```
15. In "routes.py", update entire file to be:
    ```
    from flask import (
        flash, render_template,
        request, redirect, session, url_for)
    from bson.objectid import ObjectId
    from cocktails import app, db, mongo
    from cocktails.models import Category, Users


    @app.route("/")
    def home():
        return render_template("cocktails.html")
    ```
16. In terminal, write `touch cocktails/templates/cocktails.html`
17. In "cocktails.html" add your website content here (use templates and link "base.html" to all other pages etc)
18. In terminal, "python3 run.py" to view your work.
19. add, commit, push.


Linking the databases:

1. Using category_id
2. 


Deploy the application to Heroku:

1. Create a "requirements.txt" by typing `pip3 freeze --local > requirements.txt` in the terminal. This lists what is necessary to run the project.
2. Create a Procfile by typing `echo web: python run.py > Procfile` in the terminal. In the newly created "Procfile", check to see if a blank line appears under the written code. If there is, delete and save that change. It can cause issues with Heroku.
3. Commit and push.
4. On the Heroku website. Create a new app and name it. Choose the regeion closest to you.
5. Create a new database on Heroku. Resources > Add-ons, search for heroku postgres and choose the 'Hobby Dev - Free' option, or whichever suits your needs.
6. Once confirmed, go to Settings > Config Vars > Reveal Config Vars, and input the following:
    ```
    IP = 0.0.0.0
    PORT = 5000
    SECRET_KEY = your_secret_key_here
    MONGO_URI = mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER>.1megs.mongodb.net/<DATABASE>?retryWrites=true&w=majority
    MONGO_DBNAME = your_database_name_here
    ```
    You can add:
    ```
    DEBUG = True
    ```
    temporarily but make sure to change to `False` when finalizing the app. Keep to `True` for error fixing during development.
7. In your Config Vars in Heroku, if DATABASE_URL starts with `postgres` instead of `postgresql`, update your `__init__.py` file to:
```
import os
import re
from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

uri = os.environ.get("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku

db = SQLAlchemy(app)
mongo = PyMongo(app)

from cocktails import routes  # noqa
```
This wil ensure that the database is correctly linked.
8. In github, make sure you've added, commited and pushed your latest work.
9. The following point is an extract taken from Code Institute:

    ```Automated Deployments from GitHub disabled by Heroku
    Due to a security issue, Heroku has disabled automated deployments from GitHub. Unfortunately, we have no indication if or when they will reactivate this. In order for you to deploy while this situation persists, please follow the steps below to deploy from your Gitpod workspace:

    - Open the terminal.
    - For those of you who are using MFA/2FA: please scroll down to see the additional steps required.
    For those of you not using MFA/2FA: Log in to Heroku and enter your details.
    command: heroku login -i
    - Get your app name from heroku.
    command: heroku apps
    - Set the heroku remote. (Replace <app_name> with your actual app name and remove the <> characters)
    command: heroku git:remote -a <app_name>
    - Add and commit any changes to your code if applicable
    command: git add . && git commit -m "Deploy to Heroku via CLI"
    - Push to both GitHub and Heroku
    command: git push origin main
    command: git push heroku main

    MFA/2FA enabled?
    - Click on Account Settings (under the avatar menu) on the Heroku Dashboard.
    - Scroll down to the API Key section and click Reveal. Copy the key.
    - Back in your Gitpod workspace, enter the command: heroku_config , and enter your API key you copied when prompted.
    - Continue from step 3 above. If you get prompted to log in at any point:
      - Enter your Heroku username.
      - Enter the API key you just copied.
    
    Need to deploy again?
    You should just be able to add, commit and push, and if prompted enter your username and API key again.

10. Click 'Open App' in heroku, and your project will be displayed here.
11. Due to the automatic deployment issues on heroku's part, any changes to your app will need to manually be updated by following step 8. again.
12. We need to create our tables on the Heroku database. In Heroku, on the top-right, clcik More > Run Console.
13. Type `python3`
14. Type `from cocktails import db` then `db.create_all()` then `exit()`
15. In GitHub, change your `env.py` to reflet the newly created database by deleting `os.environ.setdefault("DB_URL", "postgresql:///cocktails")` and inserting `os.environ.setdefault("DATABASE_URL", "<heroku string>")` from Heroku's config vars.