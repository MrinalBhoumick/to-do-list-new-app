from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner

class ToDoListTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mrinalbhoumick.github.io/to-do-list-new-app/")  # Use the URL where your app is hosted

    def tearDown(self):
        self.driver.quit()

    def test_add_task(self):
        driver = self.driver
        task_input = driver.find_element(By.ID, "new-task")
        add_button = driver.find_element(By.ID, "add-button")

        task_input.send_keys("Buy groceries")
        add_button.click()

        time.sleep(1)  # Wait for the task to be added
        task_list = driver.find_element(By.ID, "task-list")
        self.assertIn("Buy groceries", task_list.text, "Task was not added successfully")

    def test_complete_task(self):
        driver = self.driver
        self.test_add_task()  # Ensure there's a task to complete

        complete_checkbox = driver.find_element(By.XPATH, "//span[text()='Buy groceries']/preceding-sibling::input[@type='checkbox']")
        complete_checkbox.click()

        time.sleep(1)  # Wait for the task to be marked as completed
        self.assertTrue(complete_checkbox.is_selected(), "Task was not marked as completed")

    def test_delete_task(self):
        driver = self.driver
        self.test_add_task()  # Ensure there's a task to delete

        delete_button = driver.find_element(By.XPATH, "//span[text()='Buy groceries']/following-sibling::button")
        delete_button.click()

        time.sleep(1)  # Wait for the task to be deleted
        task_list = driver.find_element(By.ID, "task-list")
        self.assertNotIn("Buy groceries", task_list.text, "Task was not deleted successfully")

if __name__ == "__main__":
    # Define the report path
    report_path = './reports'
    
    # Create a TestSuite
    suite = unittest.TestLoader().loadTestsFromTestCase(ToDoListTests)
    
    # Run the test suite and generate the report
    runner = HtmlTestRunner.HTMLTestRunner(output=report_path, report_title="ToDo List Test Report", descriptions="Test results for ToDo List application")
    runner.run(suite)
