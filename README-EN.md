# Sprint_6
UI testing, applied Page Object Model, Allure report.

Task: write autotests for the educational service [«Яндекс.Самокат»](https://qa-scooter.education-services.ru).  
Imagine that a manual tester handed you scenarios. They need to be covered with autotests.

## 1. Preparation
* Mozilla Firefox browser is installed.
* Selenium and Allure are connected.

## 2. Study of test scenarios
### Dropdown list in the "Вопросы о важном" section.
Check: when you click on the arrow, the corresponding text opens. It is important to write a separate test for each question.

### Scooter order.
You need to check the entire flow of the positive scenario with two sets of data.  
Check the entry points to the scenario, there are two: the "Заказать" button at the top of the page and at the bottom.
                           
**What the positive scenario consists of:**
* Click the "Заказать" button. There are two order buttons on the page.
* Fill in the order form.
Check:
* a popup window appeared with a message about successful order creation.
* if you click on the "Самокат" logo, you will go to the "Самокат" main page.
* if you click on the Yandex logo, a new window will open via redirect to the Дзена main page.

You need to write tests with different data: at least two sets. Which data to use is up to you. The scenario is the same, regardless of the different entry points: you don't need to test each of them twice.

## 3. Writing tests
* Describe the necessary locators using Page Object.
* Create a separate package for Page Object.
* For each page, create a separate class with Page Object.
* Write tests on Selenium. Tests should be divided by topic or functionality.  
  Please note: you don't need to create a separate class for each test. Add tests for one functionality in one class.
* All tests should be in the test directory. 
* Use parametrization.

## 4. Creating a report in Allure
Generate an Allure report and push it to the repository.
