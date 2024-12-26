# AMHARIC TO ENGLISH DICTIONARY WEB-BASED APPLICATION
### Video Demo: https://youtu.be/cgpdQN0CeLk
### Description:
This project is a web-based application that translates **Amharic words to English.** It is built for the final project of [CS50](https://cs50.harvard.edu/x/2023).
The idea for this project came from my wife, who works as a trasnslator and needed a simple dictionary to help her with her work.

This application is built using HTML, CSS, [bootstrap](https://getbootstrap.com/) (the most popular CSS Framework for developing responsive and mobile-first websites.), Javascript (for the frontend), Python (Flask for the backend), and SQLite (cs50's python library) for the database.

### Project Structure:
The project has the following structure:

* **`static`**  folder: holds `styles.css` file for all the CSS styles in the project

* **`templates`** folder: holds all `HTML` files:
  - `layout.html` - is a base HTML file on which other HTML files will be based. Here `Javascript` is used for some frontend functionalities.

  - `index.html` - is responsible of home page (will be discussed later). Here `javascript` is used for frontend functionalities.

  - `search.html` - where search results will be viewed. It has list of cards for each word, giving out the word's respective translations in a dropdown when chevron icon is clicked.

  - `no-result.html` - will be initiated when no search result is found and gives some random words to simply view their translations.

  - `history.html` - all clicked words will be stored in history session, therefore, list of recent searches will be viewd on history page.

  - `bookmark.html` - if a word bookmarked by clicking one of bookmarking buttons in home page words translations view cards, or on a modal dialog box section with the list of recent searches card of words, or on single word translations page, can be viewed in bookmark page.

  - `single-word.html` - This is to view a single word translation in a card with all its attributes (bookmarking included)


* **`app.py`**: This is main Python file responsible for holding backend web application using Flask.
It contains the following view functions:
    - Configure session to use filesystem (instead of signed cookies)
    - Configure cs50 library to use SQLite database

    - __*index*__ function responsible of home page view

    - __*search*__ function - When a user types or pastes a query into the search input field, "keyup" or "paste" event is triggered. The search function listens for this event and displays the search results section in modal dialog box if the word is found. If the word is no found, the no result section is displayed instead.

    - __*single_word*__ function - is responsible for displaying a single word translation when an Amharic word is clicked in the homepage, in the search result section, in the recent search list, in the history page, or in the bookmark page. This function displays the word's translation in a card with all its attributes, including bookmarking.

    - __*recent_search*__ function - is responsible for storing a clicked word in the history session if it is not  already in the history. If the word already exists in the history, the function does nothing.

    - __*bookmark*__ function - responsible of displaying the bookmark page.

    - __*history*__ function - responsible of displaying the history page.

    - __*add_or_delete_bookmark*__ function - when bookmark icon is clicked in the homepage, in the recent search list, or in the single_word page, it toggles the icon. If the word does not exist in the bookmark session, it will be added to the bookmark. If the word already exists in the bookmark session, it will be deleted.

    - __*delete_bookmark*__ function - removes a single bookmark in the session (in the bookmark page)
    - __*clear_all_bookmark*__ function - clears all the bookmarks in the session (in bookmark page)
    - __*remove_history*__ function - removes a single history in a session (in history page)
    - __*clear_all_history*__ function - clears all the history in session (in history page)

> **`dictionary.db`** - SQLite database, with dictionary table where all data stored.

### User Interface
The user interface of the application is designed to be user-friendly and easy to navigate. The main features of the user interface are:
>**Navbar brand** on the left corner of Navbar holds applications brand name "Amharic-English Dictionary". Clicking it will redirect to homepage.

>**Search Icon:**
    In the home page you have navigagtion bar with search  icon, that enable you to go for search a word, on an opened modal window (dialog box) when search icon clicked.

* Modal dialog box (based on bootstrap): There are "search input" form and modal 'cancel button' in the header, and four sections ('no recent searches', 'recent search', 'search result' and 'no search result' sections) displayed interchangibly.

    - **search input** - for query of words

    - **cancel button** - closes the modal dialog box. On a bigger screen modal dialog box will be diminished, hence 'cancel button' will be removed. Closing functionality will be done when clicked outside of modal box boundery.

    - **no recent searches section** - Just show "No recent searches" text, when no recent searches found

    - **recent search section** - view list cards of recent searches available in the history. Each card has functionality to 'bookmark/unbookmark' button/icon, and 'delete' from history button.

    - **search result section** - displayed when querying has given result. Query results will be viewed in list of card of words with expandable functionality, to view translations with limited words, when chevron icon clicked. When main card of word clicked, it will direct to homepage and will be viewed in the top order on the main section of homepage and will be recorded as history.

    - **no result section** - displayed when querying doesn't find a word. However, list of three random words will be visible if user interested to view translations. when one of this randomw words clicked it will it will direct to homepage and will be viewed in the top order on the main section of homepage and will be recorded as history.

> **Menu:**
    On the right end of navigation bar there is a menu icon, that make visible  __*Home, Bookmark, History and Theme*__, using [boostrap's](https://pages.github.com) offcanvas functionality.

* __*Home*__ redirects to home page
* __*Bookmark*__ redirect to bookmark page. In the bookmark page you will see list of words found in bookmark session and with respective delete (x) button to delete single word, and `clear` button on the top of list to delete all, if no bookmark found, "No bookmark to show" message shown on the main section.
* __*History*__ redirect to history page. In the history page you will see list of words found in history session and with respective delete (x) button to delete single word, and a `clear` button on the top of list to delete all, if no history found, "No history found" message shown on the main section.
* __*Theme*__ is a dropdown toggler, dropdowns are light, dark, and auto which are responsible of web applications color theme.

  - __*light*__ bright/light mode
  - __*dark*__ night/dark mode
  - __*auto*__ it automatically toggled to light and dark based on Day hours. `Light` mode on the day hours and `Dark` on the night hours.

> **Main section** below navigation bar.
    If recent searches of words (history) exist, that is a place where it will be showed.
    If no recent searches or history deleted no words will be seen

